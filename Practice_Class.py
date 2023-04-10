class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# create an object of the Person class
person1 = Person("John", 25)

# access the object's properties
print(person1.name)
print(person1.age)

# call the object's methods
person1.greet()