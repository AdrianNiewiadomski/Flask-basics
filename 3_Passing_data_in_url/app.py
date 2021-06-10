from flask import Flask

app = Flask(__name__)


# Now, to perform a subtraction, a user has to enter two numbers in the address filed.
@app.route("/subtraction/<minuend>/<subtrahend>")
def perform_subtraction(minuend, subtrahend):
    try:
        a = float(minuend)
        b = float(subtrahend)
        return str(a - b)

    # If the entered values are not numeric, the exception will be raised.
    except ValueError:
        return "<h1>Error!</h1><p>An invalid number has been entered.</p>"


if __name__ == "__main__":
    app.run()
