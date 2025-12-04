# Name: [Tu Nombre Completo]
# Student ID: [Tu Matrícula]
# Group: [Tu Grupo]

# --------------------------------------------------
# RESUMEN EJECUTIVO
# --------------------------------------------------

# Executive Summary:
# A **for loop** is typically used for **definite iteration**—when the number of repetitions is known
# beforehand, such as iterating over a fixed range using range() or traversing a list. A **while loop**
# is used for **indefinite iteration**, where the loop continues as long as a certain condition remains
# true (e.g., waiting for user input or checking a password). A **counter** is a variable initialized
# outside the loop and incremented inside to track the number of iterations or valid items processed.
# An **accumulator** (or total) is a variable used to sum up values across iterations. It is crucial
# to design a clear **exit condition** for while loops and ensure the control variable is updated within
# the loop to prevent **infinite loops**. This document covers six problems demonstrating these concepts,
# including range summation, table generation (for), calculating averages with a sentinel, password
# attempts, and menu systems (while), and nested loops for pattern printing.

# --------------------------------------------------
# PRINCIPIOS Y BUENAS PRÁCTICAS
# --------------------------------------------------

# - Use **for** when the number of iterations is known (e.g., iterating N times or over all elements of a collection).
# - Use **while** when the loop termination depends on a condition that changes during execution (e.g., user input, external flag).
# - Always **initialize counters and accumulators** to 0 (or a starting value) before entering the loop.
# - **Update control variables** inside a while loop to ensure the exit condition is eventually met, thus avoiding infinite loops.
# - Keep the loop body simple and focused; if the logic inside becomes too complex, consider extracting it into a separate function.
# - Use clear variable names and ensure all input validation happens before processing.

# --------------------------------------------------
# PROBLEMAS
# --------------------------------------------------

# --- CONVENTION NOTES ---
# Variables: lower_snake_case
# Constants: UPPER_SNAKE_CASE
# Control Structures: for, while, counters, accumulators
# Output Messages: English

# --------------------------------------------------
# Problem 1: Sum of range with for
# --------------------------------------------------

# Problem 1: Sum of Range with For
# Description: Calculates the total sum and the sum of only even integers from 1 up to a given limit 'n'
# using a 'for' loop and accumulators.
#
# Inputs:
# - n_input (string; limit of the range).
#
# Outputs:
# - "Sum 1..n:" <total_sum>
# - "Even sum 1..n:" <even_sum>
# - "Error: invalid input"
#
# Validations:
# - n_input must be convertible to an integer.
# - n must be >= 1.
#
# Test cases:
# 1) Normal: n=4 -> Sum 1..4: 10 (1+2+3+4), Even sum: 6 (2+4)
# 2) Border: n=1 -> Sum 1..1: 1, Even sum: 0
# 3) Error: n="zero" -> Error: invalid input

def calculate_range_sums(n_input):
    """Calculates the total sum and even sum from 1 to n using a for loop."""
    try:
        n = int(n_input)
    except ValueError:
        print("Error: invalid input")
        return

    # 1. Validation
    if n < 1:
        print("Error: invalid input")
        return

    # 2. Initialization of Accumulators
    total_sum = 0
    even_sum = 0

    # 3. For Loop (definite iteration using range)
    for i in range(1, n + 1):
        total_sum += i # Accumulator for total sum
        if i % 2 == 0:
            even_sum += i # Accumulator for even sum

    # 4. Output
    print(f"Sum 1..n: {total_sum}")
    print(f"Even sum 1..n: {even_sum}")


print("\n--- Problem 1 Test Runs ---")
calculate_range_sums("4") # Normal
calculate_range_sums("1") # Border
calculate_range_sums("0") # Error: < 1
calculate_range_sums("five") # Error: Invalid type

# --------------------------------------------------
# Problem 2: Multiplication table with for
# --------------------------------------------------

# Problem 2: Multiplication Table with For
# Description: Generates and prints the multiplication table for a 'base' number up to a limit 'm'
# using a 'for' loop.
#
# Inputs:
# - base_input (string; number to multiply).
# - m_input (string; limit of the table).
#
# Outputs:
# - Line by line: "base x i = result"
# - "Error: invalid input"
#
# Validations:
# - base and m must be convertible to integers.
# - m must be >= 1.
#
# Test cases:
# 1) Normal: base=5, m=4 -> 5x1=5, 5x2=10, 5x3=15, 5x4=20
# 2) Border: base=10, m=1 -> 10 x 1 = 10
# 3) Error: base=5, m="0" -> Error: invalid input

def generate_multiplication_table(base_input, m_input):
    """Generates a multiplication table using a for loop and range."""
    try:
        base = int(base_input)
        m = int(m_input)
    except ValueError:
        print("Error: invalid input")
        return

    # 1. Validation
    if m < 1:
        print("Error: invalid input")
        return

    print(f"Multiplication table for {base} up to {m}:")

    # 2. For Loop (definite iteration using range)
    for i in range(1, m + 1):
        result = base * i
        print(f"{base} x {i} = {result}")

    print("---")


