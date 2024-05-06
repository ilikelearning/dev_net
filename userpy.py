import yaml
from pprint import pprint

with open('user.yaml', 'r') as file:
	data = yaml.safe_load(file)
#pprint(data)
print(data)
user = data['user']
print(user['name'])

for role in user['roles']:
	print(role)


user['location']['city'] = 'Califonia'

with open('userpy_edited', 'w') as fl:
	yaml.dump(data,fl,default_flow_style=False)

