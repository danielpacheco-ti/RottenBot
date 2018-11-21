import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from settings import PASSWORD, LOGIN


class General(object):

    def login(self, driver):
        try:
            driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(LOGIN)
            time.sleep(2)
            driver.find_element_by_name('password').send_keys(PASSWORD)
            time.sleep(2)
            driver.find_element_by_class_name('oF4XW.sqdOP.L3NKy').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "aOOlW.HoLwm"))).click()
            print("Login efetuado com sucesso!")
            return True

        except Exception as exc:
            print("ERRO: ", exc)
