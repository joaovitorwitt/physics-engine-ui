import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,
 QWidget, QLabel, QPushButton, QDockWidget, QDialog,
 QFileDialog, QMessageBox, QToolBar, QStatusBar,
 QVBoxLayout)
from PyQt6.QtCore import Qt, QSize, QRect
from PyQt6.QtGui import (QIcon, QAction, QPixmap, QTransform,
 QPainter)
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        """Set up the application's GUI."""
        self.setFixedSize(650, 650)
        self.setWindowTitle("5.2 - Photo Editor GUI")
        self.setUpMainWindow()
        self.createToolsDockWidget()
        self.createActions()
        self.createMenu()
        self.createToolBar()
        self.show()


    def setUpMainWindow(self):
        # create and arrange widgets in the main window
        self.image = QPixmap()

        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.imageLabel)

        # create status bar
        self.setStatusBar(QStatusBar())

    
    def createActions(self):
        # create actions for FILE menu
        self.openAction = QAction(QIcon("images/open_file.png"), "Open")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.setStatusTip("Open a new image")
        self.openAction.triggered.connect(self.openImage)

        self.saveAction = QAction(QIcon("images/save_file.png"), "Save")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.setStatusTip("Save image")
        self.saveAction.triggered.connect(self.saveImage)

        self.printAction = QAction(QIcon("images/print.png"), "Print")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.setStatusTip("Print image")
        self.printAction.triggered.connect(self.printImage)
        self.printAction.setEnabled(False)

        self.quitAction = QAction(QIcon("images/quit.png"), "Quit")
        self.quitAction.setShortcut("Ctrl+Q")
        self.quitAction.setStatusTip("Quit program")
        self.quitAction.triggered.connect(self.close)


        # create action for EDIT menu
        self.rotate90Action = QAction("Rotate 90°")
        self.rotate90Action.setStatusTip("Rotate image 90° clockwise")
        self.rotate90Action.triggered.connect(self.rotateImage90)

        self.rotate180Action = QAction("Rotate 180°")
        self.rotate180Action.setStatusTip("Rotate image 180° clockwise")
        self.rotate180Action.triggered.connect(self.rotateImage180)

        self.flipHorizontalAction = QAction("Flip Horizontal")
        self.flipHorizontalAction.setStatusTip("Flip image across horizontal axis")
        self.flipHorizontalAction.triggered.connect(self.flipImageHorizontal)

        self.flipVerticalAction = QAction("Flip Vertical")
        self.flipVerticalAction.setStatusTip("Flip image across vertical axis")
        self.flipVerticalAction.triggered.connect(self.flipImageVertical)

        self.resizeAction = QAction("Resize Half")
        self.resizeAction.setStatusTip("Resize image to half the original size")
        self.resizeAction.triggered.connect(self.resizeImageHalf)

        self.clearAction = QAction(QIcon("images/clear.png"), "Clear Image")
        self.clearAction.setShortcut("Ctrl+D")
        self.clearAction.setStatusTip("Clear the current image")
        self.clearAction.triggered.connect(self.clearImage)


    def createMenu(self):
        # create applications menu bar 
        self.menuBar().setNativeMenuBar(False)

        # creat FILE menu and add actions
        fileMenu = self.menuBar().addMenu("File")
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.printAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.quitAction)

        # create EDIT menu and add actions
        editMenu = self.menuBar().addMenu("Edit")
        editMenu.addAction(self.rotate90)
        editMenu.addAction(self.rotate180)
        editMenu.addSeparator()
        editMenu.addAction(self.flipHorizontalAction)
        editMenu.addAction(self.flipVerticalAction)
        editMenu.addSeparator()
        editMenu.addAction(self.resizeAction)
        editMenu.addSeparator()
        editMenu.addAction(self.clearAction)

        # create VIEW menu and add actions
        viewMenu = self.menuBar().addMenu("View")
        viewMenu.addAction(self.toggleDockToolsAction)


    def createToolBar(self):
        # create the applications toolbar
        toolbar = QToolBar("Photo Editor Toolbar")
        toolbar.setIconSize(QSize(24,24))
        self.addToolBar(toolbar)

        # add actions to the toolbar
        toolbar.addAction(self.openAction)
        toolbar.addAction(self.saveAction)
        toolbar.addAction(self.printAction)
        toolbar.addAction(self.clearAction)
        toolbar.addSeparator()
        toolbar.addAction(self.quitAction)


    def createToolsDockWidget(self):
        # create the application's dock widget.
        # Use VIEW -> EDIT image tools to show/hide the dock
        dockWidget = QDockWidget()
        dockWidget.setWindowTitle("Edit Image Tools")
        dockWidget.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea |
            Qt.DockWidgetArea.RightDockWidgetArea
        )

        # create buttons for editing images
        self.rotate90 = QPushButton("Rotate 90°")
        self.rotate90.setMinimumSize(QSize(130, 40))
        self.rotate90.setStatusTip("Rotate image 90° clockwise")
        self.rotate90.clicked.connect(self.rotateImage90)

        self.rotate180 = QPushButton("Rotate 180°")
        self.rotate180.setMinimumSize(QSize(130, 40))
        self.rotate180.setStatusTip("Rotate image 180° clockwise")
        self.rotate180.clicked.connect(self.rotateImage180)

        self.flipHorizontal = QPushButton("Flip Horizontal")
        self.flipHorizontal.setMinimumSize(QSize(130, 40))
        self.flipHorizontal.setStatusTip("Flip image across horizontal axis")
        self.flipHorizontal.clicked.connect(self.flipImageHorizontal)

        self.flipVertical = QPushButton("Flip Vertical")
        self.flipVertical.setMinimumSize(QSize(130, 40))
        self.flipVertical.setStatusTip("Flip image across vertical axis")
        self.flipVertical.clicked.connect(self.flipImageVertical)

        self.resizeHalf = QPushButton("Resize Half")
        self.resizeHalf.setMinimumSize(QSize(130, 40))
        self.resizeHalf.setStatusTip("Resize Image to half the Original Size")
        self.resizeHalf.clicked.connect(self.resizeImageHalf)

        # create layout for dock widget
        dockVerticalBox = QVBoxLayout()
        dockVerticalBox.addWidget(self.rotate90)
        dockVerticalBox.addWidget(self.rotate180)
        dockVerticalBox.addStretch(1)
        dockVerticalBox.addWidget(self.flipHorizontal)
        dockVerticalBox.addWidget(self.flipVertical)
        dockVerticalBox.addStretch(1)
        dockVerticalBox.addWidget(self.resizeHalf)
        dockVerticalBox.addStretch(10)

        # create QWidget that acts as a container and set layout for the dock
        toolsContainer = QWidget()
        toolsContainer.setLayout(dockVerticalBox)
        dockWidget.setWidget(toolsContainer)

        # set initial location of dock widget
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dockWidget)

        # handle the visibility of the dock widget
        self.toggleDockAct = dockWidget.toggleViewAction()



    def openImage(self):
        # Open an image file and display its contents on the QLabel widget
        imageFile, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "JPEG Files (*.jpeg *.jpg);;PNG Files (*.png);; \
                                                   Bitmap Files (*.bmp);;GIF Files (*.gif)")
        
        if imageFile:
            self.image = QPixmap(imageFile)

            self.imageLabel.setPixmap(self.image.scaled(self.image_label_size(), 
                              Qt.AspectRatioMode.KeepAspectRatio,
                              Qt.TransformationMode.SmoothTransformation))

        else:
            QMessageBox.information(self, "No Image", "No Image Selected.", QMessageBox.StandardButton.Ok)

        self.printAction.setEnabled(True)

    
    def saveImage(self):
        # display dialog box to select image location and save image
        imageFile, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                   "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
                                                    Bitmap Files (*.bmp);;GIF Files (*.gif)")
        
        if imageFile and self.image.isNull() == False:
            self.image.save(imageFile)
        
        else:
            QMessageBox.information(self, "Not Saved", "Image not saved.", QMessageBox.StandardButton.Ok)


    def clearImage(self):
        # clears current image in the QLabel widget
        self.imageLabel.clear()
        self.image = QPixmap() # reset pixmap
        self.printAction.setEnabled(False)


    def rotateImage90(self):
        # rotate image 90° clockwise
        if self.image.isNull() == False:
            transform90 = QTransform().rotate(90)
            pixmap = QPixmap(self.image)
            mode = Qt.TransformationMode.SmoothTransformation
            rotated = pixmap.transformed(transform90, mode=mode)

            self.imageLabel.setPixmap(rotated.scaled(self.image_label_size(),
                                                     Qt.AspectRatioMode.KeepAspectRatio,
                                                     Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(rotated)
            self.imageLabel.repaint() # repaint the label


    def rotateImage180(self):
        # rotate image 180° clockwise
        if self.image.isNull() == False:
            transform180 = QTransform().rotate(180)
            pixmap = QPixmap(self.image)
            mode = Qt.TransformationMode.SmoothTransformation
            rotated = pixmap.transformed(transform180, mode=mode)

        self.imageLabel.setPixmap(rotated.scaled(self.image_label_size(),
                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                 Qt.TransformationMode.SmoothTransformation))
        
        # in order to keep from being allowed to rotate the image, set the rotated image as self.image
        self.image = QPixmap(rotated)
        self.imageLabel.repaint()


    def flipImageHorizontal(self):
        # mirror the image across the horizontal axis
        if self.image.isNull() == False:
            flipHorizontal = QTransform().scale(-1,1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flipHorizontal)

            self.imageLabel.setPixmap(flipped.scaled(self.image_label_size(),
                                                     Qt.AspectRatioMode.KeepAspectRatio,
                                                     Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(flipped)
            self.imageLabel.repaint()

    
    def flipImageVertical(self):
        # mirror the image across the vertical axis
        if self.image.isNull() == False:
            flipVertical = QTransform().scale(1,-1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flipVertical)

            self.imageLabel.setPixmap(flipped.scaled(self.image_label_size(),
                                                     Qt.AspectRatioMode.KeepAspectRatio,
                                                     Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(flipped)
            self.imageLabel.repaint()


    def resizeImageHalf(self):
        # resize the image to half its current size
        if self.image.isNull() == False:
            resize = QTransform().scale(0.5, 0.5)
            pixmap = QPixmap(self.image)
            resized = pixmap.transformed(resize)

            self.imageLabel.setPixmap(resized.scaled(self.image_label_size(),
                                                     Qt.AspectRatioMode.KeepAspectRatio,
                                                     Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(resized)
            self.imageLabel.repaint()


    def printImage(self):
        # print image and use QPrinter to select the native system format for the printer dialog
        printer = QPrinter()
        # configure the printer
        printDialog = QPrintDialog(printer)

        if printDialog.exec() == QDialog.DialogCode.Accepted:
            # use QPainter to output a PDF file
            painter = QPainter()        
            painter.begin(printer)

            # create QRect object to hold the painters current viewport, which is the imageLabel
            rect = QRect(painter.viewport())

            # get size of imageLabel and use it to set the size of the viewport
            size = QSize(self.imageLabel.pixmap().size())
            size.scale(rect.size(),
                       Qt.AspectRatioMode.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imageLabel.pixmap().rect())

            # scale imageLabel to fit the rect source (0,0)
            painter.drawPixmap(0,0,self.imageLabel.pixmap())
            painter.end()
            




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(
    Qt.ApplicationAttribute.AA_DontShowIconsInMenus, True)
    window = MainWindow()
    sys.exit(app.exec())