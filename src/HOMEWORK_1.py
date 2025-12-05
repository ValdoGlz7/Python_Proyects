# Name: Oswaldo González Charles
# Student ID: 2530088
# Group: IM 1-1

# --------------------------------------------------
# RESUMEN EJECUTIVO 
# --------------------------------------------------

# Executive Summary:
# A string in Python is an immutable sequence of characters, used to store text data.
# Basic operations like concatenation, getting length (len()), extracting substrings (slicing),
# simple pattern searching ('in' operator), and text replacement are fundamental.
# Input validation and text normalization (e.g., stripping spaces, converting case) are crucial
# practices to ensure data quality and prevent errors when processing user inputs like emails,
# names, or passwords.
# This document covers six problems involving string manipulation: full name formatting,
# email validation, palindrome checking, sentence statistics, password strength classification,
# and fixed-width label formatting. For each problem, the design (inputs/outputs),
# specific validations, and the application of various string methods are detailed with
# concrete test cases.

# --------------------------------------------------
# PRINCIPIOS Y BUENAS PRÁCTICAS
# --------------------------------------------------

# - Immutability of Strings: Any operation that seems to 'change' a string actually creates a new
#   string object in memory.
# - Normalization: It is a good practice to normalize input text using strip() and lower()
#   before comparing or processing it to handle variations in case and whitespace.
# - Avoiding "Magic Numbers": Document what is being extracted by a string slice instead of
#   leaving raw indices unexplained.
# - Method Preference: Use built-in string methods (e.g., replace, split) instead of
#   re-implementing basic logic.
# - Clear Validation Design: Implement validations in a clear sequence, typically checking for
#   empty input first, then checking for format or content constraints.
# - Legible Code: Use clear lower_snake_case variable names and provide understandable
#   error messages in the program's output.

# --------------------------------------------------
# PROBLEMAS
# --------------------------------------------------

# --- CONVENTION NOTES ---
# Variables: lower_snake_case
# Constants: UPPER_SNAKE_CASE
# Output Messages: English

# --------------------------------------------------
# Problem 1: Full name formatter (name + initials)
# --------------------------------------------------

# Problem 1: Full Name Formatter
# Description: Given a person's full name, the program normalizes it, formats the name
# in Title Case, and generates the initials (e.g., J.C.T.).
#
# Inputs:
# - full_name_input (string; full name with potential extra spaces, mixed case).
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
# - "Error: full name cannot be empty"
# - "Error: full name must contain at least two words"
#
# Validations:
# - full_name_input must not be empty after strip().
# - The stripped name must result in at least two words after split().
#
# Test cases:
# 1) Normal: "  juan  carlos tovar  " -> Formatted name: Juan Carlos Tovar, Initials: J.C.T.
# 2) Border: "mary jane" -> Formatted name: Mary Jane, Initials: M.J.
# 3) Error: "  solo uno  " -> Error: full name must contain at least two words

def format_full_name(full_name_input):
    """Normalizes a full name, formats it to Title Case, and extracts initials."""
    # 1. Normalization and Validation (Empty Check)
    cleaned_name = full_name_input.strip()
    if not cleaned_name:
        print("Error: full name cannot be empty")
        return

    # 2. Split and Validation (Word Count Check)
    # The split() method without arguments handles multiple spaces between words
    name_parts = cleaned_name.split()
    if len(name_parts) < 2:
        print("Error: full name must contain at least two words")
        return

    # 3. Formatting
    formatted_parts = [part.lower().title() for part in name_parts]
    formatted_name = " ".join(formatted_parts)

    # 4. Initials Generation
    initials_list = [part[0].upper() for part in name_parts]
    initials = ".".join(initials_list) + "."

    # 5. Output
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


print("\n--- Problem 1 Test Runs ---")
format_full_name("  juan  carlos tovar  ") # Normal: J.C.T.
format_full_name("mary jane") # Border: M.J.
format_full_name("  solo uno  ") # Error: < 2 words
format_full_name("   ") # Error: Empty

# --------------------------------------------------
# Problem 2: Simple email validator (structure + domain)
# --------------------------------------------------

