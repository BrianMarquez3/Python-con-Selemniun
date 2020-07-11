# AsserEqual
# 

import unittest
from selenium import webdriver
import time

class suite(unittest.TestCase):

    def setUp(self): #agregar el driver desde su ruta
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

    def test_assertEqual(self): # si el titulo es correcto
        driver = self.driver
        driver.get("https://www.google.com/?hl=es")
        titulodelagin = driver.title
        time.sleep(2)
        self.assertEqual("Google", titulodelagin, "El titulo de la pagina no es igual")# titulo

    def tearDown(self):#Limpiesa
        self.driver.quit()

if __name__=='__main__':
    unittest.main()




