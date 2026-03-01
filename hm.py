import tkinter as tk

def tikla(tus):
    mevcut = ekran.get()
    if tus == "=":
        try:
            ekran.delete(0, tk.END)
            ekran.insert(0, str(eval(mevcut)))
        except:
            ekran.delete(0, tk.END)
            ekran.insert(0, "Hata")
    elif tus == "C":
        ekran.delete(0, tk.END)
    else:
        ekran.insert(tk.END, tus)

pencere = tk.Tk()
pencere.title("Hesap Makinesi")

ekran = tk.Entry(pencere, font=("Arial", 20), borderwidth=5, relief="flat", justify="right")
ekran.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

tuslar = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

r, c = 1, 0
for tus in tuslar:
    tk.Button(pencere, text=tus, width=5, height=2, font=("Arial", 14),
              command=lambda t=tus: tikla(t)).grid(row=r, column=c, padx=2, pady=2)
    c += 1
    if c > 3:
        c = 0
        r += 1

pencere.mainloop()