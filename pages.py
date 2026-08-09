from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

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
        self.page_label = QLabel("This is the about page.", self)

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

