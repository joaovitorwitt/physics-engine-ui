import sys, json
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QTextEdit, QGridLayout
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # set up applications GUI
        self.setMinimumSize(500, 300)
        self.setWindowTitle("QGridLayout Example")

        self.setUpMainWindow()
        self.loadWidgetsFromFile()
        self.show()


    def setUpMainWindow(self):
        # create and arrange widgets in the main window
        headerLabel = QLabel("Simple Daily Planner")
        headerLabel.setFont(QFont("Arial", 20))
        headerLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # create widgets for the left side of the window
        todayLabel = QLabel("— Today's Focus")
        todayLabel.setFont(QFont("Arial", 14))
        self.todayTextEdit = QTextEdit()

        notesLabel = QLabel("— Notes")
        notesLabel.setFont(QFont("Arial", 14))
        self.notesTextEdit = QTextEdit()

        # organize the left side widgets into column 0 of the QGridlayout
        self.mainGrid = QGridLayout()
        self.mainGrid.addWidget(headerLabel, 0, 0)

        self.mainGrid.addWidget(todayLabel, 1, 0)
        self.mainGrid.addWidget(self.todayTextEdit, 2, 0, 3, 1) # the extra 3, 1 tell that the widget will span 3 rows and 1 column

        self.mainGrid.addWidget(notesLabel, 5, 0)
        self.mainGrid.addWidget(self.notesTextEdit, 6, 0, 3, 1)

        # create widgets for the right side of the window
        today = QDate.currentDate().toString(Qt.DateFormat.ISODate)
        dateLabel = QLabel(today)
        dateLabel.setFont(QFont("Arial", 18))
        dateLabel.setAlignment(Qt.AlignmentFlag.AlignRight)

        todoLabel = QLabel("— To Do")
        todoLabel.setFont(QFont("Arial", 14))

        # organize the right side widgets into columns 1 and 2 of the QGridLayout
        self.mainGrid.addWidget(dateLabel, 0, 2)
        self.mainGrid.addWidget(todoLabel, 1, 1, 1, 2)

        # create 7 rows, from indexes 2-8
        for row in range(2, 9):
            itemCheckbox = QCheckBox()
            itemInput = QLineEdit()
            self.mainGrid.addWidget(itemCheckbox, row, 1)
            self.mainGrid.addWidget(itemInput, row, 2)

        # set layout for the main window
        self.setLayout(self.mainGrid)


    def saveWidgetValues(self):
        # collect and save the widget values
        details = {"focus": self.todayTextEdit.toPlainText(),
                   "notes": self.notesTextEdit.toPlainText()}
        
        remainingTodo = []

        # check the values of the QCheckBox Widgets
        for row in range(2, 9):
            # retrieve the QLayoutItem object
            item = self.mainGrid.itemAtPosition(row, 1)

            # retrieve the widget (QCheckBox)
            widget = item.widget()

            if widget.isChecked() == False:
                # retrieve the QLayoutItem object
                item = self.mainGrid.itemAtPosition(row, 2)

                # retrieve the widget (input value)
                widget = item.widget()
                text = widget.text()

                if text != "":
                    remainingTodo.append(text)

                
            # save text from input widgets
            details["todo"] = remainingTodo
        
        with open("details.txt", "w") as f:
            f.write(json.dumps(details))


    def closeEvent(self, event):
        # save widgets and values when closing the window
        self.saveWidgetValues()

    
    def loadWidgetsFromFile(self):
        # retrieve previous values from last session

        # check if file exists
        try:
            with open("details.txt", "r") as file:
                details = json.load(file)

                # retrieve and set values for the widgets
                self.todayTextEdit.setText(details["focus"])
                self.todayTextEdit.setText(details["notes"])

                # set the text for input widgets
                for row in range(len(details["todo"])):
                    # retrieve the QLayoutItem object
                    item = self.mainGrid.itemAtPosition(row + 2, 2)

                    # retrieve the widget
                    widget = item.widget()
                    widget.setText(details["todo"][row])
        
        except FileNotFoundError as error:
            # create the file since it doesn't exist
            file = open("details.txt", "w")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


