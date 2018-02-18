# unconfirmaed_user = ['zhao','qian','sun','li']
# confirmaed_user = []
# while unconfirmaed_user:
# 	current_user = unconfirmaed_user.pop()
# 	print(current_user)
# 	confirmaed_user.append(current_user)
# for con in confirmaed_user:
# 	print('confirmaed:'+con)

#移除特定值
# pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)
# while 'cat' in pets:
# 	pets.remove('cat')

# print(pets)

# 调查问卷
# responses = {}
# polling_active = True
# while polling_active:
# 	name = input('what is your name?')
# 	response = input('do you like language?')
# 	responses[name] = response;
# 	repeat = input('would you like to let another person respond?(yes/no)')
# 	if repeat == 'no':
# 		polling_active = False

# for name,response in responses.items():
# 	print(name + ' would like ' + response)

# 练习
# sandwich_orders = ['smz1','smz2','smz3','smz4']
# finished_sandwichs = []
# while sandwich_orders:
# 	abc = sandwich_orders.pop()
# 	print(abc)
# 	finished_sandwichs.append(abc)
# for fin in finished_sandwichs:
# 	print(fin)

# fruits = ['apple','orange','banana','apple','kiwi','coco','apple']
# print('no apple')
# while 'apple' in fruits:
# 	fruits.remove('apple')
# print(fruits)

fruits = {}
active = True
while active:
	name = input('what is your name?')
	fruit = input('what is your like fruit?')
	fruits[name] = fruit
	next_one = input('next_one?(y/n)')
	if next_one == 'n':
		active = False
for name,fruit in fruits.items():
	print(name + ' like ' + fruit)