from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

print(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
#traversal_path = ['n', 'n']
traversal_path = []

room_list = []
visited = set()

def dft_recursive(starting_vertex): # make a path of the rooms to visit in order
    room_list.append(starting_vertex)
    if starting_vertex not in visited:
        visited.add(starting_vertex)
        for r in room_graph[starting_vertex][1].values():
            if r not in visited:
                dft_recursive(r)
                room_list.append(starting_vertex)



def convert_to_directions():
    for i in range(len(room_list) - 1): # loop through the list of rooms that are traveled in order 
        for k, val in room_graph[room_list[i]][1].items(): # look at the available exits
            if val == room_list[i + 1]: # find the direction that corresponds to the next room in the list
                traversal_path.append(k) # append that direction
            



dft_recursive(world.starting_room.id)
convert_to_directions()



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
