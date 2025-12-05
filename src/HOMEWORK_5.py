# Name: Oswaldo González Charles
# Student ID: 2530088
# Group: IM 1-1

# --------------------------------------------------
# Executive Summary
# --------------------------------------------------

# Executive Summary:
# A **function** in Python is a block of organized, reusable code that performs a single, related action.
# It serves to break down complex problems into smaller, manageable, and modular pieces. **Parameters** are 
# variables listed in the function definition, while **arguments** are the actual values passed to the function 
# when it is called. Separating logic into reusable functions is crucial for **code cleanliness** and avoiding 
# repetition. A **return value** is better than just printing because it allows the calling code to use the result 
# for further calculations or decisions, maintaining the function's purity. This document covers six problems 
# demonstrating function definition, parameter passing (including defaults), returning values (numbers, strings, 
# and dictionaries), list manipulation, and iterative calculation (factorial).

# --------------------------------------------------
# Principles and Best Practices
# --------------------------------------------------

# - **Single Responsibility Principle:** Prefer small functions that perform only one task (e.g., one function for area, another for perimeter).
# - **Avoid Repetition (DRY):** If logic is repeated, extract it into a dedicated function.
# - **Function Purity:** Aim for "pure" functions where possible (given the same input, they always produce the same output, and have no external side effects).
# - **Documentation:** Use simple comments to describe what each function does and what parameters it expects.
# - **Clear Naming:** Use descriptive names for functions (e.g., calculate_bmi, not f1 or do_it).

# --------------------------------------------------
# Problem 1: Rectangle area and perimeter (basic functions)
# --------------------------------------------------

# Problem 1: Rectangle Area and Perimeter
# Description: Defines two simple functions to calculate the area and perimeter of a rectangle, 
# given its width and height.
#
# Inputs:
# - width (float)
# - height (float)
#
# Outputs:
# - "Area:" <area_value>
# - "Perimeter:" <perimeter_value>
#
# Validations:
# - width > 0 and height > 0. If not, show "Error: invalid input".
#
# Test cases:
# 1) Normal: width=4.0, height=5.0 -> Area: 20.0, Perimeter: 18.0
# 2) Border: width=1.0, height=1.0 -> Area: 1.0, Perimeter: 4.0
# 3) Error: width=-5.0, height=5.0 -> Error: invalid input

def calculate_area(width, height):
    """Returns the area of a rectangle (width * height)."""
    return width * height

def calculate_perimeter(width, height):
    """Returns the perimeter of a rectangle (2 * (width + height))."""
    return 2 * (width + height)

def run_problem_1(width_input, height_input):
    """Main logic for Problem 1, handles validation and function calls."""
    try:
        width = float(width_input)
        height = float(height_input)
    except ValueError:
        print("Error: invalid input (must be numbers)")
        return

    # Validation
    if width <= 0 or height <= 0:
        print("Error: invalid input (width and height must be > 0)")
        return

    # Function Calls
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)

    # Output
    print(f"Area: {round(area, 2)}")
    print(f"Perimeter: {round(perimeter, 2)}")

print("\n--- Problem 1 Test Runs ---")
run_problem_1("4.0", "5.0") # Normal
run_problem_1("1.0", "1.0") # Border
run_problem_1("-5.0", "5.0") # Error

# --------------------------------------------------
# Problem 2: Grade classifier (function with return string)
# --------------------------------------------------

# Problem 2: Grade Classifier
# Description: Defines a function that classifies a score (0-100) into a letter grade 
# (A, B, C, D, F) using conditional logic.
#
# Inputs:
# - score (float)
#
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
#
# Validations:
# - 0 <= score <= 100. If not, show "Error: invalid input".
#
# Test cases:
# 1) Normal: score=85.5 -> Category: B
# 2) Border: score=90.0 -> Category: A
# 3) Error: score=101.0 -> Error: invalid input

