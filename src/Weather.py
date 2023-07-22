import requests
import json


data = json.load(open('Data\\data.json'))
WEATHER_KEY = data['weather_key']
IP_KEY = data['ip_key']


def get_current_ip() -> str:
    """
    Returns the current IP
    """
    url = 'https://api.ipify.org'
    return requests.get(url).content.decode('utf-8')


def get_current_location() -> tuple[str, str, float, float]:
    """ 
    Returns the current location in city name, country, latitude and longitude
    """
    url = f'https://ipinfo.io/{get_current_ip()}?token={IP_KEY}'
    data = requests.get(url).json()
    latitude, longitude = [float(x) for x in data['loc'].split(',')]
    return (data['city'], data['country'], latitude, longitude)


def get_city(city: str) -> tuple[str, float, float, str]:
    """
    Returns the current name, latitude, longitude and country of the given city
    """
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={WEATHER_KEY}'
    data = requests.get(url).json()[0]
    return (data['name'], data['lat'], data['lon'], data['country'])


def get_weather(latitude: float, longitude: float) -> dict:
    """
    Returns data of the weather from the given latitude and longitude
    """
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&units=metric&exclude=hourly,minutely&appid={WEATHER_KEY}'
    return requests.get(url).json()


def get_city_weather(city: str) -> tuple[str, str, dict]:
    """
    Returns its name, country and weather data of the given city
    """
    name, latitude, longitude, country = get_city(city)
    data = get_weather(latitude, longitude)
    return name, country, data


def get_current_location_weather():
    """
    Returns its name, country and weather data of the current location
    """
    name, country, latitude, longitude = get_current_location()
    data = get_weather(latitude, longitude)
    return name, country, data


def main():
    pass


if __name__ == '__main__':
    main()