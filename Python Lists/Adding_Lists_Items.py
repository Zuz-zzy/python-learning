
# There are three methods to add items to a list: append(), insert(), and extend().



# 1. append() - Adds an item to the end of the list.    
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) 
# Output: ['apple', 'banana', 'cherry', 'orange']


# 2. insert() - Adds an item at the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) 
# Output: ['apple', 'orange', 'banana', 'cherry']


# 3. extend() - Adds the elements of a list (or any iterable), to the end of the current list.
fruits= ["apple", "banana", "cherry"]
colors = ["red", "blue", "green"]
fruits.extend(colors)
print(fruits) 
# Output: ['apple', 'banana', 'cherry', 'red', 'blue', 'green']


# Note: The extend() method can also take any iterable (tuples, sets, dictionaries etc.).


# Example of using extend() with a tuple
names = ["John", "Jane", "Doe"]
more_names = ("Alice", "Bob", "Charlie")  # Tuple
names.extend(more_names)
print(names)
# Output: ['John', 'Jane', 'Doe', 'Alice', 'Bob', 'Charlie']


# Example of using extend() with a set
numbers = [1, 2, 3]
more_numbers = {4, 5, 6}  # Set
numbers.extend(more_numbers)
print(numbers)
# Output: [1, 2, 3, 4, 5, 6]


# Example of using extend() with a dictionary
person = ["John", "Doe"]
more_person = {"Alice": 25, "Bob": 30}
person.extend(more_person)
print(person)
# Output: ['John', 'Doe', 'Alice', 'Bob']  
# Note: Only the keys of the dictionary are added to the list.


# Combining two lists using the + operator
list1 = ["apple", "banana", "cherry"]   
list2 = ["date", "fig", "grape"]
combined_list = list1 + list2
print(combined_list)
# Output: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']