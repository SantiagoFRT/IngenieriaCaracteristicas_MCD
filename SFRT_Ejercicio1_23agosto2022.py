### Ejercicio 1
### Ingenieria de caracteristicas de ciencia de datos, Unison
### Santiago Francisco Robles Tamayo
### Martes 23 de agosto, 2022

# -------------

import os  # Para manejo de archivos y directorios
import urllib.request # Una forma estandard de descargar datos
# import requests # Otra forma no de las librerías de uso comun

import datetime # Fecha de descarga
import pandas as pd # Solo para ver el archivo descargado
import zipfile # Descompresión de archivos

#-----------

# print(os.getcwd()) este comando imprime el nombre de la ruta de trabajo. 

#  Estos son los datos que vamos a descargar y donde vamos a guardarlos
desaparecidos_RNPDNO_url = "http://www.datamx.io/dataset/fdd2ca20-ee70-4a31-9bdf-823f3c1307a2/resource/d352810c-a22e-4d72-bb3b-33c742c799dd/download/desaparecidos3ago.zip"
desaparecidos_RNPDNO_archivo = "desaparecidosRNPDNO.zip"
desaparecidos_corte_nacional_url = "http://www.datamx.io/dataset/fdd2ca20-ee70-4a31-9bdf-823f3c1307a2/resource/4865e244-cf59-4d39-b863-96ed7f45cc70/download/nacional.json"
desaparecidos_corte_nacional_archivo = "desaparecidos_nacional.json"
subdir = "./data/"

#---

if not os.path.exists(desaparecidos_RNPDNO_archivo):        # esta linea es si no se tiene la base de datos en tu directorio de trabajo

    if not os.path.exists(subdir):                          # Si no existe una carpeta en tu directorio de trabajo llamada "data" (subdir)

        os.makedirs(subdir)                                 # si se entra al if , se crea esa carpeta llamada "data" (subdir)

    urllib.request.urlretrieve(desaparecidos_RNPDNO_url, subdir + desaparecidos_RNPDNO_archivo)  # del URL guardado en tu variable, "desaparecidos_RNPDNO_url", 
                                                                                                # descarga el archivo .zip en la carpeta "data" (subdir) usando
                                                                                                # el nombre "desaparecidosRNPDNO.zip" guardado en 
                                                                                                # "desaparecidos_RNPDNO_archivo"

    with zipfile.ZipFile(subdir + desaparecidos_RNPDNO_archivo, "r") as zip_ref:                # Lee el contenido del archvio .zip con el nombre "desaparecidosRNPDNO.zip"
                                                                                                # guardado en la variable "desaparecidos_RNPDNO_archivo", que se encuentra
                                                                                                # dentro de la carpeta "data" (subdir)

        zip_ref.extractall(subdir)                                                              # se extrar el contenido de la variable creada en el rengló n anterior, 
                                                                                                # llamada "zip_ref", que se guarda en la carpeta "data" (subdir)
    
    urllib.request.urlretrieve(desaparecidos_corte_nacional_url, subdir + desaparecidos_corte_nacional_archivo)   # del URL guardado en tu variable, 
                                                                                                # "desaparecidos_corte_nacional_url", 
                                                                                                # descarga el archivo json en la carpeta "data" (subdir) para guardarlo
                                                                                                # con el nombre "desaparecidos_nacional.json" en el directorio de trabajo,
                                                                                                # pero llamado "desaparecidos_corte_nacional_archivo" en el código
                                                                                                

    with open(subdir + "info.txt", 'w') as f:
        f.write("Archivos sobre personas desaparecidas\n")
        info = """
        Datos de desaparecidos, corte nacional y desagregación a nivel estatal, por edad, por sexo, 
        por nacionalidad, por año de desaparición y por mes de desaparición para los últimos 12 meses.

        Los datos se obtuvieron del RNPDNO con fecha de 23 de agosto de 2021 (la base de datos se actualiza constantemente) 

        """ 
        f.write(info + '\n')
        f.write("Descargado el " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write("Desde: " + desaparecidos_RNPDNO_url + "\n")
        f.write("Nombre: " + desaparecidos_RNPDNO_archivo + "\n")
        f.write("Agregados nacionales descargados desde: " + desaparecidos_corte_nacional_url + "\n")
        f.write("Nombre: " + desaparecidos_corte_nacional_archivo + "\n")



###### Segunda base de datos ##### 

#  Estos son los datos que vamos a descargar y donde vamos a guardarlos
covid_Hermosillo_url = "https://raw.githubusercontent.com/dogomoreno/Covid19-Sonora-Municipios/master/Bases/Hermosillo%20150821.csv"
covid_Hermosillo_archivo = "covid_Hermosillo.csv"


if not os.path.exists(covid_Hermosillo_archivo): 

    urllib.request.urlretrieve(covid_Hermosillo_url, covid_Hermosillo_archivo) #quitamos la parte " subdir +" porque no creamos
                                                                                            # un subdirectorio de trabajo

                                                                                            