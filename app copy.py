from flask import Flask

import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(key_func=get_remote_address, app=app)


@app.before_first_request
def initialise_db():
    # This initialises the database before the first request and on flask load.
    pass


@app.route("/", methods=["GET", "PUT", "POST", "UPDATE", "DELETE"])
@limiter.limit("50 per hour")
def home():
    # First initialise the database and ensure that all the key configurations are set and apparent
    # Once database is connected and a new db is created to the project spec, load the db
    # Each request type should have its own function type of what arguments it takes.
    # There should be input validation for each which restricts user entry and sanitises inputs.
    # Request is made via this API to online database.
    pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host="127.0.0.1")
