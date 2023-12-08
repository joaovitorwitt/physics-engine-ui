import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLabel
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # set up applications GUI
        self.setGeometry(100,100,250,150)
        self.setWindowTitle("QCheckBox Example")

        self.setUpMainWindow()
        self.show()


    def setUpMainWindow(self):
        # create and arrange widgets in the main window
        headerLabel = QLabel("Which shifts can you work? \
                             (Please check all that apply)", self)
        headerLabel.setWordWrap(True)
        headerLabel.move(20,10)

        # set up the checkboxes
        morningCheckbox = QCheckBox("Morning [8 AM - 2 PM]", self)
        morningCheckbox.move(40, 60)
        # morningCheckbox.toggle() # start checked
        morningCheckbox.toggled.connect(self.printSelected)

        afternoonCheckbox = QCheckBox("Afternoon [1 PM - 8 PM]", self)
        afternoonCheckbox.move(40, 80)
        afternoonCheckbox.toggled.connect(self.printSelected)

        nightCheckbox = QCheckBox("Night [7 PM - 3 AM]", self)
        nightCheckbox.move(40, 100)
        nightCheckbox.toggled.connect(self.printSelected)


    def printSelected(self, checked):
        # print the text of a checkbox when selected or deselected
        # use sender() to determine which widget is sending signal
        sender = self.sender()

        if checked:
            print(f"{sender.text()} Selected")
        else:
            print(f"{sender.text()} Deselected")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
        