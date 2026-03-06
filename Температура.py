import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_temperature():
    url = "https://www.timeanddate.com/weather/ukraine/dnipro"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    temp_div = soup.find("div", class_="h2")
    if temp_div:
        temp_text = temp_div.get_text().strip()
        temp_text = temp_text.replace("°C", "").replace("°", "")
        return float(temp_text)
    return None

temperature = get_temperature()
if temperature is None:
    print("Не вдалося отримати температуру.")
    exit()

print(f"Поточна температура в Дніпрі: {temperature} °C")

conn = sqlite3.connect("WeatherInDnipro.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS temperatures (
    datetime TEXT,
    temperature REAL
)
""")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute("INSERT INTO temperatures (datetime, temperature) VALUES (?, ?)", (now, temperature))
conn.commit()
conn.close()
print("Температуру збережено.")