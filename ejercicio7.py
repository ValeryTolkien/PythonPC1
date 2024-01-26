n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

print("Seleccione una opción:")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta (primer número menos segundo número)")
print("3. Mostrar la multiplicación de los dos números")

opc = input("Ingrese una opción: ")

if opc == "1":
    resultado = n1 + n2
    print("La suma de", n1, "y", n2, "es:", resultado)
elif opc == "2":
    resultado = n1 - n2
    print("La resta de", n1, "menos", n2, "es:", resultado)
elif opc == "3":
    resultado = n1 * n2
    print("La multiplicación de", n1, "y", n2, "es:", resultado)
else:
    print("Opción inválida. Por favor, seleccione una opción válida (1, 2 o 3).")
