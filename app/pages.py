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

        # widgets
        self.header = QWidget(self)
        self.statistics = QWidget(self)
        self.about_results = QWidget(self)
        self.explore_further = QWidget(self)

        self.total_crimes = QWidget(self.statistics)
        self.common_crime = QWidget(self.statistics)

        # labels
        self.title_label = QLabel("Crime Overview for TEST\nTEST AREA • TEST MONTH", self.header)
        self.about_label = QLabel(
            "ABOUT THESE RESULTS\n\n"
            "XXX street-level crime records were reported within approximately "
            "one mile of the searched location during MONTH YEAR.\n\n"
            "Crime locations are approximate and anonymised. They should not be "
            "interpreted as the exact locations where incidents occurred.",
            self.about_results
        )

        self.explore_further_label = QLabel(
            "WANT TO EXPLORE FURTHER?\n\n"
            "Categories → See how recorded crimes are distributed by crime type.\n"
            "View Crimes → Explore individual crime records and their outcomes.",
            self.explore_further
        )

        self.total_crimes_label = QLabel("TOTAL CRIMES\n000", self.total_crimes)
        self.common_crime_label = QLabel("MOST COMMON CRIME\nTEST CRIME\n000 reports", self.common_crime)

        # tags
        self.header.setObjectName("overview-header")
        self.statistics.setObjectName("overview-statistics")
        self.about_results.setObjectName("overview-about-results")
        self.explore_further.setObjectName("overview-explore-further")

        self.total_crimes.setObjectName("overview-total-crimes")
        self.common_crime.setObjectName("overview-common-crime")

        self.title_label.setObjectName("overview-title-label")
        self.about_label.setObjectName("overview-about-label")
        self.explore_further_label.setObjectName("overview-explore-further-label")

        self.total_crimes_label.setObjectName("overview-total-crimes-label")
        self.common_crime_label.setObjectName("overview-common-crime-label")

        self.initUI()

    def initUI(self):

        # layouts
        layout = QVBoxLayout()
        layout.addWidget(self.header, 1)
        layout.addWidget(self.statistics, 2)
        layout.addWidget(self.about_results, 2)
        layout.addWidget(self.explore_further, 1)
        self.setLayout(layout)

        stats_layout = QHBoxLayout()
        stats_layout.addWidget(self.total_crimes)
        stats_layout.addWidget(self.common_crime)
        self.statistics.setLayout(stats_layout)

        # inner layouts
        header_layout = QVBoxLayout()
        header_layout.addWidget(self.title_label)
        self.header.setLayout(header_layout)

        about_results_layout = QVBoxLayout()
        about_results_layout.addWidget(self.about_label)
        self.about_results.setLayout(about_results_layout)

        explore_further_layout = QVBoxLayout()
        explore_further_layout.addWidget(self.explore_further_label)
        self.explore_further.setLayout(explore_further_layout)

        total_crimes_layout = QVBoxLayout()
        total_crimes_layout.addWidget(self.total_crimes_label)
        self.total_crimes.setLayout(total_crimes_layout)

        common_crime_layout = QVBoxLayout()
        common_crime_layout.addWidget(self.common_crime_label)
        self.common_crime.setLayout(common_crime_layout)

        # alignment
        self.title_label.setAlignment(Qt.AlignCenter)
        self.about_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.about_label.setWordWrap(True)

        self.explore_further_label.setAlignment(Qt.AlignCenter)
        self.explore_further_label.setWordWrap(True)

        self.total_crimes_label.setAlignment(Qt.AlignCenter)
        self.common_crime_label.setAlignment(Qt.AlignCenter)


    def update_display(self, geo_data, police_data):

        # header
        self.title_label.setText(
            f"Crime Overview for {geo_data["postcode"]}\n{geo_data["admin_district"]}, {geo_data["region"]} • TEST MONTH"
        )

        # statistics
        self.total_crimes_label.setText(
            f"TOTAL CRIMES\n{len(police_data)}"
        )

        most_common_crime, most_common_crime_frequency = police.get_most_common_crime(police_data)
        self.common_crime_label.setText(
            f"MOST COMMON CRIME\n{most_common_crime}\n{most_common_crime_frequency} reports"
        )

class Categories(QWidget):
    def __init__(self):
        super().__init__()
        self.tag = "categories-page"
        self.page_labe = QLabel("This is the categories page.", self)

    def update_display(self, geo_data, police_data):
        pass