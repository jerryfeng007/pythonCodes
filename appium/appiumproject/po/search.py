# 搜索空气净化器
def search(driver):
    driver.find_element_by_id('com.xiaomi.shop2.plugin.hdchannel:id/fragment_search_swither').click()
    driver.find_element_by_id('com.xiaomi.shop2.plugin.search:id/input').send_keys('空气净化器')
    driver.find_element_by_id('com.xiaomi.shop2.plugin.search:id/search_fragment_search_btn').click()
