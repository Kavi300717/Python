#Crating a contact list 

contacts = {}

while True:
    print("\nContact book App")
    print("1. Create contact")
    print("2. View Contact")
    print("3. Update number")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit")

    choice = input('Enter your choice :')

    if choice == '1':
        name = input("Enter your name :")
        if name in contacts:
            print(f'Contact name{name} already exists')
        else:
            age = input("Enter age = ")
            email = input("Enter your email = ")
            mobile = input("enter your mobile number = ")
            contacts[name] = {'age':int(age),'email':email, 'mobile':mobile}
            print(f'Contact name {name} has been created successfully!')

    elif choice == '2':
        name = input("Enter name to view =")
        if name in contacts:
            contacts = contacts[name]
            print(f'Name:{name}, age:{age}, mobile number:{mobile}')
        else:
            print('Contact not found!')

    elif choice == '3':
        name = input('Enter name to update = ')
        if name in contacts:
            age = input('Enter updated age = ')
            email = input('Enter updated email =')
            mobile = input('Enter updated mobile number = ')
            contacts[name] = {'age':int(age),'email':email, 'mobile':mobile}
        else:
            print("Contact not found3!")

    elif choice == '4':
        name = input('Enter contact name to delete =')
        if name in contacts:
            del contacts[name]
            print(f'Contact name dleted successfully!')
        else:
            print('Contact not found')

    elif choice == '5':
        search_name = input("Enter contact name to search = ")
        found = False
        for name, contaact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'found- Name:{name}, Age:{age}, mobile Number:{mobile}, Email:{email}')
                found = True
        if not found:
            print('No contact found with that name!')

    elif choice == '6':
        print(f'Total contacts in your book : {len(contacts)}')

    elif choice == '7':
        print('Good bye closing the program')
        break

    else:
        print('Invalid Syntax!')
