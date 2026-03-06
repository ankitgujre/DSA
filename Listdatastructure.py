'''
A list is a built-in data structure in Python, used to store multiple elements.

Lists are used by many algorithms.
'''

lst = [2,3,4,6,8,9,6]

# Empty list
x = []

# List with initial values
y = [1, 2, 3, 4, 5]

# List with mixed types
z = [1, "hello", 3.14, True]

print(lst)
print(x)
print(y)
print(z)

print(type(x))

# Python lists come with several built-in algorithms (called methods), to perform common operations 
# like appending, sorting, and more.

x.append(88)
print(x)
x.append(5)
print(x)
x.sort()
print(x)

'''
Create Algorithms
Sometimes we want to perform actions that are not built into Python.

Then we can create our own algorithms.

For example, an algorithm can be used to find the lowest value in a list, like in the example below:
'''

my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i
print("original array = ", my_array)
print('Lowest value:', minVal)