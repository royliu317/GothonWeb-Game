from flask import Flask
from flask import render_template

app = Flask(__name__)        # Flask(import_name)。用 __name__ 作为Flask web app的名字，即将app.py的文件名'app'用于命名（但也可以直接命名为其他str）
#app = Flask(__name__, template_folder="templates/")    # 默认就是用名为"templates"的文件夹存放html模版文件，但万一遇到找不到该文件夹的情况，可以在此显示设置该参数
@app.route('/')              # 该行代码表示装饰器。route: 为指定URL规则注册视图功能的装饰器。此处设为根目录（也能设置为更深目录，如'/test'）
def index():                 # flask调用index()函数处理来自浏览器的访问请求。index()通过修饰器知道了怎样处理Flask里的路由
    greet = 'Hello World'
    return render_template("index.html", greeting = greet)

if __name__ == "__main__":   # 判断是否由主函数文件直接调用（而非被其他文件代码引用）
    app.run()                # 调用Flask的run()方法，运行该web app   
    #app.run(debug=1)  启用Flask调试模式
    #app.run(threaded=True) 如果flask出现锁死状态（ctrl+c或关window都不管用）时，使用flask.run(threaded=True)，此时会使用线程追踪事件，然后就可用ctrl+c或其他方式解决锁死的问题了


# @route('/') 的本质就是 index = route('/')(index)


# Python模块的__name__属性：http://www.runoob.com/python3/python3-module.html
# python:浅析python中 __name__ = '__main__' 的作用： https://www.cnblogs.com/alan-babyblog/p/5147770.html
# python中__name__的使用： http://www.cnblogs.com/1204guo/p/7966461.html