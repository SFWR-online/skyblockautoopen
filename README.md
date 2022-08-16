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

#### main.py


+ 根据显示器大小调整监测屏幕内范围 

  img = pyautogui.screenshot(region=[600,200, 600, 600])  # 分别代表：左上角坐标，宽高

+ 按下N键暂停程序，再按下则继续，可以在keyboard.is_pressed('n')中修改按键
+ 为防止未触发设置未检测阈值，根据实际需要设置q的大小
+ TODO：阈值改成时间戳


#### main_gui.py

+ 增加了桌面控件显示当前状态

+ 增加了颜色提醒，当打开时颜色为绿色，经过180s后变红，代表需要清理mobs
+ 控件配置见代码注释