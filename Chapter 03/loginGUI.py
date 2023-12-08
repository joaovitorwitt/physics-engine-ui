import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

# create later
from registration import NewUserDialog 


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # set up applications GUI
        self.setFixedSize(360, 220)
        self.setWindowTitle("Login GUI")
        
        self.setUpWindow()
        self.show()

    
    def setUpWindow(self):
        # create and arrange widgets in the main window
        self.isLoginSuccessful = False

        loginLabel = QLabel("Login", self)
        loginLabel.setFont(QFont("Arial", 20))
        loginLabel.move(160, 10)

        # create widgets for username
        usernameLabel = QLabel("Username:", self)
        usernameLabel.move(20, 54)

        # username input
        self.usernameEdit = QLineEdit(self)
        self.usernameEdit.resize(250, 24)
        self.usernameEdit.move(90, 50)

        # create widgets for password
        passwordLabel = QLabel("Password:", self)
        passwordLabel.move(20, 86)

        # password input
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEdit.resize(250, 24)
        self.passwordEdit.move(90, 82)

        # create QCheckBox for displaying password
        self.showPasswordCheckbox = QCheckBox("Show Password", self)
        self.showPasswordCheckbox.move(90,110)
        self.showPasswordCheckbox.toggled.connect(self.displayPasswordIfChecked)

        # create QPush for signing in
        loginButton = QPushButton("Login", self)
        loginButton.resize(320, 34)
        loginButton.move(20, 140)
        loginButton.clicked.connect(self.clickLoginButton)

        # create SignUp QLabel and QPushButton
        notMemberLabel = QLabel("Not a member? ", self)
        notMemberLabel.move(20, 186)

        signUpButton = QPushButton("Sign Up", self)
        signUpButton.move(120, 180)
        signUpButton.clicked.connect(self.createNewUser)


    def clickLoginButton(self):
        # check if username and password match any existing entries in users file
        # if match, show QMessageBox and close the program
        # otherwise, display warning QMessageBox
        users = {}

        file = "files/users.txt"

        try:
            with open(file, "r") as f:
                for line in f:
                    userInfo = line.split(" ")
                    usernameInfo = userInfo[0]
                    passwordInfo = userInfo[1].strip("\n")
                    users[usernameInfo] = passwordInfo

            # collect user and password information
            username = self.usernameEdit.text()
            password = self.passwordEdit.text()

            if (username, password) in users.items():
                QMessageBox.information(self, "Login Successful!", "Login Successful!", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                self.isLoginSuccessful = True
                self.close()
                self.openApplicationWindow()

            else:
                QMessageBox.warning(self, "Error Message", "Username or Password are incorrect.", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)

        except FileNotFoundError as error:
            QMessageBox.warning(self, "Error", f"""<p>File not found.</p>
                                <p>Error: {error}</p>""", QMessageBox.StandardButton.Ok)
            # create file if doesnt exist
            f = open(file, "w")

    def displayPasswordIfChecked(self, checked):
        # if QCheckButton is enabled, view password
        # otherwise hide password
        if checked:
            self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif checked == False:
            self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)


    def createNewUser(self):
        # open a dialog for creating a new account
        self.createNewUserWindow = NewUserDialog()
        self.createNewUserWindow.show()

    def openApplicationWindow(self):
        # open a mock main window after the user logs in
        self.mainWindow = MainWindow()
        self.mainWindow.show()


    def closeEvent(self, event):
        # display window asking the user for confirmation before closing the window
        if self.isLoginSuccessful == True:
            event.accept()

        else:
            answer = QMessageBox.question(self,
                                          "Are you sure you want to QUIT?",
                                          QMessageBox.StandardButton.No | \
                                            QMessageBox.StandardButton.Yes,
                                            QMessageBox.StandardButton.Yes)
            
            if answer == QMessageBox.StandardButton.Yes:
                event.accept()
            if answer == QMessageBox.StandardButton.No:
                event.ignore()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    
    def initializeUI(self):
        # set up applications GUI
        self.setMinimumSize(640, 426)
        self.setWindowTitle("Main Window")

        self.setUpMainWindow()


    def setUpMainWindow(self):
        # create and arrange widgets in the main window
        image = "images/background_kingfisher.jpg"

        try:
            with open(image):
                mainLabel = QLabel(self)
                pixmap = QPixmap(image)
                mainLabel.setPixmap(pixmap)
                mainLabel.move(0,0)

        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
