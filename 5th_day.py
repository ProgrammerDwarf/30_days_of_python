# Exercises: Level 1
## 1. Declare an empty list
"""
empty_list = []
empty_list2 = list()
"""
## 2. Declare a list with more than 5 items and 3. Find the length of your list
"""
new_list: list = ['one', 2, {'number': 'three'}, (4, 'five'), 6.0]
print(len(new_list))
"""
## 4.Get the first item, the middle item and the last item of the list 
#print(new_list[0], new_list[2],new_list[-1], sep=', ')

## 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

#mixed_data_types = ['Reinid', 34, 1.65, 'Married', 'av. El centro, Los chorros, Edo. Miranda']

## 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
## 7. Print the list using print()
## 8. Print the number of companies in the list
## 9. Print the first, middle and last company
"""
it_companies = ['Facebook', 'Google',  'Microsoft', 'Apple', 'IBM','Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
middle_index = len(it_companies) // 2
print(it_companies[0], it_companies[middle_index],it_companies[-1], sep=', ')

## 10. Print the list after modifying one of the companies
it_companies[-2] = 'JourneyTrack'
print(it_companies)

## 11.Add an IT company to it_companies
it_companies.append('Intelifaz')
print(it_companies)

## 12. Insert an IT company in the middle of the companies list
print(len(it_companies))
middle_index = len(it_companies) // 2
it_companies.insert(middle_index,'Quantumleaf')
print(it_companies)

## 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print(it_companies)

## 14. Join the it_companies with a string '#;  '
print('#; '.join(it_companies))

## 15. Check if a certain company exists in the it_companies list.

print('IBM' in it_companies)

## 16. Sort the list using sort() method

it_companies.sort()
print(it_companies)

## 17. Reverse the list in descending order using reverse() method

it_companies.reverse()
print(it_companies)

## 18. Slice out the first 3 companies from the list
without_first_3 = it_companies[3:]
print(without_first_3)

## 19. Slice out the last 3 companies from the list
without_last_3 = it_companies[:-3]
print(without_last_3)

## 20. Slice out the middle IT company or companies from the list
print(len(it_companies))
middle_index = len(it_companies) // 2
middle_it_company = it_companies[middle_index:middle_index + 1]
print(middle_it_company)

## 21. Remove the first IT company from the list

it_companies.remove(it_companies[0])
print(it_companies)

## 22. Remove the middle IT company or companies from the list

middle_index = len(it_companies) // 2
it_companies.remove(it_companies[middle_index])
print(it_companies)

## 23. Remove the last IT company from the list

it_companies.remove(it_companies[-1])
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

## 25. Destroy the IT companies list
del it_companies
print(it_companies)
"""
## 26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

## 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
"""full_stack = front_end.copy()
print(full_stack.count("Redux"))
print(full_stack.index("Redux"))
full_stack.insert(full_stack.index("Redux") + 1, 'Python')
full_stack.insert(full_stack.index("Python") + 1, 'SQL')
print(full_stack)