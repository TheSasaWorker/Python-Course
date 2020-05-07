films_list = {
    'Star Wars':{
        'id': 'SW',
        'min_age': 14,
        'seats': 0,
        'price': 23
    },
    'Terminator':{
        'id': 'TMR',
        'min_age': 18,
        'seats': 10,
        'price': 25
    },
    'John Wick 4':{
        'id': 'JW4',
        'min_age': 15,
        'seats': 30,
        'price': 19
    }
}

def movie_select():
    while True:
        print('Please select which movie you would like to watch.')
        user_input = input().strip().lower()
        if user_input == 'star wars':
            return 'Star Wars'
            print('You have selected Star Wars.')
            break
        elif user_input == 'terminator':
            return 'Terminator'
            print('You have selected Terminator.')
            break
        elif user_input == 'john wick 4':
            return 'John Wick 4'
            print('You have selected John Wick 4')
            break
        else:
            print('Please input one of the movies we have available.')

def age_select():
    while True:
        print('How old are you?')
        user_input = input().strip()
        try:
            user_age = int(user_input)
            return user_age
            break
        except:
            print('Please insert an actual age.')

def money_select():
    while True:
        print('How much money are you willing to pay (in $)?')
        user_input = input().strip()
        try:
            user_money = int(user_input)
            return user_money
            break
        except:
            print('Please insert an actual amount.')
def availability_check(movie, age, money):
    if films_list[movie]['min_age'] > age:
        valid_movie = 0
        print('Your age is below the minimum required.')
    if films_list[movie]['seats'] == 0:
        valid_movie = 0
        print('There are no seats left.')
    if films_list[movie]['price'] > money:
        valid_money = 0
        print('You are unable to afford this movie.')
    if valid_movie == 0:
        return 0
    else:
        return 1


print('Welcome to Cinema Town!')
print('Here is a list of our active movies:\nStar Wars\nTerminator\nJohn Wick 4')
chosen_movie = movie_select()
chosen_age = age_select()
chosen_money = money_select()
if availability_check(chosen_movie, chosen_age, chosen_money) == 1:
    print('You are free to go!')
else:
    print('You are unable to go to the movie for the reason(s) above.')
