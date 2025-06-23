import pandas as pd
import json
import csv
from pathlib import Path

#Se extrae el target o variable y de dataW.csv

df = pd.read_csv("backend/app/data/dataW.csv") #Se lee el archivo .csv
df["condition"] = df["condition"].str.replace("'", '"') #Adapto el formato a uno compatible para JSON
target = df["condition"].apply(json.loads) #Creo una variable para convertir los datos en JSON y almacenar mis datos target o resultados(y)
print(target)

dir = Path("backend/app/data/dataWTarget.csv")

if dir.is_file():# Comprueba si ya se ha creado el archivo
    print("Archivo target ya creado!")
else:
    for i, item in enumerate(target): #Recorro "target" eliminando los datos no deseados de su .json
        if "icon" or "code" in target[i]:
            del target[i]["icon"], target[i]["code"]
    
    #Convierte la data filtrada en archivo CSV
    headers = target[0].keys()
    with open("backend/app/data/dataWTarget.csv", "w", newline="", encoding="utf-8") as fileW: 
        writer = csv.DictWriter(fileW, fieldnames=headers) 
        writer.writeheader() #Se crean encabezados del archivo CSV
        writer.writerows(target)
        print("Archivo .CSV creado exitosamente!")
        