# Problem 2: Simple Email Validator
# Description: Checks if an email has a basic valid structure (exactly one '@', at least one '.'
# after the '@', and no spaces). If valid, it extracts and displays the domain part.
#
# Inputs:
# - email_text_input (string; the email address).
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - If valid: "Domain: <domain_part>"
#
# Validations:
# - email_text_input not empty after strip().
# - Must contain exactly one '@'.
# - Must not contain any spaces (" ").
# - After the '@', there must be at least one '.' (dot).
#
# Test cases:
# 1) Normal: "user.name@example.com" -> Valid: true, Domain: example.com
# 2) Border: "a@b.c" -> Valid: true, Domain: b.c
# 3) Error: "user@example" -> Valid: false (no dot after @)

def validate_email(email_text_input):
    """Validates the basic structure of an email and extracts the domain."""
    email_text = email_text_input.strip()
    is_valid = False
    domain_part = ""
    result_message = ""

    # 1. Validation: Not Empty
    if not email_text:
        result_message = "Error: email cannot be empty"
    # 2. Validation: No Spaces
    elif " " in email_text:
        result_message = "Error: email cannot contain spaces"
    # 3. Validation: Exactly One '@'
    elif email_text.count('@') != 1:
        result_message = "Error: email must contain exactly one '@'"
    else:
        # Split into local and domain parts
        try:
            local_part, domain_part = email_text.split('@')

            # 4. Validation: Dot Check in Domain
            # Check if domain has a dot and the dot is not the first character
            if "." in domain_part and domain_part.find('.') > 0:
                is_valid = True
            else:
                result_message = "Error: domain must contain at least one '.' after '@'"
        except ValueError:
            # Should not happen if count('@') == 1, but good for robustness
            result_message = "Error: could not parse email structure"

    # 5. Output
    print(f"Valid email: {str(is_valid).lower()}")
    if is_valid:
        print(f"Domain: {domain_part}")
    elif not is_valid and not email_text:
        print(result_message)
    elif not is_valid and result_message:
        # Print the error for clarity in the test cases
        print(result_message)


print("\n--- Problem 2 Test Runs ---")
validate_email("user.name@example.com") # Normal
validate_email("a@b.c") # Border
validate_email("user@example") # Error: No dot
validate_email("user @ example.com") # Error: Space
validate_email("noat.com") # Error: No @
validate_email("   ") # Error: Empty

# --------------------------------------------------
# Problem 3: Palindrome checker (ignoring spaces and case)
# --------------------------------------------------

# Problem 3: Palindrome Checker
# Description: Determines if a phrase is a palindrome by reading the same forwards and
# backwards, ignoring spaces and case.
#
# Inputs:
# - phrase_input (string; the phrase to check).
#
# Outputs:
# - "Is palindrome: true" or "Is palindrome: false"
# - "Normalized phrase: <normalized_text>" (Optional)
#
# Validations:
# - phrase_input not empty after strip().
# - Minimum length of 3 characters after cleaning spaces.
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> Is palindrome: true
# 2) Border: "level" -> Is palindrome: true
# 3) Error: "Hola mundo" -> Is palindrome: false

MIN_PALINDROME_LENGTH = 3

def check_palindrome(phrase_input):
    """Checks if a phrase is a palindrome, ignoring case and spaces."""
    # 1. Normalization and Cleaning
    cleaned_phrase = phrase_input.strip()

    # 2. Validation: Not Empty
    if not cleaned_phrase:
        print("Error: phrase cannot be empty")
        print("Is palindrome: false")
        return

    # Normalization (lower case and remove spaces)
    normalized_text = cleaned_phrase.lower().replace(" ", "")

    # 3. Validation: Minimum Length
    if len(normalized_text) < MIN_PALINDROME_LENGTH:
        print(f"Error: normalized phrase must be at least {MIN_PALINDROME_LENGTH} characters long")
        print("Is palindrome: false")
        return

    # 4. Palindrome Check
    reversed_text = normalized_text[::-1]
    is_palindrome = (normalized_text == reversed_text)

    # 5. Output
    print(f"Normalized phrase: {normalized_text}")
    print(f"Is palindrome: {str(is_palindrome).lower()}")


print("\n--- Problem 3 Test Runs ---")
check_palindrome("Anita lava la tina") # Normal
check_palindrome("level") # Border
check_palindrome("Hola mundo") # Error: Not palindrome
check_palindrome("   ") # Error: Empty
check_palindrome("go") # Error: Too short

