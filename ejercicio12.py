def obtener_tipo_mime(nombre_archivo):
    # Definir un diccionario con las extensiones y sus correspondientes tipos MIME
    extensiones_mime = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    # Obtener la extensión del archivo (última parte después del punto)
    partes_nombre = nombre_archivo.split('.')
    if len(partes_nombre) > 1:
        extension = partes_nombre[-1].lower()  # Convertir a minúsculas para comparar
        # Verificar si la extensión está en el diccionario
        if extension in extensiones_mime:
            return extensiones_mime[extension]

    # Si la extensión no está en la lista o no hay extensión, devolver el tipo por defecto
    return 'application/octet-stream'


# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener y mostrar el tipo MIME correspondiente
tipo_mime = obtener_tipo_mime(nombre_archivo)
print(f"El tipo MIME del archivo {nombre_archivo} es: {tipo_mime}")
