from gevent.wsgi import WSGIServer
from flask import (Flask, session, render_template, request, jsonify)
from flask_debugtoolbar import DebugToolbarExtension
import hashlib

app = Flask(__name__)
app.secret_key = "BOOOMSHAKALAKA"


@app.route('/')
def home():
    """landing page"""

    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    # connect_to_db(app)
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
    DebugToolbarExtension(app)
