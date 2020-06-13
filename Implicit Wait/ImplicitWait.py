#Implicit Wait
#Esperar un tiempo para que se carge un componente
#rango de espera

import unittest
from selenium import webdriver # se Improta libreria
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")
    
    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #Espera 5 segundos
        driver.get("https://www.google.com")
        myDynamicElement = driver.find_elements_by_name("q") #componente dinamico
        
if __name__ == '__main__':
    unittest.main()     

