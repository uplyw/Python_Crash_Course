#定义函数  def

def greet_user():
	"""这是什么"""
	print('hello')
greet_user()


#向函数传递信息
def greet_user1(username):
	print('hello,' + username.title())
greet_user1('li')
greet_user1('zhao')

def display_message():
	print('学习了定义函数，形参和实参')
display_message()

def favorite_book(title):
	print('one of my favorite book is ' + title)
favorite_book('alice in wonderland')
