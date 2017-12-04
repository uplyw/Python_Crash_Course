# 在python 中 用引号括起来的都是字符串，
# 引号既可以是单引号  又可以是双引号
# 所以，你可以在在单引号中包含双引号，
# 也可以在双引号中包含单引号



# 使用方法对字符串进行修改
name = "lee evei"
print(name.title())


# title()是一个方法，使所有单词首字母大写
# upper()，使所有单词字母变大写；
# lower()，使所有单词字母变小写；
print(name.upper())
print(name.lower())



# 合并字符串

# 使用 + 号合并字符串
# 这种合并字符串的方法叫 拼接

first_name = "lee"
last_name = "evei"
print(first_name + " " + last_name)

full_name = first_name + " " + last_name;
message = "hello," + full_name.title() + "!"
print(message)


# 使用制表符或换行符来制造空白
# 制表符  \t      换行符  \n

print("python")
print("\tpython")


