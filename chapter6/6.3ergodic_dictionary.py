#遍历字典
user_0 = {
	'username':'admin',
	'first':'ad',
	'last':'min',
}
for key,value in user_0.items():
	print('\nkey:' + key)
	print('value:' + value)

favorite_language = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}
for name,language in favorite_language.items():
	print(name.title()+' like ' + language)
# 遍历字典中 的键
for name in favorite_language.keys():
	print(name)