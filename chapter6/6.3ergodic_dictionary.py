#遍历字典
user_0 = {
	'username':'admin',
	'first':'ad',
	'last':'min',
}
for key,value in user_0.items():
	print('\nkey:' + key)
	print('value:' + value)

favorite_language = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}
for name,language in favorite_language.items():
	print(name.title()+' like ' + language)
# 遍历字典中 的键
for name in favorite_language.keys():
	print(name)

print('\n')
favorite_language1 = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}
friends = ['phil','sarah']
for name in favorite_language1.keys():
	print(name)
	if name in friends:
		print('hi,'+name)

print('\n')
#按顺序遍历字典中的键
favorite_language2 = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}
for name in sorted(favorite_language2.keys()):
	print('hi,' + name)

print('\n')
for language in favorite_language2.values():
	print(language)
print('\n')
for language in set(favorite_language2.values()):
	print(language)

print('\n')
#练习
word_form = {
	'upper()':'转化大写',
	'lower()':'转化小写',
	'title()':'首字母大写',
	'lstrip()':'去除左空格',
	'rstrip()':'去除右空格',
	'strip()':'去除左右空格',
	'str()':'转换为字符串类型',
	'append()':'添加',
	'del':'删除',
	'pop()':'弹出',
	'sort()':'永久重新排序',
	'sorted()':'临时重新排序',
	'reverse()':'倒序',
	'len()':'长度',
	'range()':'生成区间内数字列表',
	'players()':'切片-截取列表片段',
	'keys()':'遍历字典中的键',
	'values()':'遍历字典中的对',
	'items()':'返回字典中的键值对',
	'set()':'过滤列表中重复项'
}
for k,v in word_form.items():
	print(k + ':' + v)

print('\n')
rivers = {
	'黄河':'中国',
	'长江':'中国',
	'尼罗河':'埃及'
}
for h,g in rivers.items():
	print(h)
	print(g)
	print('the ' + h.title() + ' runs through ' + g.title());


print('\n')

names = ['zhou','wu','li','zhao','sun']
name_list = {
	'li':'python',
	'zhao':'java',
	'qian':'rudy',
	'sun':'c++',
}
for name in names:
	if name in name_list:
		print('thanks')
	else:
		print('please')