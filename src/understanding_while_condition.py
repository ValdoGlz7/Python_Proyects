"""
    Docstring for understanding understanding_while_condition
    vamos a hacer un programa
    que describa un pin correcto
    definamos un maximo de intentos
    y el usuario tiene que ingresar el pin correcto

    si el pin es correcto mostramos un mensaje de bienvenida
    si el pin es incorrecto mostramos un mensaje de error
    si el usuario supera el maximo de intentos mostramos un mensaje de bloqueo
    mostramos un mensaje de bloqueo
    """
VALID_PIN = "2510" #Upper snake case para constantes
MAX_ATTEMPTS = 3 #Upper snake case para constantes
attempts = 0
while attempts < MAX_ATTEMPTS:
    pin = input("Please enter your Pin: ")
    if pin == VALID_PIN:
        print("Welcome, you have sucessfully logged in.")
        break
    else:
        attempts += 1
        remaining_attempts = MAX_ATTEMPTS - attempts
        if remaining_attempts > 0:
            print("Invalid pin, you have ", + remaining_attempts, " attempts left.")
        else:
            print("invalid pin. Please try again.")
else:
    print("You have exceded the number of attempts.")
