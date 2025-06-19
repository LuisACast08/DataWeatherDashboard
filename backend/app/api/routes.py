import requests #Se importa "requests" para hacer solicitudes HTTP

#Solicitud GET

response = requests.get("http://api.weatherapi.com/v1/current.json", params={

    "key": "13014822709c4c27ac3214249251906",
    "q": "Bogotá",
    "aqi": "no"
})

if response.status_code == 200:
    data = response.json()
    print(data["location"]["name"])
else:
    print("Error al obtener datos", response.status_code)

