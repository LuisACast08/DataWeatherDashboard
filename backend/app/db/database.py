import pandas as pd
import sqlite3

class dataWeatherDB():
    #test SQlite
    def migrarCSV():
        #Creación db/conexión db
        connx = sqlite3.connect("dataWeather.db")
        
        #Se lee el .csv con pandas
        df = pd.read_csv("backend/app/data/dataW.csv")
        
        #Se migra a SQlite
        df.to_sql("dataWeather", connx, if_exists="replace", index=False)
        
        connx.close()
        
        print("Migración exitosa!")
