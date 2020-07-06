#Prompt Alert

from selenium import webdriver # se Improta libreria
import time

driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

driver.get("http://127.0.0.1:5500/Prompt%20Alert/prompt.html")
time.sleep(3)
alert = driver.find_element_by_name("prompt_alert")
alert.click()
time.sleep(3)
alert = driver.switch_to_alert()
alert.accept() # decision
#alert.accept() # decision
time.sleep(3)
driver.close()
