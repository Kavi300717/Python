import random

def generate_username(full_name):
    part = full_name.split()
    initials = ''.join([part[0] for part in part])

    random_number = random.randint(100, 999)
    username = initials.lower() + str(random_number)
    return username

full_name = input("Enter your name :")
print("Generate Username :", generate_username(full_name))
