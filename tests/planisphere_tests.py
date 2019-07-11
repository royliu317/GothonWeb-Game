from nose.tools import *
from gothonweb.planisphere import *


def test_room():                                                    # Test Case 1 - Test basic function of the room
    gold_room = Room("Gold Room",
                """This room has gold in it you can grab. There's a 
                door to the north.""")
    assert_equal(gold_room.name, "Gold Room")                       # Test name property of the room
    assert_equal(gold_room.paths, {})                               # Test paths property of the room


def test_room_paths():                                              # Test Case 2 - Test paths to each room
    center_room = Room("Center Room", "Test room in the center.")   # Create paths to each room object
    north_room = Room("North Room", "Test room in the north.")
    south_room = Room("South Room", "Test room in the south.")

    center_room.add_paths({'north': north_room, 'south':south_room}) 

    assert_equal(center_room.go('north'), north_room)                
    assert_equal(center_room.go('south'), south_room)


def test_map():                                                     # Test Case 3 - Test the whole map
    start = Room("Start", "You can go west and down a hole.")       # Create each direction object. Although we use Room class for it seems a bit wired,
    west = Room("Trees", "There are trees here, you can go east.")  # but if we see room as "scene" rather than a room, it is easier to understand.
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})                    
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)


def test_gothon_game_map():
    start_room = load_room(START)
    assert_equal(start_room.go('shoot!'), generic_death)
    assert_equal(start_room.go('dodge!'), generic_death)
    assert_equal(start_room.go('*'), generic_death)

    room1 = start_room.go('tell a joke')
    assert_equal(room1, laser_weapon_armory)
    assert_equal(room1.go('*'), generic_death)

    room2 = room1.go('0132')
    assert_equal(room2, the_bridge)
    assert_equal(room2.go('throw the bomb'), generic_death)
    assert_equal(room1.go('*'), generic_death)
    
    room3 = room2. go('slowly place the bomb')
    assert_equal(room3, escape_pod)
    assert_equal(room3.go('2'), the_end_winner)
    assert_equal(room3.go('*'), the_end_loser)

