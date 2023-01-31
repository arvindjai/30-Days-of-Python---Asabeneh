# 30 Days of Python: Day 9 - Condiationals

# Excercises: Level 1
# 1
'''
age  = int(input("Enter your age:  "))
if age >= 18:
    print("You are old enough to learn to drive")

else:
    small = 18 - age
    print(f"You need {small} years to learn to drive.")

'''

# 2
'''
your_age = int(input("Enter your age:  "))
my_age = 30

if your_age > my_age:
    diff = your_age - my_age
    print(f"You are {diff} years older than me")
elif my_age > your_age:
    diff_1 = my_age - your_age
    print(f"You are {diff_1} years younger than me")
else:
    print("We both are of same age")
'''

# 3
'''
nos1 =  int(input("Enter number one:  "))
nos2 =  int(input("Enter number two:  "))

if nos1 > nos2:
    print(f"{nos1} is greater than {nos2} ")
elif nos2 > nos1:
    print(f"{nos1} is smaller than {nos2}")
else:
    print(f"{nos1} is equal to {nos2}")
'''

# Excersise : level 2
# 1
'''
score = int(input("Enter your Score:  "))
if score < 50:
    print("F")
elif score >= 50 and score < 60:
    print("D")
elif score >= 60 and score < 70:
    print("C")
elif score >= 70 and score < 80:
    print("B")
else:
    print("A")
'''
# 2
''' 
user_month = input("Enter the Month:  ")
month = user_month.title()

if month == 'September' or month == 'October'or month == 'November':
    print("Autumn")
elif month == 'December' or month == 'January' or month == 'February':
    print("Winter")
elif month == 'March' or month == 'April' or month == 'May' :
    print("Summer")
elif month == 'June' or month == 'July' or month == 'August':
    print("Spring")
else:
    print("invalid Month")
'''
# 3
'''
fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input("Enter name of Fruits: ")

if user_fruit in fruits :
    print("That fruit already exist in the list")
    print(fruits)
else:
    fruits.append(user_fruit)
    print(fruits)
'''
# Excercise 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    mid = len(person['skills']) // 2
    print(person['skills'][mid])
    print('Python' in person['skills'])
