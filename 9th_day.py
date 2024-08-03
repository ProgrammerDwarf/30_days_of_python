################ CONDITIONALS #################
separator = "Exercise print"
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output: 

"""
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
"""
print(f'{separator:@^100}')
user_age: int = int(input('Please, enter your age: \n'))

if user_age >= 18:
    print('You are old enough to learn to drive.')
else:
    years_to_adulthood: int = 18 - user_age
    print(f'You need {years_to_adulthood} more years to learn to drive.')

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

"""
Enter your age: 30
You are 5 years older than me.
"""
print(f'{separator:@^100}')

your_age: int = int(input('Please, enter your age: '))
my_age: int = 34

age_difference: int = abs(my_age - your_age)

if age_difference == 1:
    if my_age > your_age:
        print(f'I am older than you by {age_difference} year')
    else:
        print(f'You are older than me by {age_difference} year')
elif age_difference > 1:
    if my_age > your_age:
        print(f'I am older than you by {age_difference} years')
    else:
        print(f'You are older than me by {age_difference} years')
else: 
    print('We are the same age')

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

print(f'{separator:@^100}')

a: int = int(input('Please, enter the first number: '))
b: int = int(input('Please, enter the second number: '))

if a > b:
    print(f'A greater than B')
elif b > a:
    print(f'A lesser than B')
else: 
    print('A and B are equals')

## LVL 2 EXERCISES

# 1. Write a code which gives grade to students according to theirs scores:
"""
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""
grades =  {
    'A': range(90, 101),
    'B':  range(70, 90),
    'C':  range(60, 70),
    'D':  range(50, 60),
    'F':  range(0, 50)
}

student_grade: int = int(input('Please, enter the student grade\n'))

if student_grade in grades['A']:
    print('This is an A student')
elif student_grade in grades['B']:
    print('This is an B student')
elif student_grade in grades['C']:
    print('This is an C student')
elif student_grade in grades['D']:
    print('This is an D student')
else:
    print('This is an F student')
### ANOTHER STRUCTURE ####

if student_grade < 50:
    print('This is an F student')
elif student_grade < 60:
    print('This is an D student')
elif student_grade < 70:
    print('This is an C student')
elif student_grade < 90:
    print('This is an B student')
else:
    print('This is an A student')

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

seasons: dict = {
    'autumn': ['september','october','november'],
    'winter': ['december','january','february'],
    'spring': ['march','april','may'],
    'summer': ['june','jule','august']
}

month: str = input('Please, enter the current month to know the season:\n')

if month in seasons['autumn']:
    print(f'The season related to {month.capitalize()} is: Autumn')
elif month in seasons['winter']:
    print(f'The season related to {month.capitalize()} is: Winter')
elif month in seasons['spring']:
    print(f'The season related to {month.capitalize()} is: Spring')
else: 
    print(f'The season related to {month.capitalize()} is: Summer')

# 3. The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit: str = input('Please, enter a new fruit to add the list: ')

if new_fruit in fruits:
    print('That fruit already exist in the list')
else: 
    fruits.append(new_fruit)
    print('A new fruit has been added')

print(fruits)

# Exercises: Level 3
## 1. Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['MongoDB', 'Node', 'Java', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'}
    }

"""
* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

* If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.
"""
if 'skills' in person:
    skills_length: int = len(person['skills'])
    middle_term: str = person['skills'][skills_length // 2]
    print(middle_term)

    print(f"Checking if the user has python on skills: {'Python' in person['skills']}")
else:
    print('There is no skills on this dict')

if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('You are a fullstack dev')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('You are a backend dev')
elif 'React' in person['skills'] and 'Javascript' in person['skills']:
    print('You are a fronted dev')
else:
    print('unknown title')

### Last exercise
if person['is_married'] == True and person['country'] == 'Finland':
    print(f'{person['first_name']} lives in {person['country']}. He/She is married')
elif person['is_married'] == False and person['country'] == 'Finland':
    print(f'{person['first_name']} lives in {person['country']}. He/She is not married')
elif person['is_married'] == True and person['country'] != 'Finland':
    print(f'{person['first_name']} is not living in {person['country']}. He/She is married')
else:
    print('This person does not live in Finland')
