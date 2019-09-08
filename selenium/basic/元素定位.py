from selenium import webdriver
import time

print('------------------------------------基础操作------------------------------------------------------')

# driver = webdriver.Firefox()
# time.sleep(3)
#
# driver.set_window_size(666, 888)
# time.sleep(3)
#
# driver.maximize_window()
#
# driver.get('http://www.xqtesting.com/')
# print('网站名称：', driver.title)
# driver.get_screenshot_as_file('001.jpg')
#
# driver.refresh()
# time.sleep(3)
#
# driver.get('http://www.lizhi.fm/200893')
# print('网站名称：', driver.title)
# driver.get_screenshot_as_file('002.jpg')
#
# time.sleep(3)
# driver.back()
# print('网站名称：', driver.title)
#
# time.sleep(3)
# driver.forward()
# print('网站名称：', driver.title)
#
# #driver.close()
# driver.quit()


print('------------------------------------定位---id---class name--------------------------------------')

# url = 'http://www.xqtesting.com/'
# driver = webdriver.Firefox()
#
# driver.get(url)
# time.sleep(2)
# driver.find_element_by_id('words').send_keys('小强测试品牌')
# driver.find_element_by_class_name('btn-default').click()  # 不使用 btn btn-default
# time.sleep(2)
#
# # driver.find_element_by_id('words').clear()
# driver.find_element_by_id('words').send_keys('测试帮日记')
# driver.find_element_by_class_name('btn-default').click()
#
# driver.quit()

print('------------------------------------定位---link text---partial link text---------------------------')

# url = 'http://www.xqtesting.com/'
# driver = webdriver.Firefox()
# driver.get(url)
# time.sleep(2)
#
# driver.find_element_by_link_text('宝妈店铺').click()
# time.sleep(2)
#
# driver.find_element_by_partial_link_text('博').click()
#
# driver.quit()

print('------------------------------------定位---xpath-----------------------------------------------')

# ----------------可以使用安装的firepath插件

# url = 'http://www.xqtesting.com/'
# driver = webdriver.Firefox()
# driver.get(url)
# time.sleep(2)
#
# driver.find_element_by_xpath(".//*[@id='words']").send_keys('小强软件测试')
# driver.find_element_by_xpath('.//*[@id="searchbar"]/form/div/div/button').click()
#
# time.sleep(3)
# driver.find_element_by_xpath(".//*[@id='words' and @name='words']").send_keys('测试帮')
# driver.find_element_by_xpath(".//*[@id='searchbar']/form/div/div/button").click()

print('------------------------------------获取元素的文本内容------------------------------------')

# url = 'http://xqtesting.blog.51cto.com/'
# driver = webdriver.Firefox()
# driver.get(url)
# time.sleep(2)
#
# blog_name = driver.find_element_by_class_name('name').text
# print(blog_name)

print('------------------------------------定位一组元素--------------------------------------------')

# url = 'http://www.xqtesting.com/py_auto_homework8/se_class_demo/demo.html'
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get(url)
# time.sleep(2)
#
# inputs = driver.find_elements_by_tag_name('input')
#
# for input in inputs:
#     if input.get_attribute('type') == 'checkbox':
#         input.click()


# 使用下标，可以选中某一个
# url = 'http://www.xqtesting.com/py_auto_homework8/se_class_demo/demo.html'
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get(url)
# time.sleep(2)
#
# inputs = driver.find_elements_by_tag_name('input')
# inputs[5].click()


print('------------------------------------标准的下拉框----------------------------------------------')

# from selenium.webdriver.support.ui import Select
# url = 'http://www.xqtesting.com/py_auto_homework8/se_class_demo/demo.html'
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get(url)
# time.sleep(2)
#
# # -----使用select
# Select(driver.find_element_by_id('classes')).select_by_index(1)
# time.sleep(2)
# Select(driver.find_element_by_id('classes')).select_by_value('python')
# time.sleep(2)
# Select(driver.find_element_by_id('classes')).select_by_visible_text('我爱小强')
# time.sleep(2)
#
# # # -----使用xpath
# driver.find_element_by_xpath(".//*[@id='classes']/option[2]").click()  # 括号里的数字是从1开始的，不是0


print('------------------------------------a标签-----------------------------------------------')

