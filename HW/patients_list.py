import json
from openpyxl import Workbook
import string
wbook = Workbook()
wsheet = wbook.active
wsheet.title = 'Changed Sheet'
#patients list
patients = {
    'neagu': {
        'id': '123',
        'doctor': 'ivascu',
        'patient': 'neagu lucian',
        'nurses': 'abby, cindy',
        'health': 'depression',
        'days hospitalized': 7
    },
    'grumeza': {
        'id': '000',
        'doctor': 'radu',
        'patient': 'grumeza diana',
        'nurses': 'abby, chase',
        'health': 'pristine',
        'days hospitalized': 9999
    },
    'relu': {
        'id': '999',
        'doctor': 'house',
        'patient': 'nechita relu',
        'nurses': 'cameron, chase',
        'health': 'OCD',
        'days hospitalized': 20
    },
    'stirbu': {
        'id': '456',
        'doctor': 'radu',
        'patient': 'stirbu mihaela',
        'nurses': 'cindy, foreman',
        'health': 'obesity',
        'days hospitalized': 5
    },
    'imbria': {
        'id': '222',
        'doctor': 'ivascu',
        'patient': 'imbria adina',
        'nurses': 'foreman, chase',
        'health': 'tb',
        'days hospitalized': 30
    },
    'zepciuc': {
        'id': '777',
        'doctor': 'who',
        'patient': 'zepciuc ion',
        'nurses': 'ladunca, treboniu',
        'health': 'muscle infarction',
        'days hospitalized': 14
    },
    'sorohan': {
        'id': '321',
        'doctor': 'radu',
        'patient': 'sorohan vasile',
        'nurses': 'ladunca, cindy',
        'health': 'meningitis',
        'days hospitalized': 21
    },
    'foca': {
        'id': '873',
        'doctor': 'ivascu',
        'patient': 'foca mirela',
        'nurses': 'chase, ladunca',
        'health': 'accident with spring',
        'days hospitalized': 40
    },
    'adamut': {
        'id': '878',
        'doctor': 'who',
        'patient': 'adamut luminita',
        'nurses': 'treboniu, abby',
        'health': 'stabbed',
        'days hospitalized': 22
    },
    'ouatu': {
        'id': '239',
        'doctor': 'house',
        'patient': 'ouatu madalina',
        'nurses': 'abby, cameron',
        'health': 'alzheimer\'s',
        'days hospitalized': 50
    },

}
wsheet['A1'] = 'id'
wsheet['A2'] = 'doctor'
wsheet['A3'] = 'patient'
wsheet['A4'] = 'nurses'
wsheet['A5'] = 'health'
wsheet['A6'] = 'days hosp.'
row = 1
for x in patients:
    col = 1
    for y in patients[x]:
        #col to letter
        col_let = string.ascii_uppercase[col-1]
        wsheet[col_let + str(row)] = patients[x][y]
        col += 1
    row += 1
wbook.save(filename='patients_list.xlsx')