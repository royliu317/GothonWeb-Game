# Below code is used to test the usage of Page Layout

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)       

@app.route('/hello', methods=['POST', 'GET'])  
def index():
    greeting = 'Hello World'
    
    if request.method == "POST":     
        greet = request.form['greet']   
        name = request.form['name']     
        greeting = f'{greet},{name}'    
        return render_template("index_laid_out.html", greeting = greeting)
    else:
        return render_template("hello_form_laid_out.html")

if __name__ == "__main__":  
    app.run()
