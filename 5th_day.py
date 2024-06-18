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
"""
# Exercises level 2: fifth day
## Given the age list...

##
##- 8. Divide the countries list into two equal lists if it is even if not one more country for the first half.
##- 9. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

## 1. Sort the list and find the min and max age
"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()

min_age = ages[0]
max_age = ages[-1]
print(f"1. mininum age is {min_age}, and maximum age is {max_age}")

min_age = min(ages)
max_age = max(ages)
print(f"1. mininum age is {min_age}, and maximum age is {max_age}")

## 2. Add the min age and the max age again to the list
ages.insert(0, min_age)
ages.append(max_age)

## 3. Find the median age (one middle item or two middle items divided by two)
print(ages)
print(len(ages))
middle_index =  (len(ages) - 1) // 2
print('The median age is: {0}'.format(ages[middle_index]))

##-4. Find the average age (sum of all items divided by their number )
age_average = (sum(ages) / len(ages))
print('Knowing that there are {quantity} elements and the sum is {total}, the age average is: {average}'.format(quantity = len(ages), total = sum(ages), average = age_average))

##-5. Find the range of the ages (max minus min)
age_range = max(ages) - min(ages)
print(f'The age range is: {age_range}, from {min(ages)} to {max(ages)}')

##-6. Compare the value of (min - average) and (max - average), use abs() method
value_1 = abs(min(ages) - age_average)
value_2 = abs(max(ages) - age_average)
evaluation = value_1 == value_2
print(f'value 1 is {value_1}, value 2 is: {value_2} and it is {evaluation} that they are equals')
"""
##- 7. Find the middle country(ies) in the countries list
"""
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

if len(countries) % 2 != 0:
    middle_index = len(countries) // 2
    middle_country = countries[middle_index]
    print(middle_country)
else:
    middle_countries = [countries[len(countries) // 2],countries[(len(countries) // 2) + 1]]
    print(f'{middle_countries}')
"""
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_to_unpack = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
modern_empire_1, modern_empire_2, modern_empire_3, *scandic = countries_to_unpack
print(modern_empire_1, modern_empire_2, modern_empire_3, scandic)