
"""
- Lists are ordered collections of items that can be of any data type.
- Lists are separated by commas and enclosed in square brackets [].
- Lists are mutable, meaning you can change their content without changing their identity.

"""

# Creating a list
my_list = ["pink", "blue", "green", "red", "black"]




# Accessing elements in a list using indexes
# Indexing starts at 0, so the first element is at index 0, the second element is at index 1, and so on.

print(my_list[0])  # Output: pink
print(my_list[2])  # Output: green
print(my_list[4])  # Output: black



# Accessing elements in a list using negative indexes
# Negative indexing starts at -1, so the last element is at index -1, the second last element is at index -2, and so on.

print(my_list[-1])  # Output: black
print(my_list[-3])  # Output: green
print(my_list[-5])  # Output: pink




# Lists also support many data types, including integers, floats, strings, and even other lists.

my_details = ["John", 25, "Software Engineer", "5.9 YOE"]


# Checking if the specified item is present in the list using the 'in' keyword

if "John" in my_details:
    print("John is present in the list.")
else:
    print("John is not present in the list.")



