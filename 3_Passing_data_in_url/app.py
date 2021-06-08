from flask import Flask

app = Flask(__name__)


@app.route("/subtraction/<minuend>/<subtrahend>")
def perform_subtraction(minuend, subtrahend):
    try:
        a = float(minuend)
        b = float(subtrahend)
        return str(a - b)
    except ValueError:
        return "<h1>Error!</h1><p>An invalid number has been entered..</p>"


if __name__ == "__main__":
    app.run()
