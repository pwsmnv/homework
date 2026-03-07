import requests
from bs4 import BeautifulSoup
from tkinter import *

class Converter:
    def __init__(self):
        self.rate = None
        self.get_rate()

    def get_rate(self):
        url = "https://bank.gov.ua/ua/markets/exchangerates"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        for row in soup.find_all("tr"):
            cols = row.find_all("td")
            if len(cols) > 0 and cols[1].text.strip() == "USD":
                self.rate = float(cols[4].text.replace(",", "."))
                break
        return self.rate

    def to_usd(self, amount):
        if self.rate is None:
            self.get_rate()
        return amount / self.rate

conv = Converter()
rate = conv.rate

if rate is None:
    print("Не вдалося отримати курс долара.")
    exit()

root = Tk()
root.title("UAH - USD")
root.geometry("490x300")
root.configure(bg="#dfddb7")
root.resizable(False, False)

def convert():
    try:
        amt = float(entry.get())
        usd = conv.to_usd(amt)
        lbl_result.config(text=f"{amt:.2f} UAH ≈ {usd:.2f} USD")
    except ValueError:
        lbl_result.config(text="Помилка. Введіть число.")

lbl_rate = Label(root, text=f"Курс USD: 1 USD = {rate:.4f} UAH", font=("Comic Sans MS", 13, "bold"), bg="#dfddb7")
lbl_rate.pack(pady=10)
lbl_instr = Label(root, text="Введіть суму в UAH:", font=("Comic Sans MS", 14), bg="#dfddb7")
lbl_instr.pack(pady=5)
entry = Entry(root, width=20, font=("Comic Sans MS", 13), bd=3, relief="ridge")
entry.pack(pady=5)
btn_convert = Button(root, text="Конвертувати", font=("Comic Sans MS", 12), bg="#c3b709", command=convert)
btn_convert.pack(pady=10)
lbl_result = Label(root, text="", font=("Comic Sans MS", 13, "bold"), bg="#dfddb7", fg="#5f5800")
lbl_result.pack(pady=15)

root.mainloop()
