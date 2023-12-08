import sys
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtGui import QFont, QPixmap

class NewUserDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initializeUI()


    def initializeUI(self):
        # set up applications GUI
        self.setFixedSize(360, 320)
        self.setWindowTitle("Registration GUI")
        self.setUpWindow()


    def setUpWindow(self):
        # create and arrange widgets in the window for collecting new account information
        loginLabel = QLabel("Create New Account", self)
        loginLabel.setFont(QFont("Arial", 20))
        loginLabel.move(90, 20)

        # create QLabel for image
        userImage = "images/new_user_icon.png"

        try:
            with open(userImage):
                userLabel = QLabel(self)
                pixmap = QPixmap(userImage)
                userLabel.setPixmap(pixmap)
                userLabel.move(150, 60)

        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")


        # create name QLabel and QLineEdit widgets
        nameLabel = QLabel("Username:", self)
        nameLabel.move(20, 144)

        self.nameEdit = QLineEdit(self)
        self.nameEdit.resize(250, 24)
        self.nameEdit.move(90, 140)

        # full name label and input widgets
        fullNameLabel = QLabel("Full Name:", self)
        fullNameLabel.move(20, 174)

        fullNameEdit = QLineEdit(self)
        fullNameEdit.resize(250, 24)
        fullNameEdit.move(90, 170)

        # password label and input widgets
        newPasswordLabel = QLabel("Password", self)
        newPasswordLabel.move(20, 204)

        self.newPasswordEdit = QLineEdit(self)
        self.newPasswordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.newPasswordEdit.resize(250, 24)
        self.newPasswordEdit.move(90, 200)

        # password label and password input confirmation widgets
        confirmPasswordLabel = QLabel("Confirm:", self)
        confirmPasswordLabel.move(20, 234)

        self.confirmPasswordEdit = QLineEdit(self)
        self.confirmPasswordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirmPasswordEdit.resize(250, 24)
        self.confirmPasswordEdit.move(90, 230)

        # create sign up QPushButton
        signUpButton = QPushButton("Sign Up", self)
        signUpButton.resize(320, 32)
        signUpButton.move(20, 270)
        signUpButton.clicked.connect(self.confirmSignUp)


    def confirmSignUp(self):
        # check if username and password are correct
        # if so, append username and password to the text file
        nameText = self.nameEdit.text()
        passwordText = self.newPasswordEdit.text()
        confirmPasswordText = self.confirmPasswordEdit.text()

        if nameText == "" or passwordText == "":
            QMessageBox.warning(self, "Error Message",
                                "Please enter username or password values",
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)
            
        elif passwordText != confirmPasswordText:
            QMessageBox.warning(self, "Error Message",
                                "Passwords dont match",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
            
        else:
            # return to login window if passwords match
            with open("files/users.txt", "a+") as file:
                file.write("\n" + nameText + " ")
                file.write(passwordText)
            self.close()