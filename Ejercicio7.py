#Ejercicio 7
"""Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta."""

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
print("\nSelecciona una opción:")
print("1. Mostrar suma")
print("2. Mostrar resta (el primero menos el segundo)")
print("3. Mostrar multiplicación")

opcion = input("Ingresa el número de la opción deseada (1/2/3): ")
if opcion == '1':
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}")
elif opcion == '2':
    resultado = num1 - num2
    print(f"La resta de {num1} y {num2} es: {resultado}")
elif opcion == '3':
    resultado = num1 * num2
    print(f"La multiplicación de {num1} y {num2} es: {resultado}")
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")




