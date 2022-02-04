print("Para ver si tienes un descuento en el zoo.")

print(" ")
edad = int(input("¿Que edad tienes? "))
tipo = input("¿Que tipo de carnet tienes? e) Estudiante p) Pensionado f) Familia numerosa n) Nada -> ")

if (25 <= edad <= 35) and (tipo == "e") or \
        edad < 10 \
        or ((edad >= 65) and (tipo == "p")) or \
        (tipo == "f"):
    print(" ")
    print("Eres apto para descuento.")

elif tipo == "n":
    print(" ")
    print("Compra Confama prro.")
else:
    print("No eres apto para descuento.")
