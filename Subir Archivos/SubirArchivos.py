# Subir Archivos
# 

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class suite(unittest.TestCase):

    def setUp(self): #agregar el driver desde su ruta
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

    def test_subir_archivo(self): # si el titulo es correcto
        self.driver.get("https://mdbootstrap.com/plugins/jquery/file-upload/")
        time.sleep(4)
        self.driver.find_element_by_id("input-file-now").send_keys("C:\\Users\\brian\\Documents\\Python-with-Selenium\\Subir Archivos\\image.png")
        time.sleep(3)

    def tearDown(self):#Limpiesa
        self.driver.close()

if __name__=='__main__':
    unittest.main()

