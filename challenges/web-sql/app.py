from flask import Flask, request
import requests
import os

app = Flask(__name__)

FLAG = os.environ.get("CHALLENGE_FLAG", "flag{ssrf_devtools_2026}")

@app.route("/")
def index():
    return "SSRF container is alive"

@app.route("/fetch")
def fetch():
    url = request.args.get("url")
    if not url:
        return "No URL provided"
    try:
        r = requests.get(url, timeout=3)
        return r.text[:500]
    except Exception as e:
        return str(e)

@app.route("/internal/flag")
def internal_flag():
    return FLAG

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
