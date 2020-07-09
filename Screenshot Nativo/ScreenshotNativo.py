# Captura de pantalla con selenium
# screnshop Nativo

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Automatizacion\driverchrome\chromedriver.exe")
driver.get("https://github.com/BrianMarquez3")
driver.get_screenshot_as_file("C:\\Users\\brian\\Documents\\Python-with-Selenium\\Screenshot Nativo\\mi_perfil.png")
driver.quit()
