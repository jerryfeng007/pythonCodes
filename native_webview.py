import time
from appium import webdriver

# native(原生) 和 webview(微信的webview页面，刚打开是白页，上面有进度条，性能不够好)

desired_caps = {
    # 使用哪种移动平台，IOS, Android
    'platformName': 'Android',
    # 启动哪种设备，是真机还是模拟器，可有可无
    'deviceName': 'Android Emulator',
    # OS的版本，模拟器---启动一个app---主界面---设置---关于手机---Android版本
    'platformVersion': '4.4.4',
    # 被测试的App在电脑上的绝对路径，如果写了这个就可以不用写下面的两个了
    # 缺点：每次执行都会重新安装！
    # 'app':'os.path.abspath("D:\\learnPY\\appium\\tools\\xiaomishop.apk")',
    # 建议用下面这种写法
    # apk包名
    'appPackage': 'com.xiaomi.shop',
    # apk的launcherActivity
    # 注意：原生app的话要在activity前加个.
    'appActivity': 'com.xiaomi.shop.activity.MainTabActivity',
    # 隐藏手机中的软键盘，让手机中可以输入中文
    'unicodeKeyboard': True,
    'resetKeyboard': True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 翻译为上下文，其实类似于se中的句柄
contexts = driver.contexts
print('contexts=', contexts)

# 切换到webview
driver.switch_to.context('WEBVIEW_com.baidu.searchbox')
print('当前context=', driver.current_context)

# 切换之后其实就是一个浏览器了，查看元素就跟se一样了
driver.find_element_by_id('xxx').click()

# 切换回native
driver.switch_to.context('NATIVE_APP')  # 参数固定

time.sleep(5)
driver.quit()
