import sys
from PyQt6.QtWidgets import QApplication, QWidget

"""
    create an empty window
"""

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # set up application
        self.setGeometry(300,100,800,600)
        self.setWindowTitle("Physics Engine")

        # display window on the screen
        self.show()


# run program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())