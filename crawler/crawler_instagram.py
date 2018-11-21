import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CrawlerInsta(object):

    def start(self, driver, artist):
        try:
            self.count = 0
            self.driver = driver
            self.artist = artist
            self.invalid_artist = False

            while not self.__follow():
                pass

            if not self.invalid_artist:
                return True

        except Exception as exc:
            print("ERRO: ", exc)
            return None

    def __follow(self):
        try:
            print(self.artist)
            print("Acessando perfil de artista")
            if self.__acess_artist():
                print("Captando seguidores")
                self.__get_followers()

            return True

        except Exception as exc:
            print("ERRO: ", exc)

    def __acess_artist(self):
        url = "https://www.instagram.com/%s" % self.artist
        self.driver.get(url)
        return True

    def __get_followers(self):
        self.driver.find_element_by_xpath("/html/body/span/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(1)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "oF4XW.sqdOP.L3NKy")))
        perfis = self.driver.find_elements_by_class_name("oF4XW.sqdOP.L3NKy")
        for perfil in perfis:
            perfil.click()
        return True
