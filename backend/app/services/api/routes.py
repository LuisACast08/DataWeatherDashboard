import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import pandas as pd
import sqlite3
import services.dataAnalysis as SDataA

#Se utiliza inicialmente endpoints con http.server
    #Se crea una clase para manipular o responder a las solicitudes "GET, POST, PUT, etc..."

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        match self.path:
            case "/":
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "http://127.0.0.1:5500")
                self.end_headers()
                message = {"message": "Welcome to my application API!"}
                self.wfile.write(json.dumps(message).encode())
            case "/tableData":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.send_header("Access-Control-Allow-Origin", "http://127.0.0.1:5500")
                self.end_headers()
                try:
                    message = pd.read_csv("backend/app/data/dataW.csv")
                except FileNotFoundError:
                    conn = sqlite3.connect("backend/app/data/dataWeather.db")
                    message = pd.read_sql_query("SELECT * FROM dataWeather", conn)
                messageTable = message.to_json()
                self.wfile.write(messageTable.encode("utf-8"))
            case "/analisysSt":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.send_header("Access-Control-Allow-Origin", "http://127.0.0.1:5500")
                self.end_headers()
                df = SDataA.dataAnalisysClass.statisticA()
                message = df.to_json()
                self.wfile.write(message.encode("utf-8"))
                
            case _:
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                message = "Ruta desconocida..."
                self.wfile.write(message.encode("utf-8"))
                
#Config del servidor
def executeServer():
    port = 8000
    server = HTTPServer(("localhost", port), Handler)
    print(f"Servidor corriendo en http://localhost:{port}")
    server.serve_forever()
    
