# Name: [Tu Nombre Completo]
# Student ID: [Tu Matrícula]
# Group: [Tu Grupo]

# --------------------------------------------------
# RESUMEN EJECUTIVO (Executive Summary)
# --------------------------------------------------

# Executive Summary:
# Python offers three fundamental collection types: list, tuple, and dict (dictionary).
# A list is an ordered, mutable collection (changeable size and content), suitable for items
# where order and modification are necessary. A tuple is also ordered, but crucially, it is
# immutable (cannot be changed after creation), making it ideal for fixed records like coordinates.
# A dictionary is an unordered collection of key-value pairs, providing fast lookup based on the key.
# This document covers six problems demonstrating the practical use of these structures.
# Topics include shopping list management (list append/search), calculating geometric
# properties (tuples for fixed points), product catalog lookups (dict access), student grade
# statistics (dict of lists), word frequency counting (list to dict conversion), and a simple
# CRUD contact book (dict operations). Each problem includes specific validations for input
# types, keys, and list emptiness.

# --------------------------------------------------
# PRINCIPIOS Y BUENAS PRÁCTICAS (Principles and Best Practices)
# --------------------------------------------------

# - List Usage: Use lists primarily when the need to add, remove, or reorder elements is frequent.
# - Tuple Usage: Use tuples for data that should remain constant throughout the program's execution,
#   such as coordinates, database records, or function return values that represent fixed entities.
# - Dictionary Usage: Use dictionaries for fast, efficient data retrieval by a unique identifier (key).
# - Iteration Safety: Avoid modifying a list (e.g., adding/removing elements) while iterating over it
#   with a standard 'for' loop, as this can lead to logical errors or skipping elements.
# - Descriptive Keys: Use clear, descriptive key names in dictionaries (e.g., "name", "price", "status")
#   to enhance code readability and maintainability.
# - Legible Code: Always write clean, readable code and ensure error messages are informative to the user.

# --------------------------------------------------
# PROBLEMAS
# --------------------------------------------------

# --- CONVENTION NOTES ---
# Variables: lower_snake_case
# Constants: UPPER_SNAKE_CASE
# Data Types: list, tuple, dict, int, float, bool
# Output Messages: English

# --------------------------------------------------
# Problem 1: Shopping list basics (list operations)
# --------------------------------------------------

# Problem 1: Shopping List Basics
# Description: Creates a list of shopping items, allows adding a new item, displays the total
# count, and checks for the existence of a specific item.
#
# Inputs:
# - initial_items_text (string; comma-separated items).
# - new_item (string; item to add).
# - search_item (string; item to search for).
#
# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <len_list>
# - "Found item:" true|false
# - "Error: initial items cannot be empty"
# - "Error: item to add cannot be empty"
#
# Validations:
# - initial_items_text not empty after strip().
# - new_item and search_item not empty after strip().
# - Items are created by splitting the initial text and stripping spaces from each element.
#
# Test cases:
# 1) Normal: Initial: "milk, bread", New: "cheese", Search: "milk" -> Found: true, Total: 3
# 2) Border: Initial: "one", New: "two", Search: "three" -> Found: false, Total: 2
# 3) Error: Initial: "", New: "x", Search: "y" -> Error: initial items cannot be empty

def run_shopping_list_basics(initial_items_text, new_item, search_item):
    """Manages a basic shopping list using list operations."""
    initial_text = initial_items_text.strip()
    new_item_clean = new_item.strip()
    search_item_clean = search_item.strip()

    # 1. Validation: Initial Items
    if not initial_text:
        print("Error: initial items cannot be empty")
        return

    # Create initial list
    # Use list comprehension to split by comma, strip spaces, and filter out empty strings
    shopping_list = [item.strip() for item in initial_text.split(',') if item.strip()]

    # 2. Validation: New Item
    if not new_item_clean:
        print("Error: item to add cannot be empty")
        # Proceed with search on existing list for demonstration
    else:
        # 3. Add new product
        shopping_list.append(new_item_clean)

    # 4. Search product
    is_in_list = search_item_clean in shopping_list

    # 5. Output
    print(f"Items list: {shopping_list}")
    print(f"Total items: {len(shopping_list)}")
    print(f"Found item: {str(is_in_list).lower()}")


print("\n--- Problem 1 Test Runs ---")
run_shopping_list_basics("milk, bread", "cheese", "milk") # Normal
run_shopping_list_basics("one", "two", "three") # Border
run_shopping_list_basics("", "x", "y") # Error: Empty initial
run_shopping_list_basics("apple,banana", "", "apple") # Error: Empty new item

# --------------------------------------------------
# Problem 2: Points and distances with tuples
# --------------------------------------------------

