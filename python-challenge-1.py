# Create an empty list to store customer orders
orders = []

# Define the menu with item names and prices
menu_items = {
    1: {"Item name": "Apple", "Price": 0.49},
    2: {"Item name": "Tea - Thai iced", "Price": 3.99},
    3: {"Item name": "Fried banana", "Price": 4.49}
}

# Set a flag to allow continuous ordering
place_order = True

# Start the ordering loop
while place_order:
    # Print the menu
    print("\nMenu:")
    for key, item in menu_items.items():
        print(f"{key}. {item['Item name']} - ${item['Price']:.2f}")

    # Prompt customer for menu selection
    menu_selection = input("Please enter the number of the item you would like to order: ")

    # Validate that input is a number and is in menu keys
    if not menu_selection.isdigit() or int(menu_selection) not in menu_items:
        print("Invalid selection. Please try again.")
        continue  # Go back to the start of the loop if input is invalid

    # Convert to integer after validation
    menu_selection = int(menu_selection)

    # Get the item name and price from the dictionary
    item_name = menu_items[menu_selection]["Item name"]
    price = menu_items[menu_selection]["Price"]

    # Ask for quantity, default to 1 if invalid
    quantity = input(f"How many {item_name}s would you like? (default is 1): ")
    if not quantity.isdigit():
        quantity = 1
    else:
        quantity = int(quantity)

    # Append the order to the list as a dictionary
    orders.append({
        "Item name": item_name,
        "Price": price,
        "Quantity": quantity
    })

    # Ask if the customer wants to continue ordering
    continue_order = input("Would you like to order another item? (y/n): ").lower()

    match continue_order:
        case 'y':
            continue  # Continue the loop for more orders
        case 'n':
            print("Thank you for your order.")
            place_order = False  # Exit the loop
        case _:
            print("Invalid input. Please enter 'y' or 'n'.")

# Print the order receipt
print("\nReceipt:")
print(f"{'Item name':<20} | {'Price':<8} | {'Quantity':<8}")
print("-" * 40)

total_price = 0

# Loop through each order in the orders list and print the details
for order in orders:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]

    print(f"{item_name:<20} | ${price:<8.2f} | {quantity:<8}")
    total_price += price * quantity

# Print total price
print("-" * 40)
print(f"Total: ${total_price:.2f}")
