import sys, random
from PyQt6.QtWidgets import (QApplication, QMainWindow,
 QWidget, QLabel, QPushButton, QVBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # set up applications GUI
        self.setMinimumSize(200,200)
        self.setWindowTitle("Changing Icons Example")
        self.setWindowIcon(QIcon("images/pyqt_logo.png"))

        self.setUpMainWindow()
        self.show()


    def setUpMainWindow(self):
        # create and arrange widgets in the main window

        infoLabel = QLabel("Click on the button and select a fruit.")
        infoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.images = [
            "images/1_apple.png", "images/2_pineapple.png", "images/3_watermelon.png", "images/4_banana.png"
        ]

        self.iconButton = QPushButton()
        self.iconButton.setIcon(
            QIcon(random.choice(self.images))
        )
        self.iconButton.setIconSize(QSize(60,60))
        self.iconButton.clicked.connect(self.changeButtonIcon)


        # create vertical layout and add widgets
        mainVerticalBox = QVBoxLayout()
        mainVerticalBox.addWidget(infoLabel)
        mainVerticalBox.addWidget(self.iconButton)

        # set main layout window
        container = QWidget()
        container.setLayout(mainVerticalBox)
        self.setCentralWidget(container)


    def changeButtonIcon(self):
        # change the icon when clicked
        self.iconButton.setIcon(QIcon(random.choice(self.images)))
        self.iconButton.setIconSize(QSize(60,60))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())