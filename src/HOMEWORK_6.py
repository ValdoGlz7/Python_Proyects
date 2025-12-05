# Name: Oswaldo González Charles
# Student ID: 2530088
# Group: IM 1-1

# --------------------------------------------------
# Executive Summary
# --------------------------------------------------

# Executive Summary (Fibonacci Series):
# The **Fibonacci series** is a sequence of numbers where each number after the first two
# is the sum of the two preceding ones. It traditionally starts with 0 and 1. "Calculating
# the series up to *n* terms" means generating and displaying the first *n* elements of this 
# sequence. This program handles reading *n* from the user, performing basic validation 
# (n must be an integer >= 1), and then generating and printing the series using a loop.

# --------------------------------------------------
# Problem: Fibonacci series generator
# --------------------------------------------------

# Problem: Fibonacci series generator  
# Description: Program that reads an integer n and prints the first n terms of the Fibonacci 
# series starting at 0 and 1.  

# Inputs:  
# - terms_count_input (string; input for number of terms to generate)  

# Outputs:  
# - "Number of terms:" <n>
# - "Fibonacci series:" followed by the n terms separated by spaces  
# - "Error: invalid input"  

# Validations:  
# - terms_count_input must be convertible to a positive integer (>= 1).  
# - n must be <= 50 (maximum defined for stability).  

# Test cases:  
# 1) Normal: n = 7 → expected series: 0 1 1 2 3 5 8  
# 2) Border: n = 1 → expected series: 0  
# 3) Error: n = -5 or "abc" → expected message: "Error: invalid input"

# --------------------------------------------------
# Unique Problem: Fibonacci series up to n terms
# --------------------------------------------------

# Constants
MAX_TERMS = 50

def generate_fibonacci_series(terms_count):
    """Generates and prints the first 'terms_count' terms of the Fibonacci series."""
    
    # Initialization based on standard Fibonacci sequence (0, 1, 1, 2, ...)
    current_term = 0
    next_term = 1
    
    # Store results to print on one line later
    series_output = []

    # Handle special case n=1 (0) and n=2 (0, 1) cleanly within the loop logic.
    
    for i in range(terms_count):
        # The first term to be displayed is always 'current_term'
        series_output.append(str(current_term))

        # This simultaneous assignment is the core of the Fibonacci generation:
        # The new 'current_term' becomes the old 'next_term'
        # The new 'next_term' becomes the sum of the old two (a + b)
        
        # The user provided code uses (a, b = b, a + b) where 'a' is the term printed.
        # We adapt that logic, ensuring the sequence starts at 0, 1.
        
        # The next two terms are updated:
        current_term, next_term = next_term, current_term + next_term

    # Print output
    print("Fibonacci series: " + " ".join(series_output))


def main_fibonacci_generator():
    """Reads input, validates it, and calls the series generator."""
    
    # 1) Read n from standard input
    terms_count_input = input("How many elements do you want? ").strip()

    # 2) Validation
    try:
        terms_count = int(terms_count_input)
    except ValueError:
        print("Error: invalid input (must be an integer)")
        return

    if terms_count < 1 or terms_count > MAX_TERMS:
        print(f"Error: invalid input (number of terms must be between 1 and {MAX_TERMS})")
        return
    
    # Output number of terms (Optional, as per instructions)
    print(f"Number of terms: {terms_count}")

    # 3) Generate the series
    generate_fibonacci_series(terms_count)


if __name__ == "__main__":
    # Test cases section demonstrating behavior:
    print("\n--- Program Start (Test Cases Example) ---")
    
    # Run test cases directly if the program were a utility, 
    # but since it's an interactive script, we call the main function.
    
    # Example Run: n=7 (Normal)
    # To properly simulate input for validation, you might run the full interactive script.
    # For a non-interactive example, the logic is shown below (requires modifying main 
    # for automated testing, which we skip to keep the main code interactive).

    main_fibonacci_generator()
    
# --------------------------------------------------
# Conclusions
# --------------------------------------------------

# Conclusions:
# The use of a **for loop** was essential for efficiently generating the series, allowing the calculation of *n* terms without writing redundant code. The Pythonic simultaneous assignment (`a, b = b, a + b`) is highly effective for rotating the two necessary sequence values in each iteration. Handling **n=1** (outputting only 0) and **n=2** (outputting 0, 1) was automatically managed by initializing the loop variables to $0$ and $1$ and letting the loop structure take care of the flow based on the `range(n)`. This sequence generation logic, particularly the simultaneous update, is highly reusable for any program requiring iterative mathematical sequence generation, such as geometric progression or Lucas numbers.

# --------------------------------------------------
# References (Minimum 3)
# --------------------------------------------------

# References:
# 1) Python documentation – while and for loops. Available at: [Link a la documentación oficial de Python sobre bucles]
# 2) Wikipedia. (2023). Fibonacci number. Available at: [Link a la página de Wikipedia sobre Fibonacci]
# 3) Tutoriales de Python sobre Fibonacci series (e.g., GeeksforGeeks). Available at: [Link a un tutorial de Python/Fibonacci]

# --------------------------------------------------
# Git Repository Clone Instruction
# --------------------------------------------------

# To download this project from the source repository, use the following command 
# in your terminal or command prompt:
#
# git clone https://github.com/ValdoGlz7/Python_Proyects
#
# This command will create a local copy of the repository contents.