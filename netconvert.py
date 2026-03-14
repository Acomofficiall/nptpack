import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy import VideoFileClip, AudioFileClip
import os
import threading

class NetConvertGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("A.net - NetConvert v1.0")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        # Arayüz Elemanları
        self.label = tk.Label(root, text="Dönüştürülecek Dosyayı Seç", font=("Arial", 10, "bold"))
        self.label.pack(pady=10)

        self.file_path = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.file_path, width=40)
        self.entry.pack(pady=5)

        self.btn_browse = tk.Button(root, text="Dosya Seç", command=self.browse_file)
        self.btn_browse.pack(pady=5)

        self.btn_convert = tk.Button(root, text="Çeviriyi Başlat", command=self.start_conversion_thread, 
                                     bg="#2ecc71", fg="white", font=("Arial", 10, "bold"))
        self.btn_convert.pack(pady=20)

        self.status_label = tk.Label(root, text="Hazır", fg="blue")
        self.status_label.pack()

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Media Files", "*.mp4 *.mp3")])
        if filename:
            self.file_path.set(filename)

    def convert(self):
        input_path = self.file_path.get()
        if not input_path or not os.path.exists(input_path):
            messagebox.showerror("Hata", "Lütfen geçerli bir dosya seç kanka!")
            return

        self.btn_convert.config(state="disabled")
        self.status_label.config(text="Dönüştürülüyor... Lütfen bekle.", fg="orange")

        try:
            if input_path.lower().endswith(".mp4"):
                output_path = os.path.splitext(input_path)[0] + ".mp3"
                video = VideoFileClip(input_path)
                video.audio.write_audiofile(output_path)
                video.close()
            elif input_path.lower().endswith(".mp3"):
                output_path = os.path.splitext(input_path)[0] + ".mp4"
                audio = AudioFileClip(input_path)
                audio.write_videofile(output_path, fps=1, codec="libx264")
                audio.close()
            
            messagebox.showinfo("Başarılı", f"İşlem bitti kanka!\nDosya: {output_path}")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir şeyler ters gitti: {e}")
        finally:
            self.status_label.config(text="Hazır", fg="blue")
            self.btn_convert.config(state="normal")

    def start_conversion_thread(self):
        # Arayüzün donmaması için çevirme işlemini arka planda yapıyoruz
        thread = threading.Thread(target=self.convert)
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = NetConvertGUI(root)
    root.mainloop()
