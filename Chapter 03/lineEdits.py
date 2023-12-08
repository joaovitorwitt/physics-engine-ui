import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # set up application GUI
        self.setMaximumSize(310, 130)
        self.setWindowTitle("QLineEdit Example")

        self.setUpMainWindow()
        self.show()


    def setUpMainWindow(self):
        # create and arrange widgets in the main window
        QLabel("Enter your name below.", self).move(70, 10)
        nameLabel = QLabel("Name: ", self)
        nameLabel.move(20, 50)

        self.nameEdit = QLineEdit(self)
        self.nameEdit.resize(210, 20)
        self.nameEdit.move(70, 50)

        clearButton = QPushButton("Clear", self)
        clearButton.move(140, 90)
        clearButton.clicked.connect(self.clearText)

        acceptButton = QPushButton("OK", self)
        acceptButton.move(210, 90)
        acceptButton.clicked.connect(self.acceptText)


    def clearText(self):
        # clear QLineEdit input field
        self.nameEdit.clear()

    def acceptText(self):
        # accept users input and close window
        print(self.nameEdit.text())
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())