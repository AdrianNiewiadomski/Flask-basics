# 1. Import Flask
from flask import Flask

# 2. Create an instance of flask application
app = Flask(__name__)


# 3. Define an URL of your page
@app.route('/')
def display_hello_world():
    # 4. Specify the content of the returned "page"
    return 'Hello world!'


if __name__ == "__main__":
    # 5. Run the application and open http://127.0.0.1:5000/ with your browser
    app.run()
