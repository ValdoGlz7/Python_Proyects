"""
    Un list comprehension combina el for loop y la creacion de nuevos
    elementos en una sola linea y automaticamente agrega cada nuevo elemento
    a la lista sin tener que utilizar el modo append.
"""
#Generar una lista de los cuadrados de los primeros 10 numeros
squares = [value ** 2 for value in range(1, 11)]
print(squares)
#Generar una liata con los numeros pares
evens = [value for value in range(101) if value % 2 == 0]
print(evens)
#Generar una liata con los numeros impares
odds = [value for value in range(101) if value % 2 != 0]
print(odds)