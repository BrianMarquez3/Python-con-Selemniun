# Doble Click Mouse


import unittest
from selenium import webdriver # se Improta libreria
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

    def test_dobleclick(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/")
        time.sleep(4)
        dobleclick=self.driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/p")
        actions = ActionChains(self.driver)
        actions.double_click(dobleclick).perform()
        time.sleep(3)

    def tearDown(self):#Limpiesa
        self.driver.quit()

if __name__=='__main__':
    unittest.main()

