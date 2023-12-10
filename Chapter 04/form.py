import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QDateEdit, QLineEdit, QTextEdit, QComboBox,QFormLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QRegularExpression, QDate
from PyQt6.QtGui import QFont, QRegularExpressionValidator


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # Set up the application's GUI.
        self.setMinimumSize(500, 400)
        self.setWindowTitle("QFormLayout Example")
        self.setUpMainWindow()
        self.show()



    def setUpMainWindow(self):
        # create and arrange widgets in the main window
        headerLabel = QLabel("Favorite Scientist")
        headerLabel.setFont(QFont("Arial", 18))
        headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.firstNameInput = QLineEdit()
        self.firstNameInput.setPlaceholderText("First Name")
        self.firstNameInput.textEdited.connect(self.clearText)

        self.lastNameInput = QLineEdit()
        self.lastNameInput.setPlaceholderText("Last Name")
        self.lastNameInput.textEdited.connect(self.clearText)

        # create horizontal layout for names
        nameHorizontalBox = QHBoxLayout()
        nameHorizontalBox.addWidget(self.firstNameInput)
        nameHorizontalBox.addWidget(self.lastNameInput)

        # create additional widgets to be added in the window
        genderCombo = QComboBox()
        genderCombo.addItems(["Male", "Female"])

        self.phoneInput = QLineEdit()
        self.phoneInput.setInputMask("(999) 999-9999;_")
        self.phoneInput.textEdited.connect(self.clearText)

        self.birthdayInput = QDateEdit()
        self.birthdayInput.setDisplayFormat("MM/dd/yyyy")
        self.birthdayInput.setMaximumDate(QDate.currentDate())
        self.birthdayInput.setCalendarPopup(True)
        self.birthdayInput.setDate(QDate.currentDate())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
