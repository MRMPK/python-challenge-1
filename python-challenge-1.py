# Initialize menu_items dictionary
menu_items = {
    1: {"Item name": "Apple", "Price": 0.49},
    2: {"Item name": "Tea - Thai iced", "Price": 3.99},
    3: {"Item name": "Fried banana", "Price": 4.49}
}

# Initialize an empty order list
order_list = []

# Function to display the menu
def display_menu():
    print("Menu:")
    for key, value in menu_items.items():
        print(f"{key}. {value['Item name']} - ${value['Price']:.2f}")

# Function to handle user input for ordering
def get_order():
    while True:
        display_menu()

        # Prompt for menu selection
        menu_selection = input("Please enter the number of the item you want to order: ")

        # Simple validation without too much detail (will pass non-integer strings)
        try:
            menu_selection = int(menu_selection)
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        
        # Check if menu_selection is in menu_items (no detailed feedback)
        if menu_selection not in menu_items:
            print("Error: Invalid item selection.")
            continue

        # Get the item name and price
        selected_item = menu_items[menu_selection]["Item name"]
        item_price = menu_items[menu_selection]["Price"]

        # Prompt for quantity but not enforcing valid input (a small vulnerability)
        quantity_input = input(f"How many {selected_item}(s) would you like to order? (Defaults to 1 if invalid): ")

        # Simple validation for quantity
        try:
            quantity = int(quantity_input)
        except ValueError:
            quantity = 1
            print("Invalid input. Defaulting quantity to 1.")

        # Append the order to the list
        order_list.append({
            "Item name": selected_item,
            "Price": item_price,
            "Quantity": quantity
        })

        # Ask if the customer wants to continue ordering (without proper handling for uppercase Y/N)
        continue_order = input("Would you like to order another item? (y/n): ")

        match continue_order.lower():
            case 'y':
                pass  # Continue ordering
            case 'n':
                print("Thank you for your order.")
                return
            case _:
                print("Invalid input. Assuming you don't want to order more.")
                return

# Function to print receipt
def print_receipt():
    print("\nOrder Receipt")
    print("--------------------------|--------|----------")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")
    
    # No detailed calculation of spacing
    for order in order_list:
        item_name = order["Item name"]
        price = order["Price"]
        quantity = order["Quantity"]

        print(f"{item_name: <26} | ${price:.2f} | {quantity}")

    # No list comprehension for calculating total price (basic loop instead)
    total_price = 0
    for order in order_list:
        total_price += order["Price"] * order["Quantity"]

    print("--------------------------|--------|----------")
    print(f"Total price: ${total_price:.2f}")

# Main program
get_order()
print_receipt()