# Problem 2: Points and Distances with Tuples
# Description: Uses tuples to represent two 2D points (x, y) and calculates the Euclidean
# distance and the midpoint between them.
#
# Inputs:
# - x1, y1, x2, y2 (float; coordinates).
#
# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)
# - "Error: all coordinates must be valid numbers"
#
# Validations:
# - All four inputs must be convertible to float.
#
# Operaciones clave sugeridas:
# - Creation: point_a = (x1, y1)
# - Distance: ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# - Midpoint: ((x1 + x2)/2, (y1 + y2)/2)
#
# Test cases:
# 1) Normal: x1=1.0, y1=1.0, x2=4.0, y2=5.0 -> Distance: 5.0, Midpoint: (2.5, 3.0)
# 2) Border: x1=0.0, y1=0.0, x2=0.0, y2=0.0 -> Distance: 0.0, Midpoint: (0.0, 0.0)
# 3) Error: x1="invalid", y1=1.0, x2=2.0, y2=2.0 -> Error: all coordinates must be valid numbers

def run_point_calculations(x1_input, y1_input, x2_input, y2_input):
    """Calculates distance and midpoint between two points represented by tuples."""
    import math

    try:
        # 1. Validation and Conversion
        x1 = float(x1_input)
        y1 = float(y1_input)
        x2 = float(x2_input)
        y2 = float(y2_input)
    except ValueError:
        print("Error: all coordinates must be valid numbers")
        return

    # 2. Create Tuples
    point_a = (x1, y1)
    point_b = (x2, y2)

    # 3. Calculate Distance
    # Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # 4. Calculate Midpoint (New Tuple)
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    midpoint = (midpoint_x, midpoint_y)

    # 5. Output (rounding for cleaner display)
    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {round(distance, 2)}")
    print(f"Midpoint: {midpoint}")


print("\n--- Problem 2 Test Runs ---")
run_point_calculations(1.0, 1.0, 4.0, 5.0) # Normal (3, 4, 5 triangle)
run_point_calculations(0.0, 0.0, 0.0, 0.0) # Border (same point)
run_point_calculations("invalid", 1.0, 2.0, 2.0) # Error (invalid input type)

# --------------------------------------------------
# Problem 3: Product catalog with dictionary
# --------------------------------------------------

# Problem 3: Product Catalog with Dictionary
# Description: Manages a product catalog (name: price dict), reads a purchase, and calculates
# the total cost if the product exists.
#
# Inputs:
# - product_name (string; name of product).
# - quantity_input (string; quantity to buy).
#
# Outputs:
# - "Unit price:" <unit_price>
# - "Quantity:" <quantity>
# - "Total:" <total_price> (formatted to two decimal places)
# - "Error: product not found"
# - "Error: quantity must be a positive integer"
#
# Validations:
# - quantity must be an integer > 0.
# - product_name not empty after strip().
# - Check if product_name exists as a key in the dictionary.
#
# Test cases:
# 1) Normal: Product: "laptop", Quantity: 2 -> Total: 2000.00
# 2) Border: Product: "keyboard", Quantity: 1 -> Total: 50.00
# 3) Error: Product: "monitor", Quantity: 1 -> Error: product not found

PRODUCT_PRICES = {
    "laptop": 1000.00,
    "mouse": 15.50,
    "keyboard": 50.00,
    "webcam": 25.99
}

def run_product_catalog(product_name_input, quantity_input):
    """Calculates total price from a catalog dictionary."""
    product_name = product_name_input.strip()

    # 1. Validation: Product Name
    if not product_name:
        print("Error: product name cannot be empty")
        return

    # 2. Validation: Quantity
    try:
        quantity = int(quantity_input)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("Error: quantity must be a positive integer")
        return

    # 3. Check for Product Existence
    unit_price = PRODUCT_PRICES.get(product_name.lower()) # Use lower() for robustness
    if unit_price is None:
        print("Error: product not found")
        return

    # 4. Calculation and Output
    total_price = unit_price * quantity

    print(f"Unit price: {unit_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total_price:.2f}")


print("\n--- Problem 3 Test Runs ---")
run_product_catalog("laptop", 2) # Normal
run_product_catalog("keyboard", 1) # Border
run_product_catalog("monitor", 1) # Error: Not found
run_product_catalog("mouse", "zero") # Error: Invalid quantity

# --------------------------------------------------
# Problem 4: Student grades with dict and list
# --------------------------------------------------

