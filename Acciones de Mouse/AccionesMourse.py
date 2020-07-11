# Acciones del Mouse
# 

import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class suite(unittest.TestCase):

    def setUp(self): #agregar el driver desde su ruta
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

    def test_manejando_mouse(self): # si el titulo es correcto
        self.driver.get("https://nicolasalvarez.com/#")
        time.sleep(4)
        mouse_mov=self.driver.find_element_by_xpath("//*[@id='menu-item-68']/a")
        mouse_mov2=self.driver.find_element_by_xpath("//*[@id='menu-item-82']/a")
        movimiento=ActionChains(self.driver)
        movimiento.move_to_element(mouse_mov).move_to_element(mouse_mov2).click().perform()
        #movimiento.move_to_element(mouse_mov).click().perform()

        time.sleep(3)


    def tearDown(self):#Limpiesa
        self.driver.quit()

if __name__=='__main__':
    unittest.main()




