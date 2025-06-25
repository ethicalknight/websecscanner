from gui import ScannerApp
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    scanner = ScannerApp()
    scanner.show()
    sys.exit(app.exec_())
