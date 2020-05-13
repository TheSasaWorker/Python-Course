import home_md_diagnostic as dtool

print('Welcome to the Home MD Diagnostic tool!')
user_symptoms = dtool.get_symptom_list()
user_info = dtool.get_user_info()
diag = dtool.diagnostic(user_symptoms, user_info)
print('Possible diseases you may have:')
dtool.print_possible_disease(diag)
print('Your most probable disease:')
print(dtool.find_by_chance(diag))