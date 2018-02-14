#排序
#sort()永久性排序，排序过后无法回到原来的列表顺序
#sort() 正序
first_name = ['zhao','qian','sun','li','zhou','wu','zheng','wang']
first_name_zh = ['赵','钱','孙','李','周','吴','郑','王']
first_name.sort();
first_name_zh.sort()
print(first_name)
print(first_name_zh)


#sort(reverse = True) 倒序
first_name1 = ['zhao','qian','sun','li','zhou','wu','zheng','wang']
first_name1.sort(reverse=True)
print(first_name1)


#sorted() 对列表进行临时排序 原列表顺序不变
first_name2 = ['zhao','qian','sun','li','zhou','wu','zheng','wang']
first_name_zh1 = ['赵','钱','孙','李','周','吴','郑','王']
print(first_name_zh1)
print(sorted(first_name_zh1))
print(first_name2)
print(sorted(first_name2))
print(first_name2)

#reverse() 倒序数组 是永久的  如果要回到以前的顺序  只需在使用一次reverse()
first_name3 = ['zhao','qian','sun','li','zhou','wu','zheng','wang']
print(first_name3)
first_name3.reverse();
print(first_name3)


#len() 数组长度
first_name4 = ['zhao','qian','sun','li','zhou','wu','zheng','wang']
print(len(first_name4))
print(first_name4[len(first_name4)-1])



#练习
city = ['hangkang','tokyo','newyeak','beijing','lundun']
print(city)
city_sorted = sorted(city)
print(city_sorted)
city_sorted.reverse()
print(city_sorted)
print(city)
city.reverse()
print(city)
city.reverse()
print(city)
city.sort()
print(city)
city.sort(reverse=True)
print(city)