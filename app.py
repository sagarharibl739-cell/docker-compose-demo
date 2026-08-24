from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")

r = redis.Redis(
    host=redis_host,
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    count = r.incr("visits")

    return f"""
    <html>
    <head>
        <title>Docker Compose Demo</title>
    </head>
    <body>
        <h1>Docker Compose Multi-Container Application</h1>
        <h2>Python + Redis</h2>
        <p>Application is running successfully!</p>
        <p>Visitor Count: {count}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
