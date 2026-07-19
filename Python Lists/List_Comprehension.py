
# LIST COMPREHENSION

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Syntax: example_list = [expression(item) for item in iterable if condition]
   #-expression: the value to put into the new list.
   #-iterable: a sequence or collection you can loop over (lists, tuples, dictionaries, sets, strings, etc.)
   #-condition: condition checks if the item should be added to the new list or not.

# Example 1: Create a new list containing only the items that start with the letter 'a'
fruits = ["apple", "banana", "cherry", "date"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  
# Output: ['apple']


# Example 2: Create a new list with all items from the original list
newlist = [x for x in fruits]
print(newlist)  
# Output: ['apple', 'banana', 'cherry', 'date']


# Example 3: Create a new list with all items from the original list, but exclude "banana"
newlist = [x for x in fruits if x != "banana"] #!= means "not equal to"
print(newlist)  
# Output: ['apple', 'cherry', 'date']


# Example 4: Create a new list with all items converted to uppercase
newlist = [x.upper() for x in fruits] #upper() method converts the string to uppercase
print(newlist)  
# Output: ['APPLE', 'BANANA', 'CHERRY', 'DATE']


# Example 5: Create a new list with all items converted to lowercase
newlist = [x.lower() for x in fruits] #lower() method converts the string to lowercase
print(newlist)  
# Output: ['apple', 'banana', 'cherry', 'date']


# Example 6: Create a new list with the length of each item
newlist = [len(x) for x in fruits] #len() method returns the length of the string
print(newlist)  
# Output: [5, 6, 6, 4]