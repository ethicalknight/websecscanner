# WebSecSimScanner

**WebSecSimScanner** is a lightweight web vulnerability scanner tool for simulating real-time scanning on locally hosted websites.

## ✅ Features

- XSS (Cross-site scripting) detection
- SQL Injection detection
- Directory enumeration
- HTTP header security check
- Admin panel finder
- PyQt5 GUI interface

## ⚙️ How It Works

The tool scans the provided URL (typically `http://localhost:8000`) for known vulnerabilities by sending HTTP requests and analyzing responses.

## 🖥 Requirements

- Python 3.x
- PyQt5
- requests

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

```bash
python scanner.py
```

## 🔐 Disclaimer

This tool is for **educational and simulation purposes only**. Do not scan any unauthorized or live systems without explicit permission.
