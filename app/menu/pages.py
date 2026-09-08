from textwrap import dedent

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QScrollArea,
    QComboBox
)

from datetime import date
from api import postcodes, police

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

        # year selector
        self.year_selector = QComboBox()
        self.populate_year_selector()

        # month selector
        self.month_selector = QComboBox()
        self.month_selector.hide()

        self.search_button = QPushButton("Find out now", self)
        self.error_label = QLabel(self)

        self.title_label.setObjectName("home-title")
        self.tag_label.setObjectName("home-tag")
        self.input_label.setObjectName("postcode-label")
        self.postcode_input.setObjectName("postcode-input")
        self.year_selector.setObjectName("year-selector")
        self.month_selector.setObjectName("month-selector")
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

        layout.addWidget(self.year_selector, alignment=Qt.AlignCenter)

        layout.addWidget(self.month_selector, alignment=Qt.AlignCenter)

        layout.addWidget(self.search_button, alignment=Qt.AlignCenter)

        layout.addWidget(self.error_label, alignment=Qt.AlignCenter)

        layout.addStretch()
        self.setLayout(layout)

        # select year
        self.year_selector.currentIndexChanged.connect(
            self.year_selected
        )

        # select month
        self.month_selector.currentIndexChanged.connect(
            self.month_selected
        )

        # search button
        self.search_button.clicked.connect(
            self.search_postcode
        )

    def search_postcode(self):
        postcode = self.postcode_input.text().strip()

        # postcode input validation
        if postcode == "":
            self.error_label.setText("Please enter a postcode")

        # year and month selector validation
        elif self.year_selector.currentIndex() == 0 or self.month_selector.currentIndex() == 0:
            self.error_label.setText("Please choose a valid date")

        else:
            geo_data, message = postcodes.get_postcode(postcode)

            if geo_data is None:
                self.error_label.setText(message)
            else:
                date = self.get_selected_date()

                police_data, message = police.get_police_data(
                    geo_data["latitude"],
                    geo_data["longitude"],
                    date
                )

                if police_data is None:
                    self.error_label.setText(message)
                else:
                    self.search_successful.emit(geo_data, police_data)

    def populate_year_selector(self):
        current_year = date.today().year
        year = ["Please select a year"]

        while "2023" not in year:
            year.append(str(current_year))
            current_year -= 1

        self.year_selector.addItems(year)

    def populate_month_selector(self):

        # clear old items
        self.month_selector.clear()

        # full month items
        months = [
            "Please select a month", "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]

        # check year
        year = self.year_selector.currentText()
        current_year = date.today().year

        if year == "2023":
            months = [
                "Please select a month",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ]
        elif year == str(current_year):
            current_month = date.today().month

            months = months[:current_month]

        # refresh month selector
        self.month_selector.addItems(months)

    def year_selected(self):

        # disable default text option
        year = self.year_selector.currentText()

        if year.isdigit():
            item = self.year_selector.model().item(0)
            item.setEnabled(False)

            # refresh month selector and show it
            self.populate_month_selector()
            self.month_selector.show()

    def month_selected(self):

        # disable default text option
        if self.month_selector.currentIndex() > 0:
            item = self.month_selector.model().item(0)
            item.setEnabled(False)

    def get_selected_date(self):
        year = self.year_selector.currentText()
        month_name = self.month_selector.currentText().lower()

        months = [
            "january", "february", "march", "april", "may", "june",
            "july", "august", "september", "october", "november", "december"
        ]

        month = months.index(month_name) + 1

        return f"{year}-{month:02}"


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

        self.page_label = QLabel(
            "This is the how to use page.",
            self
        )

class HistoryPage(QWidget):
    def __init__(self):
        super().__init__()
        self.tag = "history-page"

        self.page_label = QLabel(
            "This is the history page.",
            self
        )