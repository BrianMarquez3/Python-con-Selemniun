# Click Derecho

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class suite(unittest.TestCase):

    def setUp(self): #agregar el driver desde su ruta
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

    def test_clickderecho(self):
        self.driver.get("https://www.w3schools.com/")
        time.sleep(3)
        clickderecho = self.driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/h1")
        actions= ActionChains(self.driver)
        actions.context_click(clickderecho).perform()
        time.sleep(3)

    def tearDown(self):#Limpiesa
        self.driver.close()

if __name__=='__main__':
    unittest.main()