# Problem 4: Student Grades with Dict and List
# Description: Uses a dictionary where the value is a list of grades to calculate a student's
# average and check if they passed (average >= 70.0).
#
# Inputs:
# - student_name_input (string; student name).
#
# Outputs:
# - "Grades:" <grades_list>
# - "Average:" <average> (rounded)
# - "Passed:" true|false
# - "Error: student not found"
# - "Error: no grades available"
#
# Validations:
# - student_name not empty after strip().
# - Check if student_name is a key in the dictionary.
# - The list of grades must not be empty.
#
# Test cases:
# 1) Normal: Student: "Alice" -> Grades: [90, 85], Average: 87.5, Passed: true
# 2) Border: Student: "Charlie" -> Grades: [70], Average: 70.0, Passed: true
# 3) Error: Student: "David" -> Error: student not found

STUDENT_GRADES = {
    "alice": [90.0, 85.0, 95.0],
    "bob": [65.0, 70.0, 68.0],
    "charlie": [70.0],
    "diana": [] # Empty list for edge case validation
}
PASSING_GRADE = 70.0

def calculate_student_average(student_name_input):
    """Calculates the average grade for a student using a dictionary of lists."""
    student_name = student_name_input.strip().lower()

    # 1. Validation: Not Empty and Key Check
    if not student_name:
        print("Error: student name cannot be empty")
        return
    
    if student_name not in STUDENT_GRADES:
        print("Error: student not found")
        return

    grades_list = STUDENT_GRADES[student_name]

    # 2. Validation: Empty Grades List
    if not grades_list:
        print(f"Grades: {grades_list}")
        print("Error: no grades available")
        return

    # 3. Calculation
    average = sum(grades_list) / len(grades_list)
    is_passed = average >= PASSING_GRADE

    # 4. Output
    print(f"Grades: {grades_list}")
    print(f"Average: {round(average, 1)}")
    print(f"Passed: {str(is_passed).lower()}")


print("\n--- Problem 4 Test Runs ---")
calculate_student_average("Alice") # Normal
calculate_student_average("Charlie") # Border: Exact passing grade
calculate_student_average("David") # Error: Not found
calculate_student_average("Diana") # Error: Empty grades list

# --------------------------------------------------
# Problem 5: Word frequency counter (list + dict)
# --------------------------------------------------

# Problem 5: Word Frequency Counter
# Description: Counts the frequency of each word in a sentence, ignoring case, and finds the
# most frequent word. Uses a list to hold split words and a dictionary for frequencies.
#
# Inputs:
# - sentence_input (string; the sentence).
#
# Outputs:
# - "Words list:" <words_list>
# - "Frequencies:" <freq_dict>
# - "Most common word:" <word>
# - "Error: sentence cannot be empty or contain only punctuation/spaces"
#
# Validations:
# - sentence not empty after strip().
# - The resulting list of words must not be empty.
# - Simple punctuation removal for cleaner words (replace(',', '').replace('.', '') etc.).
#
# Test cases:
# 1) Normal: "The quick brown fox jumps over the quick fox" -> quick/fox: 2
# 2) Border: "one word" -> one: 1, word: 1
# 3) Error: "  " -> Error: sentence cannot be empty...

PUNCTUATION_TO_REMOVE = ",.:;!?"

def count_word_frequency(sentence_input):
    """Counts word frequencies in a sentence and finds the most common word."""
    cleaned_sentence = sentence_input.strip()

    # 1. Validation: Not Empty
    if not cleaned_sentence:
        print("Error: sentence cannot be empty or contain only punctuation/spaces")
        return

    # 2. Normalization and Splitting (to List)
    processed_text = cleaned_sentence.lower()
    for punc in PUNCTUATION_TO_REMOVE:
        processed_text = processed_text.replace(punc, "")

    words_list = [word for word in processed_text.split() if word]

    # 3. Validation: Empty Words List
    if not words_list:
        print("Error: sentence cannot be empty or contain only punctuation/spaces")
        return

    # 4. Build Frequency Dictionary
    frequency_dict = {}
    for word in words_list:
        # Dictionary pattern: check existence, update/create entry
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    # 5. Find Most Common Word
    most_common_word = ""
    max_frequency = 0

    # Iterating over dictionary items for clarity and efficiency
    for word, count in frequency_dict.items():
        if count > max_frequency:
            max_frequency = count
            most_common_word = word

    # 6. Output
    print(f"Words list: {words_list}")
    print(f"Frequencies: {frequency_dict}")
    print(f"Most common word: {most_common_word}")


print("\n--- Problem 5 Test Runs ---")
count_word_frequency("The quick brown fox jumps over the quick fox.") # Normal
count_word_frequency("one word") # Border
count_word_frequency("  ") # Error: Empty
count_word_frequency("word, word!") # Test punctuation removal

# --------------------------------------------------
# Problem 6: Simple contact book (dictionary CRUD)
# --------------------------------------------------

