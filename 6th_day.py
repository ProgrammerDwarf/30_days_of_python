# Tuples
# Level 1 exercises 




## 1. Create an empty tuple

empty_tuple = ()
print(type(empty_tuple))

## 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Reinaldo', 'Carlos Luis')
sister = ('Alejandra',)

## 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sister
print(siblings)

## 4. How many siblings do you have?
print(len(siblings))

## 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Reinaldo', 'Nidia')
family_members = parents + siblings
print(family_members)

