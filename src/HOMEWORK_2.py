# Name: Oswaldo González Charles
# Student ID: 2530088
# Group: IM 1-1

# --------------------------------------------------
# RESUMEN EJECUTIVO (Executive Summary)
# --------------------------------------------------

# Executive Summary:
# In Python, **int** is used for whole numbers (counters, ages), and **float** is used for real
# numbers (salaries, temperatures) that include decimal points. The distinction ensures correct
# memory usage and arithmetic behavior. A **boolean** is a logical data type representing truth
# values: **True** or **False**. Booleans are primarily derived from **relational operators**
# (e.g., age >= 18) and are essential for controlling program flow (decisions). **Input validation**
# of ranges and preventing **division by zero** are critical programming practices to ensure mathematical
# correctness and program stability. This document covers six problems demonstrating numerical
# computation and boolean logic, including temperature conversion, salary calculation with overtime,
# discount eligibility checks, basic number statistics, loan eligibility assessment, and BMI calculation.

# --------------------------------------------------
# PRINCIPIOS Y BUENAS PRÁCTICAS
# --------------------------------------------------

# - **Type Appropriateness:** Use `int` for counting, indices, and discrete values; use `float` for measurements, money, and calculations requiring precision.
# - **Avoid Duplication:** Store the result of complex or repeated calculations (like the overtime rate or a debt ratio) in an intermediate variable to improve readability and prevent errors.
# - **Pre-Validation:** Always validate numerical inputs (e.g., ensuring hours and salaries are non-negative, and preventing zero divisors) before performing any core arithmetic operations.
# - **Clear Naming:** Use descriptive variable names (e.g., `monthly_income`, `is_eligible`) and clear, user-friendly output messages.
# - **Boolean Documentation:** Document how boolean results are interpreted (e.g., True means "eligible for discount," False means "not eligible").

# --------------------------------------------------
# PROBLEMAS
# --------------------------------------------------

# --- CONVENTION NOTES ---
# Variables: lower_snake_case
# Constants: UPPER_SNAKE_CASE
# Data Types: int, float, bool
# Output Messages: English

# --------------------------------------------------
# Problem 1: Temperature converter and range flag
# --------------------------------------------------

# Problem 1: Temperature Converter and Range Flag
# Description: Converts a temperature from Celsius (float) to Fahrenheit and Kelvin. It also
# sets a boolean flag, is_high_temperature, if the Celsius temperature is >= 30.0.
#
# Inputs:
# - temp_c_input (string; temperature in °C).
#
# Outputs:
# - "Fahrenheit:" <temp_f>
# - "Kelvin:" <temp_k>
# - "High temperature:" true|false
# - "Error: invalid input or physically impossible temperature"
#
# Validations:
# - temp_c_input must be convertible to float.
# - The resulting Kelvin temperature must be >= absolute zero (0.0 K or -273.15 °C).
#
# Test cases:
# 1) Normal: temp_c = 35.0 -> F: 95.0, K: 308.15, High: true
# 2) Border: temp_c = 29.9 -> F: 85.82, K: 303.05, High: false
# 3) Error: temp_c = -300.0 -> Error: physically impossible temperature

ABSOLUTE_ZERO_C = -273.15

def convert_temperature(temp_c_input):
    """Converts Celsius to Fahrenheit and Kelvin, and checks for high temperature."""
    # 1. Validation and Conversion
    try:
        temp_c = float(temp_c_input)
    except ValueError:
        print("Error: invalid input")
        return

    # 2. Physical Validation
    if temp_c < ABSOLUTE_ZERO_C:
        print("Error: invalid input or physically impossible temperature")
        return

    # 3. Calculations (float)
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15

    # 4. Boolean Flag (Relational Operator)
    is_high_temperature = temp_c >= 30.0

    # 5. Output
    print(f"Fahrenheit: {round(temp_f, 2)}")
    print(f"Kelvin: {round(temp_k, 2)}")
    print(f"High temperature: {str(is_high_temperature).lower()}")


print("\n--- Problem 1 Test Runs ---")
convert_temperature("35.0") # Normal
convert_temperature("29.9") # Border
convert_temperature("-300.0") # Error: Physical limit
convert_temperature("abc") # Error: Invalid type

# --------------------------------------------------
# Problem 2: Work hours and overtime payment
# --------------------------------------------------

