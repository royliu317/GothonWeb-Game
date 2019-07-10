class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.next_paths = {}

    def add_paths(self, path):                   # 完善room object的next_paths属性。即给room添加各种可能的next path（由于next path会走到哪个room，取决于用户的action，所以room_object.next_paths属性应是字典类型: {action: next_room_object} )
        self.next_paths.update(path)             # dict.update(dict2)，亦即传入的参数path必须也是字典类型

    def go(self, action):                        # 会根据用户的输入，返回next path。即通过next_paths属性的action键，返回next_room_object值
        return self.next_paths.get(action, None) # dict.get(), 返回字典中指定key的value，若值不在字典中则返回默认值


# 首先，实例化如下room，并完善每个对象的description属性（用于在html页面中中显示）：

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



# 然后，对于有next path的room，完善其字典类型paths属性（对于ending场景则无需再完善，因为它们不会再有next path）

central_corridor.add_paths({         # 字典的value并不是字符串（没有引号！），而是room类的实例化对象
    'shoot': generic_death,
    'dodge': generic_death,
    'tell a joke': laser_weapon_armory,
})


laser_weapon_armory.add_paths({
    '12': the_bridge,
    '*': generic_death               # 新的转换模式，以'*'为标记，用来在游戏引擎中实现“捕获所有操作”的功能
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


def load_room(room_name):            # 加载房间对象。即传入room_name，返回room_object(通过globals字典实现)
    """
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(room_name)  # 从globals字典中，通过键room_name，返回值room_object
                                     # global()全局变量字典会包含：{room_name: room_object}，例如：
                                     # {..., 'central_corridor': <gothonweb.planisphere.Room object at 0x0000000003492BE0>),...}
 

def name_room(room_object):          # 取得房间名称。即传入room_object，返回room_name
    """
    Same possible security problem. Can you trust room?
    What's a better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == room_object:
            return key          


##print("globals() = ", globals())
##print("globals().items = ", globals().items())



# globals() 函数会以字典类型返回当前位置的全部全局变量。
# 参数: 无; 返回值: 返回全局变量的字典。运行结果如下例：
#globals() =  { ..., 'Room': <class 'gothonweb.planisphere.Room'>, 
#'central_corridor': <gothonweb.planisphere.Room object at 0x0000000003491CC0>, 
#'laser_weapon_armory': <gothonweb.planisphere.Room object at 0x0000000003491CF8>, 
#'the_bridge': <gothonweb.planisphere.Room object at 0x0000000003491D30>, 
#'escape_pod': <gothonweb.planisphere.Room object at 0x0000000003491D68>,
#'the_end_winner': <gothonweb.planisphere.Room object at 0x0000000003491DA0>, 
#'the_end_loser': <gothonweb.planisphere.Room object at 0x0000000003491DD8>, 
#'generic_death': <gothonweb.planisphere.Room object at 0x0000000003491E10>, 
#'START': 'central_corridor', 
#'load_room': <function load_room at 0x0000000003486F28>, 
#'name_room': <function name_room at 0x0000000003496378>, ...}


#dict.items()方法 以列表返回可遍历的(键, 值) 元组数组。运行结果如下例：
#globals().items =  dict_items([..., ('Room', <class 'gothonweb.planisphere.Room'>), 
#('central_corridor', <gothonweb.planisphere.Room object at 0x0000000003491CC0>), 
#('laser_weapon_armory', <gothonweb.planisphere.Room object at 0x0000000003491CF8>), 
#('the_bridge', <gothonweb.planisphere.Room object at 0x0000000003491D30>), 
#('escape_pod', <gothonweb.planisphere.Room object at 0x0000000003491D68>), 
#('the_end_winner',<gothonweb.planisphere.Room object at 0x0000000003491DA0>), 
#('the_end_loser', <gothonweb.planisphere.Room object at 0x0000000003491DD8>), 
#('generic_death', <gothonweb.planisphere.Room object at 0x0000000003491E10>), 
#('START', 'central_corridor'), 
#('load_room', <function load_room at 0x0000000003486F28>), 
#('name_room', <function name_room at 0x0000000003496378>), ...])
