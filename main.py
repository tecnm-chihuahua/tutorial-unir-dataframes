############################################
# Author: Jose Alejandro Melendez Garcia
# Date: 15-03-2023
############################################

import pandas as pd

# Leemos los CSV y extraemos en formato DataFrame
corriente = pd.read_csv("datos/ESP32-PZEM004-corriente.csv")
energia = pd.read_csv("datos/ESP32-PZEM004-energia.csv")
fp = pd.read_csv("datos/ESP32-PZEM004-fp.csv")
frecuencia = pd.read_csv("datos/ESP32-PZEM004-frecuencia.csv")
potencia = pd.read_csv("datos/ESP32-PZEM004-potencia.csv")

# Hacemos un rename de la columna value al valor representado 
# y almacenamos en una lista de dataframes
dataframes = [
    corriente.rename(columns={'value': 'corriente'}),
    energia.rename(columns={'value': 'energia'}),
    fp.rename(columns={'value': 'fp'}),
    frecuencia.rename(columns={'value': 'frecuencia'}),
    potencia.rename(columns={'value': 'potencia'}),
]

df = None

# Iteramos sobre los dataframes y hacemos merge en la columna time
for dataframe in dataframes:
    if df is None:
        df = dataframe
        continue
    df = df.merge(right=dataframe, on='time')

# Guardamos en un csv en el directorio output
df.to_csv('output/refri.csv', encoding='utf-8')

print("Se ha guardado el archivo correctamente. \n Este es el preview: \n\n")

# TIP:
# Se recomienda agregar como index_col=0 la primer columna para evitar 
# un duplicado de indices y que apareca como unamed.
print(pd.read_csv('refri.csv', index_col=0).head())
