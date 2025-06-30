import pandas as pd
import json
import csv
from pathlib import Path 
import services.api.weatherApi as wApi
import sqlite3

response = wApi.Apiclass.weatherHist() 
dirDataW = Path("backend/app/data/dataW.csv")

class dataAnalisysClass():
    def extractData():
        #Si la API esta Ok se extraen los datos
        if response.status_code == 200:
            data = response.json()
            dataFilter = data["forecast"]["forecastday"][0]["hour"]#Se filtra "data" solo extrallendo el historial climático de un día durante sus 24h
            #print(json.dumps(dataFilter, indent=4, ensure_ascii=False)) #Imprime datos filtrados
            
            if dirDataW.is_file(): #Valida si ya se ha creado el archivo .csv
                print("Archivos ya creados!")
            else:
                #Se crea archivo .csv
                for item in dataFilter: 
                    item["condition"] = item["condition"]["text"] #Se filtran solo los datos deseados ("text") para la columna "condition"
                    
                headers = dataFilter[0].keys()
                with open("backend/app/data/dataW.csv", "w", newline="", encoding="utf-8") as fileW: #Convierte la data filtrada en archivo CSV
                    writer = csv.DictWriter(fileW, fieldnames=headers) 
                    writer.writeheader() #Se crean encabezados del archivo CSV
                    writer.writerows(dataFilter)
                    print("Archivo .CSV creado exitosamente!")
        else:
            print("Error al obtener datos", response.status_code)

    #Entregar análisis estadístico
    def statisticA():
        try:
            df = pd.read_csv("backend/app/data/dataW.csv")
            return df.describe()
        except FileNotFoundError:
            conn = sqlite3.connect("backend/app/data/dataWeather.db")
            print("Archivo no encontrado")
            df = pd.read_sql_query("SELECT * FROM dataWeather", conn)
            return df.describe()
            
        

