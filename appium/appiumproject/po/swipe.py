import time
from common import laoshi_swipe_demo


# 滑动操作


def swipe(driver):
    # 点击返回按钮
    driver.find_element_by_id('com.xiaomi.shop2.plugin.hdchannel:id/iv_backLeftGrey').click()

    # 滑动操作
    time.sleep(3)
    swipe_test = laoshi_swipe_demo.SwipeDemo()

    # 左滑
    swipe_test.swipeLeft(driver, 1000)
    ss = driver.find_element_by_android_uiautomator('new UiSelector().text("手机")')
    print(ss.text)

    time.sleep(3)
    # 左滑
    swipe_test.swipeLeft(driver, 2000)
    cc = driver.find_element_by_android_uiautomator('new UiSelector().text("智能")')
    print(cc.text)

    # 右滑
    time.sleep(3)
    swipe_test.swipeRight(driver, 2000)
    mm = driver.find_element_by_android_uiautomator('new UiSelector().text("手机")')
    print(mm.text)

    # 上滑
    time.sleep(3)
    swipe_test.swipeUp(driver, 2000)

    # 下滑
    time.sleep(3)
    swipe_test.swipeDown(driver, 2000)
