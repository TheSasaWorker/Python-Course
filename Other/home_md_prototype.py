#GET USER SYMPTOM

def get_symptom_from_input(symptom_input):     # function to check if input is valid symptom
    symptom_input.strip()

    # symptoms list
    symptoms = ['sneezing', 'coughing', '38 fever', '40 fever', 'rash', 'nausea', 'sweating', 'dizziness', 'shortness of breath', 'slurred speech', 'chest pain', 'headache', 'vomiting', 'numbness', 'back pain', 'tachycardia', 'bradycardia', 'jaundice', 'dysphagia', 'sore throat', 'stomach pain', 'hematuria', 'hypergonadism', 'hypogonadism', 'diarrhea', 'bloating', 'constipation', 'blood in stool', 'cold extremities', 'tingling', 'spasms', 'runny nose', 'nose bleed', 'ear ringing', 'decreased hearing', 'subconjunctival hemorrhage', 'memory loss', 'twitching', 'hair loss', 'unconsciousness']
    #symptoms list

    if symptom_input not in symptoms:           
        return 0                                # not actual symptom, asks for more input
    else:
        return 1                                # valid symptom, continues loop
#GET USER SYMPTOM

# PHASE 1(SYMPTOMS)
def get_symptom_list():
    user_symptoms_list = []
    print('Phase 1 - symptoms')
    while True:
        user_input = input('If you wish to continue to the 2nd phase, type \'END\'. Otherwise, continue adding more symptoms.').strip()
        if user_input == 'END':
            break
        else:
            if get_symptom_from_input(user_input) == 0:
                print('Please insert a valid symptom. You can find a list of symptoms over at our website.')
            elif get_symptom_from_input(user_input) == 1:
                print('Your symptom has been added to the database.')
                user_symptoms_list.append(user_input)
    return user_symptoms_list
# PHASE 1(SYMPTOMS)

# GET USER AGE FUNC

def find_user_age():
    while True:             # loop until valid age
        print('Please insert your age.')
        user_age = input().strip()
        try:                # tests if input is int
            user_age = int(user_age)
            if user_age > 110 or user_age < 0:              # tests if user is a moron
                print('Your inserted age is not valid.')
            else:
                break                   # valid age, stops loop
        except:                                       # if not int gives error, hence try/except
            print('You have not inserted an age.')
    return user_age

# GET USER AGE FUNC

# GET USER COUNTRY FUNC

def find_user_country():
    while True:             # loop until valid country code
        print('Please insert your country\'s initials(2 long)')
        user_country = input().strip()
        try:                                # tests if input is an int
            user_country = int(user_country)                # if int() doesn't give error it means it's an int, therefore not cc
            print('You have not inserted a country code.')
        except:
            if len(user_country) == 2:
                print('Your country has been added to our database.')
                break
            else:
                print('Please insert a valid country code.')
    return user_country

# GET USER COUNTRY FUNC

# GET USER GENDER FUNC

def find_user_gender():
    while True:         # loop until user inserts valid gender
        print('Please insert your gender. M/F')
        user_gender = input().strip()
        if user_gender == 'F' or user_gender == 'M':
            print('Your gender has been added to our database.')
            break                                                           # valid gender, stops loop
        else:
            print('Please insert a valid gender.')                          # invalid gender, continues loop
    return user_gender

# GET USER GENDER FUNC

# PHASE 2(GENERAL INFO)
def get_user_info():
    user_info = {
        'age': -1,
        'country': 'placeholder',
        'gender': 'placeholder'
    }          # dict containing user info
    print('Phase 2 - general info')
    user_info['age'] = find_user_age()                   #  3 functions
    user_info['country'] = find_user_country()           #  to find
    user_info['gender'] = find_user_gender()             #  user info
    return user_info

# PHASE 2(GENERAL INFO)

print('Welcome to the Home MD Diagnostic tool!')
user_symptoms = get_symptom_list()
user_info = get_user_info()
print(user_symptoms)
print(user_info)