print("\n--- Problem 2 Test Runs ---")
generate_multiplication_table("5", "4") # Normal
generate_multiplication_table("10", "1") # Border
generate_multiplication_table("5", "0") # Error: m < 1

# --------------------------------------------------
# Problem 3: Average of numbers with while and sentinel
# --------------------------------------------------

# Problem 3: Average of Numbers with While and Sentinel
# Description: Reads numbers continuously using a 'while' loop until a SENTINEL_VALUE is entered.
# Calculates the count and average of the valid numbers entered.
#
# Inputs:
# - number_input (string; read repeatedly).
# - SENTINEL_VALUE (Constant: -1).
#
# Outputs:
# - "Count:" <count>
# - "Average:" <average_value>
# - "Error: no data"
#
# Validations:
# - Input must be convertible to float.
# - Check for the SENTINEL_VALUE.
# - Handle the case where no valid numbers (count = 0) are entered.
#
# Test cases:
# 1) Normal: 10, 20, 30, -1 -> Count: 3, Average: 20.0
# 2) Border: 50, -1 -> Count: 1, Average: 50.0
# 3) Error: -1 -> Error: no data

SENTINEL_VALUE = -1.0

def calculate_average_with_sentinel():
    """Reads numbers until a sentinel value is input and calculates the average."""
    total_sum = 0.0 # Accumulator
    count = 0 # Counter

    print(f"Enter numbers (enter {int(SENTINEL_VALUE)} to stop):")

    while True:
        number_input = input("> ").strip()

        # 1. Validation: Convert to Float
        try:
            current_number = float(number_input)
        except ValueError:
            print("Error: invalid input (not a number)")
            continue

        # 2. Check for Sentinel (Exit Condition)
        if current_number == SENTINEL_VALUE:
            break

        # 3. Update Accumulator and Counter
        total_sum += current_number
        count += 1

    # 4. Final Calculation and Output
    if count == 0:
        print("Error: no data")
    else:
        average = total_sum / count
        print(f"Count: {count}")
        print(f"Average: {round(average, 2)}")

# --- Test execution for Problem 3 (requires interactive input) ---
print("\n--- Problem 3 Test Runs ---")
print("1) Normal: Enter 10, 20, 30, then -1")
# calculate_average_with_sentinel() # Uncomment to run interactively
print("\n2) Border: Enter 50, then -1")
# calculate_average_with_sentinel() # Uncomment to run interactively
print("\n3) Error: Enter -1 immediately")
# calculate_average_with_sentinel() # Uncomment to run interactively
print("--- End of interactive tests for Problem 3 ---")

# --------------------------------------------------
# Problem 4: Password attempts with while
# --------------------------------------------------

# Problem 4: Password Attempts with While
# Description: Implements a simple password entry system that allows a maximum number of
# attempts (MAX_ATTEMPTS) before locking the account. Uses a 'while' loop and a counter.
#
# Inputs:
# - user_password (string; read repeatedly).
#
# Outputs:
# - "Login success"
# - "Account locked"
#
# Validations:
# - MAX_ATTEMPTS must be set as a positive constant.
# - Comparison of input string to the CORRECT_PASSWORD constant.
#
# Test cases:
# 1) Normal: Input correct password on 1st attempt. -> Login success
# 2) Border: Fail 2 times, succeed on 3rd attempt (MAX_ATTEMPTS=3). -> Login success
# 3) Error: Fail 3 times (MAX_ATTEMPTS=3). -> Account locked

CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3

def handle_password_attempts():
    """Manages password attempts using a while loop and fixed limit."""
    attempts = 0 # Counter
    is_logged_in = False

    # While loop runs as long as the max attempts limit hasn't been reached
    while attempts < MAX_ATTEMPTS:
        user_password = input(f"Enter password (Attempt {attempts + 1}/{MAX_ATTEMPTS}): ").strip()

        if user_password == CORRECT_PASSWORD:
            is_logged_in = True
            break # Exit loop immediately on success
        else:
            attempts += 1
            print("Error: incorrect password")

    # Final Output based on loop result
    if is_logged_in:
        print("Login success")
    else:
        print("Account locked")

# --- Test execution for Problem 4 (requires interactive input) ---
print("\n--- Problem 4 Test Runs ---")
print("1) Normal: Enter 'admin123'")
# handle_password_attempts() # Uncomment to run interactively
print("\n2) Border: Enter 'fail1', 'fail2', then 'admin123'")
# handle_password_attempts() # Uncomment to run interactively
print("\n3) Error: Enter 'fail1', 'fail2', 'fail3'")
# handle_password_attempts() # Uncomment to run interactively
print("--- End of interactive tests for Problem 4 ---")

# --------------------------------------------------
# Problem 5: Simple menu with while
# --------------------------------------------------

# Problem 5: Simple Menu with While
# Description: Implements a text-based menu that repeats using a 'while' loop until the user
# selects the 'Exit' option (0). Manages an internal counter.
#
# Inputs:
# - option_input (string/int; user's choice).
#
# Outputs:
# - "Hello!" (Option 1)
# - "Counter:" <counter_value> (Option 2)
# - "Counter incremented" (Option 3)
# - "Bye!" (Option 0)
# - "Error: invalid option"
#
# Validations:
# - Input must be convertible to an integer.
# - Option must be 0, 1, 2, or 3.
#
# Test cases:
# 1) Normal: 3, 3, 2, 1, 0 -> Counter: 2, Hello!, Bye!
# 2) Border: 0 immediately. -> Bye!
# 3) Error: 99, 1. -> Error, Hello!, Bye!

