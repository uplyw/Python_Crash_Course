#传递列表
# def greet_users(names):
# 	for name in names:
# 		msg = 'hello,' + name.title()
# 		print(msg)

# usersname = ['zhao','qian','sun','li']
# greet_users(usersname)

# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []
# while unprinted_designs:
# 	current_design = unprinted_designs.pop()
# 	print("printing model:" + current_design)
# 	completed_models.append(current_design)
# print('\nthe following models have been printed:')
# for completed in completed_models:
# 	print(completed)

# def print_models(unprinted_designs,completed_models):
# 	while unprinted_designs:
# 		current_design = unprinted_designs.pop()
# 		print('printing model:' + current_design)
# 		completed_models.append(current_design)

# def show_completed_models(completed_models):
# 	print('\nthe following models have been printed:')
# 	for completed_model in completed_models:
# 		print(completed_model)
# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []
# print_models(unprinted_designs,completed_models)
# show_completed_models(completed_models)

# 使用列表副本
# def print_models(unprinted_designs,completed_models):
# 	while unprinted_designs:
# 		current_design = unprinted_designs.pop()
# 		print('printing model:' + current_design)
# 		completed_models.append(current_design)
# def show_completed_models(completed_models):
# 	print('\nthe following models have been printed:')
# 	for completed_model in completed_models:
# 		print(completed_model)
# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []
# print_models(unprinted_designs[:],completed_models)
# show_completed_models(completed_models)

# 练习
# def show_name(names):
# 	for name in names:
# 		print(name)
# username = ['zhao','qian','sun','li']
# show_name(username)

# username = ['zhao','qian','sun','li']
# for name in username:
# 	name = name + ' the great'
# 	print(name)

# def show_magicians(name1):
# 	for name in name1:
# 		print(name1)

# def make_magicians(name2):
# 	for name in name2:
# 		name = name + ' the great'
# 	return name
# # make_magicians()
# magician = ['zhao','qian','sun','li']
# magicians = make_magicians(magician)
# show_magicians(magicians)

# def gaibian(un,ok):
# 	while un:
# 		inggb = un.pop()
# 		print(inggb)
# 		ok.append(inggb + ' the great')
# def prigb(ok):
# 	for ojbk in ok:
# 		print(ojbk)

# ungb = ['zhao','qian','sun','li']
# okgb = []
# gaibian(ungb, okgb)
# prigb(okgb)