# Problem 2: Work Hours and Overtime Payment
# Description: Calculates a worker's total weekly pay, including overtime (hours > 40) paid
# at 150% the normal rate. Generates a boolean indicating if overtime occurred.
#
# Inputs:
# - hours_worked_input (string; hours worked).
# - hourly_rate_input (string; pay per hour).
#
# Outputs:
# - "Regular pay:" <regular_pay>
# - "Overtime pay:" <overtime_pay>
# - "Total pay:" <total_pay>
# - "Has overtime:" true|false
# - "Error: invalid input"
#
# Validations:
# - hours_worked >= 0.0
# - hourly_rate > 0.0
#
# Test cases:
# 1) Normal: Hours: 45.0, Rate: 10.0 -> Total: 475.0 (400 + 75), Has overtime: true
# 2) Border: Hours: 40.0, Rate: 10.0 -> Total: 400.0, Has overtime: false
# 3) Error: Hours: 45.0, Rate: -5.0 -> Error: invalid input

MAX_REGULAR_HOURS = 40.0
OVERTIME_MULTIPLIER = 1.5

def calculate_weekly_pay(hours_worked_input, hourly_rate_input):
    """Calculates weekly pay including overtime using floats and conditionals."""
    # 1. Validation and Conversion
    try:
        hours_worked = float(hours_worked_input)
        hourly_rate = float(hourly_rate_input)
    except ValueError:
        print("Error: invalid input")
        return

    if hours_worked < 0.0 or hourly_rate <= 0.0:
        print("Error: invalid input")
        return

    # 2. Boolean Flag
    has_overtime = hours_worked > MAX_REGULAR_HOURS

    # 3. Calculation (float)
    if has_overtime:
        regular_hours = MAX_REGULAR_HOURS
        overtime_hours = hours_worked - MAX_REGULAR_HOURS
    else:
        regular_hours = hours_worked
        overtime_hours = 0.0

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
    total_pay = regular_pay + overtime_pay

    # 4. Output
    print(f"Regular pay: {round(regular_pay, 2)}")
    print(f"Overtime pay: {round(overtime_pay, 2)}")
    print(f"Total pay: {round(total_pay, 2)}")
    print(f"Has overtime: {str(has_overtime).lower()}")


print("\n--- Problem 2 Test Runs ---")
calculate_weekly_pay("45.0", "10.0") # Normal
calculate_weekly_pay("40.0", "10.0") # Border: Exactly 40h
calculate_weekly_pay("45.0", "-5.0") # Error: Negative rate
calculate_weekly_pay("abc", "10.0") # Error: Invalid hours type

# --------------------------------------------------
# Problem 3: Discount eligibility with booleans
# --------------------------------------------------

# Problem 3: Discount Eligibility with Booleans
# Description: Determines discount eligibility (10%) based on customer status (student, senior)
# OR a high purchase total (>= 1000.0). Calculates the final discounted price.
#
# Inputs:
# - purchase_total_input (string; total purchase amount).
# - is_student_text (string; "YES" or "NO").
# - is_senior_text (string; "YES" or "NO").
#
# Outputs:
# - "Discount eligible:" true|false
# - "Final total:" <final_total>
# - "Error: invalid input"
#
# Validations:
# - purchase_total >= 0.0
# - is_student_text and is_senior_text must be "YES" or "NO".
#
# Test cases:
# 1) Normal: Total: 500.0, Student: YES, Senior: NO -> Eligible: true, Final: 450.0
# 2) Border: Total: 1000.0, Student: NO, Senior: NO -> Eligible: true, Final: 900.0
# 3) Error: Total: 500.0, Student: INVALID, Senior: NO -> Error: invalid input

MIN_TOTAL_FOR_DISCOUNT = 1000.0
DISCOUNT_RATE = 0.10

def check_discount_eligibility(purchase_total_input, is_student_text, is_senior_text):
    """Checks discount eligibility using combined boolean logic (OR) and calculates final total."""
    # 1. Validation and Conversion
    try:
        purchase_total = float(purchase_total_input)
    except ValueError:
        print("Error: invalid input")
        return

    student_text = is_student_text.strip().upper()
    senior_text = is_senior_text.strip().upper()

    if purchase_total < 0.0 or student_text not in ("YES", "NO") or senior_text not in ("YES", "NO"):
        print("Error: invalid input")
        return

    # 2. Boolean Conversions
    is_student = (student_text == "YES")
    is_senior = (senior_text == "YES")
    is_high_purchase = (purchase_total >= MIN_TOTAL_FOR_DISCOUNT)

    # 3. Combined Boolean Logic (AND, OR)
    discount_eligible = is_student or is_senior or is_high_purchase

    # 4. Final Calculation (float)
    if discount_eligible:
        final_total = purchase_total * (1.0 - DISCOUNT_RATE)
    else:
        final_total = purchase_total

    # 5. Output
    print(f"Discount eligible: {str(discount_eligible).lower()}")
    print(f"Final total: {round(final_total, 2)}")


