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
            profile = webdriver.FirefoxProfile(profile_directory='C:\\Users\\sug5824\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\csv57ylv.default-1532354219947')
            binary = 'C:\\Users\\sug5824\\AppData\\Local\\Microsoft\\AppV\\Client\\Integration\\A83ED08A-61E3-428B-AC93-4BD0D572786C\\Root\\VFS\\AppVPackageDrive\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
            driver = webdriver.Firefox(firefox_options=options, firefox_profile=profile, firefox_binary=binary)
            driver.set_page_load_timeout(60)

            return driver

        except Exception as exc:
            print('Erro no webdriver: ', exc)
