
# Exercises Continued

# Header
print('\r\n'+'='*60+'\r\n\nPython Crash Course practice work By: Joseph Lemois')
print('\r\n'+'_'*60+'\r\n')

# Create dictionary of person
# exercise requested per line print
person1 = {'FirstName': 'Joseph', 'LastName': 'Lemois', 'Age': 36, 'Gender': 'Male', 'City': 'Greenville'}
for element in person1.items():
    print(element)

print(f'\n{person1["FirstName"]} {person1["LastName"]} aged {person1["Age"]} is a {person1["Gender"]} '
      f'living in the city of {person1["City"]}.\n')

# peoples favorite number
# exercise requested per line
print('People and their lucky numbers.')
peopleNumbers = {'Joe': 13,
                 'Miles': 16,
                 'Shay': 7,
                 'Joseph': 2,
                 'Jules': 22}
for element in peopleNumbers.items():
    print(element)

print('\r\n'+'_'*60+'\r\n')

# Book example
favorite_language = {'jen': 'python',
                     'sarah': 'c',
                     'edward': 'rust',
                     'phil': 'python'}
friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(f'Hi {name.title()}.')
    if name in friends:
        language = favorite_language[name].title()
        print(f'\t{name.title()}, I see you like {language}.')
print()
# cleanup original dictionary prints from above
luckyNumber = [13, 7]
for people, number in peopleNumbers.items():
    print(f'{people} chose the number:\t{number}')
    if number in luckyNumber:
        print(f'\t{people} is lucky.')

print('\r\n'+'_'*60+'\r\n')
# create 2 more people than add all 3 (top one) to new list
person2 = {'FirstName': 'Joe', 'LastName': 'Leemuss', 'Age': 21, 'Gender': 'Male', 'City': 'Charleston'}
person3 = {'FirstName': 'Jon', 'LastName': 'Smith', 'Age': 25, 'Gender': 'Female', 'City': 'Spartanburg'}
people = [person1, person2, person3]
for individual in people:
    print(f'{individual["FirstName"]} {individual["LastName"]} is a {individual["Age"]} '
          f'year old {individual["Gender"]} '
          f'that lives in {individual["City"]}.')
