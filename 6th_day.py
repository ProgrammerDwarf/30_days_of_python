# Tuples
# Level 1 exercises 

## 1. Create an empty tuple
"""
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

# Exercises: Level 2


## nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

## 1. Unpack siblings and parents from family_members
print(family_members)
parents, brothers, sister, *_ = family_members[:2],family_members[2:4],family_members[4:]
print(parents)
"""
## 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('tomato', 'pineapple', 'pear')
vegetables = ('onion', 'garlic', 'carrot', 'peppers')
animal = ('cow','rabbit', 'fish', 'chicken')

food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

## 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))

## 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
quantity = len(food_stuff_tp)
print(quantity)
quantity_odd_even = len(food_stuff_tp) % 2 == 0
print(quantity_odd_even)
middle_index =  len(food_stuff_tp) // 2 
middle_item = food_stuff_tp[middle_index : middle_index + 1]
print(middle_item)

## 5. Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print(first_three_items)
print(last_three_items)

## 6. Delete the food_staff_tp tuple completely
#del food_stuff_tp

## 7. Check if an item exists in tuple:
check = 'rabbit' in food_stuff_tp   

## 8. Check if 'Estonia' is a nordic country 
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

## 9. Check if 'Iceland' is a nordic country 
check = 'Iceland' in nordic_countries
print(check)