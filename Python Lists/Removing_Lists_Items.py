
# There are various methods to remove items from the list: pop(), remove(), del, clear()

# 1. pop() - Removes the item at the specified index (or the last item if no index is specified).
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # Removes the item at index 1
print(thislist)  # Output: ['apple', 'cherry']

thislist.pop()  # Removes the last item
print(thislist)  # Output: ['apple']



# 2. remove() - Removes the first occurrence of the specified value.
thislist = ["apple", "banana", "cherry", "banana"]  
thislist.remove("banana")  # Removes the first occurrence of "banana"
print(thislist)  # Output: ['apple', 'cherry', 'banana']



# 3. del - Removes the item at the specified index or deletes the entire list.
thislist = ["apple", "banana", "cherry"]
del thislist[1]  # Removes the item at index 1
print(thislist)  # Output: ['apple', 'cherry']

del thislist  # Deletes the entire list
#print(thislist)  # Output: NameError: name 'thislist' is not defined



# 4. clear() - Removes all items from the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # Output: []


