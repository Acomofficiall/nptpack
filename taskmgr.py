import sys
import psutil
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QProgressBar, QWidget
from PyQt6.QtCore import QTimer

class GorevYoneticisi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistem İzleyici")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()
        self.cpu_label = QLabel("CPU Kullanımı: %0")
        self.cpu_bar = QProgressBar()
        
        self.ram_label = QLabel("RAM Kullanımı: %0")
        self.ram_bar = QProgressBar()

        layout.addWidget(self.cpu_label)
        layout.addWidget(self.cpu_bar)
        layout.addWidget(self.ram_label)
        layout.addWidget(self.ram_bar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

    def update_stats(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        
        self.cpu_label.setText(f"CPU Kullanımı: %{cpu}")
        self.cpu_bar.setValue(int(cpu))
        
        self.ram_label.setText(f"RAM Kullanımı: %{ram}")
        self.ram_bar.setValue(int(ram))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GorevYoneticisi()
    ex.show()
    sys.exit(app.exec())