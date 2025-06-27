import requests

class Apiclass():#Aquí se guardan conexiones con Weather API 
    def weatherHist():
        #Solicitud GET a la API del endpoint history.json
        response = requests.get("http://api.weatherapi.com/v1/history.json", params={
            "key": "13014822709c4c27ac3214249251906",
            "q": "Tunja",
            "dt": "2025-06-21"
        })
        return response