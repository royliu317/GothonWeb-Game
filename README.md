# GothonWeb Game
 A web game made by Python.  
 ![spaceship](/img/spaceship.jpg)

# Description
 This is a text-based adventure game called **Gothons From Planet Percal #25** running on web browser, which is similar with **Zork** or **Adventure**. 
 
 The background is the alien has invaded our spacecraft, and you are the one, who needs to go across the maze made by kinds of rooms, beat the aliens, get the Lifeboat, and return to our planet.
 
 The game will use an engine to hold a map with full of rooms. When Player enters a room, it will shows its description and tells the engine what the next room is.


# Prereqquisites
1. Install Python 3
2. Install Flask
3. Install nosetests


# What's Going On?
Here's what's happening when your browser hits your application:
1. Your browser makes a network connection to your own computer, which is called localhost and is a standard way of saying "whatever my own computer is called on the network." It also uses port 5000.
2. Once it connects, it makes an HTTP request to the app.py application and asks for the / URL, which is commonly the first URL on any website.
3. Inside app.py you've got a list of URLs and what functions they match. The only one we have is the '/', 'hello_world' mapping. This means that whenever someone goes to / with a browser, flask will find the def hello_world and run it to handle the request.
4. Now that flask has found def hello_world, it calls it to actually handle the request. This function runs and simply returns a string for what flask should send to the browser.
5. Finally, flask has handled the request and sends this response to the browser, which is what you are seeing.


# How the Web Works?
![Flow](/img/Flow.png)
1. You type in the url http://test.com/ into your browser, and it sends the request on line (A) to your computer's network interface.
2. Your request goes out over the internet on line (B) and then to the remote computer on line (C) where my server accepts the request.
3. Once my computer accepts it, my web application gets it on line (D), and my Python code runs the index.GET handler.
4. The response comes out of my Python server when I return it, and it goes back to your browser over line (D) again.
5. The server running this site takes the response off line (D), then sends it back over the internet on line (C).
6. The response from the server then comes off the internet on line (B), and your computer's network interface hands it to your browser on line (A).
7. Finally, your browser then displays the response.


# Code Logic 
 1. Create room class，instantiate each room_object，add next_path property {action: next_room_object} for each room_object
 2. Use room_name to get room_object based on globals() dictionary {room_name：room_object}（Default value is central_corridor）
 3. Use the action input by Player for trying to get next_room_object based on the room_object.next_path property {action: next_room_object}
 4. If the action is valid，then get next_room_object and go to the next room. If not, then redirect back to current room.

| Language  |  Usage |
| --- | --- |
| HTML    |  Handle the rendering and display of webpages |
| Python  |  Build the classes and functions, handle web app's circulation, test the functionalities of the game|

# More Resources
-   [Flask - web development, one drop at a time](http://flask.pocoo.org/docs/1.0/)
-   [Jinja2 - a templating engine for Python](http://jinja.pocoo.org/docs/2.9/)
-   [nosetests - nicer testing for Python](https://nose.readthedocs.io/en/latest/man.html)
