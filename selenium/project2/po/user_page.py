# 退出
def element(driver, keyword):
    return driver.find_element_by_link_text(keyword).text
