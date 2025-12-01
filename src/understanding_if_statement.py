cars = ["audi", "bmw", "volvo", "tesla", "toyota"]
for car in cars:
    if car == "bmw" or car == "tesla":
        print(car.upper())
    else:
        print (car.lower())
#El condicional es el corazon de un if
#Ejemplos de condicionales
#Condicional "true"
print("--------------------------")
car_1 = "bmw"
print("condicional ture= ", car_1 == "bmw")
#Condicional false
print("--------------------------")
car_2 = "Audi"
print("condicioanal false= ",  car_2 == "audi")
car_3 = "Audi"
print(car_3.lower() == "audi")
#Condicional != para determinar descigualdad
print("--------------------------")
requested_topping = "anchovies"
if requested_topping == "anchovies":
    print("Hold the anchovies")
#comparaciones numericas
age = 18
print (age == 18) #"True"
answer = 17
if answer != 42: #"True"
    print("Esta no es la respuesta correcta,  intente de nuevo")
age = 19
print(age < 21) #True
print(age<=21) #True
print(age>21) #False
print(age >= 21) #False
#Condicionales multiples
print("--------------------------")
age_0 = 22
age_1 = 18
print (age_0 >= 21 and age_1 > 21) #False
print (age_0 >= 21 and age_1 >= 18) #True
#operacion logica r
print (age_0 >= 21 or age_1 > 21) #True
print (age_0 >= 23 or age_1 >= 26) #False
#Preguntame si un valor esta en una lista
cars = ["micro", "vocho", "tsuru", "subaru"]
print("vocho" in  cars)
print("koeniggseg" in cars)
#prefuntae si un valor no esta en alumnos
alumnos = ["victor", "ana", "maiki", "gera"]
user = "josue"
print(user not in alumnos)
print ("maiki" not in alumnos)
"""Nuevo built in method:
input_msj = input("Ingrese su valor:")
"""
"""
Programa para pedir la edad a un usuario que diga si el usuario es mayor o menor de edad
"""
print("--------------------------")
try:
    age = int(input("Please enter your age: "))
    if age >= 18 and age <= 100 :
        print("You are an adult.")
    elif age < 18 and age > 0 :
        print("You are a minor.")
    elif age > 101 :
        print("How are you alive")
    else:
        print("Are you dumb?")
except ValueError as err:
    print(err)
    print("Letters are not allowed")
"""
    Ejercicio:
        Elabore un programa que contemple lo siguiente
        -Si la edad es menor a 4 años, la entrada es gratuita
        -Si la edad esta dentro de 4 y 18 (inclusivo) la entrada es de $200
        -Costo para alguien mayor de 18 $500
"""
print("--------------------------")
try:
    age_person = int(input("Please enter your age: "))
    if age_person < 4 and age_person >= 0:
        print("Your ticket is free")
    elif age_person >= 4 and age_person <= 18:
        print("Your ticket is $200")
    elif age_person > 18:
        print("Your ticket is $500")
    else:
        print("Not possible")
except ValueError as err:
    print(err)
    print("Letters are not allowed")
#multiple if-elif-else blocks
#else en ocasiones se puede omitir (depende de la situacion)
#como se va ejecutando el if-elif-else

##Multiple conditions
print("--------------------------")
guisos = ["deshebrada", "salsa verde", "picadillo"]
if "deshebrada" in guisos:
    print("hay deshebrada".upper())
if "salsa verde" in guisos:
    print("hay salsa verde".swapcase())
if "picadillo" in guisos:
    print("hay picadillo".swapcase())
print("--------------------------")
guisos  = []
if guisos:
    print ("Hay guisos")
else:
    print("No hay guisos")
print("--------------------------")
guisos_disponibles = ["deshebrada", "barbacoa", "salsa verde", "picadillo"]
guisos_a_ordenar = ["deshebrada", "salsa verde", "picadillo", "chicharron"]
for guiso in guisos_a_ordenar:
    if guiso in guisos_disponibles:
        print(f"Agregando {guiso} a su orden")
    else:
        print(f"Lo siento, no tenemos {guiso} disponible")