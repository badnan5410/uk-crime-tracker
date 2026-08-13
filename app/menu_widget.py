import sys
from PyQt5.QtWidgets import (
    QWidget,
    QStackedWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)

from app.pages import HomePage, AboutPage, HowToUsePage, HistoryPage


class MenuWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.nav_bar = QWidget()
        self.nav_bar.setObjectName("nav-bar")

        self.stack = QStackedWidget()

        # navigation nav_buttons
        self.home_button = self.create_nav_button("Home", "home-page")
        self.about_button = self.create_nav_button("About Us", "about-page")
        self.how_to_use_button = self.create_nav_button("How to Use", "how-to-use-page")
        self.history_button = self.create_nav_button("Your History", "history-page")
        self.exit_button = self.create_nav_button("Exit")

        self.nav_buttons = [
            self.home_button,
            self.about_button,
            self.how_to_use_button,
            self.history_button,
            self.exit_button
        ]

        # pages
        self.home_page = HomePage()
        self.about_page = AboutPage()
        self.how_to_use_page = HowToUsePage()
        self.history_page = HistoryPage()

        self.pages = {
            "home-page": self.home_page,
            "about-page": self.about_page,
            "how-to-use-page": self.how_to_use_page,
            "history-page": self.history_page
        }

        self.initUI()

    def initUI(self):

        # main window layout
        layout = QHBoxLayout()
        layout.addWidget(self.nav_bar, 1)
        layout.addWidget(self.stack, 4)
        self.setLayout(layout)

        # nav-bar layout
        nav_layout = QVBoxLayout()
        nav_layout.addWidget(self.home_button)
        nav_layout.addWidget(self.about_button)
        nav_layout.addWidget(self.how_to_use_button)
        nav_layout.addWidget(self.history_button)
        nav_layout.addWidget(self.exit_button)
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
            sys.exit()

        button_tag = button.objectName()

        page = self.pages.get(button_tag)

        if page.tag == "home-page":
            page.postcode_input.setText("")
            page.error_label.setText("")

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

    @staticmethod
    def create_nav_button(button_name, button_tag=None):
        button = QPushButton(button_name)

        if button_tag is not None:
            button.setObjectName(button_tag)

        return button