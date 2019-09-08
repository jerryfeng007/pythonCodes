import unittest
from selenium import webdriver
import time
from project2.po import login_page, user_page


class TestLoginPage(unittest.TestCase):
    '''用户登录页'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.url = 'http://xqtesting.com/user-login.html'
        self.driver.get(self.url)
        
    def tearDown(self):  
        time.sleep(3)
        self.driver.quit()

    def test_01_click(self):
        '''立即注册'''
        time.sleep(3)
        login_page.click(self.driver, '立即注册')
        try:
            self.assertIn('注册', self.driver.title, '失败')
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它

    def test_02_click(self):
        '''登录之后验证用户名'''
        login_page.input_box(self.driver, 'xxxxxxxxxx', 'xxxxxxxxxxxxxxx')
        time.sleep(3)
        try:
            self.assertIn('退出', user_page.element(self.driver, "退出"), '失败')
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它

