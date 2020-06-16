#Select Con For

import unittest
from selenium import webdriver # se ImpoRta libreria
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys #Enviar Acciones de teclado
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

    def test_usando_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(3)
        select = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
        opcion = select.find_elements_by_tag_name("option")
        time.sleep(3)
        for option in opcion:
            print("Lo valores son: %s" % option.get_attribute("value"))
            option.click()
            time.sleep(3)
        selecionar = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        selecionar.select_by_value("10")

if __name__ == '__main__':
    unittest.main()