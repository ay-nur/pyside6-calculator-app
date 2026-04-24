"""
basic_app.py
by HundredVisionsGuy
A demo of the most basic input/output: labels, text inputs, and buttons.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QSpinBox,
    QDoubleSpinBox,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic App")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 300)

        layout = QVBoxLayout()
        title_label = QLabel("Basic App: a simple greeting app.")

        # TODO: add a text input for user's name
        self.name_input = QLineEdit(placeholderText="Name")
        self.name_input.setContentsMargins(0,0,0,12)
        self.town_input = QLineEdit(placeholderText="Town")
        self.state_input = QLineEdit(placeholderText="State")

        # TODO: add one or more horizontal layouts with widgets side by side
        age_layout = QHBoxLayout()
        year_spinbox = QSpinBox()
        age_spinbox = QSpinBox()
        age_layout.addWidget(age_spinbox)
        age_layout.addWidget(year_spinbox)

        label_layout = QHBoxLayout()
        age_label = QLabel("Age", alignment=Qt.AlignmentFlag.AlignHCenter)
        year_label = QLabel("Year", alignment=Qt.AlignmentFlag.AlignHCenter)
        label_layout.addWidget(age_label)
        label_layout.addWidget(year_label)

        # TODO: add margins and spacing
        

        # TODO: add a push button to greet user
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.get_input)
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_inputs)

        # TODO: add a label to greet user
        self.instructions = "Enter your name, town, and state, then click the button."
        self.output_label = QLabel(self.instructions)
        self.output_label.setWordWrap(True)
        self.greet_label = QLabel()

        """
        Challenges:
            * Add another text input (last name, home town, etc.)
            * Add a clear button that, when clicked will
                - clear the text in the name input
                - reset the output text to its initial value
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.output_label)
        layout.addWidget(self.name_input)
        #layout.addWidget(self.town_input)
        #layout.addWidget(self.state_input)
        layout.addLayout(label_layout)
        layout.addLayout(age_layout)
        layout.addWidget(submit_button)
        layout.addWidget(clear_button)
        layout.addWidget(self.greet_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
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
            output = f"Hello, {name} from {town}, {state}!"

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