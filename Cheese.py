import random

serendipia = 1
numero = 0
no = 0
while numero != serendipia:
    serendipia = random.randint(1, 10000000)
    numero = random.randint(1, 10000000)
    no += 1
    print("No. {}".format(no) + " Ser. {}".format(serendipia) + " Me: {}".format(numero))

print("Cheese! {}".format(numero))

