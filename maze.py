import os

import readchar as readchar
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
my_position = [12, 12]
random.randint(1, MAP_WIDTH-1)
random.randint(1, MAP_HEIGHT-1)
map_objects = []
init = True
active_star = 5
colission = False

def create_star(num):
    for m in range (0,num):
        map_objects.append([random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)])

    while True:
        for coor in map_objects:
            count = 0

            for comp in map_objects:
                if coor[POS_X] == comp[POS_X] and coor[POS_Y] == comp[POS_Y]:
                    count += 1
                else:
                    pass

            if count == 1:
                pass

            elif count > 1:
                coor = [[random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]]

        break

create_star(active_star)

while True:

    char_to_draw = " "
    if colission == False:
        pass
    elif colission ==True:
        colission = False
        create_star(active_star)

    print("+" + "---" * (MAP_WIDTH) + "+")
    for coor_y in range(MAP_HEIGHT):
        print("|", end="")
        char_to_draw = " "
        for coor_x in range(MAP_WIDTH):
            char_to_draw = " "

            if my_position[POS_Y] == coor_y and my_position[POS_X] == coor_x:
                char_to_draw = "@"

            for point in map_objects:
                if point[POS_X] == coor_x and point[POS_Y] == coor_y:
                    char_to_draw = "*"

                if my_position[POS_X] == point[POS_X] and my_position[POS_Y] == point[POS_Y]:

                    map_objects = []
                    colission = True
                    active_star -= 1

            print(" {} ".format(char_to_draw), end="")
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

    if active_star == 0:
        print("GAME OVER")
        break


