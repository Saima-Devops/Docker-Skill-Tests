from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Flask App</title>
        </head>
        <body style="display:flex; justify-content:center; align-items:center; height:100vh; margin:0;">
            <h1>Welcome to Dockerized Flask Application!</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
