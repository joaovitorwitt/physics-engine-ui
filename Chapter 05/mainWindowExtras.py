import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QCheckBox, QTextEdit, QDockWidget, QToolBar, QStatusBar, QVBoxLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Adding More Window Features")
        self.setUpMainWindow()
        self.createDockWidget()
        self.createActions()
        self.createMenu()
        self.createToolBar()
        self.show()

    
    def setUpMainWindow(self):
        # create and arrange widgets in the main window
        # create and set the central widget
        self.textInput = QTextEdit()
        self.setCentralWidget(self.textInput)

        # create status bar
        self.setStatusBar(QStatusBar())


    def createActions(self):
        # create the menu actions

        # create actions for FILE menu
        self.quitAction = QAction(QIcon("images/exit.png"), "Quit")
        self.quitAction.setShortcut("Ctrl+Q")
        self.quitAction.setStatusTip("Quit Program")
        self.quitAction.triggered.connect(self.close)

        # create actions for the VIEW menu
        self.fullScreenAction = QAction("Full Screen", checkable=True)
        self.fullScreenAction.setStatusTip("Swtich to full screen mode")
        self.fullScreenAction.triggered.connect(self.switchToFullScreen)


    def createMenu(self):
        # create the applications menu bar
        self.menuBar().setNativeMenuBar(False)

        # create FILE menu and add actions
        fileMenu = self.menuBar().addMenu("File")
        fileMenu.addAction(self.quitAction)

        # create VIEW menu, APPEARANCE submenu and add actions
        viewMenu = self.menuBar().addMenu("View")

        appearanceSubmenu = viewMenu.addMenu("Appearance")
        appearanceSubmenu.addAction(self.fullScreenAction)


    def switchToFullScreen(self, state):
        # if state is true, display the main window
        if state: self.showFullScreen()
        else: self.showNormal()


    def createToolBar(self):
        # create applications toolbar
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        # add actions to the toolbar
        toolbar.addAction(self.quitAction)


    # dock widgets are secondary windows that provide additional functionality to GUI windows
    def createDockWidget(self):
        dockWidget = QDockWidget()
        dockWidget.setWindowTitle("Formatting")
        dockWidget.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)

        # create widget examples to add to the dock
        autoBulletCheckbox = QCheckBox("Auto Bullet List")
        autoBulletCheckbox.toggled.connect(self.changeTextEditSettings)

        # create layout for dock widget
        dockVerticalBox = QVBoxLayout()
        dockVerticalBox.addWidget(autoBulletCheckbox)
        dockVerticalBox.addStretch(1)

        # create QWidget that acts as a container to hold widgets
        dockContainer = QWidget()        
        dockContainer.setLayout(dockVerticalBox)

        # set the main widget for the dock widget
        dockWidget.setWidget(dockContainer)

        # set initial location of dock widget in main window
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dockWidget)


    def changeTextEditSettings(self, checked):
        # change formatting features for QTextEdit
        if checked:
            self.textInput.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoBulletList)
        else:
            self.textInput.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)



        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())