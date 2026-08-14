from pathlib import Path

from PyQt5.QtWidgets import (
    QWidget,
    QStackedWidget, QVBoxLayout
)

from app.menu_widget import MenuWidget
from app.results_widget import ResultsWidget

class CrimeTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.window_stack = QStackedWidget()

        # widgets
        self.menu_widget = MenuWidget()
        self.results_widget = ResultsWidget()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Crime Tracker by Ali Ansari")
        self.setGeometry(700, 300, 1200, 1000)

        # full styles
        self.setStyleSheet(self.load_styles())

        # add windows to the stack
        self.window_stack.addWidget(self.menu_widget)
        self.window_stack.addWidget(self.results_widget)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.window_stack)
        self.setLayout(layout)

        # switching to results
        self.menu_widget.home_page.search_successful.connect(
            self.open_results
        )

        # switching to menu
        self.results_widget.new_search.connect(
            self.open_menu
        )

    def open_results(self, data):
        self.results_widget.geo_data = data
        self.window_stack.setCurrentWidget(self.results_widget)
        self.results_widget.highlight_button(self.results_widget.overview_button)

    def open_menu(self):
        self.window_stack.setCurrentWidget(self.menu_widget)



    @staticmethod
    def load_styles():
        folder = Path("styles")
        combined_styles = ""

        for file in folder.glob("*.css"):
            with open(file, "r") as f:
                combined_styles += f.read()

        return combined_styles