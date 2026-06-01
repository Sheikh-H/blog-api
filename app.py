from flask import Flask

import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(key_func=get_remote_address, app=app)


@app.before_first_request
def initialise_db():
    


@app.route("/", methods=["GET"])
@limiter.limit("50 per hour")
def home():
    
    pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host="127.0.0.1")
