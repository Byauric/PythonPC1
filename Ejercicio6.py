# Problema 6:
edad = int(input("Ingrese la edad del cliente: "))
if edad < 4:
    precio_entrada = 0  
elif 4 <= edad <= 18:
    precio_entrada = 5 
else:
    precio_entrada = 10 
# Mostrar el precio de la entrada
print("El precio de la entrada es: S/{}".format(precio_entrada))
