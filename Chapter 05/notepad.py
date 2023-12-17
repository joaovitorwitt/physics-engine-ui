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

        self.findAction = QAction(QIcon("images/find.png"), "Find")
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


    def clearText(self):
        # clear input field
        answer = QMessageBox.question(self, "Clear Text", "Do you want to clear the text?",
                                    QMessageBox.StandardButton.No | \
                                    QMessageBox.StandardButton.Yes,
                                    QMessageBox.StandardButton.Yes)

        if answer == QMessageBox.StandardButton.Yes:
            self.textInput.clear()

    
    def openFile(self):
        # clear text or html file and display its contents
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "HTML files (*.html);;Text Files (*.txt)")

        if fileName:
            with open(fileName, "r") as f:
                notepadText = f.read()
            self.textInput.setText(notepadText)


    def saveFile(self):
        # if the save button is clicked, ask user how they want to save the file
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "HTML Files (*.html);;Text Files (*.txt)")

        if fileName.endswith(".txt"):
            notepadText = self.textInput.toPlainText()
            with open(fileName, "w") as f:
                f.write(notepadText)

        elif fileName.endswith(".html"):
            notepadRichText = self.textInput.toHtml()
            with open(fileName, "w") as f:
                f.write(notepadRichText)

        else:
            QMessageBox.information(self, "Not Saved", "Text not saved.", QMessageBox.StandardButton.Ok)

    
    def searchText(self):
        # input dialog to ask user for search text
        findText, ok = QInputDialog.getText(self, "Search Text", "Find:")

        if ok:
            extraSelections = []

            # set cursor to the beginning
            self.textInput.moveCursor(
                QTextCursor.MoveOperation.Start
            )
            color = QColor(Qt.GlobalColor.gray)

            while (self.textInput.find(findText)):
                # mark the text searched for as gray
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(color)

                selection.cursor = self.textInput.textCursor()
                extraSelections.append(selection)

            # highlight all selections in the QTextEdit widget
            self.textInput.setExtraSelections(extraSelections)

    def removeHighlights(self):
        # reset selections after editing text
        self.textInput.setExtraSelections([])


    def chooseFont(self):
        # select a font from the QFontDialog
        current = self.textInput.currentFont()

        option = QFontDialog.FontDialogOption.DontUseNativeDialog
        font, ok = QFontDialog.getFont(current, self, options=option)

        if ok:
            self.textInput.setCurrentFont(font)

    
    def chooseFontColor(self):
        # select a font from the QColorDialog
        color = QColorDialog.getColor()

        if color.isValid():
            self.textInput.setTextColor(color)

    
    def chooseFontBackgroundColor(self):
        # select a color for texts background
        color = QColorDialog.getColor()

        if color.isValid():
            self.textInput.setTextBackgroundColor(color)


    def aboutDialog(self):
        # display the ABOUT dialog
        QMessageBox.about(self, "About Notepad", """<p>Beginner's Practical Guide to PyQt</p>
                                                    <p>Project 5.1 - Notepad GUI</p>""")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())        




