
from selenium import webdriver 
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("http://127.0.0.1:5500/ConfirmAlert/Alert.html")
time.sleep(3)
confirm_Simple = driver.find_element_by_name("Confirmar_alert")
confirm_Simple.click()
time.sleep(3)
confirm_Simple = driver.switch_to_alert()
confirm_Simple.accept()
time.sleep(3)
driver.close()
