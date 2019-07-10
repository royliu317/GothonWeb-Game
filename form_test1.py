from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)       

@app.route('/hello')   # After Server gets request to .../hello from web borwser，flask web app will handle it， then python will run the handler of index.GET
def index():
    name = request.args.get('name', 'Nobody')   # Use request.args to get data from web browser，and return a simple dictionary.
    # radiansdict.get(key, default=None) ：return the specific value. if it is not in the dictionary, then return the default value
    greet = request.args.get('greet', 'Hello')
    
    if name:
        greeting = f'{greet}, {name}'
    else:                              # In fact else is not necessary since the name will never be empty（it will be Nobody string by default）
        greeting = 'Hello, Mr.World'
    
    return render_template("index.html", greeting = greeting)

if __name__ == "__main__":  
    app.run()               
