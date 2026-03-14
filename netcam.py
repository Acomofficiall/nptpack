import cv2

def kamera_baslat():
    # 0 genellikle varsayılan laptobun/PC'nin kamerasıdır
    kamera = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Windows için CAP_DSHOW daha hızlı açılır
    
    if not kamera.isOpened():
        print("[-] Kamera bulunamadı veya başka bir uygulama kullanıyor!")
        return

    print("[!] Kamera açıldı. Kapatmak için 'ESC' tuşuna bas.")
    
    while True:
        ret, kare = kamera.read()
        if not ret:
            break
            
        # Görüntüyü pencerede göster
        cv2.imshow('Neo-8 Kamera Modulu', kare)
        
        # ESC tuşuna basılınca döngüden çık
        if cv2.waitKey(1) == 27:
            break
            
    kamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    kamera_baslat()