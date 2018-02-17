#使用字典
alien_0 = {'color':'green'}
print(alien_0['color'])
print('\n')

#往字典里添加键值对
alien_1 = {'color':'green','points':5}
print(alien_1)						#{'color': 'green', 'points': 5}
alien_1['x_position'] = 0
alien_1['y_position'] = 5
print(alien_1)						#{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 5}
print('\n')


# 修改字典里的值
alien_2 = {'color':'green','points':5}
alien_2['color'] = 'yellow'
print(alien_2);						#{'color': 'yellow', 'points': 5}
print('\n');

alien_3 = {'x_position':0,'y_position':25,'speed':'medium'}
print('old x_position: ' + str(alien_3['x_position']))
if alien_3['speed'] == 'slow':
	x_increment = 1
elif alien_3['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_3['x_position'] = alien_3['x_position'] + x_increment;
print('new x_position：' + str(alien_3['x_position']))
print('\n')
#删除键值对
# del 删除键值对 是永久删除  不可恢复
alien_4 = {'color':'green','points':5}
del alien_4['points']				#删除键为 ‘points’
print(alien_4)						#{'color': 'green'}
print('\n')

#练习
friend = {
	'name':'li',
	'sex':'man',
	'age':20,
	'city':'huizhou',
	}
print(friend['name'])
print(friend['sex'])
print(friend['age'])
print(friend['city'])
love_num = {
	'li':3,
	'zhao':6,
	'qian':9,
}