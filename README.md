# 🗂️ Open Directory Honeypot

## 🧩 Features

- Delivering your **payload**
- Logging of all visits

## 📥 Deployment
After downloading, edit the ```config.py``` configure

```python
HONEYPOT_LIST = ["chrome.exe", "firefox.exe"] # LIST OF FILES
PAYLOAD_PATH = "" # PATH FOR PAYLOAD FILE
LOG_FILE = "honeypot.log" # PATH FOR LOG FILE
```

After that, open the console, go to the directory and enter the following commands

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
