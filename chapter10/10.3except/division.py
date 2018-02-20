# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("you can't divide by zero!")


print("give me two number:")
print("enter 'q' to quit")
while True:
	first_num = input("first number:")
	if first_num == 'q':
		break
	secoud_num = input("secoud number:")
	if secoud_num == 'q':
		break
	try:
		answer = int(first_num) / int(secoud_num)
	except ZeroDivisionError:
		print('you can not')
	else:
		print(answer)
	
