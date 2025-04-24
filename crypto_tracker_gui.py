import tkinter as tk
from tkinter import messagebox
import requests

def get_crypto_price():
    crypto = entry.get().strip().lower()
    if not crypto:
        messagebox.showwarning("Input Error", "Please enter a cryptocurrency name!")
        return

    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': crypto,
        'vs_currencies': 'usd,inr'
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if crypto in data:
            usd_price = data[crypto]['usd']
            inr_price = data[crypto]['inr']
            result_label.config(
                text=f"{crypto.capitalize()} Prices:\nUSD: ${usd_price}\nINR: ₹{inr_price}",
                fg="green"
            )
        else:
            result_label.config(text="Cryptocurrency not found!", fg="red")

    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")


# GUI Setup
root = tk.Tk()
root.title("💰 Crypto Price Tracker")
root.geometry("350x250")
root.resizable(False, False)
root.config(bg="#f0f0f0")

title = tk.Label(root, text="Crypto Price Checker", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry.pack(pady=5)

btn = tk.Button(root, text="Get Price", font=("Helvetica", 12), command=get_crypto_price)
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 13), bg="#f0f0f0")
result_label.pack(pady=10)

root.mainloop()
