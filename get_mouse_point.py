import pyautogui
import time

#########################
# キャプチャ座標計測
#########################

# 左上座標を取得
print('キャプチャ範囲の左上座標にマウスカーソルを合わせる')
time.sleep(3)
print('左上座標：' + str(pyautogui.position()))

# １秒待機
time.sleep(1)

# 右下座標を取得
print('キャプチャ範囲の右下座標にマウスカーソルを合わせる')
time.sleep(3)
print('右下座標：' + str(pyautogui.position()))