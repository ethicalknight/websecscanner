from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QLineEdit
from modules import xss, sqli, dir_enum, header_check, admin_finder

class ScannerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WebSecSimScanner - GUI")
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout()

        self.url_label = QLabel("Target URL:")
        self.url_input = QLineEdit()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)

        self.scan_button = QPushButton("Start Scan")
        self.scan_button.clicked.connect(self.start_scan)
        layout.addWidget(self.scan_button)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)

        self.setLayout(layout)

    def start_scan(self):
        url = self.url_input.text().strip()
        if not url:
            self.result_box.setText("Please enter a valid URL.")
            return
        self.result_box.append(f"[*] Scanning {url} ...\n")
        self.result_box.append(xss.scan(url))
        self.result_box.append(sqli.scan(url))
        self.result_box.append(dir_enum.scan(url))
        self.result_box.append(header_check.scan(url))
        self.result_box.append(admin_finder.scan(url))
        self.result_box.append("\n[+] Scan Complete!")
