# Name: Oswaldo González Charles
# Student ID: 2530088
# Group: IM 1-1

# --------------------------------------------------
# Executive Summary
# --------------------------------------------------

# Executive Summary:
# CRUD stands for Create, Read, Update, and Delete—the four basic operations necessary
# for persistent data storage management. For this in-memory inventory manager, I chose
# **Option A: a dictionary** where the key is the 'item_id' (int) and the value is another
# dictionary containing "name" (str), "price" (float), and "quantity" (int). This structure
# was chosen because it provides **O(1) average time complexity** for R-U-D operations, 
# relying on fast key lookup. The program uses dedicated **functions** (e.g., create_item)
# for each operation, promoting modularity and code reuse. The main loop presents a menu
# to the user, delegates all business logic to these functions, and displays the result.

# --------------------------------------------------
# Conventions (Naming and Output in English)
# --------------------------------------------------

# Everything in English
# Naming Style: lower_snake_case for functions/variables, UPPER_SNAKE_CASE for constants.
# Data Structure Chosen: Dictionary (key: item_id, value: item_details_dict)

# Global Data Structure (In-memory storage)
INVENTORY_DATA = {}

# Constants
EXIT_OPTION = 0
MIN_ID = 1

# --------------------------------------------------
# Utility Functions
# --------------------------------------------------

def validate_item_id(item_id_input):
    """Validates if the ID input is a positive integer."""
    try:
        item_id = int(item_id_input)
        if item_id < MIN_ID:
            print(f"Error: ID must be a positive integer (>= {MIN_ID})")
            return None
        return item_id
    except ValueError:
        print("Error: ID must be an integer")
        return None

def validate_numeric_field(field_input, field_name, min_value=0.0):
    """Validates if a numeric field input is a number greater than or equal to min_value."""
    try:
        if field_name == "quantity":
            value = int(field_input)
        else:
            value = float(field_input)
            
        if value < min_value:
            print(f"Error: {field_name} must be greater than or equal to {min_value}")
            return None
        return value
    except ValueError:
        print(f"Error: {field_name} must be a valid number")
        return None

# --------------------------------------------------
# Template for Documenting the Problem
# --------------------------------------------------

# Problem: In-memory CRUD manager with functions  

# Description: This program implements a simple CRUD (Create, Read, Update, Delete) system 
# for inventory items stored in an in-memory dictionary. It uses distinct functions for each 
# CRUD operation and a text-based menu for user interaction.

# Inputs:
# - User menu options (int).
# - For CREATE/UPDATE: item_id (int), name (string), price (float), quantity (int).
# - For READ/DELETE: item_id (int).

# Outputs:
# - Messages indicating the result of each operation:
#   - "Item created", "Item updated", "Item deleted", "Item not found", "Items list:", etc.
# - "Error: invalid input" for validation failures.

# Validations:
# - Menu option must be valid (0 to 5).
# - item_id must be convertible to a positive integer.
# - Numeric fields (price, quantity) must be convertible to numbers and greater than or equal to 0.
# - In CREATE: Duplicates are NOT allowed. If the ID exists, the operation fails.
# - In READ/UPDATE/DELETE: If the ID does not exist, show "Item not found".

# Test cases:
# 1) Normal: create(1, "Laptop", 1200.0, 5) -> read(1) -> update(1, "Laptop Pro", 1500.0, 3) -> delete(1) → All successful messages.
# 2) Border: create(2, "Mouse", 0.0, 0) (valid minimal data) -> read(2).
# 3) Error: create(1, "Monitor", 500.0, 1) when item 1 already exists. Then, update(99, "X", 1, 1). -> Expected messages: "Error: ID already exists", "Item not found".

# --------------------------------------------------
# Unique Problem: CRUD with Functions
# --------------------------------------------------

# --- CREATE Function ---
def create_item(data_structure, item_id, name, price, quantity):
    """
    Adds a new item to the inventory.
    Returns True if successful, False otherwise (e.g., ID already exists).
    """
    if item_id in data_structure:
        print("Error: ID already exists")
        return False

    if not name.strip():
        print("Error: name cannot be empty")
        return False

    data_structure[item_id] = {
        "name": name.strip(),
        "price": price,
        "quantity": quantity
    }
    return True

# --- READ Function ---
def read_item(data_structure, item_id):
    """
    Reads an item by its ID.
    Returns the item dictionary if found, None otherwise.
    """
    return data_structure.get(item_id)

# --- UPDATE Function ---
def update_item(data_structure, item_id, new_name, new_price, new_quantity):
    """
    Updates the details of an existing item.
    Returns True if successful, False if item not found.
    """
    if item_id not in data_structure:
        print("Item not found")
        return False
    
    if not new_name.strip():
        print("Error: name cannot be empty")
        return False

    data_structure[item_id]["name"] = new_name.strip()
    data_structure[item_id]["price"] = new_price
    data_structure[item_id]["quantity"] = new_quantity
    return True

# --- DELETE Function ---
def delete_item(data_structure, item_id):
    """
    Removes an item from the inventory by its ID.
    Returns True if successful, False if item not found.
    """
    if item_id in data_structure:
        del data_structure[item_id]
        return True
    else:
        print("Item not found")
        return False

