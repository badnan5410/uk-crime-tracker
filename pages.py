from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.tag = "home-page"
        self.page_label = QLabel("This is the home page.", self)

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

