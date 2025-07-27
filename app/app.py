from flask import Flask
from redis import Redis

app = Flask(__name__)
r = Redis(host='localhost', port=6379, decode_responses=True)

@app.route("/")
def index():
    html = """
    <h1>Welcome to my flask app.</h1>
    <form action="/count">
             <button type="submit">Go to Counter</button>
    </form>
    """
    return html

@app.route("/count")
def count():
    visits = r.incr('visits')
    print(r.get('visits'))
    return f"""<h1>{visits} visits</h1>"""