# Create a function which wil call it 
def adventure_game():
    #Giving the start game instructions
    print("Welcome to sentence adventure game")
    print("You will find your self in crossroads in the dense forest.")

    #Presenting the choice to the player
    print("1. Enter the dark cave.")
    print("2. Follow the path through the forest.")

    choice1 = input("What do you want to do? (1 or 2):")

    #Select the choice according to the player
    if choice1 == '1':
        print("\nYou choose to enter the dark cave.Inside, you find a treasure.")
        print("1. Open the chest.")
        print("2. Leave the cave.")

        choice2 = input("What do you want to do? (1 or 2):")

        if choice2 == '1':
            print("\nYou choose to open the chest. Congratulation! You found a valuable gem.")
        elif choice2 == '2':
            print("\nYou choose to leave the cave. As you eait, the cave entrance collapses behind you.")
        else:
            print("\nInvalid choice. The adventure ends here.")
    
    elif choice1 == '2':
        print("\nYou chose to follow the path through the forest. The path splits into two directions.")
        print("1. Take the left path.")
        print("2. Take the right path.")

        choice2 == input("What do you want to do? (1 or 2):")

        if choice2 == '1':
            print("\nYou chose the left path. After a short walk, you find a beautiful clearing with hidden water.")
        elif choice2 == '2':
            print("\nYou chose the right path. Unfortunately, it leads to dead end.")
        else:
            print("\nInvalid choice. The adventure ends here.")

    else:
        print("\n Invalid choice. The adventure ends here.")

adventure_game()