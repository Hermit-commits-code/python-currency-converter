import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import requests


class CurrencyConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("500x450+300+150")
        self.resizable(width=0, height=0)

    def build_gui(self):
        self.logo = tk.PhotoImage(file="logo.png")
        tk.Label(self, image=self.logo).pack()


if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.mainloop()
