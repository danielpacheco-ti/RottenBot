from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class DriverThreads(object):

    def get_driver(self):
        driver = self.__init_driver()
        while not driver:
            driver = self.__init_driver()
        return driver

    @staticmethod
    def __init_driver():

        try:
            options = Options()
            #options.add_argument("--headless")
            profile = webdriver.FirefoxProfile()
            binary = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            driver = webdriver.Firefox(firefox_options=options, firefox_profile=profile, firefox_binary=binary)
            driver.set_page_load_timeout(60)

            return driver

        except Exception as exc:
            print('Erro no webdriver: ', exc)
