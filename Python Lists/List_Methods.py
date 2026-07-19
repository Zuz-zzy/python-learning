
#LIST METHODS

# There are several methods available for lists in Python. Here are some commonly used list methods: append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), and sort().
  
   # -append()	Adds an element at the end of the list 
   # -clear()	Removes all the elements from the list 
   # -copy()	Returns a copy of the list 
   # -count()	Returns the number of elements with the specified value 
   # -extend()	Add the elements of a list (or any iterable), to the end of the current list 
   # -index()	Returns the index of the first element with the specified value 
   # -insert()	Adds an element at the specified position 
   # -pop()	    Removes the element at the specified position 
   # -remove()	Removes the item with the specified value 
   # -reverse()	Reverses the order of the list 
   # -sort()	Sorts the list


# using copy() method to create a copy of a list
vegetables = ["carrot", "broccoli", "spinach"]
# create a copy of the vegetables list  
thislist = vegetables.copy()
print(thislist) 
# Output: ['carrot', 'broccoli', 'spinach']


# using count() method to count the number of occurrences of an element in a list
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.count("banana"))  
# Output: 2


# using index() method to find the index of the first occurrence of an element in a list
fruits = ["apple", "banana", "cherry"]  
print(fruits.index("banana"))  
# Output: 1


# using reverse() method to reverse the order of elements in a list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)
# Output: [5, 4, 3, 2, 1]


# using sort() method to sort the elements of a list in ascending order
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)
# Output: [1, 2, 5, 5, 6, 9]
