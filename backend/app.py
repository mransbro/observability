from flask import Flask
from random import uniform
from time import sleep

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    r = round(uniform(0.1, 3.0), 2)
    sleep(r)
    return f"{r}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