# --------------------------------------------------
# Problem 4: Sentence word stats (lengths and first/last word)
# --------------------------------------------------

# Problem 4: Sentence Word Stats
# Description: Given a sentence, calculate the total word count, identify the first and last
# words, and find the shortest and longest words by length.
#
# Inputs:
# - sentence_input (string; the sentence).
#
# Outputs:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"
#
# Validations:
# - sentence_input not empty after strip().
# - Must contain at least one word after split().
#
# Test cases:
# 1) Normal: " The quick brown fox jumps over the lazy dog "
#    -> Count: 9, First: The, Last: dog, Shortest: fox/the, Longest: quick/brown/jumps
# 2) Border: "one" -> Count: 1, First/Last/Shortest/Longest: one
# 3) Error: "  " -> Error: sentence cannot be empty or contain only spaces

def analyze_sentence(sentence_input):
    """Analyzes a sentence for word statistics."""
    # 1. Normalization and Validation (Empty Check)
    cleaned_sentence = sentence_input.strip()
    if not cleaned_sentence:
        print("Error: sentence cannot be empty or contain only spaces")
        return

    # 2. Split and Validation (Word Count Check)
    # Filter out potential empty strings from split (though strip() helps)
    words = [word for word in cleaned_sentence.split() if word]

    if not words:
        print("Error: sentence must contain at least one valid word")
        return

    # 3. Calculations
    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]

    # Find shortest and longest word
    shortest_word = words[0]
    longest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    # 4. Output
    print(f"Word count: {word_count}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


print("\n--- Problem 4 Test Runs ---")
analyze_sentence(" The quick brown fox jumps over the lazy dog ") # Normal
analyze_sentence("one") # Border
analyze_sentence("  ") # Error: Empty
analyze_sentence("A B C") # Simple Case

# --------------------------------------------------
# Problem 5: Password strength classifier
# --------------------------------------------------

# Problem 5: Password Strength Classifier
# Description: Classifies a password as "weak", "medium", or "strong" based on length,
# and the presence of uppercase, lowercase, digits, and symbols.
#
# Rules:
# - STRONG_MIN_LENGTH = 8
# - Weak: Length < 8 OR lacks both upper/lower and digits/symbols.
# - Medium: Length >= 8 AND contains a mix of two out of three categories: (upper/lower), (digit), (symbol).
# - Strong: Length >= 8 AND contains at least one of each: uppercase, lowercase, digit, and symbol.
#
# Inputs:
# - password_input_raw (string; the password).
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
#
# Validations:
# - password_input_raw must not be empty.
#
# Test cases:
# 1) Normal: "P@sswOrd1" -> Strong
# 2) Border: "abcde123" -> Medium
# 3) Error: "short" -> Weak

STRONG_MIN_LENGTH = 8
SYMBOLS = "!@#$%^&*()-_+=[]{}|;:,.<>?/~`"

def classify_password_strength(password_input_raw):
    """Classifies a password's strength."""
    password_input = password_input_raw.strip()

    # 1. Validation: Not Empty
    if not password_input:
        print("Error: password cannot be empty")
        return

    # 2. Check for character types
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in SYMBOLS:
            has_symbol = True

    # 3. Length Check
    is_long_enough = len(password_input) >= STRONG_MIN_LENGTH

    # 4. Classification Logic
    if is_long_enough and has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    elif is_long_enough:
        # Check for Medium: A reasonable mix of types (e.g., at least two different non-symbol types, or symbols + one other)
        # Simplified rule: Medium if long enough and has at least two *distinct* type categories present
        type_count = sum([has_upper or has_lower, has_digit, has_symbol])
        if type_count >= 2:
            strength = "medium"
        else:
            strength = "weak"
    else: # Not long enough
        strength = "weak"

    # 5. Output
    print(f"Password strength: {strength}")


print("\n--- Problem 5 Test Runs ---")
classify_password_strength("P@sswOrd1") # Normal: Strong
classify_password_strength("abcde123") # Border: Medium (len=8, lower, digit)
classify_password_strength("short") # Error: Weak (len < 8)
classify_password_strength("LongButOnlyLetters") # Weak (len > 8, but no digit/symbol)
classify_password_strength("A1B2C3D4") # Medium (len=8, upper, digit, no lower/symbol)

# --------------------------------------------------
# Problem 6: Product label formatter (fixed-width text)
# --------------------------------------------------

# Problem 6: Product Label Formatter
# Description: Creates a fixed-width product label (exactly 30 characters) from a product name
# and price. The format is "Product: <NAME> | Price: $<PRICE>". It pads with spaces if shorter
# or truncates if longer.
#
# Inputs:
# - product_name_input (string).
# - price_value_input (string or number, converted to string for formatting).
#
# Outputs:
# - "Label: <exactly 30 characters>" (between quotes to show padding)
#
# Validations:
# - product_name_input not empty after strip().
# - price_value_input must be a number greater than 0.
#
# Test cases:
# 1) Normal: "Laptop" and 1200.5 -> Label: "Product: Laptop | Price: $1200.5"
# 2) Border: "A Very Long Product Name" and 9.99 -> Label: "Product: A Very Long Pro" (Truncated)
# 3) Error: "" and 10 -> Error: product name cannot be empty

LABEL_LENGTH = 30
PRICE_FORMAT = "{:.2f}"

def format_product_label(product_name_input, price_value_input):
    """Formats a product label to a fixed width of 30 characters."""
    product_name = product_name_input.strip()

    # 1. Validation: Not Empty Name
    if not product_name:
        print("Error: product name cannot be empty")
        return

    # 2. Validation: Price
    try:
        price_value = float(price_value_input)
        if price_value <= 0:
            print("Error: price must be a positive number")
            return
        price_str = PRICE_FORMAT.format(price_value)
    except ValueError:
        print("Error: price is not a valid number")
        return

    # 3. Create Base Label
    base_label = f"Product: {product_name} | Price: ${price_str}"

    # 4. Format to Fixed Length
    label_length = len(base_label)

    if label_length < LABEL_LENGTH:
        # Padding
        padding_spaces = " " * (LABEL_LENGTH - label_length)
        final_label = base_label + padding_spaces
    elif label_length > LABEL_LENGTH:
        # Truncating
        final_label = base_label[:LABEL_LENGTH]
    else:
        # Perfect match
        final_label = base_label

    # 5. Output
    print(f"Label: \"{final_label}\"")
    print(f"Length: {len(final_label)}")


print("\n--- Problem 6 Test Runs ---")
format_product_label("Laptop", 1200.5) # Normal: Padded (30)
format_product_label("A Very Long Product Name for Truncation Test", 9.99) # Border: Truncated (30)
format_product_label("Simple", 100) # Padded (30)
format_product_label("", 10) # Error: Empty name
format_product_label("Product", "zero") # Error: Invalid price

# --------------------------------------------------
# CONCLUSIONES
# --------------------------------------------------

# Conclusions:
# String manipulation is undeniably essential for handling data input and output in any
# application. Methods like lower(), strip(), and split() are fundamental tools; for instance,
# split() is ideal for tokenizing sentences, while join() efficiently reconstructs them.
# Normalizing text before comparison—typically with strip() to remove surrounding spaces and
# lower() for case-insensitivity—is critical to avoid bugs caused by inconsistent user input.
# The design of robust validations, checked before core processing logic, acts as a primary
# defense against data corruption and program errors. Lastly, understanding string
# immutability is key: operations like slicing or replacing a substring always yield a new
# string, preventing unintended side effects on the original variable.

# --------------------------------------------------
# REFERENCIAS
# --------------------------------------------------

# References:
# 1) Python documentation - Built-in Types: Text Sequence Type — str. Available at: [Link a la documentación oficial de Python sobre strings]
# 2) Real Python. (2023). Python String Formatting. Available at: [Link a un tutorial de Real Python sobre f-strings o format]
# 3) W3Schools. (2023). Python String Methods. Available at: [Link a W3Schools sobre métodos de string]
# 4) Lutz, M. (2013). Learning Python (5th ed.). O'Reilly Media. (O similar libro de programación)
# 5) Wikipedia. Palindrome. Available at: [Link a la entrada de Wikipedia sobre palíndromos para concepto]

# --------------------------------------------------
# Git Repository Clone Instruction
# --------------------------------------------------

# To download this project from the source repository, use the following command 
# in your terminal or command prompt:
#
# git clone https://github.com/ValdoGlz7/Python_Proyects
#
# This command will create a local copy of the repository contents.