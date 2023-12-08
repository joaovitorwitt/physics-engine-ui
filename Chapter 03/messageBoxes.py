import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QLineEdit, QPushButton
from PyQt6.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        # set up applications GUI
        self.setGeometry(100,100,340,140)

        self.setWindowTitle("QMessageBox Example")

        self.setUpMainWindow()
        self.show()


    def setUpMainWindow(self):
        # create and arrange widgets in the main window
        catalogueLabel = QLabel("Author Catalogue", self)
        catalogueLabel.move(100,10)
        catalogueLabel.setFont(QFont("Arial", 18))

        searchLabel = QLabel("Search the index for an author: ", self)
        searchLabel.move(20, 40)

        # create author label and input widgets
        authorLabel = QLabel("Name:", self)
        authorLabel.move(20, 74)

        self.authorEdit = QLineEdit(self)
        self.authorEdit.move(70, 70)
        self.authorEdit.resize(240, 24)
        self.authorEdit.setPlaceholderText("Enter name as: First Last")

        # create search QPushButton
        searchButton = QPushButton("Search", self)
        searchButton.move(140, 100)
        searchButton.clicked.connect(self.searchAuthors)


    def searchAuthors(self):
        # search through list of names
        # if name is found, display the author found dialog
        # otherwise, display author not found dialog

        file = "files/authors.txt"

        try:
            with open(file, "r") as f:
                authors = [line.strip("\n") for line in f]

            if self.authorEdit.text() in authors:
                QMessageBox.information(self, "Author Found", "Author found in catalogue!", QMessageBox.StandardButton.Ok)

            else:
                answer = QMessageBox.question(self, "Author Not Found",
                    """<p>Author not found in catalogue.</p>
                    <p>Do you wish to continue?</p>""",
                    QMessageBox.StandardButton.Yes | \
                    QMessageBox.StandardButton.No, 
                    QMessageBox.StandardButton.Yes)
                
                if answer == QMessageBox.StandardButton.No:
                    print("Closing application")
                    self.close()

        except FileNotFoundError as error:
            QMessageBox.warning(self, "Error",
                                f"""<p>File not found.</p>
                                    <p>Error: {error}</p>
                                    Closing application.""",
                                    QMessageBox.StandardButton.Ok)
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())