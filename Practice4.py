# Exercises Continued

seperator = '\r\n'+'_'*60+'\r\n'

# Header
print('\r\n'+'='*60+'\r\n\nPython Crash Course practice work By: Joseph Lemois')
print(seperator)

# ask user number then check against another
userInput = input("Please enter how many people will be in your party: ")
userInput = int(userInput)
if userInput > 8:
    print(f'Sorry, your party of {userInput} people will have to wait on a table.')
else:
    print(f'We can seat your party of {userInput} as soon as the next table is cleaned.')

print(seperator)
# use modulo to check users input if multiple of 10
theInput = input("Please enter a number to check if divisible by 10: ")
theInput = int(theInput)
if theInput % 10 == 0:
    print(f'The number {theInput} is divisible by 10.')
else:
    print(f'The number {theInput} is not divisible by 10.')

print(seperator)

# input to determine price of ticket for user
print('The price for entry is dependent on your age. Once done checking prices type quit.')
keepGoing = True
while keepGoing:
    userInput = input("How old are you? ")
    if userInput == 'quit':
        keepGoing = False
        print("\nThank you! Goodbye.\n")
    else:
        userInput = int(userInput)
        if userInput <= 3:
            price = 'Free'
        if userInput > 3 & userInput <= 12:
            price = '$10'
        if userInput > 12:
            price = '$15'
        print(f'The price of entry for the age of {userInput} is {price}.')

print(seperator)

# Make list of sandwiches then loop through 'completed' sandwiches to another list
print('\nList of sandwich orders: ')
sandwich_orders = ['pastrami', 'pastrami', 'pastrami', 'italian', 'italian', 'italian', 'meatball', 'meatball',
                   'meatball', 'club', 'club']
for order in sandwich_orders:
    print(order)
completed_orders = []

print('\nMoving orders to a completed list.')
while sandwich_orders:
    order = sandwich_orders.pop()
    completed_orders.append(order)
print('\nThese orders have been completed: ')
for order in completed_orders:
    print(order.title())

print('\nWe have sadly run out of pastrami sandwiches, updating completed orders: ')
while 'pastrami' in completed_orders:
    completed_orders.remove('pastrami')
for order in completed_orders:
    print(order.title())