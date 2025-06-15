# TGBOTFIXED

🌦 Telegram Бот Погоди Description: Цей бот — зручний інструмент для отримання поточної погоди у вибраних країнах або будь-якому місті світу. Побудований на aiogram, він використовує API OpenWeatherMap для отримання актуальних погодних даних. Інтуїтивно зрозумілий інтерфейс дозволяє обрати місто за допомогою клавіатури або ввести його вручну.

🔧 Функціонал

Обрання країни та міста через клавіатуру

Отримання погоди з OpenWeatherMap

Підтримка ручного введення міста

Форматоване виведення погодних даних

Підтримка української мови

📦 Встановлення

Клонуй репозиторій:

git clone https://github.com/твій_нік/назва_проєкту.git

cd назва_проєкту

Створи віртуальне середовище (опційно):

python -m venv venv

source venv/bin/activate або venv\Scripts\activate на Windows

Встанови залежності:

pip install -r requirements.txt

Створи .env файл та додай свої токени:

TELEGRAM_TOKEN=тут_твій_токен_бота

OPENWEATHER_API_KEY=тут_твій_ключ_від_OpenWeather

🚀 Запуск

python main.py

🧪 Залежності

aiogram

python-dotenv

requests

📝 Приклад .env файлу

TELEGRAM_TOKEN=123456789:ABCDefGhi_JKLmnopQRStuvwxYZ

OPENWEATHER_API_KEY=abc123yourapikey456def
