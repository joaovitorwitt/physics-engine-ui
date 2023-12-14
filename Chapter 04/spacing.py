import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout


# example to demonstrate spacing
class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # set applications GUI
        self.setMinimumSize(300, 200)
        self.setWindowTitle("Spacing example")

        label = QLabel("Enter text")
        lineInput = QLineEdit()
        button = QPushButton("End")

        mainVerticalBox = QVBoxLayout()
        mainVerticalBox.addWidget(label)

        # spacing between label and input
        mainVerticalBox.addSpacing(20)
        mainVerticalBox.addWidget(lineInput)

        # makes input field go all the way to the bottom
        mainVerticalBox.addStretch()
        mainVerticalBox.addWidget(button)

        # add space to the outside of the layout
        mainVerticalBox.setContentsMargins(40,30,40,30)

        self.setLayout(mainVerticalBox)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())