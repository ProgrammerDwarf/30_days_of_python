# Excercise 1
""""
    Write a python comment saying 'Day 2: 30 Days of python programming'
    Declare a first name variable and assign a value to it
    Declare a last name variable and assign a value to it
    Declare a full name variable and assign a value to it
    Declare a country variable and assign a value to it
    Declare a city variable and assign a value to it
    Declare an age variable and assign a value to it
    Declare a year variable and assign a value to it
    Declare a variable is_married and assign a value to it
    Declare a variable is_true and assign a value to it
    Declare a variable is_light_on and assign a value to it
    Declare multiple variable on one line

"""

# 1. Day 2: 30 Days of python programming

# 2. Declare a first name variable and assign a value to it
first_name: str = 'Reinid'
last_name: str = 'Valarino'
full_name: str = first_name + " " + last_name
country: str = 'Venezuela'
city: str = 'Caracas'
age: int = 34
year: int = 1989
is_married = True
is_true = True
is_light_on = True

spouse_first_name, spouse_last_name, spouse_age, year = \
'Jenesis','Rios',31,1992

"""
    1.Check the data type of all your variables using type() built-in function
    2.Using the len() built-in function, find the length of your first name
    3.Compare the length of your first name and your last name
    4.Declare 5 as num_one and 4 as num_two
        i.Add num_one and num_two and assign the value to a variable total
        ii.Subtract num_two from num_one and assign the value to a variable diff
        iii.Multiply num_two and num_one and assign the value to a variable product
        iv.Divide num_one by num_two and assign the value to a variable division
        v.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
        vi.Calculate num_one to the power of num_two and assign the value to a variable exp
        vii.Find floor division of num_one by num_two and assign the value to a variable floor_division
    5.The radius of a circle is 30 meters.
        i.Calculate the area of a circle and assign the value to a variable name of area_of_circle
        ii.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
        iii.Take radius as user input and calculate the area.
    6.Use the built-in input function to get first name,
    last name, country and age from a user and store the value to their corresponding variable names
    7.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""
# 1
print(type(first_name))
print(type(full_name))
print(type(age))
print(type(year))
print(type(is_married))
# 2 
print(len(first_name))
# 3.Compare the length of your first name and your last name

if len(first_name) > len(last_name):
    print('First name has more letters than Last name')
elif len(last_name) > len(first_name):
    print('Last name has more letters than first name')
else:
    print('You have the same amount of letters for you first name than your last name')

# 4.Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
# i.Add num_one and num_two and assign the value to a variable total
sum = num_one + num_two
print(sum)
# ii.Subtract num_two from num_one and assign the value to a variable diff
substract = num_two - num_one
print(substract)
# iii.Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print(product)
# iv.Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)
# v.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two %  num_one
print(remainder)
# vi.Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)
# vii.Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

#5.The radius of a circle is 30 meters.
radius = 30
PI_VALUE = 3.1415926
# i.Calculate the area of a circle and assign the value to a variable name of area_of_circle
circle_area = 2 * PI_VALUE * radius
print(circle_area)
# ii.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circumference = PI_VALUE * radius ** 2
print(circumference)
# iii.Take radius as user input and calculate the area.
radius = float(input("Please, set a radius:\n"))
circle_area = 2 * PI_VALUE * radius
print(f'The area is: {circle_area}')
 
"""
6.Use the built-in input function to get first name,last name, country and age
from a user and store the value to their corresponding variable names
"""    
user_fn = input('What is your first name?\n > ')
user_ln = input('What is your last name?\n > ')
user_country = input('Where do you reside?\n > ')
user_age = int(input('How old are you?\n > '))

# 7.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords



