import unittest
from selenium import webdriver
import time
from project.po import search_page


class TestSearch(unittest.TestCase):
    '''搜索类'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(2)
        self.url = 'http://www.xqtesting.com'
        
    def tearDown(self):  
        time.sleep(2)
        self.driver.quit()
        
    def test_01_search(self):
        '''测试搜索的演示1 成功'''
        keywords = '挨踢脱口秀'
        s1 = search_page.SearchPage(self.driver)  # 把driver传过去
        s1.input_keyword_run(self.url, keywords)
        
        try:
            self.assertIn(keywords, s1.return_title(), '失败')
            print('搜索成功,搜索的关键字为：', keywords)
            
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            raise  # 仅捕获异常不去处理它
        
    def test_02_search(self):
        '''测试搜索的演示1 失败'''
        keywords = '人民'
        s1 = search_page.SearchPage(self.driver)  # 把driver传过去
        s1.input_keyword_run(self.url, keywords)
            
        try:
            self.assertIn(keywords, '2', '失败')
            print('搜索成功，搜索的关键字为：', keywords)
                
        except Exception as e:
            print('出错了', str(e))
            self.imgs.append(self.driver.get_screenshot_as_base64())  # 避免重复的截图
            raise
