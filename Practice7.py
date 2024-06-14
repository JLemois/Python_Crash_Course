seperator = '\r\n' + '_' * 60 + '\r\n'

# Header
print('\r\n' + '=' * 60 + '\r\n\nPython Crash Course practice work By: Joseph Lemois')
print(seperator)


class Restaurant:
    # Restaurant class creation that has name and description
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine = cuisine
        self.number_served = 0
        self.star_rating = 3

    def describe_restaurant(self):
        print(f'The restaurant {self.restaurant_name} serves really good {self.cuisine}.')

    def open_restaurant(self):
        print(f'The restaurant {self.restaurant_name} is now open for business.\n')

    def set_number_served(self, number_served):
        if number_served >= self.number_served:
            self.number_served = number_served
            print(f'The restaurant {self.restaurant_name} has served {self.number_served}')
        else:
            print('You can\'t decrease the amount of people you\'ve already served.')

    def increment_number_served(self, guests):
        self.number_served += guests
        print(f'The restaurant {self.restaurant_name} served {guests} more guests.'
              f'\nThe new total number of guests served is {self.number_served}')

    def set_star_rating(self, star_rating):
        if star_rating >= self.star_rating:
            self.star_rating = star_rating
            print(f'{self.restaurant_name} has a star rating of {self.star_rating}.')

    def alter_star_rating(self, stars):
        if stars > self.star_rating:
            self.star_rating = stars
            print(f'{self.restaurant_name} has improved it\'s star rating to {self.star_rating}.')
        elif stars == self.star_rating:
            print(f'{self.restaurant_name} had no change in its star rating.')
        else:
            self.star_rating = stars
            print(f'{self.restaurant_name} has decreased its star rating to {self.star_rating}.')


firstRestaurant = Restaurant('Romeos', 'Pizza')
firstRestaurant.describe_restaurant()
firstRestaurant.set_number_served(25)
firstRestaurant.increment_number_served(20)
firstRestaurant.set_number_served(10)  # test
firstRestaurant.open_restaurant()

secondRestaurant = Restaurant('Starbucks', 'Coffee')
secondRestaurant.describe_restaurant()
secondRestaurant.set_star_rating(4)
secondRestaurant.alter_star_rating(5)
secondRestaurant.open_restaurant()

thirdRestaurant = Restaurant('Smoothie King', 'Smoothies')
thirdRestaurant.describe_restaurant()
<<<<<<< HEAD
thirdRestaurant.alter_star_rating(2)  # default rating is 3
=======
thirdRestaurant.alter_star_rating(2) # default rating is 3
>>>>>>> origin/main
thirdRestaurant.open_restaurant()

print(seperator)


class User:
    # User Class that takes name and username with a greeting
    def __init__(self, first_name, last_name, user_name):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name

    def describe_user(self):
        print(f'Created the user {self.user_name} for {self.first_name} {self.last_name}.')

    def greet_user(self):
        print(f'Hello {self.user_name} and welcome!\n')


user1 = User('Joseph', 'Lemois', 'ColdFire')
user1.describe_user()
user1.greet_user()

user2 = User('Joe', 'Lemois', 'DarkSpark')
user2.describe_user()
user2.greet_user()

user3 = User('Josef', 'Lahmoy', 'Joe')
user3.describe_user()
user3.greet_user()

print(seperator)
