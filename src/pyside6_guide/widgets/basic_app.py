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
        title_label = QLabel("Game Price Calculator")
        title_label.setContentsMargins(0,0,0,12)

        # TODO: add a text input for game name
        self.name_input = QLineEdit(placeholderText="Name")
        self.name_input.setContentsMargins(0,0,0,12)

        # TODO: add one or more horizontal layouts with widgets side by side
        game_layout = QHBoxLayout()
        game_label = QLabel("Initial Price:")
        self.game_spinbox = QDoubleSpinBox()
        game_layout.addWidget(game_label)
        game_layout.addWidget(self.game_spinbox)

        sale_layout = QHBoxLayout()
        self.sale_spinbox = QSpinBox()
        sale_label = QLabel("Percent Off:")
        sale_layout.addWidget(sale_label)
        sale_layout.addWidget(self.sale_spinbox)

        # TODO: add limits for spinbox and labels
        self.game_spinbox.setMinimum(0.00)
        self.sale_spinbox.setMinimum(0)
        self.sale_spinbox.setMaximum(100)

        self.game_spinbox.setPrefix("$")
        self.sale_spinbox.setSuffix("%")

        # TODO: add a push button to display output
        buttons_layout = QHBoxLayout()
        submit_button = QPushButton("Calcluate")
        submit_button.clicked.connect(self.get_input)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_inputs)

        buttons_layout.addWidget(submit_button)
        buttons_layout.addWidget(clear_button)

        # TODO: add instructions
        self.instructions1 = "Enter the name of the game."
        self.instructions2 = "Enter the initial price and sale percentage."
        self.output_label = QLabel(self.instructions1)
        self.output_label.setWordWrap(True)
        self.gameprice_label = QLabel(self.instructions2)
        self.price_label = QLabel()

        # TODO: add stylesheets
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.output_label.setStyleSheet("font-size: 14px;")
        self.gameprice_label.setStyleSheet("font-size: 14px;")

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.output_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.gameprice_label)
        layout.addLayout(game_layout)
        layout.addLayout(sale_layout)
        layout.addLayout(buttons_layout)
        layout.addWidget(self.price_label)

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
        game = self.game_spinbox.value()
        sale = self.sale_spinbox.value()

        # Calculation
        convert = sale * 0.01
        price_off = game * convert
        output_sale = game - price_off
        
        # Output
        if not name:
            output = "Please enter the game name."
        elif game == 0.00:
            output = f'{name} is free!'
        elif sale == 0:
            output = f'{name} is not on sale.'
        else:
            output = f'{name} is on sale for {output_sale} dollars.'

        self.price_label.setText(output)
    
    def clear_inputs(self):        
        """Clear the text in the name input and reset the output label to its initial value."""
        self.name_input.clear()
        self.price_label.clear()
        self.game_spinbox.setValue(0)
        self.sale_spinbox.setValue(0)
        self.output_label.setText(self.instructions1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()