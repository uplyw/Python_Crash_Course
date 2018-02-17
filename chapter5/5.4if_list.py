# 处理列表
fruits = ['apple','banana','orange','kiwi']
for fruit in fruits:
	if fruit == 'banana':
		print('no banana')
	else:
		print('have' + fruit)

print('\n')
# 确定列表不为空
fruits1 = []
if fruits1:
	for fruit1 in fruits1:
		print('have' + fruit1)
else:
	print('no no no')


fruits2 = ['apple','banana','kiwi','coco','pear']
fruits3 = ['apple','banana','orange']

for fruit3 in fruits3:
	if fruit3 in fruits2:
		print('have ' + fruit3)
	else:
		print('not hove ' + fruit3)


print('\n')
#练习 - 动手试一试

users = ['zhao','qian','admin','sun','li']
#判断列表是否为空
if users:
	#遍历列表
	for user in users:
		#判断列表中'admin'用户，打印特殊语句
		if user == 'admin':
			print('Hello ' + user.title() + ',would you like to see a status report?')
		else:
			print('Hello ' + user.title() + ',thank you for logging in again!')
else:
	print('we need to find some users!')


print('\n');
#判断用户是否存在
current_users = ['zhao','qian','sun','li','zhang']
new_users = ['Zhou','Sun','wu','zheng','zhang']

for new_user in new_users:
	if new_user.lower() in current_users:
		print(new_user + ' user exist')
	else:
		print('can add user ' + new_user)

print('\n')
#输出一到九的序数
num = list(range(1,10))
for n in num:
	if n == 1:
		print(str(n) +'st')
	elif n == 2:
		print(str(n) + 'nd')
	elif n == 3:
		print(str(n) + 'rd')
	else:
		print(str(n) + 'th')