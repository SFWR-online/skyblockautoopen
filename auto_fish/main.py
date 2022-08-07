import pyautogui
import cv2
import numpy as np
import time
p=0
flag=1
import keyboard  # using module keyboard
while 1:
	if keyboard.is_pressed('n'):
		flag=1^flag
		time.sleep(1)
	if flag==0:
		img = pyautogui.screenshot(region=[600,200, 600, 600])
		#img.save("test_screen.jpg")
		img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
		himg = cv2.cvtColor(np.asarray(img), cv2.COLOR_BGR2HSV)
		thresh1 = np.array([0, 120, 120])     
		thresh2 = np.array([10, 255, 255]) 
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
			cen_v =points[2,0]-points[1,0]
			cen_h =points[2,1]-points[0,1]
			if(cen_h>20 and cen_v<20):
				pyautogui.click(button='right')
				time.sleep(0.2)
				pyautogui.click(button='right')
				time.sleep(1)
				p=p+1
			   #cv2.drawContours(img, [points], -1, (255,0,0), 2)
		if p==4:
			x, y = pyautogui.position()
			pyautogui.moveTo(x+1200, y, duration=0.1)
			pyautogui.moveTo(x-1200, y, duration=0.1)
			#pyautogui.moveTo(x+1200, y, duration=0)
			p=0
		cv2.waitKey(0)
