import sys
from PyQt5.QtWidgets import QApplication
from app.crime_tracker import CrimeTracker

if __name__ == "__main__":
    app = QApplication(sys.argv)
    crime_tracker = CrimeTracker()
    crime_tracker.show()
    sys.exit(app.exec_())