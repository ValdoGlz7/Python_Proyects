"""
    Docstring for understanding understanding_while_centinel
    centinel is useful when you want to ensure that a loop
    runs at least once before checking a condition
    Vamos a realizar un ejemplo que realice la suma de n numeros ingresados
    por el usuario, no sabemos cuantos numeros se han ingresado,
    mostrar la suma, el minimo y el maxiomo de los numeros ingresados
"""
counter = 0
sum_addition = 0.0
minimum = None
maximum = None
while True:
    number = input("Enter a number (or 'done' to finish): ")
    if number.lower() == 'done':
        break
    try:
        number = float(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        break
    counter += 1
    sum_addition += number
    if minimum is None or number < minimum:
        minimum = number
    if maximum is None or number > maximum:
        maximum = number

if counter > 0:
    print(f"Sum: {sum_addition}")
    print(f"Count: {counter}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
else:
    print("No numbers were entered.")