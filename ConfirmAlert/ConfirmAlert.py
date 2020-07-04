
from selenium import webdriver 
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("http://127.0.0.1:5500/ConfirmAlert/Alert.html")
time.sleep(3)
#Alert_Simple = driver.find_element_by_name("alert")
#Alert_Simple.click()