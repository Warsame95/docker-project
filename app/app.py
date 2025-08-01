from flask import Flask, render_template
from redis import Redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/count")
def count():
    visits = r.incr('visits')
    return render_template("count.html", count=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5002)