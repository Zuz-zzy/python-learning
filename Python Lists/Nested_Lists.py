
# NESTED LISTS

# A nested list is a list that contains other lists as its elements. It allows you to create multi-dimensional data structures in Python.

#To access elements inside nested lists, we use multiple indexes:
   #-First index → selects the inner list
   #-Second index → selects the item inside that inner list

# Example of a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing elements in a nested list
print(nested_list[0])  # Output: [1, 2, 3]
print(nested_list[1][2])  # Output: 6
print(nested_list[2][0])  # Output: 7