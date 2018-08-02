class polygon:
    def __init__(self,no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputsides(self):
        self.sides = [float(input("Enter side " + str(i + 1)+":" )) for i in range(self.n)]
    
    def dispSides(self):
        for i in range(self.n):
            print("side is "+ self.sides[i])