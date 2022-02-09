print("BIENVENIDO AL SISTEMA DE COMPRA AUTOSERVICIO.")
print(" ")

carrito = []
inventario = ["Papas","Melocotón","Leche","Nutella","Pan","Pescado"]
i = 0

while(i < len(inventario)):
    peticion = input("¿Desea comprar {}? Y - Comprar / N - No Comprar / Q - Salir. ".format(inventario[i]))
    print(" ")

    if peticion == "Y":
        carrito.append(inventario[i])

    elif peticion == "N":
        pass

    elif peticion == "Q":
        print("Saliendo...")
        print(" ")
        break
    else:
        print("No se digito un comando válido")
        print(" ")
        i-=1

    i+=1

if len(carrito)>=1:
        print("Se compró lo siguiente: {}".format(carrito))
        print("Gracias por su compra.")
else:
    print("Vuelva pronto.")





