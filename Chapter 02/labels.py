import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    
    def initializeUI(self):
        # set up UI
        self.setGeometry(100,100,250,250)
        self.setWindowTitle("Physics Engine")
        
        self.setUpMainWindow()
        self.show()


    def setUpMainWindow(self):
        # create Qlabel to be displayed in the main window
        helloLabel = QLabel(self)
        helloLabel.setText("Knee grow")
        helloLabel.move(105, 15)

        image = "images/world.png"
        try:
            with open(image):
                worldLabel = QLabel(self)
                pixmap = QPixmap(image)
                worldLabel.setPixmap(pixmap)
                worldLabel.move(25, 40)
        except FileNotFoundError as error:
            print(f"Image Not Found. \nError: {str(error)}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())