print("\n--- Problem 3 Test Runs ---")
check_discount_eligibility("500.0", "YES", "NO") # Normal: Student
check_discount_eligibility("999.99", "NO", "YES") # Normal: Senior
check_discount_eligibility("1000.0", "NO", "NO") # Border: High total
check_discount_eligibility("500.0", "INVALID", "NO") # Error: Invalid text input

# --------------------------------------------------
# Problem 4: Basic statistics of three integers
# --------------------------------------------------

# Problem 4: Basic Statistics of Three Integers
# Description: Reads three integers and calculates their sum, average, min, max, and checks
# if all three numbers are even using modular arithmetic and boolean AND.
#
# Inputs:
# - n1_input, n2_input, n3_input (strings; three integers).
#
# Outputs:
# - "Sum:" <sum_value>
# - "Average:" <average_value> (float)
# - "Max:" <max_value>
# - "Min:" <min_value>
# - "All even:" true|false
# - "Error: invalid input"
#
# Validations:
# - All three inputs must be convertible to int.
#
# Test cases:
# 1) Normal: 10, 20, 30 -> Sum: 60, Avg: 20.0, Max: 30, Min: 10, All even: true
# 2) Border: 1, 1, 1 -> Sum: 3, Avg: 1.0, Max: 1, Min: 1, All even: false
# 3) Error: 10, twenty, 30 -> Error: invalid input

def calculate_three_int_stats(n1_input, n2_input, n3_input):
    """Calculates basic statistics for three integers."""
    # 1. Validation and Conversion (int)
    try:
        n1 = int(n1_input)
        n2 = int(n2_input)
        n3 = int(n3_input)
    except ValueError:
        print("Error: invalid input")
        return

    # 2. Calculations (int and float)
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3.0 # Ensures float result
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    # 3. Boolean Logic (Relational and Logical AND)
    # Check if a number is even: number % 2 == 0
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    # 4. Output
    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")


print("\n--- Problem 4 Test Runs ---")
calculate_three_int_stats("10", "20", "30") # Normal: All even
calculate_three_int_stats("1", "2", "3") # Normal: Mixed
calculate_three_int_stats("1", "1", "1") # Border: All odd
calculate_three_int_stats("10", "twenty", "30") # Error: Invalid type

# --------------------------------------------------
# 7.5 Problem 5: Loan eligibility (income and debt ratio)
# --------------------------------------------------

# Problem 5: Loan Eligibility (Income and Debt Ratio)
# Description: Determines if a person is eligible for a loan based on three criteria: minimum
# monthly income, maximum debt-to-income ratio (debt_ratio <= 0.4), and minimum credit score.
#
# Inputs:
# - monthly_income_input (string; monthly income).
# - monthly_debt_input (string; monthly debt payments).
# - credit_score_input (string; credit score).
#
# Outputs:
# - "Debt ratio:" <debt_ratio>
# - "Eligible:" true|false
# - "Error: invalid input"
#
# Validations:
# - monthly_income > 0.0 (prevents zero division)
# - monthly_debt >= 0.0
# - credit_score >= 0
#
# Test cases:
# 1) Normal: Income: 10000.0, Debt: 3000.0, Score: 700 -> Ratio: 0.3, Eligible: true
# 2) Border: Income: 8000.0, Debt: 3200.0, Score: 650 -> Ratio: 0.4, Eligible: true
# 3) Error: Income: 10000.0, Debt: 5000.0, Score: 700 -> Ratio: 0.5, Eligible: false

MIN_INCOME = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650

def check_loan_eligibility(monthly_income_input, monthly_debt_input, credit_score_input):
    """Checks loan eligibility based on income, debt ratio, and credit score."""
    # 1. Validation and Conversion (float and int)
    try:
        monthly_income = float(monthly_income_input)
        monthly_debt = float(monthly_debt_input)
        credit_score = int(credit_score_input)
    except ValueError:
        print("Error: invalid input")
        return

    # 2. Range Validation (Crucial: Avoid division by zero)
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
        return

    # 3. Intermediate Calculation (float)
    debt_ratio = monthly_debt / monthly_income

    # 4. Combined Boolean Logic (Logical AND)
    is_high_income = monthly_income >= MIN_INCOME
    is_low_debt_ratio = debt_ratio <= MAX_DEBT_RATIO
    is_high_credit_score = credit_score >= MIN_CREDIT_SCORE

    eligible = is_high_income and is_low_debt_ratio and is_high_credit_score

    # 5. Output
    print(f"Debt ratio: {round(debt_ratio, 3)}")
    print(f"Eligible: {str(eligible).lower()}")


