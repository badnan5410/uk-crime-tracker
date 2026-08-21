from PyQt5.QtWidgets import (
    QWidget,
    QStackedWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)

from PyQt5.QtCore import pyqtSignal
from app.results.pages import Overview, Categories, ViewCrimes

class ResultsWidget(QWidget):
    new_search = pyqtSignal()

    def __init__(self):
        super().__init__()

        # api data
        self.geo_data = None
        self.police_data = None

        self.nav_bar = QWidget()
        self.nav_bar.setObjectName("results-nav-bar")

        self.stack = QStackedWidget()

        # navigation buttons
        self.overview_button = self.create_nav_button("Overview", "overview-page")
        self.categories_button = self.create_nav_button("Categories", "categories-page")
        self.view_crimes_button = self.create_nav_button("View Crimes", "view-crimes-page")

        self.new_search_button = self.create_nav_button("New Search")

        self.nav_buttons = [
            self.overview_button,
            self.categories_button,
            self.view_crimes_button,
            self.new_search_button
        ]

        # pages
        self.overview_page = Overview()
        self.categories_page = Categories()
        self.view_crimes_page = ViewCrimes()

        self.pages = {
            "overview-page": self.overview_page,
            "categories-page": self.categories_page,
            "view-crimes-page": self.view_crimes_page
        }

        self.initUI()

    def initUI(self):

        # main widget layout
        layout = QVBoxLayout()
        layout.addWidget(self.nav_bar)
        layout.addWidget(self.stack, 1)
        self.setLayout(layout)

        # nav-bar layout
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.overview_button)
        nav_layout.addWidget(self.categories_button)
        nav_layout.addWidget(self.view_crimes_button)
        nav_layout.addStretch()
        nav_layout.addWidget(self.new_search_button)
        self.nav_bar.setLayout(nav_layout)

        # add pages to stack
        for page in self.pages.values():
            self.stack.addWidget(page)

        # show pages
        for button in self.nav_buttons:
            button.clicked.connect(self.display_page)

    def display_page(self):
        button = self.sender()

        if not button.objectName():
            self.stack.setCurrentWidget(self.overview_page)
            self.new_search.emit()

        button_tag = button.objectName()
        page = self.pages.get(button_tag)

        self.stack.setCurrentWidget(page)
        self.highlight_button(button)

    def highlight_button(self, active_button):
        for button in self.nav_buttons:
            button.setStyleSheet("")

        active_button.setStyleSheet("""
            QPushButton {
                background-color: #6B7280;
                color: white;
            }

            QPushButton:hover {
                background-color: #4B5563;
                color: white;
            }
        """)

    def refresh_results(self):

        for page in self.pages.values():
            page.update_display(self.geo_data, self.police_data)

    @staticmethod
    def create_nav_button(button_name, button_tag=None):
        button = QPushButton(button_name)

        if button_tag is not None:
            button.setObjectName(button_tag)

        return button