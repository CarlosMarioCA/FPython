print("Cómo preparar un Colacao")
print(" ")
print("xx Abro la nevera")
print(" ")

hay_leche = input("¿Hay leche? ")
if hay_leche == "s":
    print("Hay leche en la nevera.")
    print(" ")
elif hay_leche == "n":
    print("Kompra leche prro.")
else:
    print("Comando no válido.")

hay_colacao = input("¿Hay colacao? ")
if hay_colacao =="s":
    print("Parece que si tienes colacao.")
    print(" ")
elif hay_colacao == "n":
    print("Pailas parce.")
else:
    print("Comando no válido.")

if hay_colacao == "n" or hay_leche == "n":
    hay_colacao = "s"
    hay_leche = "s"
    print("Ve a la tienda a comprar. Luego de volver...")
    print(" ")

if hay_colacao == "s" and hay_leche == "s":
    print("Ponemos la leche en el vaso.")
    print("Ponemos el colacao en el vaso con leche.")
    print("Mezclamos.")
    print("Bebemos.")