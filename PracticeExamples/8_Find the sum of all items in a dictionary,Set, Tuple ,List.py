# Function to find the sum of all items in a dictionary
def sum_of_dict_items(data):
    return sum(data.values())

# Function to find the sum of all items in a set
def sum_of_set_items(data):
    return sum(data)

# Function to find the sum of all items in a tuple
def sum_of_tuple_items(data):
    return sum(data)

# Function to find the sum of all items in a list
def sum_of_list_items(data):
    return sum(data)

# Example usage
sample_dict = {'a': 10, 'b': 20, 'c': 30}
sample_set = {1, 2, 3, 4}
sample_tuple = (5, 10, 15)
sample_list = [7, 14, 21]

print("Sum of dictionary items:", sum_of_dict_items(sample_dict))
print("Sum of set items:", sum_of_set_items(sample_set))
print("Sum of tuple items:", sum_of_tuple_items(sample_tuple))
print("Sum of list items:", sum_of_list_items(sample_list))