from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"D:\driverchrome\chromedriver.exe")#Ubicacion de Driver de Chrome
driver.get("http://www.python.org")
driver.close()
#driver.stop()