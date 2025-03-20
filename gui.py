import tkinter as tk
from tkinter import messagebox
from main import prev_day_info, daily_returns

def get_stock_info():
    ticker = entry.get().upper()
    if not ticker:
        messagebox.showwarning("Input Error", "Please enter a stock ticker.")
        return

    info = prev_day_info(ticker)
    returns = daily_returns(ticker)

    output.delete(1.0, tk.END)
    output.insert(tk.END, info + "\n" + returns)



root = tk.Tk()
root.title("Stock Info Viewer")
root.geometry("400x300")

label = tk.Label(root, text="Enter Stock Ticker:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Get Info", command=get_stock_info)
button.pack(pady=10)

output = tk.Text(root, height=10, width=45)
output.pack(pady=10)

root.mainloop()
