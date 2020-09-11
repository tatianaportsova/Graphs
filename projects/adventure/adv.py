# python3 projects/adventure/adv.py -v

from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = []

opposite_directions = {"n": "s",
                       "s": "n",
                       "w": "e",
                       "e": "w"}

# Check if the room was visited
def room_was_visited(room, visited):
    return visited.get(room.id, False)

def get_path(player, visited=None):
    # Instantiate a dictionary to store rooms' id and if they were visited
    if visited is None:
        visited = {}
    # Store current room's id and mark it as visited
    visited[player.current_room.id] = True

    path = []
    # Get exits from the current room
    exits = player.current_room.get_exits()
    # For each exit in the room
    for direction in exits:
        # Get the next room in that direction
        next_room = player.current_room.get_room_in_direction(direction)
        # If that room was not visited before:
        if next_room and not room_was_visited(next_room, visited):
            # Move to the room in that direction
            player.travel(direction)
            # Store the direction to that room to 'path'
            path.append(direction)
            # Recurse and get the paths to all the other rooms
            next_room_path = get_path(player, visited)
            # Extend the 'path' with all of those directions
            path.extend(next_room_path)
            # Then travel back
            player.travel(opposite_directions[direction])
            # Append that direction to the path
            path.append(opposite_directions[direction])
    
    return path


traversal_path = get_path(player)
# print(traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
