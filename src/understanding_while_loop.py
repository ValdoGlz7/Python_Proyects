"""
    Estructira basica del bulce while
    while conditional:
        actions
"""
#while infinito
while True:
    try:
        number = int(input("ingrese un numero entre 25 y 50:" ))
        if number >= 25 and number <= 50:
                print("Hola esta en el rango")
                break
        else:
            print("El numero no esta en el rango, intente de nuevo")
    except ValueError:
        print("Entrada invalida, por favor ingrese un numero entero.")
    except KeyboardInterrupt:
        print("\n El programa ha sido interrumpido por el usuario")
        break
#While con centinela
"""
    prompt = "Ingrese un numero para elevarlo al cuadrado"
"""
print("\n Captura de importe. bienvenidos a la calculadora de impuestos")
print("Para salir en cualquier momento ingrese 'exit'")
counter = 0
sum = 0.0
maximum = None
minimum = None
while True:
    user_input = input("Ingresa una cantidad (MXN): ")
    if user_input == "exit":
        break
    try:
        quantity = float(user_input)
    except:
        print("Ingrse un valor valido")
        continue
    counter += 1 #counte = counter + 1 (contador)
    sum+=quantity #sum = sum + quantity (acumulador)
    if minimum is None  or quantity or quantity < minimum:
        minimum = quantity
    if maximum is None  or quantity or quantity > maximum:
        maximum = quantity
    #Ahora a imprimir los resultados, valor total, numero de entradas, y valor maximo y minimo
print("\nResultados finales:")
print("Cantidad total ingresada: $", sum, " MXN")
print("Número de entradas: ", counter)
print("Valor máximo ingresado: $", maximum, " MXN")
print("Valor mínimo ingresado: $", minimum, " MXN")