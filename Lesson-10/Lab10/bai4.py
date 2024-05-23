names = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName': 'Friedland'},
        {'firstName': 'Aron', 'lastName': 'Wilkins'}
        ],
        'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}
    ]
}


# bai 4:

# print(f'List of students:\n- {'\n- '.join([f'{i['firstName']} {i['lastName']}' for i in names['students']])}')


# bai 5:

print(f'List of students:\n- {'\n- '.join([f'{i['firstName']} {i['lastName']}' for i in names['students']])}\nList of teachers:\n- {'\n- '.join([f'{i['firstName']} {i['lastName']}' for i in names['teachers']])}')