import pandas as pd
import json
import csv
from pathlib import Path


df = pd.read_csv("backend/app/data/dataW.csv") #Se lee el archivo .csv
df["condition"] = df["condition"].str.replace("'", '"') #Adapto el formato a uno compatible para JSON
target = df["condition"].apply(json.loads) #Creo una variable para convertir los datos en JSON y almacenar mis datos target o resultados(y)
targetText = target.apply(lambda x: x["text"])
print(target)

dir = Path("backend/app/data/dataWTarget.csv")

if dir.is_file():
    print("Archivo target ya creado!")
else:
    headers = target[0].keys()
    with open("backend/app/data/dataWTarget.csv", "w", newline="", encoding="utf-8") as fileW: #Convierte la data filtrada en archivo CSV
        writer = csv.DictWriter(fileW, fieldnames=headers) 
        writer.writeheader() #Se crean encabezados del archivo CSV
        writer.writerows(target)
        print("Archivo .CSV creado exitosamente!")