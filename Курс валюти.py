import requests
from tkinter import *

class CurrencyConverter:
    def __init__(self):
        self.usd_rate = None

    def fetch_usd_rate(self):
        url = "https://bank.gov.ua/NBU_Exchange/exchange?json"
        response = requests.get(url)
        data = response.json()
        for item in data:
            if item.get("CurrencyCodeL") == "USD":
                self.usd_rate = float(item.get("Amount"))
                return self.usd_rate
        return None

    def convert_to_usd(self, amount_ua):
        if self.usd_rate is None:
            self.fetch_usd_rate()
        return amount_ua / self.usd_rate

converter = CurrencyConverter()
usd_rate = converter.fetch_usd_rate()

if usd_rate is None:
    print("Не вдалося отримати курс долара.")
    exit()

window = Tk()
window.title("Конвертер UAH - USD")
window.geometry("490x300")
window.configure(background="#dfddb7")
window.resizable(False, False)

def convert_currency():
    try:
        uah_amount = float(entry_amount.get())
        usd_amount = converter.convert_to_usd(uah_amount)
        label_result.config(text=f"{uah_amount:.2f} UAH ≈ {usd_amount:.2f} USD")
    except ValueError:
        label_result.config(text="Будь ласка, введіть число!")

label_rate = Label(window, text=f"Офіційний курс USD: 1 USD = {usd_rate:.4f} UAH", font=("Comic Sans MS", 13, "bold"), bg="#dfddb7", fg="black")
label_rate.pack(pady=10)
label_instruction = Label(window, text="Введіть суму в UAH:", font=("Comic Sans MS", 14), bg="#dfddb7")
label_instruction.pack(pady=5)

entry_amount = Entry(window, width=20, font=("Comic Sans MS", 13), bd=3, relief="ridge")
entry_amount.pack(pady=5)

button_convert = Button(window, text="Конвертувати", font=("Comic Sans MS", 12), bg="#c3b709", fg="black", command=convert_currency)
button_convert.pack(pady=10)
label_result = Label(window, text="", font=("Comic Sans MS", 13, "bold"), bg="#dfddb7", fg="#5f5800")
label_result.pack(pady=15)

window.mainloop()