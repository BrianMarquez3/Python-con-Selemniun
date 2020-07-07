# Trabajando con Archivos - INI / .CONFIG

import configparser
configuracion = configparser.ConfigParser()

configuracion['General'] = {'chrome' : 'D:\Automatizacion\driverchrome\chromedriver.exe'}
configuracion['Paginas'] = {'page': 'https://www.google.com'}

with open('configuracion.ini', 'w') as archivoconfi():
    configuracion.write(archivoconfig)