string = 'this is a string.'
print(string)

#首字母大写
print(string.title())

#所有字母大写
print(string.upper())

#所有字母小写
print(string.lower())

str1 = ' this is a tail!'
#拼接字符串
print(string+str1)

#制表符 \t
str2 = '\tpython'
print(str2)

#换行符 \n
str3 = 'python\njava\nhtml'
print(str3)

#删除空白
str4 = 'python '
#删除右空白
print(str4.rstrip())
str5 = ' python'
#删除左空白
print(str5.lstrip())
str6 = ' python '
#删除左右空白
print(str6.strip())

#为避免不必要的错误，务必注意字符串中的引号套用


#练习题
str7 = 'lee'
print('hello ' + str7 + ',would you like to learn some python today?')
print('hello ' + str7.upper() + ',would you like to learn some python today?')
print('hello ' + str7.lower() + ',would you like to learn some python today?')
print('hello ' + str7.title() + ',would you like to learn some python today?')
str8 = ' albert einstein '
str9 = ' once said,'
str10 = '"A person who never made a mistake never tried anything new"'
print(str8.title()+str9+str10)
print(str8.strip().title()+str9+'\n\t'+str10)
