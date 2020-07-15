# Descargar Archivos

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class suite(unittest.TestCase):

    def setUp(self): 
        chromeOptions=Options()
        chromeOptions.add_experimental_option("prefs", 
        {
            "download.default_directory" : "D:\\Automatizacion",
        })
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe", chrome_options=chromeOptions)

    def test_descargando_archivos(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")
        time.sleep(3)
        driver._switch_to.frame(driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div/iframe"))
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/p[2]/a/img").click()
        time.sleep(3)

    def tearDown(self):#Limpiesa
        self.driver.close()

if __name__=='__main__':
    unittest.main()