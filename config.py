import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    raise ValueError("Не знайдено TELEGRAM_TOKEN у .env файлі")

COUNTRIES = {
    "🇺🇦 Україна": ["Київ", "Львів", "Одеса", "Харків", "Дніпро"],
    "🇵🇱 Польща": ["Варшава", "Краків", "Вроцлав"],
    "🇩🇪 Німеччина": ["Берлін", "Мюнхен", "Гамбург"],
    "🇮🇹 Італія": ["Рим", "Мілан", "Венеція"]
}

class Config:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

config = Config()