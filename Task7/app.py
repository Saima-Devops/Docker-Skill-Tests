# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h3 style='font-size:60px;'>👋 Hello from Flask Multi-Stage Build!</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