# Problem 6: Simple Contact Book (Dictionary CRUD)
# Description: Implements a basic CRUD (Create, Read, Update, Delete) system for a contact
# book using a dictionary (name: phone).
#
# Inputs:
# - action_text (string; "ADD", "SEARCH" or "DELETE").
# - name_input (string; contact name).
# - phone_input (string; phone number, only for "ADD").
#
# Outputs:
# - For "ADD": "Contact saved:" name, phone
# - For "SEARCH": If exists: "Phone:" <phone>, If not: "Error: contact not found"
# - For "DELETE": If exists: "Contact deleted:" name, If not: "Error: contact not found"
# - "Error: invalid action"
# - "Error: name cannot be empty"
#
# Validations:
# - action_text must be "ADD", "SEARCH", or "DELETE" (case-insensitive check).
# - name not empty after strip().
# - For "ADD": phone not empty after strip().
#
# Test cases:
# 1) Normal: Action: "ADD", Name: "Sam", Phone: "9876543210" -> Contact saved
# 2) Border: Action: "SEARCH", Name: "Sam" (from step 1) -> Phone: 9876543210
# 3) Error: Action: "DELETE", Name: "Nonexistent" -> Error: contact not found

CONTACT_BOOK = {
    "alice": "1234567890",
    "bob": "0987654321",
}

def manage_contact_book(action_text, name_input, phone_input=""):
    """Performs ADD, SEARCH, or DELETE operations on the contact book dictionary."""
    action = action_text.strip().upper()
    name = name_input.strip().lower()
    phone = phone_input.strip()

    # 1. Validation: Action Type
    VALID_ACTIONS = ("ADD", "SEARCH", "DELETE")
    if action not in VALID_ACTIONS:
        print("Error: invalid action. Use ADD, SEARCH, or DELETE.")
        return

    # 2. Validation: Name
    if not name:
        print("Error: name cannot be empty")
        return

    # 3. Handle Actions (Dictionary CRUD)
    if action == "ADD":
        if not phone:
            print("Error: phone number cannot be empty for ADD action")
            return
        # Add or Update
        CONTACT_BOOK[name] = phone
        print(f"Contact saved: {name.title()}, {phone}")
    
    elif action == "SEARCH":
        # Search (Read)
        if name in CONTACT_BOOK:
            print(f"Phone: {CONTACT_BOOK[name]}")
        else:
            print("Error: contact not found")
            
    elif action == "DELETE":
        # Delete (using pop for safe removal and existence check)
        try:
            CONTACT_BOOK.pop(name)
            print(f"Contact deleted: {name.title()}")
        except KeyError:
            print("Error: contact not found")


print("\n--- Problem 6 Test Runs ---")
manage_contact_book("ADD", "Sam", "9876543210") # Normal: ADD
manage_contact_book("SEARCH", "Sam") # Border: SEARCH existing
manage_contact_book("DELETE", "Nonexistent") # Error: DELETE non-existent
manage_contact_book("search", "Alice") # Test case-insensitivity
manage_contact_book("ADD", "Sam", "1112223333") # Test update
manage_contact_book("DELETE", "Sam") # Test final delete

# --------------------------------------------------
# CONCLUSIONES
# --------------------------------------------------

# Conclusions:
# Choosing the right collection type is essential for efficient programming. Lists are best suited
# for dynamic data collections requiring frequent modification (addition/deletion), while tuples
# provide integrity for fixed data structures, preventing accidental modification. Dictionaries are
# paramount for rapid data retrieval, making them superior to lists for lookups based on a key (like
# a name or ID). The common pattern of using a dictionary with lists as values (e.g., student grades)
# is a powerful way to organize complex data, linking a unique identifier to a sequence of related
# records. This practice facilitates quick access to all related data points for a single entity,
# such as a student's entire history of grades.

# --------------------------------------------------
# REFERENCIAS
# --------------------------------------------------

# References:
# 1) Python documentation - Built-in Types: list, tuple, dict. Available at: [Link a la documentación oficial de Python sobre list, tuple, dict]
# 2) GeeksforGeeks. (2023). Python Data Structures - List, Tuple, Dictionary. Available at: [Link a un tutorial sobre estructuras de datos básicas]
# 3) Real Python. (2023). Python Dictionaries. Available at: [Link a un tutorial de Real Python sobre diccionarios]
# 4) Severance, C. (2016). Python for Everybody: Exploring Data in Python 3. (O similar libro de programación)
# 5) Stack Overflow (for best practices and specific methods).

# --------------------------------------------------
# Git Repository Clone Instruction
# --------------------------------------------------

# To download this project from the source repository, use the following command 
# in your terminal or command prompt:
#
# git clone https://github.com/ValdoGlz7/Python_Proyects
#
# This command will create a local copy of the repository contents.