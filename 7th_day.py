# Sets - unordered and inmutable
## Exercises: Level 1 - Given the following sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

## 1. Find the length of the set it_companies
quantity = len(it_companies)
print(quantity)

## 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

## 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['JourneyTrack', 'QuantumLeaf', 'Vacunar', 'G4'])

## 4. Remove one of the companies from the set it_companies
## 5. What is the difference between remove and discard - Remove shows an error when the item is not found.
it_companies.discard('G4')
it_companies.remove('Twitter')

# Exercises: Level 2


## 1. Join A and B
a_set = {'JourneyTrack', 'QuantumLeaf', 'Keylime'}
b_set = {'G4', 'Vacunar','JourneyTrack'}

c_set = a_set.union(b_set)
print(c_set)

## 2. Find A intersection B
print(a_set.intersection(b_set))

## 3. Is A subset of B
print(a_set.issubset(b_set))

## 4. Are A and B disjoint sets
print(a_set.isdisjoint(b_set))

## 5. Join A with B and B with A
#a_set.update(b_set)
#b_set.update(a_set)

## 6. What is the symmetric difference between A and B
print(a_set.symmetric_difference(b_set))

## 7. Delete the sets completely
del a_set, b_set

# Level 3 exercises

## 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print(f'This is the set length: {len(age_st)} and this is the list length {len(age)}')

## 2. Explain the difference between the following data types: string, list, tuple and set
print('string: chain of characters')
print('''list: ordered data structure where multiples data types can be stored.
      it allows duplicated items and it is mutable ''')
print('''tuple: ordered data structure where multiples data types can be stored.
      it allows duplicated items and it is not mutable''')
print('''set: unordered data structure where multiples data types can be stored.
      it does not allows duplicated items and it is limited mutable, user can add and remove data
      but changing an existing element is not possible due to we cannot access to it by an index ''')

## 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
phrase = 'I am a teacher and I love to inspire and teach people'
new_set = set(phrase.split(' '))
print(new_set)
