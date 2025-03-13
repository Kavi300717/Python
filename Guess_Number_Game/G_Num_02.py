import random
secret_number = random.randint(1,100)

def guess_number():
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too Low! try again.")

        guess_number()

    elif guess > secret_number:
        print("Too high! Try again.")

        guess_number()

    else:
        print("Correct! You guessed the number.")

guess_number()
