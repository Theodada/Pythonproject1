class Fruit:
    def __init__(self, name, colour, shape, ripe):
        self.name = name
        self.colour = colour
        self.shape = shape
        self.ripe = ripe

    def __str__(self):
        return f'{self.name} with a colour {self.colour}'

    def eatfruit(self):
        print("is the fruit ripe =  ")
        if True:
            print("Eat fruit")
        else:
            print("Fruit not ripe")

mango = fruit("mango", "yellow", "oval", True)
print(mango.ripe)