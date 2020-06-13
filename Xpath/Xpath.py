#Xparth
#Relatiivo y Absoluto
#¿que es Xpath? es una estructura de carpetas, objetos


import unittest
from selenium import webdriver # se Improta libreria
from selenium.webdriver.common.keys import Keys #Enviar Acciones de teclado
import time
class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\driverchrome\chromedriver.exe")

    def test_buscar_por_xpath(self):
        driver=self.driver
        driver.get("https://www.google.com")
        time.sleep(3)
        buscar_por_xpath=driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")#xpath relativo
        time.sleep(3)
        buscar_por_xpath.send_keys("selenium", Keys.ARROW_DOWN) #HACE UN TECHA HACI ABAJO _:usado para sleecioanr el la busqueda
        time.sleep(3)

    def tearDown(self):#cerrar el driver
        self.driver.close()

if __name__ == '__main__':
    unittest.main()        
        



#existen 2 tipos de Xpath
#EXPATH RELATIVO:  Parte de un nodo especifico, busca el todo el arbol sin importa su cambio de ubicacion
#EJEMPLO: //*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input

#EXPATH ABSOLUTO: es tda la direccion de la carpeta, arbol, no muy usado


