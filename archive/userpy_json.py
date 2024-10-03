import json
from pprint import pprint

with open('user.json', 'r') as file:
	data = json.load(file)
#pprint(data)
print(data)
user = data['user']
print(user['name'])

for role in user['roles']:
	print(role)


user['location']['city'] = 'Dallas'

with open('userpy_edited', 'w') as fl:
	json.dump(data,fl,indent=4)


