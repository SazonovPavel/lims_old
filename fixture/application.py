from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.first_application import FirstApplicationHelper


class Application:

    def __init__(self):
        # self.wd = WebDriver(executable_path='tools//chromedriver.exe')
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(15)
        self.session = SessionHelper(self)
        self.first_application = FirstApplicationHelper(self)

    def open_home_page(self):
        wd = self.wd
# Stage
#        wd.get('http://lims-stage.bitsoft.com.ua')
# Test
        wd.get('http://lims-test.bitsoft.com.ua/')
# Dev
#        wd.get('http://lims-dev.bitsoft.com.ua')



    def destroy(self):
        self.wd.quit()