# --- LIST Function ---
def list_items(data_structure):
    """Prints all items currently in the inventory."""
    print("\n--- Items List ---")
    if not data_structure:
        print("The inventory is empty.")
        return

    # Print header
    print(f"{'ID':<5} | {'Name':<20} | {'Price':<10} | {'Quantity':<8}")
    print("-" * 47)
    
    # Iterate and print items
    for item_id, data in data_structure.items():
        name = data['name'][:18] + '...' if len(data['name']) > 18 else data['name']
        print(f"{item_id:<5} | {name:<20} | {data['price']:<10.2f} | {data['quantity']:<8}")
    print("--------------------")

# --------------------------------------------------
# Main Loop and Menu
# --------------------------------------------------

def display_menu():
    """Prints the main menu options."""
    print("\n--- Inventory Manager Menu ---")
    print("1) Create item")
    print("2) Read item by ID")
    print("3) Update item by ID")
    print("4) Delete item by ID")
    print("5) List all items")
    print(f"{EXIT_OPTION}) Exit")
    print("------------------------------")

def get_item_input(prompt_id=True, prompt_details=True):
    """Handles common input and validation for item details."""
    validated_id = None
    validated_price = None
    validated_quantity = None
    name = None

    if prompt_id:
        item_id_input = input("Enter Item ID: ").strip()
        validated_id = validate_item_id(item_id_input)
        if validated_id is None:
            return None, None, None, None

    if prompt_details:
        name = input("Enter Item Name: ").strip()
        
        price_input = input("Enter Item Price (float, >= 0.0): ").strip()
        validated_price = validate_numeric_field(price_input, "price", 0.0)
        if validated_price is None:
            return None, None, None, None

        quantity_input = input("Enter Item Quantity (int, >= 0): ").strip()
        validated_quantity = validate_numeric_field(quantity_input, "quantity", 0)
        if validated_quantity is None:
            return None, None, None, None
            
    return validated_id, name, validated_price, validated_quantity

def main_crud_manager():
    """Main function to run the CRUD manager loop."""
    
    # Pre-populate with a test case for Border 2 (minimal valid data)
    INVENTORY_DATA[2] = {"name": "Mouse", "price": 0.0, "quantity": 0} 

    while True:
        display_menu()
        option_input = input("Enter option: ").strip()
        
        try:
            option = int(option_input)
        except ValueError:
            print("Error: invalid input. Please enter a number from the menu.")
            continue

        if option == EXIT_OPTION:
            print("Exiting application. Goodbye!")
            break
        
        # --- Option 1: CREATE ---
        elif option == 1:
            item_id, name, price, quantity = get_item_input(prompt_id=True, prompt_details=True)
            if item_id is not None and name is not None:
                if create_item(INVENTORY_DATA, item_id, name, price, quantity):
                    print("Item created")
                # Error message handled inside create_item

        # --- Option 2: READ ---
        elif option == 2:
            item_id_input = input("Enter Item ID to Read: ").strip()
            item_id = validate_item_id(item_id_input)
            
            if item_id is not None:
                item = read_item(INVENTORY_DATA, item_id)
                if item:
                    print(f"\n--- Item Found (ID: {item_id}) ---")
                    print(f"Name: {item['name']}")
                    print(f"Price: {item['price']:.2f}")
                    print(f"Quantity: {item['quantity']}")
                    print("------------------------------")
                else:
                    print("Item not found")

        # --- Option 3: UPDATE ---
        elif option == 3:
            item_id, new_name, new_price, new_quantity = get_item_input(prompt_id=True, prompt_details=True)
            if item_id is not None and new_name is not None:
                if update_item(INVENTORY_DATA, item_id, new_name, new_price, new_quantity):
                    print("Item updated")
                # Error message handled inside update_item

        # --- Option 4: DELETE ---
        elif option == 4:
            item_id_input = input("Enter Item ID to Delete: ").strip()
            item_id = validate_item_id(item_id_input)
            
            if item_id is not None:
                if delete_item(INVENTORY_DATA, item_id):
                    print("Item deleted")
                # Error message handled inside delete_item
        
        # --- Option 5: LIST ---
        elif option == 5:
            list_items(INVENTORY_DATA)

        else:
            print("Error: invalid option. Please choose an option from the menu (0-5).")

if __name__ == "__main__":
    main_crud_manager()

# --------------------------------------------------
# Conclusions
# --------------------------------------------------

# Conclusions:
# Using functions (create_item, read_item, etc.) significantly simplified the CRUD implementation by separating concerns. The main loop only handles user interaction and delegation, making it clean and readable. Choosing the dictionary structure was advantageous because item IDs provide a natural, unique key, enabling **O(1)** average-time lookups for reading, updating, and deleting items, which is highly efficient. The primary challenge was input validation, especially ensuring correct type conversion (string to int/float) and range checks (price >= 0). This was solved by centralizing validation in helper functions. This in-memory model could be extended to a larger system by simply replacing the global `INVENTORY_DATA` dictionary with functions that read from and write to a JSON file or a SQL database.

# --------------------------------------------------
# References
# --------------------------------------------------

# Python Software Foundation. “Built-in Types – Mapping Types — dict.”:
# https://docs.python.org/3/library/stdtypes.html#dict
# Python Software Foundation. “Defining Functions.”:
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# GeeksforGeeks. “CRUD Operations in Python.”:
# https://www.geeksforgeeks.org/crud-operations-in-python/

# --------------------------------------------------
# Git Repository Clone Instruction
# --------------------------------------------------

# To download this project from the source repository, use the following command 
# in your terminal or command prompt:
#
# git clone https://github.com/ValdoGlz7/Python_Proyects
#
# This command will create a local copy of the repository contents.