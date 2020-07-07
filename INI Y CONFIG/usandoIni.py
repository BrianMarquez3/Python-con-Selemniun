# INIT

import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class usando_unitttest(unittest.TestCase):

    def setUp(self):
        configuracion = configparser.ConfigParser()
        configuracion.read('INI Y CONFIG\configuracion.ini')
        configuracion.sections()
        obtenerExplorer = configuracion['General']['chrome']
        self.page = configuracion['Paginas']['page']

        self.driver = webdriver.Chrome(executable_path=obtenerExplorer)

    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #segundo
        driver.get(self.page)
        navegador = driver.find_element_by_name("q")

if __name__ == "__main__":
    unittest.main()

