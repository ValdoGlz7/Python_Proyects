#Uso de los bucles (Looping)
Musicians=['Kirk Hammett', 'Dave Mustaine', 'Tom Araya', 'Paul Gray', 'Dimebag Darrell', 'Joey Jordison']
print(Musicians[0], Musicians[1], Musicians[2])
print("--------------------------------")
for musician in Musicians:
    print(musician)
    print(musician.upper())
    print("\n")
print("Gracias a todos los musicos")
print("--------------------------------")
"""
    python utiliza la identacion para determinar cuando una line de codigo esta conectada a la linea de coidgo anterior,
    basicamente se utiliazn 4 espacios en blanco para obligarnos a escribir codgo ordenado y estructurado
"""
for musician in Musicians:
        print(musician)
        print(musician.upper())
        print(f"Gracias a {musician.upper()} por ser un gran musico")
#Identacion inecesaria
for musician in Musicians:
    print(musician)
    print(musician.upper())
    print(f"Gracias a {musician.upper()} por ser un gran musico")   
#Esto generara un error de identacion