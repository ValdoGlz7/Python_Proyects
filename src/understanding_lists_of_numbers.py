"""
    Las listas tambien pueden almacenar nymeros y de hecho son indeakes para eso.
    Python ofrece muchas herramientas que ayudan a trabajar de manera eficiente las listas
    de numeros.
"""
#Metodo range() nos ayuda a generar facilmente series de numeros
print("imprime los numeros del 1 al 4")
for number in range(1, 5):
    print(number)
print("--------------------------------")
print("Imprime los numeros pares del 0 al 10")
for number in range(0, 11, 2):
    print(number)
print("--------------------------------")
print("Imprime la tabla del 7")
for number in range (7, 71, 7):
    print(number)
print("--------------------------------")
print("generar una lista de los cuadrados de los primeros 10 numeros")
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
print("--------------------------------")
#Otros metodos built in
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Minimo:", min(digits)) #Salida 1
print("Maximo:", max(digits)) #Salida 10
print("Suma:", sum(digits)) #alida 55