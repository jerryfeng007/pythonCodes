# xpath操作
def xpath(driver):
    # 点击返回按钮
    driver.find_element_by_id('com.xiaomi.shop2.plugin.hdchannel:id/iv_backLeftGrey').click()

    driver.find_element_by_xpath(
        '//android.widget.RelativeLayout[contains(@index, "2")]/android.widget.ImageView[contains(@index, "2")]'
        ).click()
