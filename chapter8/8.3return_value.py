# 返回简单值
# def get_formatted_name(first_name,last_name):
# 	full_name = first_name + ' ' + last_name
# 	return full_name.title()
# musician = get_formatted_name('li', 'lei')
# print(musician)

# 让实参可选
# def get_formatted_name(first_name,last_name,middle_name = ''):
# 	if middle_name:
# 		full_name = first_name + ' ' + middle_name + ' ' + last_name
# 	else:
# 		full_name = first_name + ' ' + last_name
# 	return full_name.title()
# musician = get_formatted_name('jimi','hendrix')
# print(musician)
# musician = get_formatted_name('jimi', 'hooker','lee')
# print(musician)

#返回字典
# def build_person(first_name,last_name):
# 	person = {'first':first_name,'last':last_name}
# 	return person
# musician = build_person('jimi', 'hendrix')
# print(musician)

# def build_person(first_name,last_name,age = ''):
# 	person = {'first':first_name,'last':last_name}
# 	if age:
# 		person['age'] = age
# 	return person
# musician = build_person('jimi', 'hendrix')
# print(musician)
# musician = build_person('jimi', 'hendrix', age = 18)
# print(musician)


# 结合使用函数和while循环
# def get_formatted_name(first_name,last_name):
# 	full_name = first_name + ' ' + last_name
# 	return full_name
# while True:
# 	print('\nplease tell me your name?')
# 	f_name = input('your first name:')
# 	l_name = input('your last name:')
# 	formatted = get_formatted_name(f_name, l_name)
# 	print('hello ' + formatted)

# def get_formatted_name(first_name,last_name):
# 	full_name = first_name + ' ' + last_name
# 	return full_name
# active = True
# while active:
# 	print('\nplease tell me your name?')
# 	print('enter "q" to be end')
# 	f_name = input('your first name:')
# 	if f_name == 'q':
# 		active = False
# 	l_name = input('your last name:')
# 	if l_name == 'q':
# 		active = False
# 	formatted = get_formatted_name(f_name, l_name)
# 	print(formatted)

# def get_formatted_name(first_name,last_name):
# 	full_name = first_name + ' ' + last_name
# 	return full_name
# while True:
# 	print('\nplease tell me your name?')
# 	print('enter "q" to be end')
# 	f_name = input('your first name:')
# 	if f_name == 'q':
# 		break
# 	l_name = input('your last name:')
# 	if l_name == 'q':
# 		break
# 	formatted = get_formatted_name(f_name, l_name)
# 	print(formatted)

# 练习
# def city_country(city,country):
# 	print(city + ' 属于 ' + country)
# city_country('纽约', '美国')
# city_country('台北', '中国')
# city_country('香港', '中国')

# def song_singer(song,singer):
# 	song_info = {'song_name':song,'singer_name':singer}
# 	return song_info
# songs = song_singer('成都', '赵雷')
# print(songs)


# def song(song,singer,genre=''):
# 	song_info = {'song_name:':song,'singer_name:':singer}
# 	if genre:
# 		song_info['genre:'] = genre
# 	return song_info
# songs = song('成都', '赵雷')
# print(songs)
# songs = song('七月下', 'jam','民谣')
# print(songs)

def song_info(song_name,singer_name):
	songs = 'you like ' + singer_name + "'s " + song_name
	return songs

while True:
	print('\nplease input you like song and singer:')
	print('enter "q" to end')
	song = input('song:')
	if song == 'q':
		break
	singer = input('singer:')
	if song == 'q':
		break
	songsinger = song_info(song, singer)
	print(songsinger)