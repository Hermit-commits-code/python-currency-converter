import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

import requests

API_KEY = os.getenv("API_KEY")
if API_KEY is None:
    messagebox.showerror("API Key Error", "API_KEY environment variable is not set.")
    sys.exit(1)

API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/"


class CurrencyConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x450+300+150")
        self.title("Currency Converter")
        self.resizable(width=0, height=0)
        self.build_gui()

    def build_gui(self):
        self.logo = tk.PhotoImage(file="images/logo.png")
        tk.Label(self, image=self.logo).pack()
        frame = tk.Frame(self)
        frame.pack()

        from_label = ttk.Label(frame, text="From:")
        from_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        to_label = ttk.Label(frame, text="To:")
        to_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.from_combo = ttk.Combobox(frame)
        self.from_combo.grid(row=1, column=0, padx=5, pady=5)

        self.to_combo = ttk.Combobox(frame)
        self.to_combo.grid(row=1, column=1, padx=5, pady=5)

        amount_label = ttk.Label(frame, text="Amount:")
        amount_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.amount_entry = ttk.Entry(frame)
        self.amount_entry.insert(0, "1.00")
        self.amount_entry.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W + tk.E
        )

        self.result_label = ttk.Label(font=("Arial", 20, "bold"))
        self.result_label.pack()

        convert_button = ttk.Button(
            self, text="Convert", width=20, command=self.convert
        )
        convert_button.pack()

        currencies = self.get_currencies()

        self.from_combo["values"] = currencies
        self.from_combo.current(0)

        self.to_combo["values"] = currencies
        self.to_combo.current(0)

    def get_currencies(self):
        response = requests.get(f"{API_URL}/latest/USD")
        data = response.json()
        return list(data["conversion_rates"])

    def convert(self):
        src = self.from_combo.get()
        dest = self.to_combo.get()
        amount = self.amount_entry.get()
        response = requests.get(f"{API_URL}/pair/{src}/{dest}/{amount}").json()
        result = response["conversion_result"]
        self.result_label.config(text=f"{amount} {src} = {result} {dest}")


if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.mainloop()
