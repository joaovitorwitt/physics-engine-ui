import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout

"""
    program dealing with positions
"""

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # set up application
        self.setMinimumWidth(500)
        self.setFixedHeight(60)
        self.setWindowTitle("QHBox Layout Example")

        # display window on the screen
        self.setUpMainWindow()
        self.show()

    
    def setUpMainWindow(self):
        # create and arrange widgets
        nameLabel = QLabel("New Username")

        nameInput = QLineEdit()
        nameInput.setClearButtonEnabled(True)
        nameInput.textEdited.connect(self.checkUserInput)

        self.acceptButton = QPushButton("Confirm")
        self.acceptButton.setEnabled(False)
        self.acceptButton.clicked.connect(self.close)

        mainHBox = QHBoxLayout()
        mainHBox.addWidget(nameLabel)
        mainHBox.addWidget(nameInput)
        mainHBox.addWidget(self.acceptButton)
        self.setLayout(mainHBox)


    def checkUserInput(self, text):
        # check length and content of name input
        if len(text) > 0 and all(t.isalpha() or t.isdigit() for t in text):
            self.acceptButton.setEnabled(True)
        else:
            self.acceptButton.setEnabled(False)


# run program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())