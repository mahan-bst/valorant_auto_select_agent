import pyautogui
import time
import numpy as np
from cv2 import cv2
# 900 x 850
LOCK_POS = [900, 850]
raze = 'img/raze.png'
phonix = 'img/phonix.png'
omen = "img/omen.png"
selec_agent = input('plz select ur agent : phonix, raze, omen \n')


while True:
    im = pyautogui.screenshot()
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(eval(selec_agent), 0)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < 0.8:
        continue

    pos = max_loc
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])
        time.sleep(0.5)
        pyautogui.moveTo(LOCK_POS[0], LOCK_POS[1])
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.click()
        break
