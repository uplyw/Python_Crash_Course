#切片 顾名思义  切取列表中的片段元素
fruits = ['apple','banana','orange','pear','kiwi','coco']
print(fruits)

#切取 列表中前三个元素
print(fruits[0:3])
print(fruits[:3])

#切取 列表中第三个元素以后的所有元素
print(fruits[3:])

#切取 列表中后三个元素
print(fruits[-3:])


#遍历切片
for fruit in fruits[4:]:
	print(fruit)

#复制一个列表
new_fruits = fruits[:]
print(new_fruits)
fruits.append('fruit1')
new_fruits.append('fruit2')
print(fruits)
print(new_fruits)

#  ！！！ 不能直接使用赋值的方法复制列表
