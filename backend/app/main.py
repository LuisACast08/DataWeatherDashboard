import services.dataAnalysis as SDataA
import db.database as db 
import services.api.routes as rt

#Inicio el servicio para crear data .csv
dataA = SDataA.dataAnalisysClass
dataA.extractData()

#Inicio servicio para crear backup en SQlite
backup = db.dataWeatherDB
backup.migrarCSV()

#Inicio servidor
rt.executeServer()