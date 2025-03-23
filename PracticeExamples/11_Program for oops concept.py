class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Charlie", 22)

# Displaying information for each person
person1.display_info()
person2.display_info()
person3.display_info()