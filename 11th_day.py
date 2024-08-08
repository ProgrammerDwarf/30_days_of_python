### Day 11 - Functions ###

"""
7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]

10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]


13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050

14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

Exercises: Level 2

1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.


2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

Exercises: Level 3

1. Write a function called is_prime, which checks if a number is prime.
2. Write a functions which checks if all items are unique in the list.
3. Write a function which checks if all the items of the list are of the same data type.
4. Write a function which check if provided variable is a valid python variable
5. Go to the data folder and access the countries-data.py file.
    5.1 Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spokenlanguages in the world in descending order
    5.2 Create a function called the most_populated_countries. It should return 10 or 20 most populatedcountries in descending orde
"""

## Lvl 1 
## 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# def add_two(num_1: float, num_2: float) -> None:
#     sum: float = num_1 + num_2
#     return sum
# print(add_two(5,7))

## 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# def area_of_circle(radius: float) -> float:
#     PI_VALUE:float = 3.14
#     area: float = PI_VALUE * radius * radius
#     return area
# print(area_of_circle(5))
    
## 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

# def add_all_nums(*args) -> float:
#     total:int = 0
#     for arg in args:
#         if type(arg) != int and type(arg) != float:
#             print('Please, enter a number')
#         else:
#             total += arg
#     else:
#         return total
# print(add_all_nums('te',5,6))

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

# def convert_celsius_to_farenheit(celsius:float= 0) -> float:
#     farenheit: float = celsius * (9/5) + 32
#     return farenheit
# print(convert_celsius_to_farenheit(-8))

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# def check_season(month_to_check:str) -> str:
#     seasons: dict = {
#     'autumn': ['september','october','november'],
#     'winter': ['december','january','february'],
#     'spring': ['march','april','may'],
#     'summer': ['june','july','august']
#     }
#     for each in seasons:
#         if month_to_check in seasons[each]:
#             return each
# print(check_season('july'))

# 6. Write a function called calculate_slope which return the slope of a linear equation
