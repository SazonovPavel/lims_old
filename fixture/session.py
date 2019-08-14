import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, name, password):
        wd = self.app.wd
        self.app.open_home_page()
        # Користувач
        wd.find_element_by_xpath("//input[@id='edtUserName']").send_keys(name)

        # Пароль
        wd.find_element_by_xpath("//input[@id='edtPassword'] ").send_keys(password)

        # 13 Проверяю наличие элемента (заголовок Портал Держликслужбы)
        wd.find_element_by_name("LoginButton").click()

        time.sleep(1)

        # 13 Проверяю наличие элемента (заголовок Єдина автоматизована інформаційна система)
        wd.find_element_by_xpath("//td[contains(text(), 'Єдина автоматизована інформаційна система')]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@id='ctl00_hlLogout']").click()
        time.sleep(1)
        # Проверяю наличие эленмента (Заголовок)
        wd.find_element_by_xpath("//span[@id='lbTitle']")
