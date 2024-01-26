horaIngresada = input("Ingrese la hora en formato HH:MM: ")

try:
    horas, minutos = map(int, horaIngresada.split(":"))
except ValueError:
    print("Formato de hora incorrecto. Ingrese la hora en formato HH:MM.")
    exit()

if 7 <= horas < 8:
    print("¡Es la hora del desayuno!")
elif 12 <= horas < 13:
    print("¡Es la hora del almuerzo!")
elif 18 <= horas < 19:
    print("¡Es la hora de la cena!")
else:
    pass
