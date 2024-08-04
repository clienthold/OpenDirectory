from flask import Flask
from flask import request
from flask import render_template
from flask import abort
from flask import send_file
from datetime import datetime
from config import *

if (not HONEYPOT_LIST) or (not PAYLOAD_PATH) or (not LOG_FILE):
    raise ValueError("Honeypot is not configured! Please check config.py") 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return render_template("directory.html", files=HONEYPOT_LIST)

@app.route("/<file>", methods=["GET"])
def get_payload(file):
    if file in HONEYPOT_LIST:
        return send_file(PAYLOAD_PATH, download_name=file, mimetype="application/octet-stream", as_attachment=True)
    else:
        return abort(404)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.after_request
def logging(response):
    current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    with open(LOG_FILE, "a+", encoding="utf-8") as log:
        log.write(f"[{current_time}] {request.remote_addr} {request.method} {request.path}\n")
    
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)