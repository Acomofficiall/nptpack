import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QPushButton, 
                             QWidget, QFileDialog, QSlider, QHBoxLayout, QLabel)
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl, Qt

class GelsimisMedyaOynatici(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyOS Media Player Pro")
        self.setGeometry(100, 100, 900, 700)
        self.setStyleSheet("background-color: #121212; color: white;")

        # Medya Bileşenleri
        self.mediaPlayer = QMediaPlayer()
        self.videoWidget = QVideoWidget()
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        self.playback_rate = 1.0
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)

        # Zaman Çizelgesi
        self.positionSlider = QSlider(Qt.Orientation.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.set_position)
        layout.addWidget(self.positionSlider)

        # Kontrol Paneli
        controls = QHBoxLayout()
        
        self.openBtn = QPushButton("📂 Dosya Ac")
        self.openBtn.clicked.connect(self.open_file)
        
        self.playBtn = QPushButton("⏯ Oynat/Duraklat")
        self.playBtn.clicked.connect(self.play_video)

        self.speedLabel = QLabel("Hiz: 1.0x")
        
        self.volumeSlider = QSlider(Qt.Orientation.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(70)
        self.volumeSlider.setFixedWidth(100)
        self.volumeSlider.valueChanged.connect(self.set_volume)

        controls.addWidget(self.openBtn)
        controls.addWidget(self.playBtn)
        controls.addWidget(self.speedLabel)
        controls.addStretch()
        controls.addWidget(QLabel("🔊"))
        controls.addWidget(self.volumeSlider)
        
        layout.addLayout(controls)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Sinyaller
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
        # HATA BURADAYDI: directory parametresi QUrl() olarak verildi.
        file_url, _ = QFileDialog.getOpenFileUrl(
            self, 
            "Medya Dosyasi Sec", 
            QUrl(), 
            "Video Files (*.mp4 *.mkv *.avi *.mp3)"
        )
        if not file_url.isEmpty():
            self.mediaPlayer.setSource(file_url)
            self.mediaPlayer.play()

    def play_video(self):
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def set_volume(self, volume):
        self.audioOutput.setVolume(volume / 100)

    def position_changed(self, position):
        self.positionSlider.setValue(position)

    def duration_changed(self, duration):
        self.positionSlider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def keyPressEvent(self, event):
        # Klavye Kısayolları
        if event.key() == Qt.Key.Key_Space:
            self.play_video()
        elif event.key() == Qt.Key.Key_Right:
            self.mediaPlayer.setPosition(self.mediaPlayer.position() + 5000) # 5sn ileri
        elif event.key() == Qt.Key.Key_Left:
            self.mediaPlayer.setPosition(self.mediaPlayer.position() - 5000) # 5sn geri
        elif event.key() == Qt.Key.Key_Up:
            self.playback_rate = min(self.playback_rate + 0.25, 3.0)
            self.mediaPlayer.setPlaybackRate(self.playback_rate)
            self.speedLabel.setText(f"Hiz: {self.playback_rate}x")
        elif event.key() == Qt.Key.Key_Down:
            self.playback_rate = max(self.playback_rate - 0.25, 0.25)
            self.mediaPlayer.setPlaybackRate(self.playback_rate)
            self.speedLabel.setText(f"Hiz: {self.playback_rate}x")
        elif event.key() == Qt.Key.Key_F:
            if self.isFullScreen(): self.showNormal()
            else: self.showFullScreen()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = GelsimisMedyaOynatici()
    player.show()
    sys.exit(app.exec())