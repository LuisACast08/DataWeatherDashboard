import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import pandas as pd

#Se utiliza inicialmente endpoints con http.server
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