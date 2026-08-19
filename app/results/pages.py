from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout
)

from api import police


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
        self.title_label = QLabel(
            "Crime Overview for TEST\nTEST AREA • TEST MONTH",
            self.header
        )

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

        self.total_crimes_label = QLabel(
            "TOTAL CRIMES\n000",
            self.total_crimes
        )

        self.common_crime_label = QLabel(
            "MOST COMMON CRIME\nTEST CRIME\n000 reports",
            self.common_crime
        )

        # object names
        self.header.setObjectName("overview-header")
        self.statistics.setObjectName("overview-statistics")
        self.about_results.setObjectName("overview-about-results")
        self.explore_further.setObjectName("overview-explore-further")

        self.total_crimes.setObjectName("overview-total-crimes")
        self.common_crime.setObjectName("overview-common-crime")

        self.title_label.setObjectName("overview-title-label")
        self.about_label.setObjectName("overview-about-label")
        self.explore_further_label.setObjectName(
            "overview-explore-further-label"
        )

        self.total_crimes_label.setObjectName(
            "overview-total-crimes-label"
        )
        self.common_crime_label.setObjectName(
            "overview-common-crime-label"
        )

        self.initUI()

    def initUI(self):
        # main layout
        layout = QVBoxLayout()
        layout.addWidget(self.header, 1)
        layout.addWidget(self.statistics, 2)
        layout.addWidget(self.about_results, 2)
        layout.addWidget(self.explore_further, 1)
        self.setLayout(layout)

        # statistics layout
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
        date = police.format_date(police_data[0]["month"])

        self.title_label.setText(
            f'Crime Overview for {geo_data["postcode"]}\n'
            f'{geo_data["admin_district"]}, {geo_data["region"]} • {date}'
        )

        # statistics
        self.total_crimes_label.setText(
            f"TOTAL CRIMES\n{len(police_data)}"
        )

        most_common_crime, most_common_crime_frequency = (
            police.get_most_common_crime(police_data)
        )

        self.common_crime_label.setText(
            f"MOST COMMON CRIME\n"
            f"{most_common_crime}\n"
            f"{most_common_crime_frequency} reports"
        )

        # about
        self.about_label.setText(
            "ABOUT THESE RESULTS\n\n"
            f"{len(police_data)} street-level crime records were reported within "
            f"approximately one mile of the searched location during {date}.\n\n"
            "Crime locations are approximate and anonymised. They should not be "
            "interpreted as the exact locations where incidents occurred."
        )


class Categories(QWidget):
    def __init__(self):
        super().__init__()
        self.tag = "categories-page"

        self.page_label = QLabel(
            "This is the categories page.",
            self
        )

    def update_display(self, geo_data, police_data):
        pass