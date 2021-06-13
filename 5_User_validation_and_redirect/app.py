from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# This time we will bind two URLs with our function to add an optional argument.
@app.route("/")
@app.route("/<message>")
def display_login_page(message=None):
    # Let us say that index.html contains a login form.
    return render_template("index.html", message=message)


@app.route("/verify")
def verify_credentials():
    # To get the data from the inputs from the form in index.html we can use:
    login = request.args.get("login")
    password = request.args.get("password")

    # Usually, the login and the password will be obtained from the database. However, this time they will be hardcoded.
    if login == "Adrian" and password == "password":
        return f"Hello {login}!"

    # If credentials are incorrect, the user will be redirected to the login page.
    return redirect(url_for("display_login_page", message="Invalid username or password!"))


if __name__ == "__main__":
    app.run()
