edadCliente = int(input("Ingrese la edad del cliente: "))

if edadCliente < 4:
    precioEntrada = 0  # Gratis para menores de 4 años
elif 4 <= edadCliente <= 18:
    precioEntrada = 5  # $5 para clientes de 4 a 18 años
else:
    precioEntrada = 10  # $10 para clientes mayores de 18 años

print("El precio de la entrada es: $", precioEntrada)
