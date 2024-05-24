"""
The first day the challenge focused on install python, VScode and knowing basic math operators.
Also it was explained some of the data types that are in python and how to write them
"""
# Day 1 - 30  Days of Python challenge

print (2 + 3)           # Addition
print (2 - 3)           # Substraction
print (4 * 8)           # Multiplication
print (5 / 2)           # Division
print (5 ** 2)          # Exponential
print (7 % 3)           # Modulus
print (9 // 2)          # Floor division operator

# Checking data types
print(type(10))         # Integer
print(type(3.14))       # Float number
print(type(1 + 3j))     # Complex number
print(type('Jenesis'))  # String 
print(type([1, 5.77, 'Reinid']))  # List
print(type((1, 5.77, 'Reinid')))  # Tuple
print(type({1, 5.77, 2, 3, 1, "Reinid"}))  # Set
print(type({'name': 'Reinid', 'age': 34, 'is_married': True}))  # Dictionary

# Exercise level 3
# Find the euclidian distance between (2, 3) and (10, 8)
print('''Hi, this is a program that calculates the euclidian distance between two given points.
A (2,3)
B (10,8)
''')
print(f'''First we have to find the
difference on the Y-axis from those points
and find the square of that number''')
print((8 - 3) ** 2)
print(f'''Then we have to find the
difference on the X-axis from those points
and find the square of that number''')
print((10 - 2) ** 2)
print(f'''As a final step, 
take those values ​​and make a sum with them and calculate
the square root from the result.''')
print((((8 -3) ** 2) + ((10 - 2) ** 2)) ** (1 / 2))
