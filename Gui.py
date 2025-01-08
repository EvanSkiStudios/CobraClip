from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

# https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/
# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cobra Clip")

        self.setFixedSize(QSize(400, 300))

        label = QLabel("YADA YADA DOODLES")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("test")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

