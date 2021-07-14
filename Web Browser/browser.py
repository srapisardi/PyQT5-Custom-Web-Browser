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

        home_btn = QAction(QIcon('home-icon.png'), 'Click to open Home page', self)
        home_btn.triggered.connect(self.browser.back)
        nav.addAction(home_btn)




app = QApplication(sys.argv)
QApplication.setApplicationName("Sal's Custom Web Browser")
window = MainWindow()
app.exec_()
