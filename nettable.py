import tkinter as tk

class MiniExcel:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Excel")
        
        # 10x5'lik bir tablo oluşturalım
        self.hucreler = {}
        for i in range(100): # Satır
            for j in range(100): # Sütun
                e = tk.Entry(root, justify='center', font=("Arial", 10))
                e.grid(row=i, column=j, sticky="nsew")
                e.insert(0, "") # Varsayılan değer
                self.hucreler[(i, j)] = e

    #     tk.Button(root, text="Toplamı Hesapla (Sütun 1)", command=self.topla).grid(row=11, column=0, columnspan=5)

    # def topla(self):
    #     toplam = 0
    #     for i in range(10):
    #         try:
    #             toplam += float(self.hucreler[(i, 0)].get())
    #         except: pass
    #     tk.messagebox.showinfo("Sonuç", f"İlk sütunun toplamı: {toplam}")

root = tk.Tk()
MiniExcel(root)
root.mainloop()