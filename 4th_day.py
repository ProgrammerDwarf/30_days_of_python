# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
"""word_1 = 'Thirty'
word_2 = 'Days'
word_3 = 'Of'
word_4 = 'Python'
print(word_1 +" "+ word_2 +" "+ word_3 + " " + word_4)
"""
# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
# 4. Print the variable company using print().
word_1 = 'Coding'
word_2 = 'For'
word_3 = 'All'

company = '%s %s %s' %(word_1, word_2, word_3)
print(company)

# 5. Print the length of the company string using len() method and print(). Remember to uncomment the previous exercise
#print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
#print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
#print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
"""print(company.capitalize())
print(company.title())
print(company.swapcase())"""

# 9. Cut(slice) out the first word of Coding For All string.
#print(company[0:6])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
"""
answer = company.index('Coding')
print(answer)
answer = company.find('Coding')
print(answer)
answer = 'Coding' in company
print(answer)
answer = company.rfind('Coding')
print(answer)
answer = company.rindex('Coding')
print(answer)
"""
# 11. Replace the word coding in the string 'Coding For All' to Python.
"""
answer = company.replace('Coding', 'Python')
print(answer)"""

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
"""answer = answer.replace('All', 'Everyone')
print(answer)"""

# 13. Split the string 'Coding For All' using space as the separator (split()) .
"""answer_splitted = answer.split(" ", 1)
print(answer_splitted)"""

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
"""companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
splitted_companies = companies.split(', ')
print(splitted_companies)"""

# 15. What is the character at index 0 in the string Coding For All.
#print('The character is: ', company[0])

# 16. What is the last index of the string Coding For All.
#print('The last character is: ', company[-1])
#print('The last character is: ', company[len(company) - 1])

# 17. What character is at index 10 in "Coding For All" string.
#print('The character is: ', company[10])

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
"""company_acronym = company.split()
company_acronym = company_acronym[0][0] + company_acronym[1][0] + company_acronym[2][0] 
print(company_acronym)"""

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
"""company_first_occurence = company.index('C')
print('First occurence\'s index is: ', company_first_occurence)"""

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
"""company_first_occurence = company.index('F')
print('First occurence\'s index is: ', company_first_occurence)"""

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
"""company_last_occurence = company.rindex('l')
print('Last occurence\'s index is: ', company_last_occurence)"""

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
"""sentence = 'You cannot end a sentence with because because because is a conjunction'
index_first_occurence = sentence.find('because')
print(index_first_occurence)"""

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
"""index_last_occurence = sentence.rfind('because')
print(index_last_occurence)"""

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
"""word_len = (len('because'))
sliced_sentence = sentence[31:47 + word_len]
print(sliced_sentence)"""
# Since 26 is the same as 23 I considered as done   
# 27. It seems that 27 is the same as 25

# 28. Does ''Coding For All' start with a substring Coding?
"""
word_to_seek = 'Coding'

is_in_sentence =  word_to_seek in company
word_index = company.find(word_to_seek)
print('{}, the word {} is in the sentence "{}"'.format(is_in_sentence, word_to_seek, company))
print('Its position is: {}'.format(word_index))
print('So, that sentence starts with', word_to_seek )
# Another way
starts_with_word: bool = company.startswith(word_to_seek)
print(starts_with_word)

"""



# 29. Does 'Coding For All' end with a substring coding?
"""word_to_seek = 'coding'
is_in_sentence =  word_to_seek in company
word_index = company.find(word_to_seek)
print('{}, the word {} is in the sentence "{}"'.format(is_in_sentence, word_to_seek, company))
print('Its position is: {}'.format(word_index))
print('So, that sentence does not start with', word_to_seek)"""

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
"""company = '   Coding For All      '
print(company)
company = company.strip()
print(company)"""

# 31. Which one of the following variables return True when we use the method isidentifier(): 
"""word_as_identifier: str = '30DaysOfPython'
is_identifier: bool = word_as_identifier.isidentifier()
print('{0}, word: "{1}", is not an identifier'.format(is_identifier, word_as_identifier))

word_as_identifier: str = 'thirty_days_of_python'
is_identifier: bool = word_as_identifier.isidentifier()
print('{0}, word: "{1}", is an identifier'.format(is_identifier, word_as_identifier))"""

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
"""
python_libraries: list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
python_libraries_as_string: str = "#".join(python_libraries)
print(python_libraries_as_string)
"""
# 33. Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
"""print('I am enjoying this challenge.\nI just wonder what is next.')"""

# 34. Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
line_1 = 'Name\tAge\tCountry\tCity'
line_2 = 'Asabeneh\t250\tFinland\tHelsinki'
print(line_1)
print(line_2)

# 35. Use the string formatting method to display the following:
"""
radius = 10
area = 3.14 * radius ** 2
answer = 'The area of a circle with radius {r} is {a} meters square.'.format(r = radius, a = int(area))
print(answer)
"""

# 36. Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

num_1 = 8
num_2 = 6
print('{0} + {1} =  {result}'.format(num_1, num_2, result = num_1 + num_2))
print('{0} - {1} =  {result}'.format(num_1, num_2, result = num_1 - num_2))
print('{0} * {1} =  {result}'.format(num_1, num_2, result = num_1 * num_2))
print('{0} / {1} =  {result}'.format(num_1, num_2, result = round(num_1 / num_2, 2)))
print('{0} % {1} =  {result}'.format(num_1, num_2, result = num_1 % num_2))
print('{0} // {1}6 = {result}'.format(num_1, num_2, result = num_1 // num_2))
print('{0} ** {1}6 = {result}'.format(num_1, num_2, result = num_1 ** num_2))
