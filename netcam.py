import cv2
import datetime
import os
import platform

def netcam_baslat():
    # İşletim sistemini kontrol et
    is_windows = platform.system() == "Windows"
    
    # Windows'ta CAP_DSHOW daha hızlıdır, Linux'ta standart açılır
    if is_windows:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    else:
        cap = cv2.VideoCapture(0) # Linux / RPi için
    
    if not os.path.exists("captures"):
        os.makedirs("captures")

    recording = False
    out = None

    

    while True:
        ret, frame = cap.read()
        if not ret: break

        # Arayüz Bilgisi
        status = "KAYITTA" if recording else "HAZIR"
        color = (0, 0, 255) if recording else (0, 255, 0)
        cv2.putText(frame, f"F: Foto | V: Kayıt Başlat/Durdur | Q: Çıkış\n{status}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        cv2.imshow('A.net NetCam Pro', frame)

        if recording and out is not None:
            out.write(frame)

        key = cv2.waitKey(1) & 0xFF

        # F: Fotoğraf Çek
        if key == ord('f'):
            zaman = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            isim = f"captures/foto_{zaman}.jpg"
            cv2.imwrite(isim, frame)
            print(f"[+] Fotoğraf kaydedildi: {isim}")

        # V: Video Kaydı
        elif key == ord('v'):
            if not recording:
                zaman = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                h, w = frame.shape[:2]
                
                # Codec Seçimi: Windows'ta XVID, Linux'ta genelde mp4v veya MJPG daha stabil
                if is_windows:
                    fourcc = cv2.VideoWriter_fourcc(*'XVID')
                    isim = f"captures/video_{zaman}.avi"
                else:
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                    isim = f"captures/video_{zaman}.mp4"
                
                out = cv2.VideoWriter(isim, fourcc, 20.0, (w, h))
                recording = True
                print(f"[*] Kayıt başladı: {isim}")
            else:
                recording = False
                if out: out.release()
                print("[+] Kayıt durduruldu.")

        elif key == ord('q') or key == 27:
            if recording and out: out.release()
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    netcam_baslat()
