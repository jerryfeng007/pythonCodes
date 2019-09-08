# 搜索框
def search(driver, keyword):
    driver.find_element_by_id('words').send_keys(keyword)
    driver.find_element_by_class_name('btn-default').click()


# link_text
def link(driver, text):
    driver.find_element_by_link_text(text).click()
