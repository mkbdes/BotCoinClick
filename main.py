import time
import cv2 as cv
import numpy as np
import os
import pyautogui
from vision import ClickPositions
from mss import mss
from PIL import ImageGrab

os.chdir(os.path.dirname(os.path.abspath(__file__)))
while True:
    class CoinClick:
        print("COMEÇANDO..")
        time.sleep(15)

        start = pyautogui.click(x=557, y=485, duration=2)
        time.sleep(5)
        start2 = pyautogui.click(x=954, y=452, duration=2)
        time.sleep(2.8)
        
        x = 530
        y = 250
        w = 840
        h = 462
        timeout = 50
        timeout_start = time.time()
        loop_time = time.time()
        with mss() as sct:
            monitor = {"top": 250, "left": 530, "width": 840, "height": 462}
            
            while time.time() < timeout_start + timeout:
                if x and y and w and h:
                    screenshot = np.array(sct.grab(monitor))
                    haystack_img = cv.cvtColor(screenshot, cv.COLOR_RGB2GRAY)

                    #cv.imshow('Computer Vision', screenshot)

                    ClickPositions("img/dash.png", haystack_img, 0.6, "rectangles")
                    #if cv.waitKey(1) == ord('q'):
                        #cv.destroyAllWindows()
                    print("FPS {:.2f}".format(1 / (time.time() - loop_time)))
                    loop_time = time.time()
                else:
                    print("espere")
                    break
                
        x, y, w, h = 530, 250, 840, 462
        if x and y and w and h:
            gain = pyautogui.locateOnScreen("img/gainpower.png", confidence=0.8)
            rest = pyautogui.locateOnScreen("img/restart.png", confidence=0.8)
            pyautogui.click(gain)
        else:
            pyautogui.click(rest)
        time.sleep(20)
        chose_game = pyautogui.doubleClick(x=927, y=120, duration=1)
