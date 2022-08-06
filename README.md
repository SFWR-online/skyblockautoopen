# skyblock_auto_open
用于skyblock自动开箱


&#9888;需要安装skytil并打开treasure helper


## 前置

具有python环境，安装opencv库和pyautogui库

## 使用
+ 根据显示器大小调整监测屏幕内范围 

  img = pyautogui.screenshot(region=[600,200, 800, 800])  # 分别代表：左上角坐标，宽高

  pyautogui.moveTo(600+cen_v, 200+cen_h, duration=0)
+ 若需要退出程序，将鼠标向左上角滑动即可
