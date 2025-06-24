import pandas as pd
import json
import csv
from pathlib import Path
import requests 


#Solicitud GET a la API del endpoint history.json 
response = requests.get("http://api.weatherapi.com/v1/history.json", params={
    "key": "13014822709c4c27ac3214249251906",
    "q": "Tunja",
    "dt": "2025-06-21"
})

#Si la API esta Ok se extraen los datos
if response.status_code == 200:
    data = response.json()
    dataFilter = data["forecast"]["forecastday"][0]["hour"]#Se filtra data solo extrallendo el historial climático de un día durante sus 24h
    #print(json.dumps(dataFilter, indent=4, ensure_ascii=False)) #Imprime datos filtrados
    
    dir = Path("backend/app/data/dataW.csv")
    
    if dir.is_file(): #Valida si ya se ha creado el archivo .csv
        print("Archivos ya creados!")
    else:
        #Se crea archivo .csv
        headers = dataFilter[0].keys()
        with open("backend/app/data/dataW.csv", "w", newline="", encoding="utf-8") as fileW: #Convierte la data filtrada en archivo CSV
            writer = csv.DictWriter(fileW, fieldnames=headers) 
            writer.writeheader() #Se crean encabezados del archivo CSV
            writer.writerows(dataFilter)
            print("Archivo .CSV creado exitosamente!")
else:
    print("Error al obtener datos", response.status_code)



#Se extrae el target o variable y de dataW.csv

df = pd.read_csv("backend/app/data/dataW.csv") #Se lee el archivo .csv
df["condition"] = df["condition"].str.replace("'", '"') #Adapto el formato a uno compatible para JSON
target = df["condition"].apply(json.loads) #Creo una variable para convertir los datos en JSON y almacenar mis datos target o resultados(y)

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
        