def classify_grade(score):
    """
    Classifies a score (0-100) into a letter grade (A, B, C, D, F).
    Returns the grade letter string.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def run_problem_2(score_input):
    """Main logic for Problem 2, handles validation and function calls."""
    try:
        score = float(score_input)
    except ValueError:
        print("Error: invalid input (must be a number)")
        return

    # Validation
    if not (0 <= score <= 100):
        print("Error: invalid input (score must be between 0 and 100)")
        return

    # Function Call
    grade_letter = classify_grade(score)

    # Output
    print(f"Score: {round(score, 1)}")
    print(f"Category: {grade_letter}")

print("\n--- Problem 2 Test Runs ---")
run_problem_2("85.5") # Normal
run_problem_2("90.0") # Border (A/B)
run_problem_2("59.9") # Border (D/F)
run_problem_2("101.0") # Error

# --------------------------------------------------
# Problem 3: List statistics function (min, max, average)
# --------------------------------------------------

# Problem 3: List Statistics Function
# Description: Defines a function that takes a list of numbers and returns a dictionary 
# containing the minimum, maximum, and average of the list.
#
# Inputs:
# - numbers_text (string; e.g., "10,20,30")
# - Internally: numbers_list (list of float)
#
# Outputs:
# - "Min:" <min_value>
# - "Max:" <max_value>
# - "Average:" <average_value>
#
# Validations:
# - List must not be empty.
# - All elements must be convertible to numbers.
#
# Test cases:
# 1) Normal: "10, 20, 30" -> Min: 10.0, Max: 30.0, Average: 20.0
# 2) Border: "5.5" -> Min: 5.5, Max: 5.5, Average: 5.5
# 3) Error: "" or "1, 2, three" -> Error: invalid input

def summarize_numbers(numbers_list):
    """
    Calculates the min, max, and average of a list of numbers.
    Returns a dictionary with the results.
    """
    if not numbers_list:
        # This case should ideally be caught by validation before calling, 
        # but handled here for completeness.
        return None 

    # Use built-in functions
    min_val = min(numbers_list)
    max_val = max(numbers_list)
    average_val = sum(numbers_list) / len(numbers_list)

    return {
        "min": min_val,
        "max": max_val,
        "average": average_val
    }

def run_problem_3(numbers_text):
    """Main logic for Problem 3, handles text conversion, validation, and function calls."""
    number_strings = [s.strip() for s in numbers_text.split(',') if s.strip()]
    
    if not number_strings:
        print("Error: invalid input (list cannot be empty)")
        return

    numbers_list = []
    try:
        # Convert all elements to float (validation)
        for s in number_strings:
            numbers_list.append(float(s))
    except ValueError:
        print("Error: invalid input (all elements must be numbers)")
        return

    # Function Call
    summary = summarize_numbers(numbers_list)
    
    # Output
    if summary:
        print(f"Min: {round(summary['min'], 2)}")
        print(f"Max: {round(summary['max'], 2)}")
        print(f"Average: {round(summary['average'], 2)}")
    else:
        # Should not be reached if initial empty check is correct, but safe guard.
        print("Error: could not summarize numbers.") 

print("\n--- Problem 3 Test Runs ---")
run_problem_3("10, 20, 30") # Normal
run_problem_3("5.5") # Border
run_problem_3("1, 2, three") # Error: non-numeric

# --------------------------------------------------
# Problem 4: Apply discount list (pure function)
# --------------------------------------------------

# Problem 4: Apply Discount List (Pure Function)
# Description: Defines a pure function that applies a discount rate to a list of prices 
# and returns a NEW list of discounted prices, leaving the original list unmodified.
#
# Inputs:
# - prices_text (string; e.g., "100,200,300")
# - discount_rate (float, between 0 and 1)
#
# Outputs:
# - "Original prices:" <original_list>
# - "Discounted prices:" <discounted_list>
#
# Validations:
# - List not empty, all prices > 0.
# - 0 <= discount_rate <= 1.
#
# Test cases:
# 1) Normal: "100, 200", 0.10 (10%) -> Original: [100.0, 200.0], Discounted: [90.0, 180.0]
# 2) Border: "1.0", 0.0 -> Original: [1.0], Discounted: [1.0]
# 3) Error: "100, -5", 0.10 -> Error: invalid input (price < 0)

def apply_discount(prices_list, discount_rate):
    """
    Applies a discount rate to a list of prices and returns a new list.
    (Pure function: does not modify prices_list).
    """
    # Calculate multiplier outside the loop for efficiency
    multiplier = 1.0 - discount_rate
    
    discounted_prices = []
    for price in prices_list:
        discounted_prices.append(price * multiplier)
        
    return discounted_prices

def run_problem_4(prices_text, discount_rate_input):
    """Main logic for Problem 4, handles validation and function calls."""
    try:
        discount_rate = float(discount_rate_input)
    except ValueError:
        print("Error: invalid input (rate must be a number)")
        return
    
    # Validation 1: Discount rate
    if not (0.0 <= discount_rate <= 1.0):
        print("Error: invalid input (discount rate must be between 0 and 1)")
        return

    price_strings = [s.strip() for s in prices_text.split(',') if s.strip()]
    if not price_strings:
        print("Error: invalid input (price list cannot be empty)")
        return
    
    prices_list = []
    try:
        # Validation 2: Prices must be numbers > 0
        for s in price_strings:
            price = float(s)
            if price <= 0:
                print("Error: invalid input (all prices must be > 0)")
                return
            prices_list.append(price)
    except ValueError:
        print("Error: invalid input (all elements must be numbers)")
        return
    
    # Function Call
    discounted_prices = apply_discount(prices_list, discount_rate)
    
    # Output (rounding for clean display)
    print(f"Original prices: {[round(p, 2) for p in prices_list]}")
    print(f"Discounted prices: {[round(p, 2) for p in discounted_prices]}")

print("\n--- Problem 4 Test Runs ---")
run_problem_4("100, 200", "0.10") # Normal
run_problem_4("1.0", "0.0") # Border
run_problem_4("100, -5", "0.10") # Error: price < 0

# --------------------------------------------------
# Problem 5: Greeting function with default parameters
# --------------------------------------------------

# Problem 5: Greeting Function with Default Parameters
# Description: Defines a function with a default parameter for 'title' to create flexible 
# greeting messages.
#
# Inputs:
# - name (string)
# - title (string optional, defaults to "")
#
# Outputs:
# - "Greeting:" <greeting_message>
#
# Validations:
# - name must not be empty.
#
# Test cases:
# 1) Normal: name="Alice", title="Dr." -> Hello, Dr. Alice!
# 2) Border: name="Bob" (no title) -> Hello, Bob!
# 3) Error: name="" -> Error: invalid input

def greet(name, title=""):
    """
    Returns a greeting message, optionally including a title.
    Title defaults to an empty string.
    """
    name = name.strip()
    title = title.strip()
    
    if title:
        full_name = f"{title}. {name}"
    else:
        full_name = name
        
    return f"Hello, {full_name}!"

def run_problem_5(name_input, title_input=""):
    """Main logic for Problem 5, handles validation and function calls."""
    name = name_input.strip()
    
    # Validation
    if not name:
        print("Error: invalid input (name cannot be empty)")
        return

    # Function Calls (demonstrating positional and named arguments)
    if title_input:
        # Call with named argument for title
        greeting_message = greet(name=name, title=title_input)
    else:
        # Call with only positional argument
        greeting_message = greet(name) 

    # Output
    print(f"Greeting: {greeting_message}")

print("\n--- Problem 5 Test Runs ---")
run_problem_5("Alice", "Dr") # Normal (named argument)
run_problem_5("Bob") # Border (default parameter used)
run_problem_5("  ") # Error

# --------------------------------------------------
# Problem 6: Factorial function (iterative or recursive)
# --------------------------------------------------

# Problem 6: Factorial Function (Iterative)
# Implementation choice: Iterative (using a for loop), documented below.
#
# Description: Defines a function to calculate n! (n factorial).
#
# Inputs:
# - n (int)
#
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
#
# Validations:
# - n must be a non-negative integer.
# - Max limit for n: 20 (to prevent excessively large numbers/overflow).
#
# Test cases:
# 1) Normal: n=5 -> Factorial: 120
# 2) Border: n=0 -> Factorial: 1
# 3) Error: n=-5 or n=21 -> Error: invalid input

MAX_FACTORIAL_N = 20

def factorial(n):
    """
    Calculates n! (n factorial) using an iterative approach (for loop).
    Returns the integer result.
    """
    # Implementation choice: Iterative.
    # Rationale: Iterative is generally safer and more memory-efficient in Python 
    # than deep recursion for large inputs.
    
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    return result

def run_problem_6(n_input):
    """Main logic for Problem 6, handles validation and function calls."""
    try:
        n = int(n_input)
    except ValueError:
        print("Error: invalid input (n must be an integer)")
        return

    # Validation
    if n < 0 or n > MAX_FACTORIAL_N:
        print(f"Error: invalid input (n must be between 0 and {MAX_FACTORIAL_N})")
        return

    # Function Call
    factorial_value = factorial(n)

    # Output
    print(f"n: {n}")
    print(f"Factorial: {factorial_value}")

print("\n--- Problem 6 Test Runs ---")
run_problem_6("5") # Normal
run_problem_6("0") # Border
run_problem_6("-5") # Error

# --------------------------------------------------
# Conclusions
# --------------------------------------------------

# Conclusions:
# Functions proved essential for **organizing and reusing** code, as demonstrated by the simple calculation functions in Problem 1 and the list processing logic in Problems 3 and 4. The main advantage of using **return** over simple printing is that the function's output can be used by the calling code for subsequent operations (e.g., saving the discounted list), making the function a true reusable component. **Parameters** and **default values** (Problem 5) offered flexibility, allowing a single function definition to handle both titled and untitled greetings. Encapsulating logic in functions was most comfortable for **repeated calculations** (factorial) and for isolating complex data manipulation (list processing), ensuring the main script remains clean. I learned that the main script's role is to handle input/output and coordinate calls, while the functions perform the heavy lifting.

# --------------------------------------------------
# References 
# --------------------------------------------------

# References:
# 1) Python documentation – Defining Functions (def, return, parameters). Available at: [Link a la documentación oficial de Python sobre funciones]
# 2) Tutorialspoint. (2023). Python Functions. Available at: [Link a un tutorial sobre funciones y sus tipos]
# 3) GeeksforGeeks. (2023). Python Function Arguments and Scope. Available at: [Link a un recurso sobre argumentos y scope]
# 4) Zelle, J. M. (2017). Python Programming: An Introduction to Computer Science (3rd ed.). (O similar libro de programación).
# 5) Clean Code principles (Single Responsibility Principle).

# --------------------------------------------------
# Git Repository Clone Instruction
# --------------------------------------------------

# To download this project from the source repository, use the following command 
# in your terminal or command prompt:
#
# git clone https://github.com/ValdoGlz7/Python_Proyects
#
# This command will create a local copy of the repository contents.