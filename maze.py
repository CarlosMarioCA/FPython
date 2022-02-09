import os

import readchar as readchar
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
my_position = [12,12]
random_x = random.randint(0,MAP_WIDTH)
random_y = random.randint(0,MAP_HEIGHT)
map_objects = [[random_x,random_y],[random_x,random_y],[random_x,random_y],[random_x,random_y]]

while True:

    print("+" + "---" * (MAP_WIDTH) + "+")
    for coor_y in range(MAP_HEIGHT):
        char_to_draw = "   "
        print("|", end="")
        for coor_x in range(MAP_WIDTH):
            if my_position[POS_Y] == coor_y and my_position[POS_X] == coor_x:
                char_to_draw = " @ "
            for point in map_objects:
                if point[0] == coor_x and point[1] == coor_y:
                    char_to_draw = " * "


    print(char_to_draw,end="")
    print("|")

    print("+" + "---" * (MAP_WIDTH) + "+")

    # direction = input("¿Movimiento? [WASD]")
    direction = readchar.readchar().decode()

    if direction == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        break

    os.system("cls")


