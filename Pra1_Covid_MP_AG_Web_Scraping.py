# -*- coding: utf-8 -*-

#    ------------------ IMPORTACIÓ LLIBRERIES ----------------------
from bs4 import BeautifulSoup
import requests
import time
import os

#    ------------------  WEB SCRAPING  ---------------------
# Seleccionem la pàgina:
url = "https://www.worldometers.info/coronavirus/#countries"

# Baixem el codi de la pàgina:
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

# Definim el fitxer .csv on guardarem les dades i definim variables:
csv = "C:\python\Covid.csv"
fichero = open(csv, 'a+')

#Comprovem si el fitxer existeix, si no  es crearà i s'afegirà la capçalera amb el títol del camps
EscriureTitol=False
if os.stat("C:\python\Covid.csv").st_size == 0:
    EscriureTitol =True

# Afegim la data del dia en què hem baixat les dades, si no hem d'escriure la capçalera:
if EscriureTitol == False:   
    fichero.write(time.strftime("%d/%m/%y")+";") 

# Cerquem la capçalera de la taula a "rascar" i baixem les dades per a Europa:
taula_europa = soup.findAll("table", id="main_table_countries_today" )
for i in taula_europa:
    #capçalera del .csv només quan es fitxer no te res
    if EscriureTitol == True:
        titol = i.find('tr').get_text()
        fichero.write(";Europe;;;;;;;;Spain;;;;;;;")
        fichero.write('\n')
        titol_net= titol.split(sep='\n')
        fichero.write("Date;")
        titol_net= titol_net[3:13]
        text =""
        for j in range(8):
            text = text + titol_net[j]+";"   
        fichero.write(text)
        fichero.write(text)
        fichero.write('\n')
        fichero.write(time.strftime("%d/%m/%y")+";")
    resum = i.find('tr', attrs={'data-continent':"Europe"}).get_text()
    totalsEuropa = resum.split(sep='\n')


# Extraiem les dades del total d'Europa que ens interessen i en netegem el format:  
totalsEuropa_netes = totalsEuropa[5:13]
for j in range(8):
    text=totalsEuropa_netes[j]
    text=text.replace('\n',"")
    text=text.replace(',',"")
    text=text.replace('+',"") 
    fichero.write(text+';')


# Extraiem les dades per a l'Estat Espanyol que ens interessen i en netegem el format:
espanya = soup.find(href="country/spain/").parent.find_next_siblings()
for j in range(8):
    text =espanya[j].get_text()
    text=text.replace('\n',"")
    text=text.replace(',',"")
    text=text.replace('+',"")
    fichero.write(text+';')

fichero.write('\n')



