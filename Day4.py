# Day 4 : 30 days of python - String Operations

# ex1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty' + ' '+'Days'+ ' '+ 'Of'+ ' '+ 'Python')
# ex2 - ex7
'''
company = 'Coding For All'
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.swapcase())
print(company.title())
print(company[0:6])
print(company.index('All'))
print(company.rindex('All'))
print(company.replace('All', 'Everyone'))
str2 = 'I am enjoying this challenge. \n I just wonder what is next.'
print(str2)
'''
str3 = 'Name\t Age\t Country\t City \nArvind\t 28 \t India\t\t Mumbai'
print(str3)

radius = 10
area  = 3.14 * radius ** 2
print('The Radius of circle is : {} and area of circle is : {}'.format(radius,area))