print("\n--- Problem 5 Test Runs ---")
check_loan_eligibility("10000.0", "3000.0", "700") # Normal
check_loan_eligibility("8000.0", "3200.0", "650") # Border
check_loan_eligibility("10000.0", "5000.0", "700") # Error: High debt ratio
check_loan_eligibility("0.0", "100.0", "700") # Error: Zero income

# --------------------------------------------------
# Problem 6: Body Mass Index (BMI) and category flag
# --------------------------------------------------

# Problem 6: Body Mass Index (BMI) and Category Flag
# Description: Calculates the Body Mass Index (BMI) and sets three boolean flags to categorize
# the result (is_underweight, is_normal, is_overweight) based on standard thresholds.
#
# Inputs:
# - weight_kg_input (string; weight in kg).
# - height_m_input (string; height in meters).
#
# Outputs:
# - "BMI:" <bmi_redondeado>
# - "Underweight:" true|false
# - "Normal:" true|false
# - "Overweight:" true|false
# - "Error: invalid input"
#
# Validations:
# - weight_kg > 0.0
# - height_m > 0.0 (prevents division by zero)
#
# Test cases:
# 1) Normal: Weight: 70.0, Height: 1.75 -> BMI: 22.86, Normal: true
# 2) Border: Weight: 60.0, Height: 1.80 -> BMI: 18.52 (Normal), Overweight: false
# 3) Error: Weight: 70.0, Height: 0.0 -> Error: invalid input

UNDERWEIGHT_THRESHOLD = 18.5
OVERWEIGHT_THRESHOLD = 25.0

def calculate_bmi_and_category(weight_kg_input, height_m_input):
    """Calculates BMI and categorizes the result using boolean flags."""
    # 1. Validation and Conversion (float)
    try:
        weight_kg = float(weight_kg_input)
        height_m = float(height_m_input)
    except ValueError:
        print("Error: invalid input")
        return

    # 2. Range Validation (Crucial: Avoid division by zero)
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
        return

    # 3. Calculation (float)
    # BMI = weight / height^2
    bmi = weight_kg / (height_m ** 2)

    # 4. Boolean Flags (Relational Operators)
    is_underweight = bmi < UNDERWEIGHT_THRESHOLD
    is_normal = (bmi >= UNDERWEIGHT_THRESHOLD) and (bmi < OVERWEIGHT_THRESHOLD)
    is_overweight = bmi >= OVERWEIGHT_THRESHOLD

    # 5. Output
    print(f"BMI: {round(bmi, 2)}")
    print(f"Underweight: {str(is_underweight).lower()}")
    print(f"Normal: {str(is_normal).lower()}")
    print(f"Overweight: {str(is_overweight).lower()}")


print("\n--- Problem 6 Test Runs ---")
calculate_bmi_and_category("70.0", "1.75") # Normal: Normal weight
calculate_bmi_and_category("55.0", "1.75") # Normal: Underweight
calculate_bmi_and_category("80.0", "1.75") # Normal: Overweight
calculate_bmi_and_category("70.0", "0.0") # Error: Zero height

# --------------------------------------------------
# CONCLUSIONES
# --------------------------------------------------

# Conclusions:
# Integers and floats are used co-dependently in real-world calculations, where **int** often defines countable quantities (e.g., credit score) and **float** represents measured or calculated values (e.g., salary, BMI). **Comparisons** between these numerical types are the mechanism that generates **booleans**, which are then used with **logical operators** (`and`, `or`) to build complex **decision criteria** (like discount eligibility or loan approval). It is paramount to validate input ranges and preemptively guard against **division by zero** to maintain the program's mathematical integrity and stability. The design of combined conditions, seen in the loan and BMI problems, highlights how logical operators allow us to model complex, multi-factor real-world rules efficiently. These fundamental patterns underpin applications across finance (payroll, loans), health (BMI), and commerce (discounts).

# --------------------------------------------------
# REFERENCIAS
# --------------------------------------------------

# References:
# 1) Python documentation - Numeric and Boolean types. Available at: [Link a la documentación oficial de Python sobre tipos numéricos]
# 2) Real Python. (2023). Python Booleans and Logical Operators. Available at: [Link a un tutorial de Real Python sobre lógica booleana]
# 3) W3Schools. (2023). Python Operators. Available at: [Link a W3Schools sobre operadores aritméticos y lógicos]
# 4) Stack Overflow (community best practices on data validation and type checking).
# 5) Smith, J. M. (2020). Principles of Programming with Python. (O similar libro de programación básica).

# --------------------------------------------------
# Git Repository Clone Instruction
# --------------------------------------------------

# To download this project from the source repository, use the following command 
# in your terminal or command prompt:
#
# git clone https://github.com/ValdoGlz7/Python_Proyects
#
# This command will create a local copy of the repository contents.