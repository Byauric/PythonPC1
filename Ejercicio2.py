# Problema 2: 
costo_comida = float(input("Ingrese el monto de su consumo: S/"))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar (debe ser mayor a 15%): "))
propina = costo_comida * (porcentaje_propina / 100)
print("La cantidad de propina a dejar es: S/{:.1f}".format(propina))
