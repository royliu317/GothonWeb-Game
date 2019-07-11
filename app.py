from flask import Flask
from flask import render_template

app = Flask(__name__)                                   # Flask(import_name)。use __name__ as the name of Flask web app
#app = Flask(__name__, template_folder="templates/")    # By default, html template is stored in "templates" folder. In case the folder can't be found，it can be set in here
@app.route('/')                                         # Decorator. route: Set view function decorator for specific URL rule. In here it is set in the root folder.
def index():                                            # flask calls index() function to handle the request from web browser. index() use decorator to know who to handle the route in Flask.
    greet = 'Hello World'
    return render_template("index.html", greeting = greet)

if __name__ == "__main__":                              # Check whether it is called by main function file
    app.run()                                           # Call run() function in Flask，then run the web app   
    #app.run(debug=1)  Enable Flask debug mode
    #app.run(threaded=True) If deadlock occurs in flask, set flask.run(threaded=True) to use threads track event，then we just can use ctrl+c to get rid of the issue.


# @route('/') --> index = route('/')(index)
