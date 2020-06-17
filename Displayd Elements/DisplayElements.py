#Display Elements

from selenium import webdriver # se Improta libreria
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(3)
displayelem = driver.find_element_by_name("btnI")
print(displayelem.is_displayed()) #True False
print(displayelem.is_enabled())



        
