"""
    Las tupleas son las listas de elementos que no cambian de tamaño.
    las tuplas son listas inmutables.

    Se utilizan los () para definir una tupla o la palabra reservada touple().

    Si tenemos un rectangulo que siempre va a tener cierto tamaño podemos asegurar que su tamaño
    no va a cambiar si colocamos sus valorsa en una tupla.
"""
#Ejemplos de tuplas
dimensions = (200,50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])
print("--------------------------------------")
#dimensions[0] = 300 #DA UN ERROR #TypeError
for dimension in dimensions:
    print(dimension)
"""
    No podemos modificar una tupla directamente, lo que si podemos hacer cambiar
    la asignacion a una variable que almacena una tupla
"""
dimensions = (200,50)
print(dimensions)
dimensions = (300,20, 50)
print(dimensions)