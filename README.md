# skyblock_auto
用于skyblock的脚本

## 前置

具有python环境，安装**opencv&&pyautogui&&keyboard**库

## Auto_open

&#9888;需要安装skytil并打开treasure helper

### 使用
+ 根据显示器大小调整监测屏幕内范围 

  img = pyautogui.screenshot(region=[600,200, 800, 800])  # 分别代表：左上角坐标，宽高

  pyautogui.moveTo(600+cen_v, 200+cen_h, duration=0)
+ 按下N键暂停程序，再按下则继续，可以在keyboard.is_pressed('n')中修改按键

## Auto_fish

&#9888;需要安装NotEnoughUpdate并打开钓鱼提示（感叹号）

### 使用
+ 根据显示器大小调整监测屏幕内范围 

  img = pyautogui.screenshot(region=[600,200, 600, 600])  # 分别代表：左上角坐标，宽高

+ 按下N键暂停程序，再按下则继续，可以在keyboard.is_pressed('n')中修改按键
