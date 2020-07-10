# Generar reportes con HTML - TestRunner

# Test Plan
# Estructura para realizar una automatizar

import HtmlTestRunner
import unittest
from selenium import webdriver
import time

class suite(unittest.TestCase):

    def setUp(self): #agregar el driver desde su ruta
        self.driver = webdriver.Chrome(executable_path=r"C:\Automatizacion\driverchrome\chromedriver.exe")

    def test_busqueda(self):# Funciones
        self.driver.get("https://www.google.com/?hl=es")
        self.busqueda = self.driver.find_element_by_name("q")
        self.busqueda.send_keys("selenium")
        self.busqueda.submit()
        time.sleep(3)

    def test_scroll_down(self):
        self.driver.get("https://www.amazon.com/-/es/")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)

    def tearDown(self):#Limpiesa
        self.driver.quit()


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Resultados de mi Test'))
    


