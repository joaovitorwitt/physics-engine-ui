import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTextEdit, QFileDialog, QInputDialog,QFontDialog, QColorDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QTextCursor, QColor, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # set up applications GUI
        self.setMinimumSize(400, 500)
        self.setWindowTitle("Notepad App")

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()


    
    def setUpMainWindow(self):
        # create and arrange widgets in the main window
        self.textInput = QTextEdit()
        self.textInput.textChanged.connect(self.removeHighlights)
        self.setCentralWidget(self.textInput)


    def createActions(self):
        # create applications menu actions

        # create actions for FILE menu
        self.newAction = QAction(QIcon("images/new_file.png"), "New")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.clearText)

        self.openAction = QAction(QIcon("images/open_file.png"), "Open")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.openFile)

        self.saveAction = QAction(QIcon("images/save_file.png"), "Save")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.saveFile)

        self.quitAction = QAction(QIcon("images/exit.png"), "Quit")
        self.quitAction.setShortcut("Ctrl+Q")
        self.quitAction.triggered.connect(self.close)


        # create actions for the EDIT menu
        self.undoAction = QAction(QIcon("images/undo.png"), "Undo")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.textInput.undo)

        self.redoAction = QAction(QIcon("images/redo.png"), "Redo")
        self.redoAction.setShortcut("Ctrl+Shift+Z")
        self.redoAction.triggered.connect(self.textInput.redo)

        self.cutAction = QAction(QIcon("images/cut.png"), "Cut")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.textInput.cut)

        self.copyAction = QAction(QIcon("images/copy.png"), "Copy")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.textInput.copy)

        self.pasteAction = QAction(QIcon("images/paste.png"), "Paste")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.textInput.paste)

        self.findAction = QAction(QAction("images/find.png"), "Find")
        self.findAction.setShortcut("Ctrl+F")
        self.findAction.triggered.connect(self.searchText)

        # create actions for TOOLS menu
        self.fontAction = QAction(QIcon("images/font.png"), "Font")
        self.fontAction.setShortcut("Ctrl+T")
        self.fontAction.triggered.connect(self.chooseFont)

        self.colorAction = QAction(QIcon("images/color.png"), "Color")
        self.colorAction.setShortcut("Ctrl+Shift+C")
        self.colorAction.triggered.connect(self.chooseFontColor)

        self.highlightAction = QAction(QIcon("images/highlight.png"), "Highlight")
        self.highlightAction.setShortcut("Ctrl+Shift+H")
        self.colorAction.triggered.connect(self.chooseFontBackgroundColor)


        # create actions for HELP menu
        self.aboutAction = QAction("About")
        self.aboutAction.triggered.connect(self.aboutDialog)


    def createMenu(self):
        # create the applications menu bar
        self.menuBar().setNativeMenuBar(False)

        # create FILE menu and add actions
        fileMenu = self.menuBar().addMenu("File")
        fileMenu.addAction(self.newAction)

        fileMenu.addSeparator()

        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)

        fileMenu.addSeparator()

        fileMenu.addAction(self.quitAction)


        # create EDIT menu and add actions
        editMenu = self.menuBar().addMenu("Edit")
        editMenu.addAction(self.undoAction)
        editMenu.addAction(self.redoAction)

        editMenu.addSeparator()

        editMenu.addAction(self.cutAction)
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)

        editMenu.addSeparator()

        editMenu.addAction(self.findAction)

        # create TOOLS meny and add actions
        toolMenu = self.menuBar().addMenu("Tools")
        toolMenu.addAction(self.fontAction)
        toolMenu.addAction(self.colorAction)
        toolMenu.addAction(self.highlightAction)

        # create HELP menu and add actions
        helpMenu = self.menuBar().addMenu("Help")
        helpMenu.addAction(self.aboutAction)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())        




