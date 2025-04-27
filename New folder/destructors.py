class Employee:

    def __init__(self):
        print('Employee created.')

    def __del__(self):
        print('Destructor called, employee deleted.')

# obj = Employee()
# del obj

class Employee1:
    def __init__(self):
        print('Employee created')

    def __del__(self):
        print("Destructor called")

    def created_obj():
        print('Making Object....')
        obj = Employee1()
        print('function end...')
        return obj

print('Calling created_obj() function...')
obj = Employee1.created_obj()
print('Program end')