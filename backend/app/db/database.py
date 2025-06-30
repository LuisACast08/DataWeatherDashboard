import pandas as pd
import sqlite3
from pathlib import Path 

dirDataW = Path("backend/app/data/dataW.csv")

class dataWeatherDB():
    #test SQlite
    def migrarCSV():
        if dirDataW.is_file():
                #Creación db/conexión db
                connx = sqlite3.connect("backend/app/data/dataWeather.db")
                
                #Se lee el .csv con pandas
                df = pd.read_csv("backend/app/data/dataW.csv")
                
                #Se migra a SQlite
                df.to_sql("dataWeather", connx, if_exists="replace", index=False)
                
                connx.close()
                
                print("Migración exitosa!")
        else:
            print("Archivo no encontrado!")

