# 'Day 2: 30 Days of python programming'
''' 
firstName, lastName, fullName, Country, City, age, year, is_married = 'Arvind','Jaiswal', "Arvind Jaiswal", 'India', 'Mumbai', 29 , 2022, False
is_true, is_light_on = 0 , True

print(firstName, lastName, fullName, Country, City, age, year, is_married)
print(is_true, is_light_on)
print(len(firstName))
print(len(lastName))
'''

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

# Problem of Circle
from math import pi
#radius = 30
radius = int(input("Enter the Radius:  "))
Area_circle = round(pi * (radius**2), 3)
print("The area of square is: ", Area_circle)
print(pi)
circum_circle = round(2 * pi * radius, 3)
print("Circumference of circle is: ", circum_circle)

