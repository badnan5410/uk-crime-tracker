from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QScrollArea
from PyQt5.QtCore import Qt, pyqtSignal
from textwrap import dedent
from api import postcodes, police

# menu widget
class HomePage(QWidget):
    search_successful = pyqtSignal(dict, list)

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
        self.error_label = QLabel(self)

        self.title_label.setObjectName("home-title")
        self.tag_label.setObjectName("home-tag")
        self.input_label.setObjectName("postcode-label")
        self.postcode_input.setObjectName("postcode-input")
        self.search_button.setObjectName("search-button")
        self.error_label.setObjectName("error-label")

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

        layout.addWidget(self.error_label, alignment=Qt.AlignCenter)

        layout.addStretch()
        self.setLayout(layout)

        # search button
        self.search_button.clicked.connect(self.search_postcode)

    def search_postcode(self):
        postcode = self.postcode_input.text().strip()

        if postcode == "":
            self.error_label.setText("Please enter a postcode")
        else:
            geo_data, message = postcodes.get_postcode(postcode)

            if geo_data is None:
                self.error_label.setText(message)
            else:
                police_data, message = police.get_police_data(geo_data["latitude"], geo_data["longitude"])

                if police_data is None:
                    self.error_label.setText(message)
                else:
                    self.error_label.clear()
                    self.postcode_input.clear()
                    self.search_successful.emit(geo_data, police_data)

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

# results widget
class Overview(QWidget):
    def __init__(self):
        super().__init__()
        self.tag = "overview-page"
        self.page_label = QLabel("This is the overview page.", self)

class Categories(QWidget):
    def __init__(self):
        super().__init__()
        self.tag = "categories-page"
        self.page_labe = QLabel("This is the categories page.", self)