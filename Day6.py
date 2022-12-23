# 30 Days of python - DAY 6
# Excercise 1

# empty = ()
# Brothers = ('Vipin', 'Arjun','Lalit')
# Sisters = ('Rekha', 'Priyanka', 'Pooja')
# Siblings = Brothers + Sisters
# print(Siblings)
# print(len(Siblings))
# Mom_Dad = ('Kamlavati', 'Musafir')
# Family_member = Siblings + Mom_Dad
# print(Family_member)

# Excercise 2
# (brother1, brother2, brother3,*Sister,Mom,dad ) = Family_member
# print(Sister)
Fruits = ('apple', 'orange', 'banana')
Vegetables = ('Tomoto', 'Spinach', 'carrot')
animal_product = ('Milk', 'Egg')
food_stuff_tp = Fruits + Vegetables + animal_product
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt[3:5])
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
del food_stuff_tp
# print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
state = 'Estonia' in nordic_countries
state1 = 'Iceland' in nordic_countries
print(state)
print(state1)