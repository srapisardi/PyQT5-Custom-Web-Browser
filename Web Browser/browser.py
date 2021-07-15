from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        nav = QToolBar()
        nav.setIconSize(QSize(24,24))
        self.addToolBar(nav)

        home_btn = QAction(QIcon('home-icon.png'), 'Click to go home', self)
        home_btn.triggered.connect(self.browser.back)
        nav.addAction(home_btn)

        back_btn = QAction(QIcon('back-icon.png'), 'Click to go back', self)
        back_btn.triggered.connect(self.browser.back)
        nav.addAction(back_btn)

        forward_btn = QAction(QIcon('forward-icon.png'), 'Click to go forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        nav.addAction(forward_btn)

        reload_btn = QAction(QIcon('reload-icon.png'), 'Click to reload page', self)
        reload_btn.triggered.connect(self.browser.reload)
        nav.addAction(reload_btn)

        self.url_entry = QLineEdit()
        self.url_entry.returnPressed.connect(self.navigate_to_url)
        nav.addWidget(self.url_entry)
        self.browser.urlChanged.connect(self.update_url)

    def home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_entry.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, entered_url):
        self.url_entry.setText(entered_url.toString())



app = QApplication(sys.argv)
QApplication.setApplicationName("Sal's Custom Web Browser")
window = MainWindow()
app.exec_()
