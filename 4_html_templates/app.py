from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def display_main_page():
    # Instead of returning a string, this time we will call function render_template.
    # return "<h1>Hello World!</h1>"

    # The function returns a string from the given file in folder templates.
    return render_template("index.html")
    # If there is no index.html or there is any other problem with the template file,
    # the following message will be displayed:
    # Internal Server Error
    # The server encountered an internal error and was unable to complete your request.
    # Either the server is overloaded or there is an error in the application.


@app.route("/welcome")
def display_welcome_page():
    # You may pass arguments to templates.
    return render_template("welcome.html", user_name="Adrian")


if __name__ == "__main__":
    app.run()
