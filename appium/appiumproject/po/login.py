# 登陆后返回用户名
def login(driver):
    # 点击购物车图标
    driver.find_element_by_id('com.xiaomi.shop2.plugin.hdchannel:id/iv_cart_grey').click()

    # 输入手机号
    driver.find_element_by_id('com.xiaomi.shop:id/et_account_name').send_keys('1860xxxxxxxx')

    # 输入密码
    driver.find_element_by_id('com.xiaomi.shop:id/et_account_password').send_keys('xxxxxxxx')

    # 点击登陆
    driver.find_element_by_id('com.xiaomi.shop:id/btn_login').click()

    # 点击返回按钮
    driver.find_element_by_id('com.xiaomi.shop2.plugin.hdchannel:id/iv_backLeftGrey').click()

    # 点击“我的”
    driver.find_element_by_id('com.xiaomi.shop.plugin.homepage:id/main_bottom_tab_mine_text').click()

    # 点击立即安装
    driver.find_element_by_id('com.xiaomi.shop.plugin.homepage:id/update_dialog_btn_ok').click()

    # 点击取消
    driver.find_element_by_id('com.android.packageinstaller:id/cancel_button').click()

    # 定位到用户名
    username = driver.find_element_by_id('com.xiaomi.shop.plugin.homepage:id/usercentral_listheader_username')

    # 返回用户名
    return username.text
