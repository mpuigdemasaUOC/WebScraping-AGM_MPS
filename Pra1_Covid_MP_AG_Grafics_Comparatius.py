# -*- coding: utf-8 -*-

# ------------ GENERACIÓ DE GRÀFIQUES COMPARATIVES ---------------
# Importem llibreries
import pandas as pd
import matplotlib.pyplot as plt
# Carreguem amb pandas el fitxer Covid.csv com un dataframe:
dadescovid=pd.read_csv("Covid.csv", sep=';', index_col=0, header=1) 
# Seleccionem el nom de les fileres, la data, com a variable per a l'eix de les x:
x=dadescovid.index
# Iteracionem amb un for-loop sobre els primeres 8 columnes per a recòrrer totes les variables:
for i in list(range(8)):
    # Seleccionem la columna corresponent al conjunt d'Europa:
    y=dadescovid.iloc[:,i]
    # Seleccionem la columna corresponent a l'Estat Espanyol:
    y2=dadescovid.iloc[:,(i+8)]
    # Muntem un gràfic de línies per a ambdues variables:
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(x, y, label='Europa')
    ax.plot(x, y2, label='Estat Espanyol')
    plt.legend(loc='upper left')
    plt.ylabel(dadescovid.columns[i])
    plt.xticks(rotation=45)
    plt.xlabel('Dia')
    plt.savefig(str(dadescovid.columns[i]), bbox_inches='tight')
    plt.show()
    plt.close()
