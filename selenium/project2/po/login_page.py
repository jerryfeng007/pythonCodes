# 登陆
def input_box(driver, account, password):
    driver.find_element_by_xpath(".//*[@id='account']").send_keys(account)
    driver.find_element_by_xpath(".//*[@id='password']").send_keys(password)
    driver.find_element_by_id('submit').submit()


# 立即注册
def click(driver, text):
    driver.find_element_by_link_text(text).click()
