import random
import os

INI_QUILAVA = 35
vida_quilava = INI_QUILAVA
ataque_quilava = 10

INI_DWG = 40
vida_dwg = INI_DWG
ataque_dwg = 9

ronda = 0

print("Comienza el combate")
print(" ")

while vida_quilava > 0 and vida_dwg > 0:

    ronda += 1
    turno = random.randint(1,2)
    print("Ronda {}".format(ronda))

    if turno == 1:
        print("Quilava ataca.")
        vida_dwg -= ataque_quilava
        print("QUILAVA [" + "/"*vida_quilava + "-"*(INI_QUILAVA-vida_quilava) + "]" +
              " - {}/{}".format(vida_quilava, INI_QUILAVA))
        print("DEWGONG [" + "/"*vida_dwg + "-"*(INI_DWG-vida_dwg) + "]" +
              " - {}/{}".format(vida_dwg, INI_DWG))
        print(" ")


    elif turno == 2:
        print("Dewgong  ataca.")
        vida_quilava -= ataque_dwg
        print("Quilava [" + "/"*vida_quilava + "-"*(INI_QUILAVA -vida_quilava) + "]" +
              " - {}/{}".format(vida_quilava, INI_QUILAVA ))
        print("Dewgong [" + "/"*vida_dwg + "-"*(INI_DWG-vida_dwg) + "]" +
              " - {}/{}".format(vida_dwg, INI_DWG))
        print(" ")


if vida_quilava <= 0:
    print("Gano Dewgong.")

elif vida_dwg <= 0:
    print("Gano Quilava.")