import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt

"""
    late night late night
"""

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # set up application
        self.setGeometry(100,100,250,150)
        self.setWindowTitle("QPushButton Example")

        # display window on the screen
        self.setUpMainWindow()
        self.show()


    def setUpMainWindow(self):
        # create and arrange widgets in the main window
        self.timesPressed = 0

        self.nameLabel = QLabel("Do not press the button", self)
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nameLabel.move(60,30)

        self.button = QPushButton("Press the button", self)
        self.button.move(80, 70)
        self.button.clicked.connect(self.buttonClicked)

    
    def buttonClicked(self):
        # code for when the button is clicked;
        # demonstrate how to change text for widgets;
        # update sizes and locations, and how to close the window due to events
        self.timesPressed += 1

        if self.timesPressed == 1:
            self.nameLabel.setText("Why did you press me? ")
        
        if self.timesPressed == 2:
            # change label's text
            self.nameLabel.setText("I am warning you!")
            
            # change button's text
            self.button.setText("Feeling Lucky?")
            self.button.adjustSize()
            self.button.move(70,70)

        if self.timesPressed == 3:
            print("The window has been closed.")
            self.close()
        


# run program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())