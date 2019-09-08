from project.po import base_page

# 该类主要是封装登陆页面的操作


class LoginPage(base_page.BasePage):
    # 访问>输入用户名、密码>点击登陆
    def input_account_password_run(self, url, account, password):
        self.open_max(url)
        self.input('id--account', account)
        self.input('id--password', password)
        self.click_submit('id--submit', click=False)
