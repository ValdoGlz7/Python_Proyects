"""
Un string es de manera sencilla una serie de cadenas
    en python todo lo que se encuetre 
    dentro de comillas simples (' ') o 
    dobles (" ") sera considerado un string.

    por ejemplo:
    'esto es un string'
    "esto tambien es un string"
    'le dije a mi amigo "¡python es mi lenguaje favorito!"'
    " El lenguaje 'python' lleva el nombre de la serie Monty Python "
"""
name = "Clase de Programación"
first_name = "Oswaldo"
last_name = "González"
full_name = first_name + " " + last_name
print()
print(name)
print()
print(name.title())
print()
print("para mayusculas usamos .upper()", name.upper())
print()
print("para minusculas usamos .lower()", name.lower())
print()
#Para concatenar strings usamos el simbolo +, first_name + ''  + last name 
print(full_name)
# whitespaces
"""
    los white spaces son espacios en blanco que se encuentran
    al inicio o al final de un string.
"""
print ("\n\n Whitespaces")
print("python")
print ("\tpython") # tabulador al inicio
print("\t\t python")
print ("Lenguages:\nPython\nJavaScript\nC++") # salto de linea
#Eliminar espacios en blanco 
favorite_language = "  python  "
print ("\n\n Eliminacion de espacios en blanco")
print(favorite_language)
print(favorite_language.lstrip()) # elimina espacios a la izquierda
print(favorite_language.rstrip()) # elimina espacios a la derecha
print(favorite_language.strip())  # elimina espacios a ambos lados
#Syntax Errors con Strings
print ("\n\n Syntax Errors con Strings")
message = 'Una fortaleza de python es su comunidad activa'
print(message)
message_ =  'una fortaleza de "python" es su comunidad activa'
first_name_1 = " Oswaldo "
last_name_1 = " González"
print("\n\nf-strings")
full_name = f"{first_name_1.strip()} {last_name_1.strip()}"
print(full_name)
"""
Ejercicio:
    Imprime el nombre de un personaje famoso y una cita famosa que haya dicho"
"""
Famous_person = "Kirk Hammet"
quote = "WHERE IS RIDE THE LIGTHNING???"
full_sentence = f'{Famous_person} una vez dijo: "{quote}"'
print (full_sentence)
print(f"{Famous_person} una vez dijo: '{quote}'")
#Numbers
"""
Integers
Los enteros son numeros sin decimales, pueden ser positivos o negativos
    ejemplos:
    10
    -5
    0
    los podemos usar en operaciones matematicas como:
    suma: +
    resta: -
    multiplicacion: *
    division: /
    exponente: ^
    modulo: %
"""
Number_1 = 35
Number_2 = 15
suma = Number_1 + Number_2
resta = Number_1 - Number_2
multiplicacion = Number_1 * Number_2
division = Number_1 / Number_2
exponente = Number_1 ** 2
modulo = Number_1 % 6
print("\n\n Operaciones con enteros")
print("Sum is:", suma, type(suma))
print("Subtraction is:", resta, type(resta))
print("Product is:", multiplicacion, type(multiplicacion))
print("Division is:", division, type(division))
print("The second exponent is:", exponente, type(exponente))
print("Module: is", modulo, type (modulo))
"""
floats
Los floats son numeros con decimales, pueden ser positivos o negativos
    ejemplos:
    10.5
    -5.3
    0.0
    los podemos usar en operaciones matematicas como:
    suma: +
    resta: -
    multiplicacion: *
    division: /
    exponente: ^
    modulo: %
    python llama flaots a los numeros decimales
"""
print("\n\n Operaciones con floats")
print(1.5 +3.2)
print(4.4 + 3.5)
print(5.5 * 1.2)
print(7.5 / 2.5)
print(3.5 ** 2)
print(5.5 % 2.0)
#imprimir la edad de alguien
age = 18
name_2 = "Oswaldo"
message_2 = name_2 + " tiene " +  str(age)  + " años"
print(f"{name_2} tiene {age} años")
print(message_2)
"""
    TypeError: pasa
"""