#我用 Python 计算生肖属相
year = int(input("请输入你的出生年份： "))
if (year - 2000) % 12 == 0:
  sign = '龙'
if (year - 2000) % 12 == 1:
  sign = '蛇' 
if (year - 2000) % 12 == 2:
  sign = '马'
if (year - 2000) % 12 == 3:
  sign = '羊'
if (year - 2000) % 12 == 4:
  sign = '猴'
if (year - 2000) % 12 == 5:
   sign = '鸡'    
if (year - 2000) % 12 == 6:
  sign = '狗'
if (year - 2000) % 12 == 7:
  sign = '猪'
if (year - 2000) % 12 == 8:
  sign = '鼠'
if (year - 2000) % 12 == 9:
  sign = '牛'    
if (year - 2000) % 12 == 10:
  sign = '虎'
if (year - 2000) % 12 == 11:
  sign = '兔'

print("你的生肖是:",sign)