# url = 'http://www.xqtesting.com/py_auto_homework8/se_class_demo/demo.html'
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get(url)
# time.sleep(2)
#
# driver.find_element_by_link_text('百度搜索').click()
# # driver.find_element_by_xpath("html/body/b/b/a[1]").click()
# # driver.find_element_by_xpath("//a[@href='http://www.baidu.com/s?wd=小强测试品牌']").click()
# # driver.find_element_by_xpath("//a[contains(@href,'小强测试品牌')]").click()

print('-----------------------------------弹框-----------------------------------------------')

# alert
# url = 'http://www.xqtesting.com/py_auto_homework8/se_class_demo/demo.html'
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get(url)
# time.sleep(3)
#
# driver.find_element_by_id('alert').click()
# alert = driver.switch_to.alert
# print(alert.text)
# time.sleep(2)
# alert.accept()

# confirm
# url = 'http://www.xqtesting.com/py_auto_homework8/se_class_demo/demo.html'
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get(url)
# time.sleep(3)
#
# driver.find_element_by_id('confirm').click()
# confirm = driver.switch_to.alert
# print(confirm.text)
# time.sleep(2)
# confirm.accept()
# time.sleep(3)
#
# driver.find_element_by_id('confirm').click()
# confirm = driver.switch_to.alert
# print(confirm.text)
# time.sleep(2)
# confirm.dismiss()

# prompt
# url = 'http://www.xqtesting.com/py_auto_homework8/se_class_demo/demo.html'
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get(url)
# time.sleep(3)
#
# driver.find_element_by_id('prompt').click()
# prompt = driver.switch_to.alert
# print(prompt.text)
# time.sleep(2)
# prompt.dismiss()
# time.sleep(3)
# driver.get_screenshot_as_file('001.jpg')
# driver.back()
# time.sleep(3)
#
# driver.find_element_by_id('prompt').click()
# confirm = driver.switch_to.alert
# print(confirm.text)
# time.sleep(2)
# confirm.send_keys('哈哈哈哈')
# time.sleep(2)
# confirm.accept()
# time.sleep(3)
# driver.get_screenshot_as_file('002.jpg')
# driver.back()

print('-----------------------------------鼠标悬浮--------------------------------------------------')

# from selenium.webdriver.common.action_chains import ActionChains
# url = 'http://www.xqtesting.com/'
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get(url)
# time.sleep(3)
#
# e = driver.find_element_by_link_text('内部学员')
# ActionChains(driver).move_to_element(e).perform()
# time.sleep(2)
# driver.find_element_by_partial_link_text('百度').click()

print('-----------------------------------frame--------------------------------------------------')

# url = 'http://www.xqtesting.com/py_auto_homework8/se_class_demo/demo.html'
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get(url)
# time.sleep(3)
#
# driver.switch_to.frame('frame1')       # id定位
# # driver.switch_to.frame('myframe')    # name定位
# # driver.switch_to.frame(0)            # index索引定位，第一个是0
# driver.find_element_by_link_text('我为自己代言').click()

print('-----------------------------------多窗口切换------------------------------------------------')

# 逻辑：访问官网，获得句柄--->跳到新窗口之后，获得所有句柄---->for循环排除当前句柄，另一个就是新句柄

# url = 'http://www.xqtesting.com/'
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get(url)
# time.sleep(2)
#
# curr_handle = driver.current_window_handle
# print('title=', driver.title)
# print('curr_handle=', curr_handle)
#
# driver.find_element_by_link_text('脱口秀').click()
#
# all_handles = driver.window_handles
# print('all_handles', all_handles)
#
# for h in all_handles:
#     if h != curr_handle:
#         driver.switch_to.window(h)
# curr_handle = driver.current_window_handle
# print('title=', driver.title)
# print('curr_handle=', curr_handle)

print('-----------------------------------断言------------------------------------------------')

# driver = webdriver.Firefox()
# driver.get('http://www.xqtesting.com/user-login.html')
# time.sleep(5)
#
# driver.find_element_by_id('account').send_keys('fenci')
# driver.find_element_by_id('password').send_keys('xxxxxxxxxx')
# driver.find_element_by_id('submit').click()
# time.sleep(5)
#
# try:
#     assert 'fenci' in driver.find_element_by_xpath(".//*[@id='").text
#     print('有')
# except Exception as e:
#     print('无', str(e))
#
# time.sleep(5)
# driver.quit()
