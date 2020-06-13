# Pagina siguiente o anterior
#Abrir Pesatañas del Navegador Chrome


import unittest
from selenium import webdriver # se Improta libreria
from selenium.webdriver.common.keys import Keys #Enviar Acciones de teclado
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

    def test_pagin_sigueinte_o_anterior(self):
        driver=self.driver
        driver.get("https://www.gmail.com")#todas las paginas cargaran en un misma pestaña
        time.sleep(3)
        driver.get("https://www.google.com")
        time.sleep(3)
        driver.get("https://www.youtube.com")
        time.sleep(3)
        driver.back()#atras
        time.sleep(3)
        driver.back()#gmail.com
        time.sleep(3)
        driver.forward()#adelante
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()     