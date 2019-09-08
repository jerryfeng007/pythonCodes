import unittest
from selenium import webdriver
import time
import HTMLTestRunner_CN_Chart_Screen  # 先把HTMLTestRunner_CN_Chart_Screen.py放在D:\Python34\Lib


# class TestSearch(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(2)
#         self.url = 'http://www.xqtesting.com/'
#         self.driver.get(self.url)
#
#     def tearDown(self):
#         time.sleep(2)
#         self.driver.quit()
#
#     def test_01_search(self):
#         self.driver.find_element_by_id('words').send_keys('挨踢脱口秀')
#         self.driver.find_element_by_class_name('btn-default').click()
#
#     def test_02_search(self):
#         self.driver.find_element_by_id('words').send_keys('小强测试品牌')
#         self.driver.find_element_by_class_name('btn-default').click()
#
#
# if __name__ == '__main__':
#     unittest.main()


class TestSearch(unittest.TestCase):
    '''测试类'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.url = 'http://www.xqtesting.com'
        self.driver.get(self.url)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_01_search(self):
        '''测试搜索演示1'''
        self.driver.find_element_by_id('words').send_keys('挨踢脱口秀')
        self.driver.find_element_by_class_name('btn-default').click()

    def test_02_search(self):
        '''测试搜索演示2'''
        self.driver.find_element_by_id('words').send_keys('小强测试品牌')
        self.driver.find_element_by_class_name('btn-default').click()


if __name__ == '__main__':

    report_path = r'D:\learnPY\from github\selenium\basic\demo.html'
    all_suite = unittest.makeSuite(TestSearch)
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner_CN_Chart_Screen.HTMLTestRunner(verbosity=2, stream=fp, title='班', description='演示')
    runner.run(all_suite)
    fp.close()
