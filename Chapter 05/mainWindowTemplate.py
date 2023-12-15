import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # set applications GUI
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Main Window Template")

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()


    def setUpMainWindow(self):
        # create and arrange widgets on the main window
        pass

    def createActions(self):
        # create application's menu

        # actions for the file menu
        self.quitAct = QAction("&Quit")
        self.quitAct.setShortcut("Ctrl+Q")
        self.quitAct.triggered.connect(self.close)

    
    def createMenu(self):
        # create the applications menu bar
        self.menuBar().setNativeMenuBar(False)

        # create file menu and add actions
        fileMenu = self.menuBar().addMenu("File")
        fileMenu.addAction(self.quitAct)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())