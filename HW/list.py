
films = {
    'finding nemo': {
        'age':10,
        'seats':40
    },
    'spooderman': {
        'age':17,
        'seats':10
    },
    '5gang': {
        'age':2,
        'seats':0
    },
    'hannah montana': {
        'age':7,
        'seats':70
    },
    'lord of the rings': {
        'age':18,
        'seats':5
    },
    'hobbit': {
        'age':18,
        'seats':15
    },
    'overwatch': {
        'age':21,
        'seats':3
    },
    '2 and a half men': {
        'age':20,
        'seats':40
    },
    'dr. house': {
        'age':19,
        'seats':10
    },
    'corona the sequel': {
        'age':100,
        'seats':1
    },
    
}
user_age = int(input('How old are you? '))
movie_select = 0
while movie_select == 0:
    print('Movies available: nemo, spooderman, 5gang, hannah montana, LOTR, hobbit, overwatch, 2 and a half men, dr. house, corona')
    user_movie = input('Please select what movie you would like to watch. ')
    if user_movie == 'nemo':
        if films['finding nemo']['age'] <= user_age and films['finding nemo']['seats'] > 0:
            movie_select = 1
            print('This movie is available! Have fun!')
    elif user_movie == 'spooderman':
        if films['spooderman']['age'] <= user_age and films['spooderman']['seats'] > 0:
            movie_select = 1
            print('This movie is available! Have fun!')
    elif user_movie == '5gang':
        if films['5gang']['age'] <= user_age and films['5gang']['seats'] > 0:
            movie_select = 1
            print('This movie is available! Have fun!')
    elif user_movie == 'hannah montana':
        if films['hannah montana']['age'] <= user_age and films['hannah montana']['seats'] > 0:
            movie_select = 1
            print('This movie is available! Have fun!')
    elif user_movie == 'LOTR':
        if films['lord of the rings']['age'] <= user_age and films['lord of the rings']['seats'] > 0:
            movie_select = 1
            print('This movie is available! Have fun!')
    elif user_movie == 'hobbit':
        if films['hobbit']['age'] <= user_age and films['hobbit']['seats'] > 0:
            movie_select = 1
            print('This movie is available! Have fun!')
    elif user_movie == 'overwatch':
        if films['overwatch']['age'] <= user_age and films['overwatch']['seats'] > 0:
            movie_select = 1
            print('This movie is available! Have fun!')
    elif user_movie == '2 and a half men':
        if films['2 and a half men']['age'] <= user_age and films['2 and a half men']['seats'] > 0:
            movie_select = 1
            print('This movie is available! Have fun!')
    elif user_movie == 'dr. house':
        if films['dr. house']['age'] <= user_age and films['dr. house']['seats'] > 0:
            movie_select = 1
            print('This movie is available! Have fun!')
    elif user_movie == 'corona':
        if films['corona the sequel']['age'] <= user_age and films['corona the sequel']['seats'] > 0:
            movie_select = 1
            print('This movie is available! Have fun!')
    if movie_select == 0:
        print('Your selected movie is not available. Please try at a later date.')