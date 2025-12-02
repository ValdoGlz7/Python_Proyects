#Lists
"""
    las listas  nos permiten almacenar informacion en un lugar
    la cantidad que tenfas: ya sea pocos o muchos elementos
    en python los corchetes[] indican o definen una lista
    los elementos dentro de una lista pueden se separados por comas ,
    Ejemplo:
"""
bicycles = ['trek', 'cannondale', 'redline', 'giant']
print(bicycles, type(bicycles))
#Agregar elementos en una posicion especifica
print(bicycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print("Lista de motocicletas", motorcycles)
motorcycles.insert(0, 'ducati')
print("Lista de motocicletas", motorcycles)
motorcycles.insert(3, 'bmw')
print("Lista de motocicletas", motorcycles)
print(motorcycles[2])
#Eliminando elementos de las listas usando (del)
print("--------------------------------")
del motorcycles[0]
print("Lista de motocicletas", motorcycles)
#Eliminando elementos de las listas usando (pop)
print ("Lista original de motocicletas", motorcycles)
popped_motorcycle = motorcycles.pop()
print("Lista de motocicletas despues de usar pop", motorcycles)
print("Motocicleta eliminada", popped_motorcycle)
#usar pop para eliminar un elemento en una posicion especifica
lista_original_de_las_motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati', 'bmw']
print("Lista original de motocicletas", lista_original_de_las_motocicletas)
motocicleta_eliminada = lista_original_de_las_motocicletas.pop(2) #Eliminando el objeto 2
print("Lista de motocicletas despues de usar pop en una posicion especifica", lista_original_de_las_motocicletas)
#Eliminar por valor elementos de una lista
print("--------------------------------")
print("Lista original de motocicletas", lista_original_de_las_motocicletas)
lista_original_de_las_motocicletas.remove('ducati')
print("Lista de motocicletas despues de eliminar por valor 'ducati'", lista_original_de_las_motocicletas)
#Ordenar listas
"""
    permanente: metodo .sort()
    temporal: funcion sorted()
"""
cars = ['bmw', 'kia', 'toyota', 'ford']
print("Lista original de carros", cars)
cars.sort()
print("Lista de carros ordenada permanentemente", cars)
cars.sort(reverse=True)
print("Lista de carros ordenada permanentemente en orden inverso", cars)
print("--------------------------------")
print (len(cars))  #len() nos permite conocer la cantidad de elementos en una lista
#Reverse el orden de una lista
print("--------------------------------")
Lists_favorite_bands = ['Metallica', 'Megadeth', 'Slayer', 'Anthrax', 'Queens of the Stone Age', 'Pantera']
Lists_favorite_bands.reverse()
print(Lists_favorite_bands)