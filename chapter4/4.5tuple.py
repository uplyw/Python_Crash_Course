#元组
#元组是不可变的列表
#和列表不同的是元组使用圆括号来标识，而非方括号
fruits = ('banana','apple','orange','kiwi','coco')
print(fruits)
print(fruits[2])
print(fruits[4])

#元组是不可变的  因此改变元组内的元素是会报错
# fruits[1] = 'qqqq'


#不过可以通过改变元组的整体  来改变
fruits = ('aaa','bbb','ccc','ddd')
print(fruits)