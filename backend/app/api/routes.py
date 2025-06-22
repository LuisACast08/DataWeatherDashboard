import requests #Se importa "requests" para hacer solicitudes HTTP
import csv
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import pandas as pd

#Solicitud GET del endpoint history.json 

response = requests.get("http://api.weatherapi.com/v1/history.json", params={

    "key": "13014822709c4c27ac3214249251906",
    "q": "Tunja",
    "dt": "2025-06-21"
})

#Muestra los datos del historial climático de un día durante sus 24h
if response.status_code == 200:
    data = response.json()
    dataFilter = data["forecast"]["forecastday"][0]["hour"]
    headers = dataFilter[0].keys()
    dir = Path("backend/app/data/dataW.csv")
    # print(json.dumps(dataFilter, indent=4, ensure_ascii=False)) #Imprime datos filtrados
    
    if dir.is_file(): #Valida si ya se ha creado el archivo .csv
        print("Archivos ya creados!")
    else:
        #Se crea archivo .csv
        with open("backend/app/data/dataW.csv", "w", newline="", encoding="utf-8") as fileW: #Convierte la data filtrada en archivo CSV
            writer = csv.DictWriter(fileW, fieldnames=headers) 
            writer.writeheader() #Se crean encabezados del archivo CSV
            writer.writerows(dataFilter)
            print("Archivo .CSV creado exitosamente!")
            
        #Se crea archivo .xlsx a partir del archivo .csv
        df= pd.read_csv("backend/app/data/dataW.csv") #Crea dataframe del archivo "dataW.csv"
        df.to_excel("backend/app/data/dataW.xlsx", index= False, engine="openpyxl")
        print("Archivo .XLSX creado exitosamente!")
else:
    print("Error al obtener datos", response.status_code)

#Test endpoint con http.server
    #Se crea una clase para manipular o responder a las solicitudes "GET, POST, PUT, etc..."

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        match self.path:
            case "/":
                self.send_response(200)
                self. send_header("Content-type", "application/json")
                self.end_headers()
                message = {"message": "Welcome to my application API!"}
                self.wfile.write(json.dumps(message).encode())
            case "/current":
                self.send_response(200)
                self. send_header("Content-type", "application/json")
                self.end_headers()
                if response.status_code == 200:
                    message = response.json()
                else:
                    message = {"message": "Error"+ response.status_code}
                self.wfile.write(json.dumps(message).encode())
            case "/data":
                if response.status_code == 200:
                    try:
                        dfXlsx = pd.read_excel("backend/app/data/dataW.xlsx") #Se lee el archivo Excel
                        htmlTable = dfXlsx.to_html(index=False, border=1, classes="tabla", justify="center") #Se convierte a formato HTML
                        
                        self.send_response(200)
                        self. send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write(htmlTable.encode("utf-8")) #Se muestra tabla
                    except FileNotFoundError:
                        self.send_response(404)
                        self.end_headers()
                        self.wfile.write("Archivo .xlsx no encontrado.")
                else:
                    message = {"message": "Error"+ response.status_code}
                    self.wfile.write(json.dumps(message).encode())

#Config del servidor
def executeServer():
    port = 8000
    server = HTTPServer(("localhost", port), Handler)
    print(f"Servidor corriendo en http://localhost:{port}")
    server.serve_forever()
    
#Se ejecuta el servidor
if __name__ == "__main__":
    executeServer()