from ast import Try
from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["NO_PROXY"] = "127.0.0.1"
backend_ip = os.getenv("BACKEND_IP", "127.0.0.1")
backend_port = os.getenv("BACKEND_PORT", "5001")
secret_key = os.getenv("SECRET_KEY", "asUqfwin362gGRY44dT2fgus")

app = Flask(__name__)

app.config["SECRET_KEY"] = secret_key


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":

        try:
            r = requests.get(f"http://{backend_ip}:{backend_port}")
            message = r.text

        except requests.exceptions.ConnectionError:
            message = "Ping error. Check all services are running."

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
