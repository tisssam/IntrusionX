from flask import Flask, render_template, jsonify
from log_analysis import analyze_logs

app = Flask(__name__)

LOG_FILE = "sample_logs/auth.log"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/alerts")
def alerts():

    data = analyze_logs(LOG_FILE)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)