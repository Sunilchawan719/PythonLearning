# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Adding a new key-value pair
my_dict["country"] = "USA"
print("After Adding:", my_dict)

# Updating an existing key-value pair
my_dict["age"] = 26
print("After Updating:", my_dict)

# Deleting a key using del
del my_dict["city"]
print("After Deleting:", my_dict)

# Removing a key using pop (if exists)
removed_value = my_dict.pop("country", "Key not found")  # Default message if key is absent
print("After Popping:", my_dict, "| Removed Value:", removed_value)
