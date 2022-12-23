# Day 5: 30Days of python - List Operations

# Exercises: Level 1

emp_list = []
city = ['Mumbai', 'Pune', 'Hyderabad', 'Banglore','Delhi']
print(len(city))
print(city[0])
print(city[2])
print(city[-1])
mix_data_types = ['Maya', 25, 172.5, 'Single','India']
it_companies = ['Facebook','Microsoft','Amazon','flipkart','IBM']
print(it_companies)
# it_companies.append('Oracle')
it_companies.insert(2,'Oracle')
'''
print(it_companies)
print("Git First Commits")

print(it_companies[2].upper())
it_companies1 = sorted(it_companies)
print(it_companies1)
it_companies2 = sorted(it_companies,reverse=True) #17 Reverse Sort 
print(it_companies2)
'''

# print(it_companies[0:3])
# print(it_companies[-3:])         # Slicing last 3 items from list

# print(it_companies)
# it_companies.remove('Facebook')  # Removing the 1st item from list using remove(item).
# print(it_companies)
# it_companies.pop(0)              # Removing 1st item from list by using pop(index)
# print(it_companies)

# print(len(it_companies))
# it_companies.pop(5)              # Removing last item from list by using pop(index)
# print(it_companies)

del it_companies[0]                # Removing 1st item from list by using del listname[index]
print(it_companies)

it_companies = []

# del it_companies
# print(it_companies)

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# full_stack = front_end + back_end
# print(full_stack)
# full_stack.insert(5, 'Python')
# full_stack.insert(6, 'SQL')
# print(full_stack)


# _________________________________________________________________________________________
# _________________________________________________________________________________________

# EXERCISE 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages_sort = sorted(ages)
print(f"The min age is: {ages_sort[0]} & max age is : {ages_sort[-1]}")

range= ages_sort[-1] - ages_sort[0]
print("Range of ages is: " + str(range) )
print(len(ages_sort))
sum = ages_sort[0] + ages_sort[1] + ages_sort[2] + ages_sort[3] + ages_sort[4] + ages_sort[5]+ ages_sort[6] + ages_sort[7] + ages_sort[8] + ages_sort[9] 
average = sum / 10
print(average)
diff_min = average - ages_sort[0]
diff_max = ages_sort[-1] - average
print(f"The difference between (min - avg) is: {round(diff_min, 2)} & (max - avg) is: {round(diff_max, 2)} ")

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries[len(countries)//2])

First_half_country = countries[:4]
scandic_country = countries[4:]
print(f"first half od countries is: {First_half_country} % Second half is : {scandic_country}")