import random

number = random.randint(1, 10)
print(" ")
numeroUsuario = int(input("¿Cuál es su número? "))

if number == numeroUsuario:
    print(" ")
    print("Felicitaciones, has adivinado el número.")
elif numeroUsuario > 10:
    print("Te pasaste, debe ser un número entre 1 y 10.")
elif numeroUsuario <= 0:
    print("No alcanza, debe ser un número entre 1 y 10.")
else:
    print(" ")
    print("Pailas, el número ganador es {}".format(number))