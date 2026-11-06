import requests

headers = {"User-Agent": "myFirstAPI/0.1 (lisowski07m@gmail.com)"}


def get_weather_data(lat, lon):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"failed to retrieve data {response.status_code}")

lat = 59.66
lon = 10.76

weather_info = get_weather_data(lat, lon)

if weather_info:
    temp = (weather_info["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])
    time = (weather_info["properties"]["timeseries"][0]["time"])

    print(f"coordinates: {lat}, {lon}\ntempetaure: {temp}\ntime: {time}")