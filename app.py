import tkinter as tk
from forex_python.converter import CurrencyRates

def convert_currencies(): 
    amount = float(entry_amount.get())
    source_currency = entry_source.get()
    intended_currency = entry_intended.get()

    c = CurrencyRates()
    result = c.convert(source_currency, intended_currency, amount)

    label_result.config(text=f'{amount} {source_currency} = {result:.2f} {intended_currency}')

window = tk.Tk()
window.title("Currency Converter")

label_amount = tk.Label(window, text='Amount:')
label_amount.grid(row=0, column=0)

entry_amount = tk.Entry(window)
entry_amount.grid(row=0, column=1)

label_source = tk.Label(window, text="Source Currency")
label_source.grid(row=1, column=0)

entry_source = tk.Entry(window)
entry_source.grid(row=1, column=1)
entry_source.insert(0, "USD")  

label_intended = tk.Label(window, text="Intended Currency")
label_intended.grid(row=2, column=0)

entry_intended = tk.Entry(window)
entry_intended.grid(row=2, column=1)
entry_intended.insert(0, "BRL")  

btn_convert = tk.Button(window, text="Convert", command=convert_currencies)
btn_convert.grid(row=3, columnspan=2)

label_result = tk.Label(window, text="")
label_result.grid(row=4, columnspan=2)

window.mainloop()
