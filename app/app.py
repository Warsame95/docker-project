from flask import Flask
from redis import Redis

app = Flask(__name__)
r = Redis(host='localhost', port=6379, decode_responses=True)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

@app.route("/count")
def count():
    visits = r.incr('visits')
    print(r.get('visits'))
    return f"""<h1>{visits} visits</h1>"""