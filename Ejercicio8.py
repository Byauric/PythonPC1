#Ejercicio 8 
"""Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar"""

hora_usuario = input("Ingrese la hora en formato de 24 horas (HH:MM): ")
hours, minutes = hora_usuario.split(":")
hours = int(hours)
minutes = int(minutes)

if 7 <= hours < 8 and 0 <= minutes <= 59:
    print("Es hora de desayunar.")
elif hours == 8 and minutes == 0:
    print("Es hora de desayunar.")
elif 12 <= hours < 13 and 0 <= minutes <= 59:
    print("Es hora de almorzar.")
elif hours == 13 and minutes == 0:
    print("Es hora de almorzar.")
elif 18 <= hours <= 19 and 0 <= minutes <= 59:
    print("Es hora de cenar.")
elif hours == 19 and minutes == 0:
    print("Es hora de cenar.")


