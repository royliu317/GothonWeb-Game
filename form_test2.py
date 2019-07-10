from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)       

@app.route('/hello', methods=['POST', 'GET'])  # Via route decorator，index() function uses not only GET method but also POST method
def index():
    greeting = 'Hello World'
    # greeting can be marked since even if the value is none, index.html can also go to else and output Hello, world!
    # Moreover, the code has ensured greeting won't be none（at least there is ,）

    if request.method == "POST":     
        greet = request.form['greet']   # greet get the input from greet in hello_form.html（None if no input）
        name = request.form['name']     # name get the input from name in hello_form.html（None if no input）
        greeting = f'{greet},{name}'    # greeting won't be none
        return render_template("index.html", greeting = greeting)
    else:
        return render_template("hello_form.html")

if __name__ == "__main__":  
    app.run()
