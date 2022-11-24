import pyautogui
import time
n=0
while(n<4):
    screenshot=pyautogui.screenshot()
    sc="screenshot" + str(n) + ".jpg"
    screenshot.save("screenshots/"+sc)
    time.sleep(10)
    n=n+1


