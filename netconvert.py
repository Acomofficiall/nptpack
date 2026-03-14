from moviepy.editor import VideoFileClip, AudioFileClip
import os

def mp4_to_mp3(girdi_dosyasi):
    try:
        cikti_dosyasi = os.path.splitext(girdi_dosyasi)[0] + ".mp3"
        video = VideoFileClip(girdi_dosyasi)
        video.audio.write_audiofile(cikti_dosyasi)
        video.close()
        print(f"[+] Çevrildi: {cikti_dosyasi}")
    except Exception as e:
        print(f"[-] Hata: {e}")

def mp3_to_mp4(girdi_dosyasi):
    try:
        # MP3'ten MP4 yapmak için bir görsel veya siyah ekran gerekir
        # Burada sadece sesi içeren bir MP4 oluşturuyoruz
        cikti_dosyasi = os.path.splitext(girdi_dosyasi)[0] + ".mp4"
        ses = AudioFileClip(girdi_dosyasi)
        ses.write_videofile(cikti_dosyasi, fps=1, codec="libx264")
        ses.close()
        print(f"[+] Çevrildi: {cikti_dosyasi}")
    except Exception as e:
        print(f"[-] Hata: {e}")

if __name__ == "__main__":
    print("--- MP4/MP3 Çevirici ---")
    dosya = input("Dosya yolunu sürükleyin veya yazın: ").strip('"')
    
    if dosya.lower().endswith(".mp4"):
        mp4_to_mp3(dosya)
    elif dosya.lower().endswith(".mp3"):
        mp3_to_mp4(dosya)
    else:
        print("[-] Desteklenmeyen format kanka!")