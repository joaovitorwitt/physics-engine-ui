import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QComboBox, QSpinBox, QDoubleSpinBox, QStackedLayout, QFormLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap


# example include multiple pages
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # set up GUI
        self.setFixedSize(300, 340)
        self.setWindowTitle("Stacked layout example")

        self.setUpMainWindow()
        self.show()


    def setUpMainWindow(self):
        # create and arrange widgets in the main window
        # create and connect the combo box to switch pages
        pageCombo = QComboBox()
        pageCombo.addItems(["Image", "Description", "Additional Info"])
        pageCombo.activated.connect(self.switchPage)

        # create the Image page (Page 1)
        profileImage = QLabel()
        pixmap = QPixmap("images/norwegian.jpg")
        profileImage.setPixmap(pixmap)
        profileImage.setScaledContents(True)

        # create the profile page (Page 2)
        pageTwoForm = QFormLayout()
        pageTwoForm.setFieldGrowthPolicy(pageTwoForm.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        pageTwoForm.setFormAlignment(Qt.AlignmentFlag.AlignHCenter |
                                     Qt.AlignmentFlag.AlignTop)
        pageTwoForm.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        pageTwoForm.addRow("Breed:", QLabel("Norwegian Forest cat"))
        pageTwoForm.addRow("Origin:", QLabel("Norway"))
        pageTwoForm.addRow(QLabel("Description"))
        descriptionText = """ Have a long, sturdy body, long legs and a bushy tail.
        They are friendly, intelligent, and generally good with people. """

        pageTwoForm.addRow(QTextEdit(descriptionText))

        pageTwoContainer = QWidget()
        pageTwoContainer.setLayout(pageTwoForm)


        # create the about page (Page 3)
        pageThreeForm = QFormLayout()
        pageThreeForm.setFieldGrowthPolicy(pageThreeForm.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        pageThreeForm.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                   Qt.AlignmentFlag.AlignTop)
        pageThreeForm.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        pageThreeForm.addRow(QLabel("Enter your cats info."))
        pageThreeForm.addRow("Name:", QLineEdit())
        pageThreeForm.addRow("Color:", QLineEdit())

        ageInput = QSpinBox()
        ageInput.setRange(0, 30)
        pageThreeForm.addRow("Age:", ageInput)

        weightInput = QDoubleSpinBox()
        weightInput.setRange(0.0, 30.0)
        pageThreeForm.addRow("Weight (kg):", weightInput)

        pageThreeContainer = QWidget()
        pageThreeContainer.setLayout(pageThreeForm)

        # create stacked layout and add pages
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(profileImage)
        self.stackedLayout.addWidget(pageTwoContainer)
        self.stackedLayout.addWidget(pageThreeContainer)

        # create main layout
        mainVerticalBox = QVBoxLayout()
        mainVerticalBox.addWidget(pageCombo)
        mainVerticalBox.addLayout(self.stackedLayout)

        # set layout for the main window
        self.setLayout(mainVerticalBox)

    
    def switchPage(self, index):
        # slot for switching between tabs
        self.stackedLayout.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())