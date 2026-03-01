import tkinter as tk
from tkinter import filedialog, messagebox

def dosya_ac():
    dosya_yolu = filedialog.askopenfilename(defaultextension=".txt",
                                            filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
    if dosya_yolu:
        metin_alani.delete(1.0, tk.END)
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            metin_alani.insert(1.0, dosya.read())
        pencere.title(f"Not Defteri - {dosya_yolu}")

def dosya_kaydet():
    dosya_yolu = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
    if dosya_yolu:
        with open(dosya_yolu, "w", encoding="utf-8") as dosya:
            dosya.write(metin_alani.get(1.0, tk.END))
        pencere.title(f"Not Defteri - {dosya_yolu}")
        messagebox.showinfo("Başarılı", "Notun kaydedildi!")

# Ana Pencere Kurulumu
pencere = tk.Tk()
pencere.title("Basit Not Defteri")
pencere.geometry("600x400")

# Metin Giriş Alanı
metin_alani = tk.Text(pencere, wrap="word", font=("Arial", 12))
metin_alani.pack(expand=True, fill="both")

# Menü Çubuğu
menu_cubugu = tk.Menu(pencere)
pencere.config(menu=menu_cubugu)

dosya_menusu = tk.Menu(menu_cubugu, tearoff=0)
menu_cubugu.add_cascade(label="Dosya", menu=dosya_menusu)
dosya_menusu.add_command(label="Aç", command=dosya_ac)
dosya_menusu.add_command(label="Kaydet", command=dosya_kaydet)
dosya_menusu.add_separator()
dosya_menusu.add_command(label="Çıkış", command=pencere.quit)

pencere.mainloop()