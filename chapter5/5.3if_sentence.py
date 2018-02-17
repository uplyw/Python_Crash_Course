# 简单的if语句
age = 18;
if age >= 18:
	print('你成年了！')

# if-else
age1 = 17
if age1 >= 18:
	print('你成年了！')
else:
	print('你未成年！')

# if-elif-else

age2 = 18;
if age2 < 4:
	print('你是小屁孩')
elif 4 <= age2 < 18:
	print('你青年！')
else:
	print('你成年了！')


age3 = 12
if age3 < 4:
	price = 0
elif age3 < 18:
	price = 5
elif age3 < 65:
	price = 10
elif age3 >= 65:
	price = 5
print('your admission cost is $' + str(price) + '.')


# if-elif-else只能判断一个条件  一个条件成立后跳出表达式
# 但是有时我们要测试多个条件并使用
fruits =  ['apple','banana']
if 'apple' in fruits:
	print('heihei')
if 'pear' in fruits:
	print('xixi')
if 'banana' in fruits:
	print('haha')