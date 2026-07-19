
# CHANGING LIST ITEMS

# Lists are mutable, meaning their items can be changed.


# Changing the value of a specific item in a list
cars = ["Toyota", "Honda", "Ford"]
cars[1] = "BMW"
print(cars)  
# Output: ['Toyota', 'BMW', 'Ford']


# Changing a range of items in a list
phones = ["iPhone", "Samsung", "OnePlus", "Google Pixel"]
phones[1:3] = ["Nokia", "Sony"]
print(phones)  
# Output: ['iPhone', 'Nokia', 'Sony', 'Google Pixel']


# Changing a range of items with a different number of new items
cars = ["Toyota", "Honda", "Ford"]
cars[1:3] = ["BMW", "Audi", "Mercedes"]
print(cars)  
# Output: ['Toyota', 'BMW', 'Audi', 'Mercedes']


# Changing a range of items with fewer new items
fruits = ["apple", "banana", "cherry", "date"]  
fruits[1:3] = ["kiwi"]
print(fruits)  
# Output: ['apple', 'kiwi', 'date']


# Changing a range of items with no new items (removing items)
vegetables = ["carrot", "broccoli", "spinach", "pepper"]
vegetables[1:3] = []
print(vegetables)  
# Output: ['carrot', 'pepper']
