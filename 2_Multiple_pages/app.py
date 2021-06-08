from flask import Flask

app = Flask(__name__)


@app.route("/first_page")
def display_first_page():
    # This will be displayed at http://127.0.0.1:5000/first_page
    # Notice that the HTML tags may be returned.
    return "<h1>This is the first page!</h1>"


@app.route("/second_page")
def display_second_page():
    # This will be displayed at http://127.0.0.1:5000/second_page
    # The returned string may contain JavaScript code as well.
    return """
        <h1>This is the second page!</h1>
        <div id="clock">00 : 00</div>

        <script type="text/javascript">
            var hours = 0;
            var minutes = 0;
            var seconds = 0;

            function formatTime(){
                if(hours<10)
                    hours = "0" + hours;
                if(minutes<10)
                    minutes = "0" + minutes;
                if(seconds<10)
                    seconds = "0" + seconds;
            }

            function setClock(){
                var dateObject = new Date();
                hours = dateObject.getHours();
                minutes = dateObject.getMinutes();
                seconds = dateObject.getSeconds();

                formatTime();

                document.getElementById('clock').innerHTML =
                    hours
                    + ' : '
                    + minutes
                    + '<sub>'
                    + seconds
                    + '</sub>';
                setTimeout('setClock();', 1000);
            }
            
            setClock();
        </script>
    """

# Notice that if you enter http://127.0.0.1:5000/ in your browser address bar, the following content will be displayed:
# <h1>Not Found</h1> <p>The requested URL was not found on the server. If you entered the URL manually please check
# your spelling and try again.</p>
# This is a default page created by Flask.


if __name__ == "__main__":
    app.run()
