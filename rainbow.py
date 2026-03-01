import tkinter as tk

class PaintUygulamasi:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Basit Paint - Maniac Edition")
        
        self.firca_rengi = "black"
        self.tuval = tk.Canvas(self.pencere, bg="white", width=800, height=500)
        self.tuval.pack(expand=True, fill="both")
        
        # Fare hareketlerini bağla
        self.tuval.bind("<B1-Motion>", self.ciz)
        
        # Renk Seçenekleri için ana çerçeve
        buton_cercevesi = tk.Frame(self.pencere)
        buton_cercevesi.pack(fill="x", padx=5, pady=5)
        
        renkler = [
            "black", "silver", "gray", "white", "maroon", "red", "purple", "fuchsia", 
            "green", "lime", "olive", "yellow", "navy", "blue", "teal", "aqua",
            "orange", "aliceblue", "antiquewhite", "aquamarine", "azure", "beige", 
            "bisque", "blanchedalmond", "blueviolet", "brown", "burlywood", "cadetblue", 
            "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", 
            "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", 
            "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", 
            "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", 
            "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", 
            "dodgerblue", "firebrick", "floralwhite", "forestgreen", "gainsboro", 
            "ghostwhite", "gold", "goldenrod", "greenyellow", "honeydew", "hotpink", 
            "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", 
            "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", 
            "lightgoldenrodyellow", "lightgray", "lightgreen", "lightpink", 
            "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", 
            "lightsteelblue", "lightyellow", "limegreen", "linen", "magenta", 
            "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", 
            "mediumseagreen", "mediumslateblue", "mediumspringgreen", 
            "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", 
            "mistyrose", "moccasin", "navajowhite", "oldlace", "olivedrab", 
            "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", 
            "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", 
            "powderblue", "rosybrown", "royalblue", "saddlebrown", "salmon", 
            "sandybrown", "seagreen", "seashell", "sienna", "skyblue", "slateblue", 
            "slategray", "snow", "springgreen", "steelblue", "tan", "thistle", 
            "tomato", "turquoise", "violet", "wheat", "whitesmoke", "yellowgreen"
        ]

        # Butonları 3 satıra bölmek için toplam buton sayısını 3'e bölüyoruz
        buton_sayisi = len(renkler)
        satir_basina_buton = (buton_sayisi // 3) + 1

        for index, renk in enumerate(renkler):
            satir = index // satir_basina_buton
            sutun = index % satir_basina_buton
            
            # Grid kullanarak 3 satır oluşturuyoruz
            tk.Button(buton_cercevesi, bg=renk, width=1, height=1, 
                      command=lambda r=renk: self.renk_degistir(r),
                      relief="flat").grid(row=satir, column=sutun, padx=1, pady=1)
            
        # Temizle butonu (Grid'in en sağına ya da altına eklenebilir)
        tk.Button(self.pencere, text="TUVALİ TEMİZLE", bg="systemButtonFace", 
                  command=lambda: self.tuval.delete("all")).pack(fill="x")

    def ciz(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.tuval.create_oval(x1, y1, x2, y2, fill=self.firca_rengi, outline=self.firca_rengi)

    def renk_degistir(self, yeni_renk):
        self.firca_rengi = yeni_renk

root = tk.Tk()
# Pencereyi renk sayısına göre biraz genişletmek gerekebilir
root.geometry("1000x700")
PaintUygulamasi(root)
root.mainloop()