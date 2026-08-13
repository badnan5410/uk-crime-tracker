from pathlib import Path

from PyQt5.QtWidgets import (
    QWidget,
    QStackedWidget, QVBoxLayout
)

from app.menu_widget import MenuWidget

class CrimeTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.window_stack = QStackedWidget()

        # windows
        self.menu_widget = MenuWidget()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Crime Tracker by Ali Ansari")
        self.setGeometry(700, 300, 1200, 1000)

        # full styles
        self.setStyleSheet(self.load_styles())

        # add windows to the stack
        self.window_stack.addWidget(self.menu_widget)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.window_stack)
        self.setLayout(layout)

    @staticmethod
    def load_styles():
        folder = Path("styles")
        combined_styles = ""

        for file in folder.glob("*.css"):
            with open(file, "r") as f:
                combined_styles += f.read()

        return combined_styles