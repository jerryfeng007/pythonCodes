import unittest
import time
from appium import webdriver
from appiumproject.po import login


class Test1(unittest.TestCase):
    '''登陆类'''
    def setUp(self):
        appPackage = 'com.xiaomi.shop'
        desired_caps = {
            # 使用哪种移动平台，IOS, Android
            'platformName': 'Android',
            # 启动哪种设备，是真机还是模拟器，可有可无
            'deviceName': 'Android Emulator',
            # OS的版本，模拟器---启动一个app---主界面---设置---关于手机---Android版本
            'platformVersion': '4.4.4',
            # 被测试的App在电脑上的绝对路径，如果写了这个就可以不用写下面的两个了
            # 缺点：每次执行都会重新安装！
            # 'app':'os.path.abspath(r"D:\learnPY\appium\xiaomishop.apk")',
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

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

        # 广告页的跳过
        self.driver.find_element_by_id('com.xiaomi.shop:id/skip').click()

        # 点击广告
        self.driver.find_element_by_class_name('android.widget.ImageView').click()

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_01_click(self):
        '''登陆'''
        time.sleep(3)
        user = login.login(self.driver)
        try:
            self.assertEqual(user, '14629325369', '失败')
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它

    def test_02_click(self):
        '''登陆'''
        time.sleep(3)
        user = login.login(self.driver)
        try:
            self.assertEqual(user, '1462932536', '失败')
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它
