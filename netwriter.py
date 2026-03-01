import tkinter as tk
from tkinter import font, colorchooser, filedialog, messagebox

class ModernWord(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- Pencere Ayarları ---
        self.overrideredirect(True)
        self.geometry("1000x750+200+100")
        self.configure(bg="#1a1a1a")
        
        self.is_maximized = False
        self._offsetx = 0
        self._offsety = 0

        # --- Modern Başlık Çubuğu ---
        self.title_bar = tk.Frame(self, bg="#252525", height=35)
        self.title_bar.pack(fill="x", side="top")
        self.title_bar.pack_propagate(False)

        self.title_label = tk.Label(self.title_bar, text="  PYTHON WORD PRO - MODERN", 
                                   fg="#dcdcdc", bg="#252525", font=("Arial", 9, "bold"))
        self.title_label.pack(side="left")

        # Butonlar (Canvas Çizim)
        btn_frame = tk.Frame(self.title_bar, bg="#252525")
        btn_frame.pack(side="right", fill="y")
        self.draw_btn(btn_frame, "close", self.destroy, "#e81123")
        self.draw_btn(btn_frame, "max", self.toggle_maximize, "#444444")
        self.draw_btn(btn_frame, "min", self.minimize_window, "#444444")

        # --- Word İçerik Alanı ---
        self.main_container = tk.Frame(self, bg="#1a1a1a")
        self.main_container.pack(expand=True, fill="both")

        # Varsayılan Değerler
        self.current_font_family = "Arial"
        self.current_font_size = 12

        # --- Şerit (Ribbon) Tasarımı ---
        self.ribbon = tk.Frame(self.main_container, bg="#f3f3f3", bd=0)
        self.ribbon.pack(side="top", fill="x")

        # Yazı Tipi Araçları
        self.font_box = tk.OptionMenu(self.ribbon, tk.StringVar(value="Arial"), 
                                      *font.families(), command=self.yazi_tipi_degistir)
        self.font_box.config(bg="#f3f3f3", bd=0)
        self.font_box.pack(side="left", padx=5, pady=5)

        self.size_box = tk.Spinbox(self.ribbon, from_=8, to=72, width=5, command=self.boyut_degistir)
        self.size_box.pack(side="left", padx=5)

        # Stil Butonları
        self.btn_bold = tk.Button(self.ribbon, text="B", font=("Arial", 10, "bold"), width=3, command=self.kalin_yap)
        self.btn_bold.pack(side="left", padx=2)

        self.btn_italic = tk.Button(self.ribbon, text="I", font=("Arial", 10, "italic"), width=3, command=self.italik_yap)
        self.btn_italic.pack(side="left", padx=2)

        self.btn_color = tk.Button(self.ribbon, text="Renk", command=self.renk_degistir)
        self.btn_color.pack(side="left", padx=5)

        # Dosya İşlemleri Butonları (Ribbon'a taşındı)
        tk.Button(self.ribbon, text="Yeni", command=self.yeni_dosya).pack(side="left", padx=2)
        tk.Button(self.ribbon, text="Kaydet", command=self.kaydet).pack(side="left", padx=2)

        # --- Yazım Alanı ---
        self.text_frame = tk.Frame(self.main_container, bg="#333333")
        self.text_frame.pack(expand=True, fill="both")

        self.editor = tk.Text(self.text_frame, font=(self.current_font_family, self.current_font_size),
                              undo=True, wrap="word", padx=50, pady=50, bg="white", fg="black")
        self.editor.pack(expand=True, fill="both", padx=60, pady=30) 

        # --- Resize & Drag Eventleri ---
        self.title_bar.bind("<Button-1>", self.click_title)
        self.title_bar.bind("<B1-Motion>", self.drag_title)
        
        self.resizer = tk.Canvas(self, width=15, height=15, bg="#1a1a1a", highlightthickness=0, cursor="sizing")
        self.resizer.place(relx=1.0, rely=1.0, anchor="se")
        self.resizer.create_line(5, 15, 15, 5, fill="#555555", width=2)
        self.resizer.create_line(10, 15, 15, 10, fill="#555555", width=2)
        self.resizer.bind("<B1-Motion>", self.resize_window)

    # --- Görsel Yardımcılar ---
    def draw_btn(self, parent, type, cmd, hover_color):
        canvas = tk.Canvas(parent, width=45, height=35, bg="#252525", highlightthickness=0, bd=0)
        canvas.pack(side="right")
        if type == "close":
            canvas.create_line(17, 12, 27, 22, fill="white", width=2)
            canvas.create_line(27, 12, 17, 22, fill="white", width=2)
        elif type == "max":
            canvas.create_rectangle(17, 12, 27, 22, outline="white", width=2)
        elif type == "min":
            canvas.create_line(17, 18, 27, 18, fill="white", width=2)
        canvas.bind("<Enter>", lambda e: canvas.config(bg=hover_color))
        canvas.bind("<Leave>", lambda e: canvas.config(bg="#252525"))
        canvas.bind("<Button-1>", lambda e: cmd())

    # --- Pencere Yönetimi ---
    def click_title(self, event):
        self._offsetx, self._offsety = event.x, event.y

    def drag_title(self, event):
        if not self.is_maximized:
            self.geometry(f"+{event.x_root - self._offsetx}+{event.y_root - self._offsety}")

    def toggle_maximize(self):
        if self.is_maximized:
            self.state("normal")
            self.is_maximized = False
        else:
            self.state("zoomed")
            self.is_maximized = True

    def minimize_window(self):
        self.withdraw()
        self.after(100, self.update_idletasks)
        self.state('iconic')
        self.deiconify()

    def resize_window(self, event):
        x, y = self.winfo_pointerx() - self.winfo_rootx(), self.winfo_pointery() - self.winfo_rooty()
        if x > 300 and y > 300: self.geometry(f"{x}x{y}")

    # --- Word Fonksiyonları ---
    def kalin_yap(self):
        if not self.editor.tag_ranges("sel"): return
        try:
            current_tags = self.editor.tag_names("sel.first")
            if "bold" in current_tags:
                self.editor.tag_remove("bold", "sel.first", "sel.last")
            else:
                f = font.Font(self.editor, self.editor.cget("font"))
                f.configure(weight="bold")
                self.editor.tag_configure("bold", font=f)
                self.editor.tag_add("bold", "sel.first", "sel.last")
        except: pass

    def italik_yap(self):
        if not self.editor.tag_ranges("sel"): return
        try:
            f = font.Font(self.editor, self.editor.cget("font"))
            f.configure(slant="italic")
            self.editor.tag_configure("italic", font=f)
            self.editor.tag_add("italic", "sel.first", "sel.last")
        except: pass

    def renk_degistir(self):
        if not self.editor.tag_ranges("sel"): return
        renk = colorchooser.askcolor()[1]
        if renk:
            tag_name = f"color_{renk.replace('#', '')}"
            self.editor.tag_configure(tag_name, foreground=renk)
            self.editor.tag_add(tag_name, "sel.first", "sel.last")

    def yazi_tipi_degistir(self, secim):
        self.current_font_family = secim
        self.editor.configure(font=(self.current_font_family, self.current_font_size))

    def boyut_degistir(self):
        self.current_font_size = self.size_box.get()
        self.editor.configure(font=(self.current_font_family, self.current_font_size))

    def yeni_dosya(self):
        self.editor.delete("1.0", tk.END)

    def kaydet(self):
        dosya = filedialog.asksaveasfilename(defaultextension=".txt")
        if dosya:
            with open(dosya, "w", encoding="utf-8") as f:
                f.write(self.editor.get("1.0", tk.END))
            messagebox.showinfo("Başarılı", "Kaydedildi!")

if __name__ == "__main__":
    app = ModernWord()
    app.mainloop()