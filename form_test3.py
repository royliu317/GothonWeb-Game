# 本代码用于测试书中关于页面布局（Page Layout）的使用

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
