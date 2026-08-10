from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QScrollArea
from PyQt5.QtCore import Qt
from textwrap import dedent

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.tag = "home-page"

        # contents
        self.title_label = QLabel(
            "CRIME TRACKER", self
        )
        self.tag_label = QLabel(
            "Check criminal activity in your local area", self
        )
        self.input_label = QLabel(
            "Enter postcode", self
        )
        self.postcode_input = QLineEdit()
        self.postcode_input.setPlaceholderText("e.g. SW1A 1AA")
        self.search_button = QPushButton("Find out now", self)

        self.title_label.setObjectName("home-title")
        self.tag_label.setObjectName("home-tag")
        self.input_label.setObjectName("postcode-label")
        self.postcode_input.setObjectName("postcode-input")
        self.search_button.setObjectName("search-button")

        self.initUI()

    def initUI(self):
        # layout & alignment
        layout = QVBoxLayout()

        layout.addStretch()

        layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        layout.addSpacing(10)

        layout.addWidget(self.tag_label, alignment=Qt.AlignCenter)

        layout.addSpacing(100)

        layout.addWidget(self.input_label, alignment=Qt.AlignCenter)
        layout.addSpacing(12)

        layout.addWidget(self.postcode_input, alignment=Qt.AlignCenter)
        layout.addSpacing(12)

        layout.addWidget(self.search_button, alignment=Qt.AlignCenter)

        layout.addStretch()

        self.setLayout(layout)

class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        self.tag = "about-page"
        self.title_label = QLabel("ABOUT CRIME TRACKER")
        self.title_label.setObjectName("about-title")
        self.page_label = QLabel(dedent("""
            UK Crime Tracker is a desktop application designed to make publicly available
            crime data easier to explore.

            The application allows users to enter a UK postcode and view crime information
            for the surrounding area in a clear, visual format.

            The project was built using Python and PyQt5, with data retrieved from public
            APIs. It is intended as both a practical tool and a software development
            portfolio project.

            Future features will include crime category breakdowns, trends over time,
            search history, and comparison tools.

            Crime Tracker does not provide legal advice or guarantee the safety of any
            location. The information shown is based on reported crime data and should be
            treated as informational only.
        """))
        self.page_label.setObjectName("about-text")
        self.scroll_area = QScrollArea()
        self.scroll_area.setObjectName("about-scroll")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.initUI()

    def initUI(self):
        content = QWidget()
        content_layout = QVBoxLayout()
        content_layout.addWidget(self.title_label)
        content_layout.addWidget(self.page_label)
        content.setLayout(content_layout)
        self.scroll_area.setWidget(content)

        page_layout = QVBoxLayout()
        page_layout.addWidget(self.scroll_area)
        self.setLayout(page_layout)

class HowToUsePage(QWidget):
    def __init__(self):
        super().__init__()
        self.tag = "how-to-use-page"
        self.page_label = QLabel("This is the how to use page.", self)

class HistoryPage(QWidget):
    def __init__(self):
        super().__init__()
        self.tag = "history-page"
        self.page_label = QLabel("This is the history page.", self)

