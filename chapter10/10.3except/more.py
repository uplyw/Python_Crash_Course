filename = 'alice.txt'
with open(filename) as f_obj:
	contents = f_obj.read()

print(contents.count('Alice'))
print(contents.lower().count('alice'))