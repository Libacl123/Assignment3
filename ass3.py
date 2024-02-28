d = [
    {'id': 1, 'name': 'Kannur'},
    {'id': 2, 'name': 'Malappuram'},
    {'id': 3, 'name': 'Kollam'},
    {'id': 4, 'name': 'Alappuzha'},
    {'id': 5, 'name': 'Kottayam'}
]

target_id = 4

fildata = list(filter(lambda item: item["id"] == target_id, d))
print(fildata)

