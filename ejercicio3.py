pesoPayaso = 112    # gramos
pesoMuneca = 75     # gramos

cantidadPayasos = int(input("Ingrese la cantidad de payasos vendidos: "))
cantidadMunecas = int(input("Ingrese la cantidad de muñecas vendidas: "))

pesoTotal = (cantidadPayasos * pesoPayaso) + (cantidadMunecas * pesoMuneca)

print("El peso total del paquete es:", pesoTotal, "g")
