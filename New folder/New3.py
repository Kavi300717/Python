class Addition:
    first = 0
    second = 0
    answer = 0

    def __init__(self, f, s):
        self.first = f
        self.second = s


    def display(self):
        print("First number = " +str(self.first))
        print("Second number = " +str(self.second))
        print("Addition of two number = " +str(self.answer))

    def calculated(self):
        self.answer = self.first + self.second

obj = Addition(125, 325)
obj.display()
obj.calculated()
