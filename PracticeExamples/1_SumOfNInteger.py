def sum_of_n_integers(n):
    """
    Calculate the sum of the first N integer numbers.
    :param n: The number of integers to sum up.
    :return: The sum of the first N integers.
    """
    return n * (n + 1) // 2

# Example usage
if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a positive integer.")
        else:
            print(f"The sum of the first {n} integers is: {sum_of_n_integers(n)}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")