# 30 Days Of python: Day 8 - Dictionary


'''
dct1 = {'key1' : 'Value1', 'key2': 'Value2', 'key3': 'Value3'}
print(dct1.get('key4'))
print(dct1.keys())
print(dct1.values())
# dct1.pop('key1')
# dct1.popitem()          
# del dct1['key2']
print(dct1)
'''
# Excercise 
dog = {
    'name':'Sheru' ,
    'color': 'black',
    'breed' : 'labrodor',
    'age': '2'
}

student = {
    'first_name' : 'Arvind',
    'last_name' : 'Jaiswal',
    'gender': 'Male',
    'age': 30,
    'martial_status': False,
    'skills' : ['HTML', 'Python', 'Linux', 'AWS'],
    'address': {
        'City' : 'Mumbai',
        'Country' : 'India'
    }
}
print(len(student))
# print(student.get('skills'))
print(type(student['skills']))
student['skills'].append('Java')
student['skills'].append('Cloud')
keys = student.keys()
values = student.values()
print(keys)
print(values)
student.pop('first_name')
student.popitem()
print(student.items())