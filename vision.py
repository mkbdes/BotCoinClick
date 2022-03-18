import cv2 as cv
import numpy as np
import os
import pyautogui
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def ClickPositions(needle_img_path, haystack_img, threshold=0.6, debug_mode=None):
    needle_img = cv.imread(needle_img_path)
    needle_gray = cv.cvtColor(needle_img, cv.COLOR_RGB2GRAY)
    needle_w, needle_h = needle_gray.shape[::-1]
    
    method = cv.TM_CCOEFF_NORMED

    result = cv.matchTemplate(haystack_img, needle_gray, method)    
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))    
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]        
        rectangles.append(rect)
        rectangles.append(rect)
    rectangles, _ = cv.groupRectangles(rectangles, eps=0.5, groupThreshold=1)
    x, y, w, h = 530, 250, 840, 462
    for (rx, ry, rw, rh) in rectangles:
        center_x = rx + int(rw / 2)
        center_y = ry + int(rh / 2)
        pyautogui.click(x=x + center_x, y=y + center_y)
