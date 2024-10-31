# Basic Inventory Management System
inventory = {}

def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"Added {quantity} of {item_name}. Total: {inventory[item_name]}")

def remove_item(item_name, quantity):
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            print(f"Removed {quantity} of {item_name}. Remaining: {inventory[item_name]}")
            if inventory[item_name] == 0:
                del inventory[item_name]  # Remove the item if quantity is zero
                print(f"{item_name} is now out of stock.")
        else:
            print(f"Error: Only {inventory[item_name]} of {item_name} available.")
    else:
        print(f"Error: {item_name} is not in inventory.")

def view_inventory():
    print("\nCurrent Inventory:")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item, qty in inventory.items():
            print(f"{item}: {qty}")

def main():
    while True:
        print("\nInventory Management Options:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Exit")
        
        choice = input("Select an option (1, 2, 3, or 4): ")
        
        if choice == '1':
            item_name = input("Enter the item name to add: ")
            quantity = int(input("Enter the quantity to add: "))
            add_item(item_name, quantity)
        
        elif choice == '2':
            item_name = input("Enter the item name to remove: ")
            quantity = int(input("Enter the quantity to remove: "))
            remove_item(item_name, quantity)
        
        elif choice == '3':
            view_inventory()
        
        elif choice == '4':
            print("Exiting the Inventory Management System.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the main function to start the inventory management system
main()
