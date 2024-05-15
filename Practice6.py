
seperator = '\r\n' + '_' * 60 + '\r\n'

# Header
print('\r\n' + '=' * 60 + '\r\n\nPython Crash Course practice work By: Joseph Lemois')
print(seperator)

# create a list of messages then print
myMessages = [
    'Hello World!',
    'On the way!',
    'I love Python!',
    'Whats for dinner?'
]

mySentMessages = []


# Function to display list of messages
def show_messages(all_messages):
    print('Your current list of messages: ')
    for message in all_messages:
        print(message)
    print('End of your list of messages.')


# function that calls show_message function, then moves list to sent list and prints status of message
def send_messages(all_messages, sent_messages):
    show_messages(all_messages)
    print('\nList of messages that have been sent are: ')
    while all_messages:
        current_message = all_messages.pop()
        sent_messages.append(current_message)
    for message in sent_messages:
        print(f'This message has been sent: {message}')
    print()


send_messages(myMessages[:], mySentMessages)
show_messages(myMessages)
print(seperator)


# practice with functions that accept arbitrary arguments
def add_car(make, model, **car_info):
    car_info['car_make'] = make
    car_info['car_model'] = model
    return car_info


my_car = add_car('Toyota', 'Corolla', Color='Grey', Year='2011')
my_other_car = add_car('Toyota', 'Rav-4')
print(my_car, my_other_car)
print(seperator)
