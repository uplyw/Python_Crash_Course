filename = 'fruits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())


for line in lines:

	l = line.replace('like','heat')

	print(l.rstrip())