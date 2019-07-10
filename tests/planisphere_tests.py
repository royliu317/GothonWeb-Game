from nose.tools import *
from gothonweb.planisphere import *


def test_room():            # 测试用例1 - 测试房间基本功能
    gold_room = Room("Gold Room",
                """This room has gold in it you can grab. There's a 
                door to the north.""")
    assert_equal(gold_room.name, "Gold Room")     # 测试Room的name属性
    assert_equal(gold_room.paths, {})             # 测试Room的paths属性


def test_room_paths():      # 测试用例2 - 测试到达各房间的每条路径
    center_room = Room("Center Room", "Test room in the center.")   # 创建各条路径上的房间对象
    north_room = Room("North Room", "Test room in the north.")
    south_room = Room("South Room", "Test room in the south.")

    center_room.add_paths({'north': north_room, 'south':south_room}) # 此处的paths维护 {路径：对应的房间对象} 字典

    assert_equal(center_room.go('north'), north_room)                # go()表示沿某条路径走，所能到达的房间
    assert_equal(center_room.go('south'), south_room)


def test_map():             # 测试用例3 - 测试整个地图（起点，能从起点往外走的方向，能走回起点的方向）
    start = Room("Start", "You can go west and down a hole.")       # 创建各个方向对象。虽然用Room类看上去有点难以理解，
    west = Room("Trees", "There are trees here, you can go east.")  # 但如果把Room更广义的看作“场景”，而不是单纯的“房间"，就比较好理解了。
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})                    # 此处的paths维护 {方向：对应的方向对象} 字典
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

