#Introducir nombre completo
nombre = str(input('Introduce tu nombre completo'))
#Funciones para convertir las letras del nombre
nombre_min = nombre.lower()
nombre_may = nombre.upper()
nombre_ti = nombre.title()

#impresiones del nombre
print(nombre_min)
print(nombre_may)
print(nombre_ti[:1],nombre_may[4:])