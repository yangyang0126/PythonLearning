'''
下方是部分奥运会年份及举办地资料，请按注释行要求补全代码：

1984 洛杉矶

1988 汉城

1992 巴塞罗那

1996 亚特兰大

2000 雅典

2004 悉尼

2008 北京

2012 伦敦

2016 里约热内卢

2020 东京

2024 巴黎
'''

# 用range() 、list() 将1984~2024年期间
# 所有奥运会举办年份放入 years
years = range(1984,2028,4)
cities_before_2000 = ["洛杉矶", "汉城", "巴塞罗那", "亚特兰大" ]
cities_after_2000 = ["雅典", "悉尼", "北京", "伦敦", "里约热内卢"]

# 用 + 将 cities_before_2000 
# 和 cities_after_2000，赋值于 cities
cities = cities_before_2000 + cities_after_2000

# 用append() 将 "东京","巴黎"
# 依次添加至 cities
cities.append("东京")
cities.append("巴黎")

# 用 zip() 和 list() 将 years 和 cities
# 创建新列表 year_and_city
year_and_city = list(zip(years,cities))

# 输出 year_and_city 的长度
print(len(year_and_city))
