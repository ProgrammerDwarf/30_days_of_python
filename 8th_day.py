# Dictionaries


## 1. Create an empty dictionary called dog
dog = {}

## 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'nina',
    'color': 'grey',
    'breed': 'husky',
    'legs': 4,
    'age': 14,
}
print(dog)

## 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Reinid',
    'last_name': 'Valarino',
    'gender':  'female',
    'age': 34,
    'marital_status': 'married',
    'skills': ['python', 'black box testing', 'white box testing', 'draw', 'math'],
    'country': 'Venezuela',
    'city': 'Caracas',
    'address': {
        'street': 'Avenida El centro',
        'zip_code': 1768,
        'building': 'Residencias El centro'
    }
}
## 4.  Get the length of the student dictionary
print(len(student))

## 5. Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

## 6. Modify the skills values by adding one or two skills
student['skills'].append('security testing')
student['skills'][4] = 'algebra'
print(student['skills'])

## 7. Get the dictionary keys as a list
dict_keys = student.keys()
print(dict_keys)

## 8. Get the dictionary values as a list
dict_values = student.values()
print(dict_values)

## 9. Change the dictionary to a list of tuples using items() method
print('+' * 100)
print(student.items())

## 10. Delete one of the items in the dictionary
del student['last_name']
student.popitem()
print('+' * 100)
print(student)

## 11. Delete one of the dictionaries
del student
print(student)