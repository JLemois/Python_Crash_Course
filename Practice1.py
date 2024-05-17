# Basic exercises from Python Crash Course 3rd edition

# my name as variable, then printed out
theName = "Joseph Lemois"
print(f"\nHello {theName}, and welcome to Python programming!\n")

# name printed in upper, lower, and title case
print(theName.upper())
print(theName.lower())
print(theName.title() + "\n")

# my own thoughts on my work ethic in variable then printed
theQuote = "I am \"proactively lazy\", that is to say that I completely do a task to get back to doing nothing."
print(theQuote + "\n")

# printout of my quote followed by my name using variables
print(f"{theQuote}\n~{theName}\n")

# whitespace stripping exercise
spacedName = "    Joseph Lemois    "
print(spacedName.lstrip())
print(spacedName.rstrip())
print(spacedName.strip() + "\n")

# prefix and suffix removal exercises
fileName = "Python_Notes.txt"
print(fileName.removesuffix(".txt") + "\n")
print(f"The file \"{fileName.removesuffix('.txt')}\" has the extension {fileName.removeprefix('Python_Notes')}.")

# equations to equal 8 followed by favorite number and printout statement
print(6 + 2)
print(12 - 4)
print(96 / 12)
print()
favoriteNumber = 13
print(f"My favorite number is {favoriteNumber}!\n")

# list practice using names
listOfNames = [theName, "Harry Potter", "Miles Morales", "Peter Parker"]
print(listOfNames)
print()

# used for loop to display welcome message to each member on list
for i in range(len(listOfNames)):
    print(f"Hello {listOfNames[i]}, and welcome to Python programming!\n")

dinnerNames = ["Eminem", "Royce da 5 9", "You"]
print(f"I would like to invite {dinnerNames[0]} and {dinnerNames[1]} to dinner.")

# playing around with different list options and printing it out
notInvited = "You"
addedInvite = "Someone else"
print(f"{notInvited} are no longer allowed to to join me for dinner. {addedInvite} will be joining us instead.")
dinnerNames.remove(notInvited)
dinnerNames.append(addedInvite)
print(f"The current list of dinner party members are: {dinnerNames}")
dinnerNames.sort(reverse=True)
print(f"The reverse sorted list is {dinnerNames}")
dinnerNames.insert(2, notInvited)
print(sorted(dinnerNames))
dinnerNames.pop(2)
print(dinnerNames)
dinnerNames.pop(2)
print(dinnerNames)
dinnerNames.insert(0, "Eminem")
dinnerNames.remove(addedInvite)
print(dinnerNames)
