'''
2019/9/9
PCカメラの映像をグレイ処理、ぼかし処理をして表示する
git:
https://github.com/yunosuke068/VideoCapture.git
'''
import cv2
import sys

camera_id = 0
delay = 1
window_name = 'frame'

'''
VideoCapture()の引数にカメラの番号IDを入力することで
PC内蔵カメラ、Webカメラ、USBカメラの映像を取得できる
カメラ番号はPCカメラが0、USBカメラが1のように割り当てられる
'''
cap = cv2.VideoCapture(camera_id)

#IDのカメラが存在しないと終了する
if not cap.isOpened():
    sys.exit()

#while True: はbreakされるまで無限ループ
while True:
    #retをつけないとerrorがでる.retは戻り値
    ret, frame = cap.read()


    #デフォルトだと反転して表示されるため映像を反転する
    #[行:列]で行と列の最初から最後までを反転する
    frame = frame[:,::-1]


    #映像をGRAYスケール化
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #映像をぼかす
    blur = cv2.GaussianBlur(gray, (0, 0), 5)


    #映像の表示
    cv2.imshow(window_name, blur)
    #'q'が押されると終了する
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

#キャプチャを解放する
cap.release()
cv2.destroyWindow(window_name)
