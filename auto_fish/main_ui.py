import pyautogui
import cv2
import numpy as np
import time
import keyboard
import win32api
import win32con 
import tkinter
p=0
q=0
flag=1
t1=time.time()
t2=time.time()
root_window = tkinter.Tk()
root_window.geometry("100x60+1700+80")#设置窗口大小x*y和位置x+y
root_window.attributes('-topmost', 'true')#控件始终浮于上层
root_window.resizable(False, False)#删除最小化与最大化
var = tkinter.StringVar()
var.set("close")
my_show = tkinter.Label(root_window,textvariable=var,font=('Arial',12),width=10,height=2)
my_show.pack()
my_show.config(fg="green")
def change_text():
	global flag,q,p,t1,t2		
	if keyboard.is_pressed('n'):
		flag=1^flag
		if flag==0:
			t1=time.time()
			var.set("open")
		if flag==1:
			var.set("close")
			my_show.config(fg="green")
		time.sleep(2)
	if flag==1:
		time.sleep(0.5)
	if flag==0:
		img = pyautogui.screenshot(region=[600,200, 600, 600])
		img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
		himg = cv2.cvtColor(np.asarray(img), cv2.COLOR_BGR2HSV)
		thresh1 = np.array([0, 120, 120])     
		thresh2 = np.array([10, 255, 255]) 
		img_flag = cv2.inRange(himg, thresh1, thresh2)  
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
				q=0
				p=p+1
		if len(cnts_sort)==0:
			q=q+1
		if q==550:
			pyautogui.click(button='right')
			q=0
		if p==4:
			x, y = pyautogui.position()
			pyautogui.moveTo(x+1200, y, duration=0.1)
			pyautogui.moveTo(x-1200, y, duration=0.1)
			p=0
			t2=time.time()
			if t2-t1>=180:
				my_show.config(fg="red")
		cv2.waitKey(0)
	my_show.after(50, func=change_text)
my_show.after(50, func=change_text)
root_window.mainloop()
