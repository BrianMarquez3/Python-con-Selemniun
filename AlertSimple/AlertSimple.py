#Busqueda

from selenium import webdriver 
import time

driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")
driver.get("http://127.0.0.1:5500/AlertSimple/Alert.html")
time.sleep(3)
Alert_Simple = driver.find_element_by_name("alert")
Alert_Simple.click()
time.sleep(3)
Alert_Simple = driver.switch_to_alert()
Alert_Simple.dismiss()
time.sleep(3)
driver.close()

