from name_function import get_formatted_name

print("enter 'q' to quit" )
while True:
	first = input("your first name:")
	if first == 'q':
		break
	last = input("your last name:")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print("fullname:" + formatted_name)