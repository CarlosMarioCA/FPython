lista = [ 2, 3, 4, 5, 6, 2, 10]
mayor = 1
minor = 1

for n in lista:
    if n>mayor:
        mayor = n
    if n<minor:
        minor = n

print("Mayor: {}  Minor: {}".format(mayor,minor))