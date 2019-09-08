from selenium import webdriver
import time

print('------------------------利用cookies---实现免登录--------------------------------------------')

# 可以抓包看登陆前后的cookies，或者问开发

# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get("https://www.baidu.com")
# time.sleep(2)
#
# # 设置cookies
# c1 = {'domain': '.baidu.com', 'name': 'BDUSS',
#       'value': 'AAAAAAAAAAAEAAAB-8ag3utDX07frAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAArz2VoK89laSk',
#       'path': '/', 'httpOnly': True, 'secure': False}
#
# # 添加cookies
# driver.add_cookie(c1)
# time.sleep(3)
#
# # 刷新，发现登陆成功了
# driver.refresh()

print('------------------------利用profile---实现免登录--------------------------------------------')

# ff的profile文件路径查看方法：ff浏览器--帮助---故障排除信息---显示文件夹
# 必须手工登陆一次，且登陆有记住密码的选项并勾选，之后再运行此代码才可以
# 注意，这个有时效性，时间长了就会失效

# profile_ff = r"C:\Users\f\AppData\Roaming\Mozilla\Firefox\Profiles\ozb.default"
# fp = webdriver.FirefoxProfile(profile_ff)
# driver = webdriver.Firefox(fp)
#
# driver.get('https://www.baidu.com')
# driver.get('https://mail.163.com')

print('------------------------文件上传---文件下载-----------------------------------------')

# 文件上传
# url = 'http://www.xqtesting.com/py_auto_homework8/se_class_demo/demo.html'
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get(url)
# time.sleep(3)
#
# # 必须用绝对路径？
# driver.find_element_by_name('file').send_keys(r'D:\learnPY\from github\selenium\basic\002.jpg')


# 文件下载
# url = 'http://www.xqtesting.com/py_auto_homework8/se_class_demo/demo.html'
# profile_ff = r"C:\Users\f\AppData\Roaming\Mozilla\Firefox\Profiles\ozb.default"
# pf = webdriver.FirefoxProfile(profile_ff)
#
# # 指定下载路径
# pf.set_preference('browser.download.dir', 'D:\\learnPY\\from github\\selenium\\basic')
#
# # 设置为2表示使用自定义下载路径，0 表示下载到桌面，1表示下载到默认路径
# pf.set_preference('browser.download.folderList', 2)
#
# # 开始下载时是否显示下载管理器
# pf.set_preference('browser.download.manager.showWhenStarting', False)
#
# # 对所给出文件类型不再弹出框进行询问
# pf.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
#
# driver = webdriver.Firefox(pf)
# driver.maximize_window()
# driver.get(url)
# time.sleep(2)
# driver.find_element_by_link_text('点我下载').click()
# time.sleep(60)


print('-----------------------------------参数化------------------------------------------------')

# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get('https://www.baidu.com')
# time.sleep(3)
#
# with open('parameters.txt', encoding='gbk') as f:
#     for param in f:
#         driver.find_element_by_id('kw').clear()
#         driver.find_element_by_id('kw').send_keys(param)
#         driver.find_element_by_id('su').click()
#         time.sleep(3)
#
# driver.quit()

print('-----------------------------------视频播放------------------------------------------------')

'''
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://videojs.com')

video=driver.find_element_by_xpath(".//*[@id='preview-player_html5_api']")
url=driver.execute_script('return arguments[0].currentSrc;',video)
print('播放地址=',url)

duration=driver.execute_script('return arguments[0].duration;',video)
print('播放时长=',duration)

print('播放视频')
driver.execute_script('return arguments[0].play()',video)
time.sleep(10)

print('暂停视频')
driver.execute_script('arguments[0].pause',video)
time.sleep(10)
driver.quit()
'''

print('-----------------------------------日期元素------------------------------------------------')

# driver = webdriver.Firefox()
# url = 'http://www.xqtesting.com/py_auto_homework8/se_class_demo/demo.html'
# driver.maximize_window()
# driver.get(url)
# time.sleep(2)
#
# js = "document.getElementById('txtBeginDate').removeAttribute('readonly')"
# driver.execute_script(js)
#
# # 最好先clear再输入
# driver.find_element_by_id('txtBeginDate').clear()
# driver.find_element_by_id('txtBeginDate').send_keys('2018-11-11')
#
# # 也可以用js来输入
# # js = "document.getElementById('txtBeginDate').value='2018-11-11'"
# # driver.execute_script(js)

print('-----------------------------------表格------------------------------------------------')

driver = webdriver.Firefox()
url = 'http://www.xqtesting.com/py_auto_homework8/se_class_demo/demo.html'
driver.maximize_window()
driver.get(url)
time.sleep(2)

table = driver.find_element_by_id('table')

# table的总行数，包含标题
table_rows = table.find_elements_by_tag_name('tr')
print('总行数：', len(table_rows))

# table的总列数
# 在table中找到第一个tr,之后在其下找到所有的th,即是总列数
table_cols = table_rows[0].find_elements_by_tag_name('th')
print('总列数：', len(table_cols))

# 获取某单元格的文本，注意下标的取值
row2_col2 = table_rows[1].find_elements_by_tag_name('td')[1].text
print('第二行第二列：', row2_col2)

row2_col3 = table_rows[1].find_elements_by_tag_name('td')[2].text
print('第二行第三列：', row2_col3)

row3_col2 = table_rows[2].find_elements_by_tag_name('td')[1].text
print('第三行第二列：', row3_col2)
