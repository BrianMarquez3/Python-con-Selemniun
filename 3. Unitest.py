#como usar unitest
import unittest
from selenium import webdriver # se Improta libreria
from selenium.webdriver.common.keys import Keys #Enviar Acciones de teclado
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\driverchrome\chromedriver.exe")

    def test_buscar(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)#Confirmacion que entras a la pagina
        #Buscar un elemento
        elemento=driver.find_element_by_name("q")
        elemento.send_keys("selenium")
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontro el elemento" not in driver.page_source

    def tearDown(self):#cerrar el driver
        self.driver.close()

if __name__ == '__main__':
    unittest.main()