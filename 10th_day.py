####  30 Days Of Python: Day 10 - Loops ####
"""💻 Exercises: Day 10
Exercises: Level 1
"""

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
# for loop
# for iterator in range(11):
#     print(iterator)
# else:
#     print('Completed, loop finished in', iterator)
# # while loop
# iterator_2: int = 0

# while iterator_2 < 10:
#     print(iterator_2)
#     iterator_2 += 1
# else:
#     print('This while loop finished in', iterator_2)

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
# for iterator in range(10, -1, -1):
#     print(iterator)
# else:
#     print('Completed, loop finished in', iterator)

# iterator_2 = 10
# while iterator_2 > 0:
#     print(iterator_2)
#     iterator_2 -= 1
# else:
#     print('While loop finished on', iterator_2)

"""
3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
"""

# for i in range(1,8):
#     print('#' * i)

"""
4. Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""

# square_side = int(input('Please, enter square side length: \n'))

# for row in range(square_side):
#     for column_element in range(square_side):
#         print('#', end=' ')
#     print()

"""
5. Print the following pattern:
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""

# for number_square in range(11):
#     print(f'{number_square} x {number_square} = {number_square**2}')

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# skills = ['Python', 'Numpy','Pandas','Django', 'Flask']

# for skill in skills:
#     print(f'{skill}')
# else: 
#     print('Task completed!')

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
# number = 0
# while number < 101:
#     if number % 2 == 0:
#         print(number)
#     number += 1
# else: 
#     print('Task completed!')

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for number in range(101):
    if number % 2 != 0:
        print(number)
else:
    print('Task completed!')

"""💻 Exercises: Day 10
Exercises: Level 2
"""


# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum = 0
counter = 0
while counter < 101:
    sum = counter + sum
    counter += 1
else:
    print('The total is {}'.format(sum))


# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.

sum_even = 0
sum_odd = 0
counter = 0
while counter < 101:
    if counter % 2 == 0:
        sum_even += counter
    else:
        sum_odd += counter
    counter += 1
else:
    print('The total is {}'.format(sum_even))
    print('The total is {}'.format(sum_odd))

"""
Exercises: Level 3

1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

    
3. Go to the data folder and use the countries_data.py file.
    i. What are the total number of languages in the data
    ii. Find the ten most spoken languages from the data
    iii. Find the 10 most populated countries in the world
"""

# from data.countries import countries
# for country in countries:
#     if 'land' in country:
#         print(country)
# else:
#     print("task completed!")

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits: list = ['banana', 'orange', 'mango', 'lemon', 'pear', 'pinapple']

arr_length: int = len(fruits)
casket: str = ''

for iterator in range(arr_length - 1):
    print(f'<<<< antes: {fruits}')
    casket = fruits.pop()
    print(f'^^^^^^ se le quita el último elemento: {fruits}')
    fruits.insert(iterator, casket)
    print(f'***** Insertamos el elemento en el index: {iterator} - {fruits}')