def run_simple_menu():
    """Presents a menu loop using while until the exit option (0) is selected."""
    counter_value = 0
    option = -1 # Sentinel to start the loop

    while option != 0:
        print("\n--- Menu ---")
        print("1) Show greeting")
        print("2) Show current counter value")
        print("3) Increment counter")
        print("0) Exit")

        option_input = input("Enter option: ").strip()

        # 1. Validation: Convert to Integer
        try:
            option = int(option_input)
        except ValueError:
            print("Error: invalid option (must be a number)")
            continue

        # 2. Handle Options (if/elif structure)
        if option == 1:
            print("Hello!")
        elif option == 2:
            print(f"Counter: {counter_value}")
        elif option == 3:
            counter_value += 1 # Counter update
            print("Counter incremented")
        elif option == 0:
            print("Bye!") # Exit message
        else:
            print("Error: invalid option (must be 0-3)")

# --- Test execution for Problem 5 (requires interactive input) ---
print("\n--- Problem 5 Test Runs ---")
print("1) Normal: Enter 3, 3, 2, 1, 0")
# run_simple_menu() # Uncomment to run interactively
print("--- End of interactive tests for Problem 5 ---")

# --------------------------------------------------
# Problem 6: Pattern printing with nested loops
# --------------------------------------------------

# Problem 6: Pattern Printing with Nested Loops
# Description: Uses nested 'for' loops to print a right-angled triangle pattern of asterisks
# based on a given number of rows 'n'.
#
# Inputs:
# - n_input (string; number of rows).
#
# Outputs:
# - Triangle pattern printed line by line.
# - "Error: invalid input"
#
# Validations:
# - n must be convertible to an integer.
# - n must be >= 1.
#
# Test cases:
# 1) Normal: n=4 -> *, **, ***, ****
# 2) Border: n=1 -> *
# 3) Error: n=0 -> Error: invalid input

def print_triangle_pattern(n_input):
    """Prints a right-angled triangle pattern using nested for loops."""
    try:
        n = int(n_input)
    except ValueError:
        print("Error: invalid input")
        return

    # 1. Validation
    if n < 1:
        print("Error: invalid input")
        return

    print(f"Right-angled triangle pattern (n={n}):")

    # 2. Nested For Loops (Outer loop controls rows, Inner loop controls columns/content)
    # Outer loop: Iterates from 1 up to n (rows)
    for i in range(1, n + 1):
        # Pythonic way: Use string repetition to build the line
        pattern_line = "*" * i
        print(pattern_line)

    print("\nOptional: Inverted right-angled triangle pattern:")

    # Optional: Inverted right-angled triangle pattern
    for i in range(n, 0, -1):
        pattern_line = "*" * i
        print(pattern_line)
    
    print("---")


print("\n--- Problem 6 Test Runs ---")
print_triangle_pattern("4") # Normal
print_triangle_pattern("1") # Border
print_triangle_pattern("0") # Error: n < 1

# --------------------------------------------------
# CONCLUSIONES
# --------------------------------------------------

# Conclusions:
# The practical distinction between **for** and **while** loops is primarily defined by when the iteration count is known. **For** loops are chosen for fixed-length tasks like processing elements in a list or ranges, providing clear, concise, and safe iteration. **While** loops excel in scenarios requiring indefinite iteration, such as the event loops for menus or limited-attempt scenarios like password entry, where the termination depends on a runtime condition. **Counters** and **accumulators** were invaluable across all problems, serving as the core mechanism for tracking progress and aggregating results. The main risk with **while** loops is the potential for **infinite loops**, which are avoided by diligently ensuring the control variable changes toward the exit condition. Finally, **nested loops**, as seen in pattern generation, are crucial for solving problems that involve two-dimensional structures or iterating through combinations of elements.

# --------------------------------------------------
# REFERENCIAS
# --------------------------------------------------

# References:
# 1) Python documentation - for and while statements. Available at: [Link a la documentación oficial de Python sobre bucles]
# 2) FreeCodeCamp. (2023). Python For Loops and While Loops. Available at: [Link a un tutorial sobre bucles]
# 3) W3Schools. (2023). Python Loops. Available at: [Link a W3Schools sobre bucles]
# 4) Zelle, J. M. (2017). Python Programming: An Introduction to Computer Science (3rd ed.). (O similar libro de programación)
# 5) Tutorialspoint. (2023). Python Counters and Accumulators. Available at: [Link a un recurso sobre contadores y acumuladores]

# --------------------------------------------------
# Git Repository Clone Instruction
# --------------------------------------------------

# To download this project from the source repository, use the following command 
# in your terminal or command prompt:
#
# git clone https://github.com/ValdoGlz7/Python_Proyects
#
# This command will create a local copy of the repository contents.