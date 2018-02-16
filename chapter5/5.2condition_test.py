# 每条if语句的核心都是一个值为true或false的表达式
# 这个表达式被称为条件测试

# python用 '==' 检查值是否相等
# python在检测是否相等时区分大小写
# banana = 'Banana'
# banana == 'banana'			False
# banana.lower() == 'banana'	ture

# python用 '!=' 检查值是否不等
q = 'q'
if q != 'w':
	print('xixi')

# python 还为数字比较提供了 '<=' '>=' 比较符

# python 使用'and' 和 'or' 检查多个条件
# and  当所有条件都为真时  为真
# or   有一个条件为真  为真


#检查特定值是否在列表中
fruits = ['banana','apple','orange','pear']
kiwi = 'kiwi'
if kiwi not in fruits:
	print('heihei')


# 布尔表达式
# t = True;
# f = False;
