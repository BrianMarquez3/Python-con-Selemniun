#Expliat Wait

import unittest
from selenium import webdriver # se Improta libreria
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

    def test_usando_explicit_wait(self):
        driver = self.driver
        driver.get("https://www.google.com")
        try:
            element = WebDriverWait(driver, 10).until(#QUE tiene en google intentalo 10 veces
            EC.presence_of_element_located((By.NAME,"q"))) # con el nombre q
        finally:
            driver.quit()


if __name__ == '__main__':
    unittest.main()     