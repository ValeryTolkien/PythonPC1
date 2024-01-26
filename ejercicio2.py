costo = float(input("¿Cuánto fue su consumo en el restaurante? "))
porcentaje = float(input("¿Qué porcentaje de propina desea dejar al mesero? "))
propina = (porcentaje/100) * costo

print("Debe dejar una propia de", propina)