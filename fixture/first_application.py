import time

class FirstApplicationHelper:

    def __init__(self, app):
        self.app = app

    def create_production_protocols(self):
        wd = self.app.wd
        # У меню з ліва обираємо пункт «Ліцензування виробництва ЛЗ»
        wd.find_element_by_xpath("//span[contains(text(), 'Ліцензування виробництва ЛЗ')]").click()

        # У меню з ліва обираємо пункт «Журнал протоколів»
        wd.find_element_by_xpath("//tr[@id='ctl00_21_1']").click()

        # У меню з ліва обираємо пункт «Журнал протоколів»
        wd.find_element_by_xpath("//a[@id='ctl00_Content_hlAddProtocol']").click()

        wd.get('http://lims-stage.bitsoft.com.ua/PRC/ProtocolDetail_01_General.aspx?mode=a')

        time.sleep(2)



        # Ввводимо № протоколу
        wd.find_element_by_xpath("//input[@id='ctl00_Content_gridDetail_ProtocolNum']").send_keys("Z-1")
        # Ввводимо дату протоколу
        wd.find_element_by_xpath("//input[@id='ctl00_Content_gridDetail_ProtocolDate']").send_keys("01.08.2019")
        # Ввводимо № наказу
        wd.find_element_by_xpath("//input[@id='ctl00_Content_gridDetail_OrderNum']").send_keys("Z-1")
        # Ввводимо дату протоколу
        wd.find_element_by_xpath("//input[@id='ctl00_Content_gridDetail_OrderDate']").send_keys("01.08.2019")
        # Нажимаем кнопку "Зберегти"
#        wd.find_element_by_xpath("//input[@id='ctl00_Content_UpdateButton']").click()



        time.sleep(10)














