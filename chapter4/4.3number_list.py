#打印一段数字  含头不含尾
for value in range(1,6):
	print(value)			# 1，2，3，4，5


#生成一段数字列表
num0 = list(range(1,6))
print(num0)					#[1, 2, 3, 4, 5]


#生成10以内的偶数 
#三个参数分别是  起始数（包含），终止数（不包含），步长
num1 = list(range(2,11,2))
print(num1)					#[2, 4, 6, 8, 10]


#创建10以内的整数的平方数 列表
num2 = []
for num3 in range(1,11):
	num4 = num3**2
	num2.append(num4)
print(num2);


#获取 数字列表里的最大值，最小值，和列表中数字的和
num5 = [12,1,2,4,47,88,5,585,556,48]
# min1 = min(num5)
print(min(num5))
print(max(num5))
print(sum(num5))


# 列表解析
num6 = [num7**2 for num7 in range(1,11)]
print(num6)


# 练习
for num8 in range(1,21):
	print(num8)

num9 = [num10 for num10 in range(1,10001)]
print(num9)
print(min(num9))
print(max(num9))
print(sum(num9))

num11 = list(range(1,100,2))
print(num11)

for num12 in range(1,100,2):
	print(num12)