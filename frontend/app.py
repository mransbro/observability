from flask import Flask, render_template, request
import requests
import os

os.environ["NO_PROXY"] = "127.0.0.1"

app = Flask(__name__)
app.config["SECRET_KEY"] = "IOPuHGFFk773VAUEn2bcwim3"


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        r = requests.get("http://127.0.0.1:5001").text
        message = r
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
