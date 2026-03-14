from flask import Flask, render_template, jsonify
from log_analysis import analyze_logs
import requests

app = Flask(__name__)

LOG_FILE = "sample_logs/auth.log"


def get_country(ip):

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")

        data = response.json()

        return data.get("country", "Unknown")

    except:
        return "Unknown"


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/alerts")
def alerts():

    data = analyze_logs(LOG_FILE)

    for alert in data:

        alert["country"] = get_country(alert["ip"])

    return jsonify(data)


if __name__ == "__main__":

    app.run(debug=True)