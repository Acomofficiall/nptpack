import sys
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QVBoxLayout, 
                             QPushButton, QWidget, QHBoxLayout, QTabWidget, QStatusBar)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage

class ModernBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyOS Ultra Browser")
        self.setGeometry(100, 100, 1280, 720)

        # Ana Düzen
        self.layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # --- Navigasyon ve Sekme Kontrolü ---
        self.nav_bar = QHBoxLayout()
        
        self.back_btn = QPushButton("◀")
        self.back_btn.clicked.connect(lambda: self.current_browser().back())
        
        self.forward_btn = QPushButton("▶")
        self.forward_btn.clicked.connect(lambda: self.current_browser().forward())

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("URL yaz ve Enter'a bas...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
        self.new_tab_btn = QPushButton("➕")
        self.new_tab_btn.clicked.connect(lambda: self.add_new_tab(QUrl("https://www.google.com"), "Yeni Sekme"))

        self.fullscreen_btn = QPushButton("⛶")
        self.fullscreen_btn.clicked.connect(self.toggle_fullscreen)

        self.nav_bar.addWidget(self.back_btn)
        self.nav_bar.addWidget(self.forward_btn)
        self.nav_bar.addWidget(self.url_bar)
        self.nav_bar.addWidget(self.new_tab_btn)
        self.nav_bar.addWidget(self.fullscreen_btn)
        self.layout.addLayout(self.nav_bar)

        # --- Sekme Sistemi ---
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.tab_changed)
        self.layout.addWidget(self.tabs)

        # Eklenti Altyapısı (Adblocker vb. için Profil Ayarı)
        self.profile = QWebEngineProfile.defaultProfile()
        self.profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

        # İlk sekmeyi aç
        self.add_new_tab(QUrl("https://www.youtube.com"), "YouTube")

        self.status = QStatusBar()
        self.setStatusBar(self.status)

    def add_new_tab(self, qurl, label):
        browser = QWebEngineView()
        browser.setUrl(qurl)
        
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        # Sekme başlığını ve URL'yi güncelleme bağlamaları
        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_url_bar(qurl, browser))
        browser.titleChanged.connect(lambda title, browser=browser: self.update_tab_title(title, browser))

    def current_browser(self):
        return self.tabs.currentWidget()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.current_browser().setUrl(QUrl(url))

    def close_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    def update_url_bar(self, qurl, browser=None):
        if browser != self.current_browser():
            return
        self.url_bar.setText(qurl.toString())

    def update_tab_title(self, title, browser):
        index = self.tabs.indexOf(browser)
        if index != -1:
            self.tabs.setTabText(index, title[:15] + "..." if len(title) > 15 else title)

    def tab_changed(self, i):
        qurl = self.current_browser().url()
        self.update_url_bar(qurl, self.current_browser())

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
            self.nav_bar.setContentsMargins(0, 0, 0, 0)
        else:
            self.showFullScreen()
            # Tam ekranda navigasyonu gizlemek istersen buraya ekleme yapabilirsin

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F11:
            self.toggle_fullscreen()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernBrowser()
    window.show()
    sys.exit(app.exec())