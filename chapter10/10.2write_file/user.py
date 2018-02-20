filename = 'guest.txt'


while True:
	username = input('please input your name:')
	print('hello ' + username)
	with open(filename,'a') as file_object:
		file_object.write(username + "\n")