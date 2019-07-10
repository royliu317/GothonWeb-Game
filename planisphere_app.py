# 实现逻辑：
# 1. 创建room类，实例化各个room_object，添加各个room_object的next_path属性{action: next_room_object} 
# 2. 基于全局变量globals()字典{room_name：room_object}，通过room_name，得到room_objetct（初始为central_corridor）
# 3. 基于room_object.next_path属性{action: next_room_object} ，通过获取玩家输入的action，尝试得到next_room_object
# 4. 若action有效，则可得到有效的next_room_object，并走到下一房间；若action无效，则返回（重定向回）当前所在房间



from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)   

@app.route('/')           
def index():                                                          # 场景1. 当玩家访问/重定向到游戏首页时：
    # this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START                          # session的意义在于，它可以在页面加载之间保存数据（跨页面存储）
    ##print("$$$ session['room_name'] 1 is:", session['room_name'])
    return redirect(url_for("game"))                                  # url_for()函数会告诉你game对应的URL，这样就不需要你去记住它了


@app.route("/game", methods=['GET', 'POST'])
def game():                                                           # 场景2. 当玩家被重定向到game页时：
    room_name = session.get('room_name')                              # 从session会话中获取room_name变量的值(str类型)，初始值为central_corridor
    ##print("$$$ room_name is:", room_name)

    if request.method == "GET":                                       # 场景3. 当玩家进入game页且未submit时（即提交给服务器的是GET请求）时：
        if room_name:
            room_object = planisphere.load_room(room_name)            # 通过load_name函数中的globals字典{room_name：room_object}，得到room_object值
            ##print("$$$ room_object 1 is:", room_object)  
            return render_template("show_room.html", room=room_object)# 将room_object传入html，以便html读取该对象的name、description等属性，用于在页面上显示
        else:     
            # why is else here? do you need it? 没必要，但保留if-else对是一个好习惯
            return render_template("you_died.html")

    else:                                                             # 场景4. 当玩家点击game页上的submit（即提交给服务器的时POST请求）时：
        action = request.form.get('action')                           # 服务器读取form表单中，玩家提交的'action'命名参数的值
        ##print("$$$ action is:", action)
        if room_name and action:                                      # 场景5. 若玩家submit时已填写了form：
            room_object = planisphere.load_room(room_name)            # 通过load_name函数中的globals字典{room_name：room_object}，得到room_object值
            ##print("$$$ room_object 2 is:", room_object)  
            next_room_object = room_object.go(action)                 # 通过go函数中的room_object.next_paths字典{action：next_room_object}，得到next_room_object值
            ##print("$$$ next_room_object is:", room_object)  
            if not next_room_object:                                  # 场景5-1. 如果玩家在form中填写的是无效action（即next_room_object为None，说明如上的room_object.go(action)未返回有效值）：
                ##print("next_room_object 1:", next_room_object)
                session['room_name'] = planisphere.name_room(room_object)  
                ##print("$$$ session['room_name'] 2 is:", session['room_name'])
            else:
                ##print("next_room_object 2:", next_room_object)        # 场景5-2. 如果玩家在form中填写的是有效action（即next_room_object不为None，即输入的action是有效动作）：
                session['room_name'] = planisphere.name_room(next_room_object)
                ##print("$$$ session['room_name'] 3 is:", session['room_name'])
        return redirect(url_for("game"))                              # 场景6. 玩家点击submit后，最终会被重定向回game页（无论刚刚是否填写了form）
                                                                      # 如果不重定向，刷新game页可能会发生奇怪错误(浏览器不喜欢在form表单背后被刷新，所以如果玩家提交完了form再刷新，就不会发生异常）。
                                                


# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == "__main__":  
    app.run(debug=1) 
