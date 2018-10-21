import logging
import os.path
import time

def ScreenShot(driver):
    # 截图函数
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    pic_path = os.path.abspath('.') + '\\picture'
    pic_name = pic_path + rq + '.pang'
    driver.get_screenshot_as_file(pic_name)
    return pic_name
