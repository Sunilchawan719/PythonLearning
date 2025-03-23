# Simple example of exception handling in Python

try:
    # Attempt to divide by zero
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")