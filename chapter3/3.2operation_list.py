#修改列表元素
fruits = ['apple','banana','orange','pear']
print(fruits)

# 根据索引改变列表中元素的值
fruits[0] = 'mango'
print(fruits)

# 在列表末尾添加一个元素
fruits.append('kiwifruit')
print(fruits)

# 根据索引在列表中插入一个元素
fruits.insert(2, 'coconut')
print(fruits)

# 根据索引删除列表中的一个元素
del fruits[0]
print(fruits)

# pop() 弹出   列表中剔除元素，但元素还可以用
fru_pop = fruits.pop()
print(fruits)
print(fru_pop)

# pop(index) 按索引弹出列表中的元素
fruits1 = ['apple','banana','orange','pear','kiwi','coco']
print(fruits1)
fru1_pop = fruits1.pop(2)
print(fruits1)
print(fru1_pop)
print('i like eat '+fru1_pop)

#练习
people = ['zhao','qian','sun','li']
print(people)
print(people[0])
people[0] = 'zhou'
print(people)
people.append('wu')
people.insert(0,'zheng')
people.insert(3,'wang')
print(people)
del people[0]
print(people)
people1 = people.pop()
print(people)

#remove() 指定列表中要删除的元素而不是索引
people2 = people.remove('wang')
print(people)