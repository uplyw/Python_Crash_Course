def word_count(filename):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		print("没有找到 " + filename)
	else:
		words = contents.split()
		num_words = len(words)
		print(num_words)

# filename = 'alice.txt'
# word_count(filename)
filenames = ['alice.txt','siddhartha.txt','little_women.txt','moby_dick.txt']
for filename in filenames:
	word_count(filename)