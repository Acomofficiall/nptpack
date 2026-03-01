import tkinter as tk
import random
from tkinter import messagebox  # Bu satırı eklemelisin

class YilanOyunu:
    def __init__(self, root):
        self.root = root
        self.root.title("Yılan Oyunu")
        self.tuval = tk.Canvas(root, width=400, height=400, bg="black")
        self.tuval.pack()

        self.yilan = [(20, 20), (20, 40), (20, 60)]
        self.yon = "Down"
        self.yem = None
        self.puan = 0
        
        self.root.bind("<KeyPress>", self.yon_degistir)
        self.yem_olustur()
        self.hareket_et()

    def yem_olustur(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        self.yem = (x, y)
        self.tuval.create_oval(x, y, x+20, y+20, fill="red", tag="yem")

    def hareket_et(self):
        bas = self.yilan[-1]
        if self.yon == "Up": yeni_bas = (bas[0], bas[1]-20)
        elif self.yon == "Down": yeni_bas = (bas[0], bas[1]+20)
        elif self.yon == "Left": yeni_bas = (bas[0]-20, bas[1])
        elif self.yon == "Right": yeni_bas = (bas[0]+20, bas[1])

        self.yilan.append(yeni_bas)

        if yeni_bas == self.yem:
            self.puan += 1
            self.tuval.delete("yem")
            self.yem_olustur()
        else:
            self.yilan.pop(0)

        self.ciz()
        # Çarpışma kontrolü
        if (yeni_bas[0] < 0 or yeni_bas[0] >= 400 or 
            yeni_bas[1] < 0 or yeni_bas[1] >= 400 or 
            yeni_bas in self.yilan[:-1]):
            tk.messagebox.showinfo("Oyun Bitti", f"Puanın: {self.puan}")
            self.root.destroy()
            return

        self.root.after(150, self.hareket_et)

    def ciz(self):
        self.tuval.delete("gövde")
        for parca in self.yilan:
            self.tuval.create_rectangle(parca[0], parca[1], parca[0]+20, parca[1]+20, fill="green", tag="gövde")

    def yon_degistir(self, e):
        yeni_yon = e.keysym
        if yeni_yon in ["Up", "Down", "Left", "Right"]:
            self.yon = yeni_yon

root = tk.Tk()
YilanOyunu(root)
root.mainloop()