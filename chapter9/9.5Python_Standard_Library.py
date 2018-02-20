from collections import OrderedDict
from random import randint

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for key,value in favorite_languages.items():
	print(key + " " + value)

#练习

word = OrderedDict()
word['upper()'] = '字母大写'
word['lower()'] = '字母小写'
word['title()'] = '首字母大写'
word['range()'] = '范围内取值'

for k,v in word.items():
	print(k + ":" + v)



n = 10
while n > 0:
	x = randint(1, 20)
	print(x)
	n -= 1