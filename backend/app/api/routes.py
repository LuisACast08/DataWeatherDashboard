import requests #Se importa "requests" para hacer solicitudes HTTP
import csv
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

#Solicitud GET

response = requests.get("http://api.weatherapi.com/v1/current.json", params={

    "key": "13014822709c4c27ac3214249251906",
    "q": "Bogotá",
    "aqi": "no",
    "lang": "es"
})

# #En tal caso que la respuesta de la consulta se OK, se imprime el JSON
# if response.status_code == 200:
#     data = response.json()
#     print(data["location"])
# else:
#     print("Error al obtener datos", response.status_code)

# #Se convierte el JSON en archivo CSV
# with open("cursos.csv", "w", newline="", encoding="utf-8") as archivoCSV:
#     writer = csv.writer(archivoCSV)
    
#     location = data["location"]
    
#     #Escribe los datos
#     writer.writerow([
#         location["name"],
#         location["region"],
#         location["country"],
#         location["tz_id"],
#         location["localtime"]
#     ])

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

#Config del servidor
def executeServer():
    port = 8000
    server = HTTPServer(("localhost", port), Handler)
    print(f"Servidor corriendo en http://localhost:{port}")
    server.serve_forever()
    
#Se ejecuta el servidor
if __name__ == "__main__":
    executeServer()