import pyautogui
import cv2
import numpy as np
import time
import keyboard 
import sys
flag=1
while 1:
	if keyboard.is_pressed('n'):
		flag=1^flag
		time.sleep(1)
	if flag==0:
		img = pyautogui.screenshot(region=[600,200, 800, 800])
		img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
		himg = cv2.cvtColor(np.asarray(img), cv2.COLOR_BGR2HSV)
		thresh1 = np.array([140, 120, 120])     
		thresh2 = np.array([160, 255, 255]) 
		img_flag = cv2.inRange(himg, thresh1, thresh2)  
		#滤波
		img_morph = img_flag.copy()                             # 复制图像
		cv2.erode(img_morph, (3,3), img_morph, iterations= 3)   # 腐蚀运算
		cv2.dilate(img_morph, (3,3), img_morph, iterations= 3)  # 膨胀运算
		cnts, _ = cv2.findContours(img_morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # 获取图像轮廓
		cnts_sort = sorted(cnts, key= cv2.contourArea, reverse= True) # 将轮廓包含面积从大到小排列
		if len(cnts_sort):
			box = cv2.minAreaRect(cnts_sort[0])
			points = np.int0(cv2.boxPoints(box))
			cen_v = (points[0,0] + points[2,0]) / 2
			cen_h = (points[0,1] + points[2,1]) / 2
			pyautogui.moveTo(600+cen_v, 200+cen_h, duration=0)
		cv2.waitKey(0)
