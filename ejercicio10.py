listaMuestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

eliminarIndices = [0, 4, 5]

listaResultado = [valor for i, valor in enumerate(listaMuestra) if i not in eliminarIndices]

# Mostrar el resultado esperado
print("Lista original:", listaMuestra)
print("Resultado esperado:", listaResultado)
