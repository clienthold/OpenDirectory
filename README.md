# 🗂️ Open Directory Honeypot [![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge\&logo=flask\&logoColor=white)](https://flask.palletsprojects.com/)

**Flask-based open directory honeypot** that serves configurable payloads and logs every download attempt for threat analysis and security monitoring.

---

## 📋 Table of Contents

* [🔍 Features](#-features)
* [⚙️ Prerequisites](#️-prerequisites)
* [📥 Installation](#-installation)
* [🛠️ Configuration](#️-configuration)
* [▶️ Usage](#️-usage)
* [🚀 Deployment](#-deployment)

  * [🐧 Linux (Gunicorn)](#-linux-gunicorn)
  * [🪟 Windows (Waitress)](#-windows-waitress)
* [📄 Logging](#-logging)
---

## 🔍 Features

* Serve **custom payload files** on directory listings
* Log every download request with timestamp, client IP, user agent, and file requested
* Simple, configurable, and lightweight
* Ideal for deceptive directories, threat intelligence, and security research

## ⚙️ Prerequisites

* Python **3.7+**
* [Flask](https://flask.palletsprojects.com/) web framework

## 📥 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/clienthold/OpenDirectory.git
   cd OpenDirectory
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Configuration

Edit the `config.py` file to customize your honeypot:

```python
# List of filenames to present in the directory
HONEYPOT_LIST = [
    "chrome.exe",
    "firefox.exe",
    # add more as needed
]

# Absolute or relative path to the payload executable
PAYLOAD_PATH = "payload.exe"

# Path to the log file
LOG_FILE = "honeypot.log"
```

## ▶️ Usage

Run the Flask development server (for testing):

```bash
export FLASK_APP=honeypot.py  # or set FLASK_APP=honeypot.py on Windows
flask run --host=0.0.0.0 --port=8080
```

Navigate to `http://localhost:8080/` to see the directory listing.

## 🚀 Deployment

### 🐧 Linux (Gunicorn)

```bash
pip install gunicorn
gunicorn --bind 0.0.0.0:8080 honeypot:app
```

### 🪟 Windows (Waitress)

```bash
pip install waitress
waitress-serve --listen=*:8080 honeypot:app
```

## 📄 Logging

All download attempts are recorded in `honeypot.log` with the following format:

```
[2025-06-28 12:34:56] 192.0.2.1 "Mozilla/5.0..." chrome.exe
```

Use this data for forensic analysis or to feed into your SIEM.
