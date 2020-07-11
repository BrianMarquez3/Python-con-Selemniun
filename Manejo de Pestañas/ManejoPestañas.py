# Asser Not Equal
# Abir en una nueva pestaña

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class suite(unittest.TestCase):

    def setUp(self): #agregar el driver desde su ruta
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

    def test_manejando_ventanas(self): # si el titulo es correcto
        self.driver.get("https://www.google.com/intl/es/gmail/about/#")
        time.sleep(3)
        siguiente=self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/ul[1]/li/div/div/div[1]/div/div[3]/a[1]")
        siguiente.click()
        print(self.driver.current_window_handle)
        time.sleep(3)

        handles=self.driver.window_handles
        for handle in handles:
            self.driver.switch_to_window(handle)
            print(self.driver.title)

    def tearDown(self):#Limpiesa
        self.driver.quit()

if __name__=='__main__':
    unittest.main()




