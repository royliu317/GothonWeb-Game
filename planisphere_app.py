from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)   

@app.route('/')           
def index():                                                          # Scene 1. When Player visit/redirect to Homepage of the game：
    # this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START                          # Use session to save the cross-pages data
    ##print("$$$ session['room_name'] 1 is:", session['room_name'])
    return redirect(url_for("game"))                                  # url_for() function provides the url of the game


@app.route("/game", methods=['GET', 'POST'])
def game():                                                           # Scene 2. When Player is redirectd to the game page：
    room_name = session.get('room_name')                              # Get the value of room_name(str type) from the session. Default value is central_corridor
    ##print("$$$ room_name is:", room_name)

    if request.method == "GET":                                       # Scene 3. When Player enter the game but has not submitted （GET request to the server）：
        if room_name:
            room_object = planisphere.load_room(room_name)            # Get room_object value from the globals directary {room_name：room_object} in load_name() function
            ##print("$$$ room_object 1 is:", room_object)  
            return render_template("show_room.html", room=room_object)# Send room_object to html for loading the properties (name、description, etc.) of the objecct，to show in the html page
        else:     
            # why is else here? do you need it? No，but keep if-else is a good habit
            return render_template("you_died.html")

    else:                                                             # Scene 4. When Player click the submit on the game page（POST request to the server）：
        action = request.form.get('action')                           # Server load the value of the 'action' from the form table
        ##print("$$$ action is:", action)
        if room_name and action:                                      # Scene 5. If the form has been filled when Player click the submit：
            room_object = planisphere.load_room(room_name)            # Get room_object value from the globals directary {room_name：room_object} in load_name() function
            ##print("$$$ room_object 2 is:", room_object)  
            next_room_object = room_object.go(action)                 # Get room_object.next_paths directory {action：next_room_object} from go() function，to get the value of next_room_object
            ##print("$$$ next_room_object is:", room_object)  
            if not next_room_object:                                  # Scene 5-1. If Player filled in an invalid action in the form（next_room_object == None，which means room_object.go(action) doesn't return valid value）：
                ##print("next_room_object 1:", next_room_object)
                session['room_name'] = planisphere.name_room(room_object)  
                ##print("$$$ session['room_name'] 2 is:", session['room_name'])
            else:
                ##print("next_room_object 2:", next_room_object)      # Scene 5-2. If Player filled in valid actionin the form（next_room_object != None，which menas the action is valid）：
                session['room_name'] = planisphere.name_room(next_room_object)
                ##print("$$$ session['room_name'] 3 is:", session['room_name'])
        return redirect(url_for("game"))                              # Scene 6. After Player click the submit，it will be redirected to game page（no matter the form is filled or not）
                                                                     
                                                


# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == "__main__":  
    app.run(debug=1) 
