# Program to validate age using if and else

# Input age from the user
age = input("Enter your age: ")

# Check if the input is a valid number
if age.isdigit():
    age = int(age)
    if age >= 18:
        print("You are eligible.")
    else:
        print("You are not eligible.")
else:
    print("Invalid input. Please enter a valid number.")