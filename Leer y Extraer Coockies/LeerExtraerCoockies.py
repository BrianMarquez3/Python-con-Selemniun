# Manejo de Coockies

# INIT

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(executable_path=r"C:\Automatizacion\driverchrome\chromedriver.exe")
driver.get("https://www.w3schools.com/")
time.sleep(5)

all_coockies = driver.get_cookies()
print(all_coockies)
driver.close()

