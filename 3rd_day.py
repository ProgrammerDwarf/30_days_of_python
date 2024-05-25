"""
Today I learnt about: 
1. Assignment Operators
2. Arithmetic Operators
3. Comparison Operators
4. Logical Operators
"""

"""
Exercises

    1.Declare your age as integer variable
    2.Declare your height as a float variable
    3.Declare a variable that store a complex number
    4.Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

        Enter base: 20
        Enter height: 10
        The area of the triangle is 100

    5.Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

        Enter side a: 5
        Enter side b: 4
        Enter side c: 3
        The perimeter of the triangle is 12

    6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
    7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
    8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
    9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
    10. Compare the slopes in tasks 8 and 9.
    11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
    12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
    13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
    14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
    15. There is no 'on' in both dragon and python
    16.Find the length of the text python and convert the value to float and convert it to string
    17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
    18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
    19. Check if type of '10' is equal to type of 10
    20. Check if int('9.8') is equal to 10
    21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

        Enter hours: 40
        Enter rate per hour: 28
        Your weekly earning is 1120

    22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

        Enter number of years you have lived: 100
        You have lived for 3153600000 seconds.

    23. Write a Python script that displays the following table

        1 1 1 1 1
        2 1 2 4 8
        3 1 3 9 27
        4 1 4 16 64
        5 1 5 25 125
"""
# 1.Declare your age as integer variable
my_age: int = (21)
# 2.Declare your height as a float variable
my_height = (1.65)
# 3.Declare a variable that store a complex number
my_complex_number: complex = 1 + 2j
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
"""triangle_base = float(input("Please, enter the base length: "))
triangle_height = float(input("Please, enter the height length: "))
triangle_area = 0.5 * triangle_base * triangle_height
 print(triangle_area)
"""
# 5.Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
"""
triangle_side_a = float(input("Please, type the lenght of the side a:\n>> "))
triangle_side_b = float(input("Please, type the lenght of the side b:\n>> "))
triangle_side_c = float(input("Please, type the lenght of the side c:\n>> "))
triangle_perimeter = triangle_side_a + triangle_side_b + triangle_side_c
print(triangle_perimeter)
"""
# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
"""
rectangle_length = int(input('Please, type the length of the triangle: \n>> '))
rectangle_width = int(input('Please, type the width of the triangle: \n>> '))
rectangle_area = rectangle_length * rectangle_width
print(f'The area of the rectangle is: {rectangle_area} u²')
"""
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

PI_VALUE = 3.14
"""
circle_radio = int(input('Please, write the length of the radio:\n>> '))
circle_area = PI_VALUE * circle_radio * circle_radio
circle_circunmerence = 2 * PI_VALUE * circle_radio

print(f"The area of the circle is: {circle_area}")
print(f"The circunmerence of the circle is: {round(circle_circunmerence, 2)}")
"""
# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
"""
point_a_x = 0
point_a_y = int(2 * (point_a_x) - 2)
point_b_y = 0
point_b_x = int((2 + point_b_y ) / 2)
slope_1 = (point_b_y - point_a_y) / (point_b_x - point_a_x)
#print(f"The slope for point A(0,-2) and B(1, 0) is: {slope}")
#print(f"The x-intercept for the function y = 2x -2  is: {point_a_y}")
#print(f"The y-intercept for the function y = 2x -2 is: {point_b_x}")
"""
# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
"""
point_a_x = 2
point_a_y= 2
point_b_x = 6
point_b_y = 10

slope_2 = (point_b_y - point_a_y) / (point_b_x - point_a_x)
#print(f'The slope is: {int(slope)}')
"""
#10. Compare the slopes in tasks 8 and 9. Remember to take out the comment symbols for 8 and 9 exercises
"""
answer_slopes = slope_1 > slope_2 
print("The slope 1 is greater than 2?")
print(f"{answer_slopes}")

answer_slopes = slope_1 < slope_2 
print("The slope 2 is greater than 1?")
print(f"{answer_slopes}")

print("The slope are equals?")
answer_slopes = slope_1 == slope_2 
print(f"{answer_slopes}")
"""
# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
"""
x = -3
y = x ** 2 + 6 * x + 9

print(f"at {x}, y value is: {y}")
"""

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.

word_1 = 'python'
word_2 = 'dragon'

is_not_comparison = len(word_1) != len(word_2)
#print(is_not_comparison)

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'. Remember to quit comment symbol for exercise 12
"""
answer_13 = 'on' in word_1 and 'on' in word_2
print(answer_13)
"""
#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
"""
quote = "I hope this course is not full of jargon"
answer_14 = "jargon" in quote
print(answer_14)
"""

#15. There is no 'on' in both dragon and python. Remember to take out the comment symbol for exercise 12

answer_15 =  not ('on' in word_1 and 'on' in word_2)
print(answer_15)