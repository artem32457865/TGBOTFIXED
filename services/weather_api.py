import requests
from config import config

class WeatherAPI:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    @classmethod
    async def get_weather(cls, city: str):
        params = {
            "q": city,
            "appid": config.WEATHER_API_KEY,
            "units": "metric",
            "lang": "ua"  
        }
        try:
            response = requests.get(cls.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Помилка API погоди: {e}")
            return None

    @staticmethod
    def format_weather(data: dict):
        city = data.get("name", "Невідоме місто")
        country = data.get("sys", {}).get("country", "")
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"].capitalize()
        
        return (
            f"🌍 {city}, {country}\n\n"
            f"🌡 Температура: {temp}°C (відчувається як {feels_like}°C)\n"
            f"💧 Вологість: {humidity}%\n"
            f"🌬 Вітер: {wind_speed} м/с\n"
            f"☁️ {description}"
        )