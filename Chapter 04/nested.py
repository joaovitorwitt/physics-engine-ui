import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QSpinBox, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self):
        # set up applications GUI
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        self.setMinimumSize(400, 160)
        self.setWindowTitle("Nested Layout Example")

        self.setUpMainWindow()
        self.show()


    def setUpMainWindow(self):
        # create and arrange widgets
        infoLabel = QLabel("Select 2 items for lunch and their prices")
        infoLabel.setFont(QFont("Arial", 16))
        infoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # create a list of food items and two separate
        # QComboBox widgets to display all of the items
        foodList =  ["egg", "turkey sandwich", "ham sandwich",
                    "cheese", "hummus", "yogurt", "apple", "banana",
                    "orange", "waffle", "carrots", "bread", "pasta",
                    "crackers", "pretzels", "coffee", "soda", "water"]
        
        foodCombo1 = QComboBox()
        foodCombo1.addItems(foodList)

        foodCombo2 = QComboBox()
        foodCombo2.addItems(foodList)

        # Create two QSpinBox widgets to display prices
        self.priceSpinBox1 = QSpinBox()
        self.priceSpinBox1.setRange(0, 100)
        self.priceSpinBox1.setPrefix("$")
        self.priceSpinBox1.valueChanged.connect(self.calculateTotal)

        self.priceSpinBox2 = QSpinBox()
        self.priceSpinBox2.setRange(0,100)
        self.priceSpinBox2.setPrefix("$")
        self.priceSpinBox2.valueChanged.connect(self.calculateTotal)

        # create two horizontal layouts for the QComboBox and QSpinBox widgets
        item1HorizontalBox = QHBoxLayout()
        item1HorizontalBox.addWidget(foodCombo1)
        item1HorizontalBox.addWidget(self.priceSpinBox1)

        item2HorizontalBox = QHBoxLayout()
        item2HorizontalBox.addWidget(foodCombo2)
        item2HorizontalBox.addWidget(self.priceSpinBox2)


        self.totalsLabel = QLabel("Total Spent: $")
        self.totalsLabel.setFont(QFont("Arial", 16))
        self.totalsLabel.setAlignment(Qt.AlignmentFlag.AlignRight)

        # organize widgets and layouts in the main window
        mainVerticalBox = QVBoxLayout()
        mainVerticalBox.addWidget(infoLabel)
        mainVerticalBox.addLayout(item1HorizontalBox)
        mainVerticalBox.addLayout(item2HorizontalBox)
        mainVerticalBox.addWidget(self.totalsLabel)

        # lastly, set layout
        self.setLayout(mainVerticalBox)


    def calculateTotal(self, value):
        # calculate total price and update total label
        total = self.priceSpinBox1.value() + self.priceSpinBox2.value()
        self.totalsLabel.setText(f"Total Spent: ${total}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())