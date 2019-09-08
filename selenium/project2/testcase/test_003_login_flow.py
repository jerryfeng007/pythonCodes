import unittest
from selenium import webdriver
import time
from project2.po import first_page, login_page, user_page


class TestLoginFlow(unittest.TestCase):
    '''登录流程'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.url = 'http://xqtesting.com'
        self.driver.get(self.url)
        time.sleep(3)
        
    def tearDown(self):  
        time.sleep(3)
        self.driver.quit()

    def test_01_login_flow(self):
        '''登录'''
        first_page.link(self.driver, '登录')
        time.sleep(3)
        login_page.input_box(self.driver, 'xxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxx')
        time.sleep(3)
        try:
            self.assertIn('退出', user_page.element(self.driver, "退出"), '失败')
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它
