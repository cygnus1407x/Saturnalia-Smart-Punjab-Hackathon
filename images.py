import pyautogui
import time
n=0
time.sleep(10)
while(n<4):
    screenshot=pyautogui.screenshot()
    sc="image" + str(n) + ".jpg"
    screenshot.save("images/"+sc)
    time.sleep(10)
    n=n+1


