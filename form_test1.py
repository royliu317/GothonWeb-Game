from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)       

@app.route('/hello')   # 服务器从浏览器接收到访问.../hello的请求后，flask web app会去处理，然后python代码就会去运行index.GET这个handler
def index():
    name = request.args.get('name', 'Nobody')   # 使用request.args从浏览器获取数据，返回一个简单的字典（以键值对的方式包含表单值）
    # radiansdict.get(key, default=None) ：返回指定键的值，如果值不在字典中返回default值
    greet = request.args.get('greet', 'Hello')
    
    if name:
        greeting = f'{greet}, {name}'
    else:                              # 其实不需要else部分，因为name永远不会为空（就算不输入也默认为Nobody字符串）
        greeting = 'Hello, Mr.World'
    
    return render_template("index.html", greeting = greeting)

if __name__ == "__main__":  
    app.run()               
