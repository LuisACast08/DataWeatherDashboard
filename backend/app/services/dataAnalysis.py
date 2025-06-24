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

def extractData():
    #Si la API esta Ok se extraen los datos
    if response.status_code == 200:
        data = response.json()
        dataFilter = data["forecast"]["forecastday"][0]["hour"]#Se filtra "data" solo extrallendo el historial climático de un día durante sus 24h
        #print(json.dumps(dataFilter, indent=4, ensure_ascii=False)) #Imprime datos filtrados
        
        dir = Path("backend/app/data/dataW.csv")
        
        if dir.is_file(): #Valida si ya se ha creado el archivo .csv
            print("Archivos ya creados!")
        else:
            #Se crea archivo .csv
            for item in dataFilter: 
                item["condition"] = item["condition"]["text"] #Se filtran solo los datos deseados ("text")
                
            headers = dataFilter[0].keys()
            with open("backend/app/data/dataW.csv", "w", newline="", encoding="utf-8") as fileW: #Convierte la data filtrada en archivo CSV
                writer = csv.DictWriter(fileW, fieldnames=headers) 
                writer.writeheader() #Se crean encabezados del archivo CSV
                writer.writerows(dataFilter)
                print("Archivo .CSV creado exitosamente!")
    else:
        print("Error al obtener datos", response.status_code)

extractData()
        
