# GothonWeb Game
 A web game made by Python


# Logical：
 1. Create room class，instantiate each room_object，add next_path property {action: next_room_object} for each room_object
 2. Use room_name to get room_object based on globals() dictionary {room_name：room_object}（Default value is central_corridor）
 3. Use the action input by Player for trying to get next_room_object baesd on the room_object.next_path property {action: next_room_object}
 4. If the action is valid，then get next_room_object and go to the next room. If not, then redirect to current room.


# Procedure：
1. Player raises .../hello request from web browser（first request）
2. flask calls index() function to handle the request
3. Since request.method is GET，run the code in else, which means to return hello_form.html and show on the web browser（for Player to fill the form）
4. After Player filled the form and click submit，a new request is raised from web browser to server（second request）：
   （1）Since hello_form sets method="POST"，so web browser will use POST type request to send the data from from to server
   （2）since hello_form sets action="/hello"，so the request will be sent to .../hello page of the server.
5. When Server gets the request，flask will call index() function to handle it again.
6. Since the request.method == "POST"，so the code in if will be executed, which is：
   Load hello_form's greet and name value-->Assign to greeting-->Send into render template index.html-->Return index.html and show on web browser