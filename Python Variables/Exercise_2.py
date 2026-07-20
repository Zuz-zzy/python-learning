# EXERCISE 2
# Swap two variables without using a third variable.

# Taking input for two variables
a = input("Enter the first variable (a): ")
b = input("Enter the second variable (b): ")

# Swapping the two variables 
a, b = b, a

# printing the swapped variables
print("After Swapping the variables:")
print("First variable (a):", a)
print("Second variable (b):", b)