#RANGE OF INDEXES
#It can print a range of list items by specifying where you want to start, where you want to end, and if you want to skip elements in between the range.


#Syntax: List[start : end : jumpIndex]


thislist = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
print(thislist[2:5])    #using positive indexes
print(thislist[1:6:2])  #using positive indexes with jumpIndex
print(thislist[-5:-2])  #using negative indexes

# Output: ['cherry', 'date', 'fig']
# Output: ['banana', 'date', 'grape']
# Output: ['cherry', 'date', 'fig']

# The element of the end index provided will not be included.


# Printing all elements from a given index till the end
print(thislist[2:7])  #using positive indexes
print(thislist[-5:])  #using negative indexes   

# Output: ['cherry', 'date', 'fig', 'grape', 'kiwi']
# Output: ['cherry', 'date', 'fig', 'grape', 'kiwi']




# Printing all elements from the start till a given index
print(thislist[:5])   #using positive indexes   
print(thislist[:-2])  #using negative indexes

# Output: ['apple', 'banana', 'cherry', 'date', 'fig']
# Output: ['apple', 'banana', 'cherry', 'date', 'fig']



# Print alternate values
print(thislist[::2])  #using positive indexes with jumpIndex
print(thislist[-5:-2:2]) #using negative indexes with jumpIndex

# Output: ['apple', 'cherry', 'fig', 'kiwi']
# Output: ['cherry', 'fig']

# Here, the jumpIndex is 2, which means it will print every second element in the specified range.