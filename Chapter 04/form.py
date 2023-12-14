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

        self.emailInput = QLineEdit()
        self.emailInput.setPlaceholderText("Enter your email address")

        regexOption = QRegularExpression()
        regex = QRegularExpression("\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[com]{3}\\b", regexOption.PatternOption.CaseInsensitiveOption)
        self.emailInput.setValidator(QRegularExpressionValidator(regex))
        self.emailInput.textEdited.connect(self.clearText)


        extraInfoInput = QTextEdit()
        self.feedbackLabel = QLabel()
        submitButton = QPushButton("SUBMIT")
        submitButton.setMaximumWidth(140)
        submitButton.clicked.connect(self.checkFormInformation)

        # create horizontal layout for last row of widgets
        submitHorizontalBox = QHBoxLayout()
        submitHorizontalBox.addWidget(self.feedbackLabel)
        submitHorizontalBox.addWidget(submitButton)


        # organize widgets and layouts in QFormLayout
        mainForm = QFormLayout()
        mainForm.setFieldGrowthPolicy(mainForm.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        mainForm.setFormAlignment(Qt.AlignmentFlag.AlignHCenter | \
                                  Qt.AlignmentFlag.AlignTop)
        mainForm.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        mainForm.addRow(headerLabel)
        mainForm.addRow("Name", nameHorizontalBox)
        mainForm.addRow("Gender", genderCombo)
        mainForm.addRow("Date of Birth", self.birthdayInput)
        mainForm.addRow("Phone", self.phoneInput)
        mainForm.addRow("Email", self.emailInput)
        mainForm.addRow(QLabel("Comments or Messages"))
        mainForm.addRow(extraInfoInput)
        mainForm.addRow(submitHorizontalBox)

        # set the layout for the main window
        self.setLayout(mainForm)


    def clearText(self, text):
        # clear the text for the QLabel that provides feedback
        self.feedbackLabel.clear()

    def checkFormInformation(self):
        # validating user input
        if self.firstNameInput.text() == "" or self.lastNameInput.text() == "":
            self.feedbackLabel.setText("[INFO] Missing names.")

        elif self.phoneInput.hasAcceptableInput() == False:
            self.feedbackLabel.setText("[INFO] invalid phone number")

        elif self.emailInput.hasAcceptableInput() == False:
            self.feedbackLabel.setText("[INFO] invalid email address")

            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
