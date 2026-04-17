"""
app_starter.py
by HundredVisionsGuy
A bare bones starter code to begin with.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 300)

        layout = QVBoxLayout()
        title_label = QLabel("Title Label (Make this bigger, please!)")

        # get input from user
        self.name_input = QLineEdit(placeholderText="Name")
        self.town_input = QLineEdit(placeholderText="Town")
        self.state_input = QLineEdit(placeholderText="State")

        # add a push button to greet user
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.get_input)
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_inputs)

        # add a label to greet user
        self.instructions = "Enter your name, town, and state, then click the button."
        self.output_label = QLabel(self.instructions)
        self.output_label.setWordWrap(True)
        self.greet_label = QLabel()

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.output_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.town_input)
        layout.addWidget(self.state_input)
        layout.addWidget(submit_button)
        layout.addWidget(clear_button)
        layout.addWidget(self.greet_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
    
    # make functions to get input and clear input
    def get_input(self):    
        """Get the text from the name input and update the output label to greet the user."""
        output = ""
        name = self.name_input.text()
        town = self.town_input.text()
        state = self.state_input.text()

        if not name:
            output = "Please enter your name."
        elif not town:
            output = " Please enter your town."
        elif not state:
            output = " Please enter your state."
        else:
            output = f"Welcome, {name} from {town}, {state}!"

        self.greet_label.setText(output)
    
    def clear_inputs(self):        
        """Clear the text in the name input and reset the output label to its initial value."""
        self.name_input.clear()
        self.town_input.clear()
        self.state_input.clear()
        self.greet_label.clear()
        self.output_label.setText(self.instructions)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()