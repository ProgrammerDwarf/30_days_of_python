####  30 Days Of Python: Day 10 - Loops ####
"""💻 Exercises: Day 10
Exercises: Level 1
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

6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

7. Use for loop to iterate from 0 to 100 and print only even numbers

8. Use for loop to iterate from 0 to 100 and print only odd numbers
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

iterator_2 = 10
while iterator_2 > 0:
    print(iterator_2)
    iterator_2 -= 1
else:
    print('While loop finished on', iterator_2)

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