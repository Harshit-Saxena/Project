import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from functions import frame1, frame2, frame3, frame4, grid


# * initalize the app 
app = QApplication(sys.argv)

# * window and settings 

window = QWidget()
window.setWindowTitle("Who wants to be a programmer??")
window.setFixedWidth(1000)
window.setStyleSheet("background: #17191a;")


frame1()   # ? From which screen the app should start...I had it set to frame2 so it was not showing the 1st page

window.setLayout(grid)

window.show()
sys.exit(app.exec())