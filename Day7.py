# 30 Days of Python - DAY 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercise 1
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Accenture', 'Crossover', 'Wipro'])
print(it_companies)
it_companies.remove('Twitter')
print(it_companies)
# What is the difference between remove and discard ?

# Excercise 2
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))    # (A/B) U (B/A)
del A
del B
# print(B)

# Exercise 3
ages = set(age)
print(len(age))
print(len(ages))
# Explain the difference between the following data types: string, list, tuple and set

# I am a teacher and I love to inspire and teach people. How many unique words have been 
# used in the sentence? Use the split methods and set to get the unique words.
string = "I am a teacher and I love to inspire and teach people"
Teacher = list(string.split())
print(Teacher)
st_teacher = set(Teacher)
print(st_teacher)
print(len(st_teacher))