import requests
from bs4 import BeautifulSoup

database = [
    "https://uk.wikipedia.org/wiki/Географія_України",
    "https://uk.wikipedia.org/wiki/Біологія",
    "https://uk.wikipedia.org/wiki/Тварини",
    "https://uk.wikipedia.org/wiki/Океан",
    "https://uk.wikipedia.org/wiki/Космічний_простір"
]

print("--Вітаємо--")
print("Оберіть спосіб використання програми:")
print("1. Додати свій сайт для пошуку інформації")
print("2. Використовувати сайти з бази даних\n")

answer = input("Ваша відповідь (1 або 2): ")

if answer == "1":
    user = []
    while True:
        url = input("Введіть URL сайту (з https://): ")
        user.append(url)
        more = input("Хочете додати ще один сайт? (так/ні): ").lower()
        if more != "так":
            break

    info = input("Введіть текст для пошуку: ").lower()
    headers = {"User-Agent": "Mozilla/5.0"}
    found = False

    for url in user:
        try:
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text().lower()

            if info in text:
                print("Текст знайдено на сайті:", url)
                found = True

        except requests.exceptions.RequestException:
            print("Не вдалося відкрити сайт:", url)

    if not found:
        print("Текст не знайдено на жодному сайті.")

elif answer == "2":
    info_2 = input("Введіть текст для пошуку: ").lower()
    headers = {"User-Agent": "Mozilla/5.0"}
    found = False

    for url in database:
        try:
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text().lower()

            if info_2 in text:
                print("Текст знайдено на сайті:", url)
                found = True

        except requests.exceptions.RequestException:
            print("Не вдалося відкрити сайт:", url)

    if not found:
        print("Текст не знайдено на сайтах із бази даних.")

else:
    print("Помилка. Виберіть 1 або 2.")

