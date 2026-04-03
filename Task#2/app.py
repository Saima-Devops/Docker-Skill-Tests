from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    count = cache.incr('hits')
    return f"""
    <html>
        <head>
            <title>Visitor Counter</title>
            <style>
                body {{
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background: linear-gradient(135deg, #4facfe, #00f2fe);
                    font-family: Arial, sans-serif;
                    color: white;
                }}
                .card {{
                    background: rgba(0, 0, 0, 0.4);
                    padding: 40px 60px;
                    border-radius: 15px;
                    text-align: center;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
                }}
                h2 {{
                    margin-bottom: 10px;
                }}
                .count {{
                    font-size: 28px;
                    font-weight: bold;
                    color: #ffd700;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>Welcome 👋</h2>
                <p>This page has been visited</p>
                <div class="count">{count} times</div>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
