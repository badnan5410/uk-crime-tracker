import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

from pages import HomePage, AboutPage, HowToUsePage, HistoryPage


class CrimeTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.nav_bar = QWidget()
        self.nav_bar.setObjectName("nav-bar")
        self.stack = QStackedWidget()

        # buttons
        self.home_button = self.create_nav_button("Home", "home-page")
        self.about_button = self.create_nav_button("About Us", "about-page")
        self.how_to_use_button = self.create_nav_button("How to Use", "how-to-use-page")
        self.history_button = self.create_nav_button("Your History", "history-page")
        self.exit_button = self.create_nav_button("Exit")

        self.buttons = [
            self.home_button,
            self.about_button,
            self.how_to_use_button,
            self.history_button,
            self.exit_button
        ]

        # pages
        self.home_page = self.create_page("home-page")
        self.about_page = self.create_page("about-page")
        self.how_to_use_page = self.create_page("how-to-use-page")
        self.history_page = self.create_page("history-page")

        self.pages = {
            "home-page": self.home_page,
            "about-page": self.about_page,
            "how-to-use-page": self.how_to_use_page,
            "history-page": self.history_page
        }

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Crime Tracker")
        self.setGeometry(900, 500, 1000, 800)

        # main window layout
        layout = QHBoxLayout()
        layout.addWidget(self.nav_bar, 1)
        layout.addWidget(self.stack, 4)
        self.setLayout(layout)

        # full styles
        self.setStyleSheet("""
            /* =========================
               WHOLE APPLICATION
               ========================= */

            CrimeTracker {
                background-color: #F3F4F6;
            }


            /* =========================
               NAVIGATION SIDEBAR
               ========================= */

            QWidget#nav-bar {
                background-color: #1F2937;
                border-radius: 12px;
            }


            /* =========================
               NAVIGATION BUTTONS
               ========================= */

            QPushButton {
                background-color: transparent;
                color: #D1D5DB;

                border: none;
                border-radius: 8px;

                padding: 14px 18px;

                font-family: "Segoe UI";
                font-size: 32px;
                font-weight: bold;

                text-align: left;
            }

            QPushButton:hover {
                background-color: #374151;
                color: #FFFFFF;
            }

            QPushButton:pressed {
                background-color: #4B5563;
            }


            /* =========================
               MAIN PAGE AREA
               ========================= */

            QStackedWidget {
                background-color: #FFFFFF;
                border: 1px solid #E5E7EB;
                border-radius: 12px;
            }


            /* =========================
               TEXT
               ========================= */

            QLabel {
                background-color: transparent;
                color: #111827;

                font-family: "Segoe UI";
                font-size: 16px;
            }


            /* =========================
               TEXT INPUTS
               (for your Home page later)
               ========================= */

            QLineEdit {
                background-color: #FFFFFF;
                color: #111827;

                border: 2px solid #D1D5DB;
                border-radius: 8px;

                padding: 10px 12px;

                font-family: "Segoe UI";
                font-size: 16px;
            }

            QLineEdit:focus {
                border: 2px solid #3B82F6;
            }


            /* =========================
               SCROLLBARS
               (for About / How To Use later)
               ========================= */

            QScrollBar:vertical {
                background-color: #F3F4F6;
                width: 10px;
                margin: 0px;
                border: none;
            }

            QScrollBar::handle:vertical {
                background-color: #9CA3AF;
                border-radius: 5px;
                min-height: 30px;
            }

            QScrollBar::handle:vertical:hover {
                background-color: #6B7280;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            /* =========================
               HOME PAGE
               ========================= */
            
            QLabel#home-title {
                font-family: "Segoe UI";
                font-size: 40px;
                font-weight: 700;
                color: #111827;
            }
            
            QLabel#home-tag {
                font-family: "Segoe UI";
                font-size: 22px;
                font-weight: 400;
                color: #6B7280;
            }
            
            QLabel#postcode-label {
                font-family: "Segoe UI";
                font-size: 30px;
                font-weight: 600;
                color: #374151;
            }
            
            QLineEdit#postcode-input {
                min-width: 260px;
                max-width: 260px;
            
                padding: 14px 16px;
            
                background-color: #FFFFFF;
                color: #111827;
            
                border: 2px solid #D1D5DB;
                border-radius: 10px;
            
                font-family: "Segoe UI";
                font-size: 20px;
            }
            
            QLineEdit#postcode-input:focus {
                border: 2px solid #3B82F6;
            }
            
            QPushButton#search-button {
                min-width: 260px;
                max-width: 260px;
            
                padding: 14px 16px;
            
                background-color: #3B82F6;
                color: #FFFFFF;
            
                border: none;
                border-radius: 10px;
            
                font-family: "Segoe UI";
                font-size: 24px;
                font-weight: 700;
            
                text-align: center;
            }
            
            QPushButton#search-button:hover {
                background-color: #2563EB;
            }
            
            QPushButton#search-button:pressed {
                background-color: #1D4ED8;
            }
        """)

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
        for button in self.buttons:
            button.clicked.connect(self.display_page)

    def create_nav_button(self, button_name, button_tag=None):
        button = QPushButton(button_name)
        if button_tag is not None:
            button.setObjectName(button_tag)
        return button

    def create_page(self, page_tag):
        pages = {
            "home-page": HomePage(),
            "about-page": AboutPage(),
            "how-to-use-page": HowToUsePage(),
            "history-page": HistoryPage()
        }

        return pages[page_tag]

    def display_page(self):
        button = self.sender()

        if not button.objectName():
            sys.exit()

        button_tag = button.objectName()

        page = self.pages.get(button_tag)
        self.stack.setCurrentWidget(page)
        self.highlight_button(button)

    def highlight_button(self, active_button):
        for button in self.buttons:
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    crime_tracker = CrimeTracker()
    crime_tracker.show()
    sys.exit(app.exec_())