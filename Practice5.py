seperator = '\r\n' + '_' * 60 + '\r\n'

# Header
print('\r\n' + '=' * 60 + '\r\n\nPython Crash Course practice work By: Joseph Lemois')
print(seperator)


# working with functions
def display_message(name):
    print(f'Hello {name.title()}, I have learned about different loop structures, user input, '
          f'and mathematics operations.')


display_message('shay')
print(seperator)


def make_shirt(size='Large', saying='I love Shirts'):
    print(f'You ordered a {size.title()} sized shirt that says: {saying.title()}')


make_shirt()
make_shirt('small', 'Today will be great!')

print(seperator)

def game_catalog(developer, title, hours=None):
    theGame = {'developer': developer, 'title': title}
    if hours:
        theGame['hours'] = hours
    return theGame


game1 = game_catalog('Square Enix', 'Final Fantasy 16','81')
game2 = game_catalog('ArrowHead', 'Helldivers')
game3 = game_catalog('Blizzard', 'Diablo 4', '231')

print(f'Game 1: {game1}\nGame 2: {game2}\nGame 3: {game3}')
print(seperator)

while True:
    print('\nPlease enter info on a game of your choice.\nEnter \'q\' at any time to quit\n')
    exitMessage = 'Thank you and goodbye!'

    yourDev = input('Please enter the Developer of the game: ')
    if yourDev.lower() == 'q':
        print(exitMessage)
        break

    yourGame = input('Please enter the title of the game: ')
    if yourGame.lower() == 'q':
        print(exitMessage)
        break

    yourHours = input('Please enter hours played in the game: ')
    if yourHours.lower() == 'q':
        print(exitMessage)
        break

    formatEntry = game_catalog(yourDev, yourGame, yourHours)
    print(formatEntry)

print(seperator)
