import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap


"""
    this program creates a simple window displaying a users resume;
    rearranging the texts and fonts, displaying them in different sections of the window
"""

class UserProfile(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # set up application GUI
        self.setGeometry(50,50,250,400)
        self.setWindowTitle("User Profile")

        self.setUpMainWindow()
        self.show()


    def createImageLabels(self):
        # open image files and create image labels
        images = ["images/skyblue.png", "images/profile_image.png"]

        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)

                if image == "images/profile_image.png":
                    label.move(80, 20)
            except FileNotFoundError as error:
                print(f"Image Not Found.\n Error: {str(error)}")

    def setUpMainWindow(self):
        # create labels to de displayed in the window
        self.createImageLabels()

        userLabel = QLabel(self)
        userLabel.setText("John Doe")
        userLabel.setFont(QFont("Arial", 20))
        userLabel.move(85, 140)

        bioLabel = QLabel(self)
        bioLabel.setText("Biography")
        bioLabel.setFont(QFont("Arial", 17))
        bioLabel.move(15, 170)

        aboutLabel = QLabel(self)
        aboutLabel.setText("I am a Software Engineer with 10 year \
                           of experience creating awesome code.")
        aboutLabel.setWordWrap(True)
        aboutLabel.move(15, 190)

        skillsLabel = QLabel(self)
        skillsLabel.setText("Python | PHP | SQL | JavaScript")
        skillsLabel.move(15, 240)

        experienceLabel = QLabel(self)
        experienceLabel.setText("Experience")
        experienceLabel.setFont(QFont("Arial", 17))
        experienceLabel.move(15, 260)

        developerLabel = QLabel(self)
        developerLabel.setText("Python Developer")
        developerLabel.move(15, 310)

        devDatesLabel = QLabel(self)
        devDatesLabel.setText("Mar 2011 - Present")
        devDatesLabel.setFont(QFont("Arial", 10))
        devDatesLabel.move(15, 330)

        driverLabel = QLabel(self)
        driverLabel.setText("Pizza Delivery Driver")
        driverLabel.move(15, 350)

        driverDatesLabel = QLabel(self)
        driverDatesLabel.setText("Aug 2015 - Dec 2017")
        driverDatesLabel.setFont(QFont("Arial", 10))
        driverDatesLabel.move(15, 370)





# run program
if __name__ == "__main__":
    app = QApplication(sys.argv)        
    window = UserProfile()
    sys.exit(app.exec())
