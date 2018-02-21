print("input two number!")
while True:
	first_number = input("first_number:")
	secoud_number = input("secoud_number:")
	try:
		result = int(first_number) + int(secoud_number)
	except ValueError:
		print("please input number")
	else:
		print(result)