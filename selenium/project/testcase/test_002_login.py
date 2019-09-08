import unittest
from selenium import webdriver
import time
from project.po import login_page


class TestLogin(unittest.TestCase):
    '''登陆类'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.url = 'http://www.xqtesting.com/user-login.html'
        
    def tearDown(self):  
        time.sleep(5)
        self.driver.quit()
        
    def test_01_login(self):
        '''测试登陆的演示1 成功'''
        account = 'xxxxxxxxxx'
        password = 'xxxxxxxxxx'
        lp = login_page.LoginPage(self.driver)  # 把driver传过去
        lp.input_account_password_run(self.url, account, password)
        time.sleep(5)
        
        try:
            self.assertIn(account, self.driver.find_element_by_xpath(".//*[@id='siteNav']/a[1]").text, '失败')
            print('登陆成功,登陆的用户名为：', account)
            
        except Exception as e:
            print('登陆用户名出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它
        
    def test_02_login(self):
            '''测试登陆的演示1 失败'''
            account = 'xxxxxxxxxxxxxx'
            password = 'xxxxxxxxxxxx'
            lp = login_page.LoginPage(self.driver)  # 把driver传过去
            lp.input_account_password_run(self.url, account, password)
            time.sleep(5)
            
            try:
                self.assertIn(account, self.driver.find_element_by_xpath(".//*[@id='siteNav']/a[1]").text, '失败')
                print('登陆成功,登陆的用户名为：', account)
                
            except Exception as e:
                print('用户名或密码错误', str(e))
                self.imgs.append(self.driver.get_screenshot_as_base64())
                raise
