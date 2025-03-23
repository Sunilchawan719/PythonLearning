# Example of Method Overloading and Overriding in Python
# Method Overloading
class Calculator:
    def add(self, a, b, c=0):  # Default argument for overloading
        return a + b + c

# Method Overriding
class Parent:
    def greet(self):
        return "Hello from Parent!"

class Child(Parent):
    def greet(self):  # Overriding the greet method
        return "Hello from Child!"

# Testing Method Overloading
calc = Calculator()
print("Addition of two numbers:", calc.add(10, 20))
print("Addition of three numbers:", calc.add(10, 20, 30))

# Testing Method Overriding
parent = Parent()
child = Child()
print(parent.greet())
print(child.greet())