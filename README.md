# Keylogger Detection Tool

A Python-based Windows cybersecurity project that detects potential keylogger activity using process monitoring and startup registry analysis.

This project demonstrates basic endpoint threat detection techniques used in defensive security.

---

## Features

- Monitors running processes
- Detects suspicious keywords in process names
- Checks Windows startup registry entries
- Real-time monitoring loop
- Logs alerts to a file

---

## Technologies Used

- Python 3
- psutil
- pywin32
- colorama
- Windows Registry (winreg)

---

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/keylogger-detector.git

2. Navigate to the project folder:

cd keylogger-detector

3. Install required packages:

pip install psutil pywin32 colorama

---

## How to Run

python main.py

The program will:
- Scan every 15 seconds
- Display alerts in the terminal
- Save alerts inside alerts.log

---

## Project Structure

keylogger-detector/
│
├── main.py
├── process_monitor.py
├── signature_checker.py
├── registry_checker.py
├── logger.py
├── requirements.txt
└── README.md

---

## Disclaimer

This project is created for educational and defensive cybersecurity purposes only.
