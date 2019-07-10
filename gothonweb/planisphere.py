class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.next_paths = {}

    def add_paths(self, path):                   # Set next_paths property for room object, which is to add all possible next path for the room（Since next path is dependant on Player's action，so the property of room_object.next_paths should be dictionary type: {action: next_room_object} )
        self.next_paths.update(path)             # dict.update(dict2)，which also means the path must be dictionary type

    def go(self, action):                        # Return next path based on Player's input (get the value of next_room_object from the key of action in next_paths property)
        return self.next_paths.get(action, None) # dict.get(), return specific value of the key from dictionary. It will return default value if not found out.


# First, instantiate the room and perfect the description property of each object（used to show in html page）：

central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.
You are the last surviving member and your last mission is to get the neutron destruct bomo from the Weapons Armory,
put it in the bridge, and blow the ship up afer getting into an escape pod.

You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, 
and evil clown costume flowing around his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you.

So what will you do now, shoot, dodge or tell a joke???
""")


laser_weapon_armory = Room("Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know:
asdf  lasdfjlasfj l;ajsdfl jas;fljasfljs fljasdf asdfasdf.
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head putting him down, then jump though the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding.
It's dead quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb in its container.
There's a keypad lock on the box and you need the code to get the bomb out.
If you get the code wrong 3 times then the lock closes forever and you can't get the bomb.
The code is 2 digits.
""")


the_bridge = Room("The Bridge",
"""
The container clicks open and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot.

You burst onto the Bridge with the netron destruct bomo under your arm and surprise 5 Gothons who are trying to take control of the ship.
Each of them has an even uglier clown costume than the last. 
They have't pulled their weapons out yet, as they see the active bomb under your arm and don't want to set it off.

So what will you do now, throw the bomb or slowly place the bomb?
""")


escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm and the Gothons put their hands up and star to sweat.
You in ch backward to the door, open it, and then carefully place the bomb on the floor, pointint your blaster at it.
You then jump back through the door, punch the close button and blast the lock so the Gothons can't get out.
Now that the bomb is placed you run to the escape pod to get off this tin can.

You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes.
It seems like hardly any Gothons are on the ship, so your run is clear of interference.
You get to the chamber with the escape pods, and now need to pick one to take.
Some of them could be damaged but you don't have time to look.
There's 2 pods, which one do you take?             
""")


the_end_winner = Room("The End", 
"""
You jump into pod 2 and hit the eject button.
The pod easily slides out into space heading to the planet below.
As it flies to the planet, you look back and see your ship implode then explode like a bright star, taking out the Gothon ship at the same time.
You won!
""")


the_end_loser = Room("The End",
"""
You jump into a random pod and hit the eject button.
The pod escapes out into the void of space, then implodes as the hull ruptures, crushing your body into jam jelly.
""")


generic_death = Room("death", "You died.")



# Second，perfect paths property for the room which has next path

central_corridor.add_paths({         # the value of dictionary is not string type but the instantiation of room class
    'shoot': generic_death,
    'dodge': generic_death,
    'tell a joke': laser_weapon_armory,
})


laser_weapon_armory.add_paths({
    '12': the_bridge,
    '*': generic_death               # new transform mode which marked as '*' . It is used to "capture all actions" in the game engine.
})


the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod,
})


escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser   
})



START = 'central_corridor'


def load_room(room_name):            # Load room object
    """
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(room_name)  # Use roon_name key to return room_object value in globals dictionary
                                     # global() dictionary includes：{room_name: room_object}，such as：
                                     # {..., 'central_corridor': <gothonweb.planisphere.Room object at 0x0000000003492BE0>),...}
 

def name_room(room_object):          # Get room name
    """
    Same possible security problem. Can you trust room?
    What's a better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == room_object:
            return key          


##print("globals() = ", globals())
##print("globals().items = ", globals().items())

