import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QPushButton, QButtonGroup, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # set up GUI
        self.setMinimumSize(350, 200)
        self.setWindowTitle("QVBoxLayout Example")

        self.setUpMainWindow()
        self.show()


    def setUpMainWindow(self):
        # create and arrange widgets in the main window
        headerLabel = QLabel("Checkzz")
        headerLabel.setFont(QFont("Arial", 18))
        headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        questionLabel = QLabel("Favorite Physics Branch?")
        questionLabel.setAlignment(Qt.AlignmentFlag.AlignTop)

        ratings = ["Nuclear Physics", "Quantum Physics", "Classical Physics"]

        ratingsGroup = QButtonGroup(self)
        ratingsGroup.buttonClicked.connect(self.checkboxClicked)

        self.confirmButton = QPushButton("Confirm")
        self.confirmButton.setEnabled(False)
        self.confirmButton.clicked.connect(self.close)

        mainVBox = QVBoxLayout()
        mainVBox.addWidget(headerLabel)
        mainVBox.addWidget(questionLabel)

        for checkbox in range(len(ratings)):
            ratingCheckbox = QCheckBox(ratings[checkbox])
            ratingsGroup.addButton(ratingCheckbox)
            mainVBox.addWidget(ratingCheckbox)

        mainVBox.addWidget(self.confirmButton)
        self.setLayout(mainVBox)

    def checkboxClicked(self, button):
        # check if QCheckBox in the button group has been clicked
        print(button.text())
        self.confirmButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())