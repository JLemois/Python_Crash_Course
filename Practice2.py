import random as Random
# Exercises Continued

# Header
print('\r\n'+'='*60+'\r\n\nPython Crash Course practice work By: Joseph Lemois')
print('\r\n'+'_'*60+'\r\n')

# Create variable with color assignment, use if/else to run tests
alien_color = 'yellow'
if alien_color == 'yellow':
    print('The alien found is \'yellow\'.')
else:
    print('The alien found is not \'yellow\'.')

# recreate above but add points system to if/else structure
if alien_color == 'green':
    print('You earned 5 points for shooting this alien!')
else:
    print('You earned 10 points for shooting this alien!')

# recreate using elif
if alien_color == 'red':
    print('Red aliens grant 1 bonus point!')
elif alien_color == 'green':
    print('Green aliens grant 2 bonus points!')
else:
    print('This color alien does not offer bonus points!')

print('\r\n'+'_'*60+'\r\n')

# use if/elif/else to write stages of life statements
# using random int to prompt different responses
age = Random.randint(1, 100)
if age < 2:
    print(f'This person is a baby that is {age} years old.')
elif age >= 2 and age < 4:
    print(f'This person is a toddler that is {age} years old.')
elif age >= 4 and age < 13:
    print(f'This person is a kid that is {age} years old.')
elif age >= 13 and age < 20:
    print(f'This person is a teenager that is {age} years old.')
elif age >= 20 and age < 65:
    print(f'This person is an adult that is {age} years old.')
else:
    print(f'This person is an elder that is {age} years old.')

print('\r\n'+'_'*60+'\r\n')

# use 5 if/else to test against list
favorite_fruits = ['strawberry', 'banana', 'cantaloupe']
if 'strawberry' in favorite_fruits:
    print('I like strawberries the most!')
if 'banana' in favorite_fruits:
    print('I like bananas almost as much as I like strawberries.')
if 'cantaloupe' in favorite_fruits:
    print('Of the fruits I like to eat, cantaloupe comes in last.')
if 'kiwi' in favorite_fruits:
    print('I\'m not a fan of kiwi.')
if 'orange' in favorite_fruits:
    print('I really do not like oranges!')

print('\r\n'+'_'*60+'\r\n')

# Create list of users and print welcome message using loop and if condition for admin
# alter to check for blank list first
usernames = ['admin', 'Joe', 'Joseph', 'Louis', 'Harry']
if usernames:
    for username in usernames:
        if username == 'admin':
            print('Welcome admin, would you like a status report!')
        else:
            print(f'Welcome {username}, thank-you for logging in again!')
else:
    print('Sorry, you need to update your usernames first!')
print()

# create new user list to compare against original user list
new_usernames = ['Joe', 'ColdFire', 'DarkSpark', 'Joseph', 'TheBoss']
for new_username in new_usernames:
    if new_username in usernames:
        print(f'The username {new_username} is already in use!')
    else:
        print(f'Welcome {new_username}, thank you for creating an account with us!')

print('\r\n'+'_'*60+'\r\n')

#ordinal numbers list printing with if/else
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in num_list:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    else:
        print(f'{num}th')

print('\r\n'+'='*60+'\r\n\nPython Crash Course practice work By: Joseph Lemois')