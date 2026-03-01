import tkinter as tk

class PongGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tkinter Pong")
        self.window.resizable(False, False)
        
        # Oyun alanı ayarları
        self.canvas = tk.Canvas(self.window, bg="black", width=800, height=400, highlightthickness=0)
        self.canvas.pack()

        # Çubuklar ve Top
        self.paddle_left = self.canvas.create_rectangle(10, 150, 30, 250, fill="white")
        self.paddle_right = self.canvas.create_rectangle(770, 150, 790, 250, fill="white")
        self.ball = self.canvas.create_oval(390, 190, 410, 210, fill="white")

        # Skor tablosu
        self.score_left = 0
        self.score_right = 0
        self.score_display = self.canvas.create_text(400, 30, text="0 - 0", fill="white", font=("Courier", 30))

        # Hareket hızları
        self.ball_dx = 4
        self.ball_dy = 4
        self.paddle_speed = 25

        # Tuş kontrolleri
        self.window.bind("<w>", lambda e: self.move_paddle(self.paddle_left, -self.paddle_speed))
        self.window.bind("<s>", lambda e: self.move_paddle(self.paddle_left, self.paddle_speed))
        self.window.bind("<Up>", lambda e: self.move_paddle(self.paddle_right, -self.paddle_speed))
        self.window.bind("<Down>", lambda e: self.move_paddle(self.paddle_right, self.paddle_speed))

        self.play()
        self.window.mainloop()

    def move_paddle(self, paddle, y):
        coords = self.canvas.coords(paddle)
        if coords[1] + y >= 0 and coords[3] + y <= 400:
            self.canvas.move(paddle, 0, y)

    def play(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)

        # Üst ve Alt duvar çarpışması
        if ball_coords[1] <= 0 or ball_coords[3] >= 400:
            self.ball_dy *= -1

        # Çubuk çarpışması kontrolü
        paddle_left_coords = self.canvas.coords(self.paddle_left)
        paddle_right_coords = self.canvas.coords(self.paddle_right)

        # Sol çubuk
        if (ball_coords[0] <= paddle_left_coords[2] and 
            paddle_left_coords[1] < ball_coords[3] and 
            paddle_left_coords[3] > ball_coords[1]):
            self.ball_dx = abs(self.ball_dx)

        # Sağ çubuk
        if (ball_coords[2] >= paddle_right_coords[0] and 
            paddle_right_coords[1] < ball_coords[3] and 
            paddle_right_coords[3] > ball_coords[1]):
            self.ball_dx = -abs(self.ball_dx)

        # Skor durumu
        if ball_coords[0] <= 0:
            self.score_right += 1
            self.reset_ball()
        elif ball_coords[2] >= 800:
            self.score_left += 1
            self.reset_ball()

        self.canvas.itemconfig(self.score_display, text=f"{self.score_left} - {self.score_right}")
        self.window.after(10, self.play)

    def reset_ball(self):
        self.canvas.coords(self.ball, 390, 190, 410, 210)
        self.ball_dx *= -1

if __name__ == "__main__":
    PongGame()