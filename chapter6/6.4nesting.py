aliens_0 = {'color':'green','points':5}
aliens_1 = {'color':'yellow','points':10}
aliens_2 = {'color':'red','points':15}

aliens = [aliens_0,aliens_1,aliens_2]
for alien in aliens:
	print(alien)

print('\n')

aliens1 = []
for alien_number in range(30):
	new_aliens = {'color':'yellow','points':5}
	aliens1.append(new_aliens)
# print(aliens1)
for alien1 in aliens1[:5]:
	print(alien1)

print('\n')
aliens2 = []
for alien2_num in range(1,30):
	new_aliens2 = {'color':'green','points':5,'speed':'slow'}
	aliens2.append(new_aliens2)
for alien2 in aliens2[0:3]:
	if alien2['color'] == 'green':
		alien2['color'] = 'yellow'
		alien2['points'] = 10
		alien2['speed'] = 'medium'

for alien2 in aliens2[0:5]:
	print(alien2)

print('\n')
pizza = {
	'crust':'thick',
	'toppings':['mushrooms','extra cheese']
}
print(pizza['crust'] + '-crust pizza')
for topping in pizza['toppings']:
	print(topping)


favorite_languages = {
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','java'],
}
for n,l in favorite_languages.items():
	print(n.title() + 'like:')
	for lang in l:
		print('\t' + lang)

print('\n')
users = {
	'li':{
		'first':'li',
		'last':'si',
		'location':'beijing'
	},
	'wu':{
		'first':'wu',
		'last':'san',
		'location':'shanghai'
	}
}
for username,userinfo in users.items():
	print('\nusername:' + username)
	print('full name :' + userinfo['first'] + ' ' + userinfo['last'])
	print('location:' + userinfo['location'])