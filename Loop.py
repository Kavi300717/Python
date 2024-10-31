inventry = {}

def add_item(item_name, quantity):
    if item_name in inventry:
        inventry[item_name] += quantity
    else:
        inventry[item_name] = quantity
    print(f"Added {quantity} of {item_name} in Stock. Total : {inventry[item_name]}")

def remove_item(item_name, quantity):
    if item_name in inventry:
        if inventry[item_name] >= quantity:
            inventry[item_name] -= quantity
            print(f"Removed {quantity} of {item_name} from stock. Balance Stock : {inventry[item_name]}")
            if inventry[item_name] == 0:
                del inventry[item_name]
                print(f"{item_name} is out of stock.")
        else:
            print(f"Error : Only {inventry[item_name]} of {item_name} available.")
    else:
        print(f"Error : {item_name} not in inventry.")

def view_inventry():
    print("\n Current Inventry:")
    if not inventry:
        print("Inventry is empty")
    else:
        for item, qty in inventry.items():
            print(f"{item} : {qty}")


def main():
    while True:
        print("\nStock Management Options : ")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventry")
        print("4. Exit")

        choice = input("Select an option (1, 2, 3, 4):")

        if choice == '1':
            item_name = input("Enter the product name : ")
            quantity = input("Enter the quantity : ")
            add_item(item_name, quantity)

        elif choice == '2':
            item_name = input("Enter the product name you want to remove : ")
            quantity = input("Enter the quantity that you want to remove : ")
            remove_item(item_name, quantity)

        elif choice == '3':
            view_inventry()

        elif choice == '4':
            print("Exiting the Stock Management System")
            break
        
        else:
            print("Invalid choice. Please choose again")

main()
            
                
