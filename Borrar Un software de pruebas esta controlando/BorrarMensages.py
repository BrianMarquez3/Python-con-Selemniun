# Borrar el mensage de Un software de prueba esta controlando chrome

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class suite(unittest.TestCase):

    def setUp(self): 

        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe", options=chrome_options)

    def test_buscar_frame(self):
        driver = self.driver
        driver.get("https://github.com/BrianMarquez3/Python-with-Selenium")
        time.sleep(3)

    def tearDown(self):#Limpiesa
        self.driver.close()

if __name__=='__main__':
    unittest.main()