# Creando una lista
mi_lista = [1, 2, "manzana", "pera"]

# Creando una tupla
mi_tupla = (3, 4, "banana", "uva")

# Creando un conjunto
mi_conjunto = {5, 6, "naranja", "manzana"}

# Accediendo a elementos (índices comienzan desde 0)
print(mi_lista[0])  # Imprime 1
print(mi_tupla[2])  # Imprime "banana"


for elemento in mi_conjunto:
    print(elemento)

mi_lista = [10, 20, 30, 40, 50]

# Accediendo al primer elemento
print(mi_lista[0])  # Imprime 10

# Accediendo al último elemento
print(mi_lista[-1])  # Imprime 50

# Accediendo a un rango de elementos (desde el índice 1 hasta el 3, sin incluir el 3)
print(mi_lista[1:3])  # Imprime [20, 30]

# Obteniendo la longitud de la lista
print(len(mi_lista))  # Imprime 5