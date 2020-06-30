#extracion de Informacion

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(3)

valor = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[2]/td[2]").text
print(valor)

ross=len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
col=len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))

print(ross)
print(col)

for n in range(2, ross+1):
    for b in range (1, col+1):
        dato=driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text
        print(dato, end='                                                       ')
    print()