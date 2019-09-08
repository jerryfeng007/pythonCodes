import unittest
from selenium import webdriver
import time
from project2.po import first_page


class TestFirstPage(unittest.TestCase):
    '''首页'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(3)
        self.url = 'http://www.xqtesting.com'
        self.driver.get(self.url)
        
    def tearDown(self):  
        time.sleep(3)
        self.driver.quit()

    def test_01_click(self):
        '''注册'''
        first_page.link(self.driver, '注册')
        time.sleep(3)
        try:
            self.assertIn('注册', self.driver.title, '失败')
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它
        
    def test_02_click(self):
        '''宝妈店铺'''
        first_page.link(self.driver, '宝妈店铺')
        time.sleep(3)
        try:
            self.assertIn('母婴', self.driver.title, '失败')
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它

    def test_03_click(self):
        '''博客'''
        first_page.link(self.driver, '博客')
        time.sleep(3)
        try:
            self.assertIn('博客', self.driver.title, '失败')
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它

    def test_04_click(self):
        '''登陆'''
        first_page.link(self.driver, '登录')
        time.sleep(3)
        try:
            self.assertIn('登录', self.driver.title, '失败')
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它

    def test_05_search(self):
        '''搜索'''
        first_page.search(self.driver, '软件测试')
        time.sleep(3)
        try:
            self.assertIn('软件测试', self.driver.title, '失败')
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它

    def test_06(self):
        '''首页title'''
        time.sleep(3)
        try:
            self.assertIn('测试帮', self.driver.title, '失败')
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它
