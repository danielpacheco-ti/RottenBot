import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util import util

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
        util.wait()
        self.driver.find_element_by_xpath("/html/body/span/section/main/div/header/section/ul/li[2]/a").click()
        dialog = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]")))
        last_height = 100
        for x in range(1, 30):
            last_height = self.__scroll(last_height, dialog)
            if not last_height:
                break

        perfis = dialog.find_elements_by_tag_name('button')
        self.__perfil_click(perfis)

    def __perfil_click(self, perfis):
        try:
            for perfil in perfis:
                if perfil.text == "Seguir":
                    perfil.click()
                else:
                    print('Já solicitado')
                util.wait()
        except:
            pass

    def __scroll(self, last_height, dialog):
        SCROLL_PAUSE_TIME = 0.5

        self.driver.execute_script("arguments[0].scrollTo(0, " + str(last_height) + ");", dialog)
        time.sleep(SCROLL_PAUSE_TIME)

        last_height += 100
        new_height = self.driver.execute_script("return arguments[0].scrollHeight", dialog)
        if new_height <= last_height:
            return None

        return last_height
