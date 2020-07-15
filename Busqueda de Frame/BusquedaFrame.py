# Busqueda de Flame
# Open Meet

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class suite(unittest.TestCase):

    def setUp(self): #agregar el driver desde su ruta
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

    def test_buscar_frame(self):
        driver = self.driver
        driver.get("https://www.google.com.pe/")
        time.sleep(3)
        click1 = driver.find_element_by_id("gbwa")
        time.sleep(3)
        click1.click()
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div[3]/iframe"))
        time.sleep(3)
        click2= driver.find_element_by_id("yDmH0d")
        time.sleep(2)
        click2.click()
        time.sleep(4)

    def tearDown(self):#Limpiesa
        self.driver.close()

if __name__=='__main__':
    unittest.main()