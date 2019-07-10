from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)       

@app.route('/hello', methods=['POST', 'GET'])  # 通过route装饰器，index函数中使用的不再只是GET方法，还有POST方法
def index():
    greeting = 'Hello World'
    # 如上语句是给greeting变量赋一个初始值，但可被mark掉，因为并不需要。原因是：
    # 即使变量的值为None，index.html也可导至else部分，并输出Hello, world!
    # 更何况当前的代码，已经确保了greeting变量不可能为None（至少它还会包含一个逗号）

    if request.method == "POST":     
        greet = request.form['greet']   # greet变量取hello_form.html中greet的input（未输入则为None）
        name = request.form['name']     # name变量取hello_form.html中name的input（未输入则为None）
        greeting = f'{greet},{name}'    # greeting变量不可能为None，因为至少它还有一个逗号
        return render_template("index.html", greeting = greeting)
    else:
        return render_template("hello_form.html")

if __name__ == "__main__":  
    app.run()



# 程序完整执行过程：
# 1. 用户从浏览器提出访问.../hello的请求（初次请求）
# 2. flask调用本python代码中的index()函数处理该请求
# 3. 由于该请求的类型(request.method)是GET，而非POST，所以执行else代码块，即返回hello_form.html呈现在浏览器上（供用户填充表单）
# 4. 用户填好表单后，点submit，即从浏览器向服务器提交新的请求（第2次请求）：
#   （1）由于hello_form设置了method="POST"，因此浏览器会使用POST类型的请求，将(form中用户输入的)数据发送给服务器
#   （2）由于hello_form设置了action="/hello"，因此该请求会被发送至服务器的.../hello页面
# 5. 服务器接收到发送至.../hello页面的新请求时，flask会再次调用本python代码中的index()函数处理请求
# 6. 由于本次请求的request.method == "POST"，所以执行if代码块，也就是：
#    读取hello_form中greet与name的值-->赋给此处的greeting变量-->将其作为命名参数传入渲染模版index.html，并返回index.html呈现在浏览器上


# GET请求：找服务器要东西；
# POST请求：你要发给服务器的数据，用作存储或处理