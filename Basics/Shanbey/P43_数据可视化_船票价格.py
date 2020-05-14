# td_survive_fare 为泰坦尼克号部分幸存者的船票价格
td_survive_fare = [
  39.6, 79.65, 26.0, 49.5, 108.9, 
  211.34, 30.5, 63.36, 53.1, 16.7, 
  135.63, 49.5, 75.25, 83.16, 35.5, 
  53.1, 39.0, 57.98, 93.5, 26.39, 
  26.55, 39.4, 134.5, 90.0, 56.93, 
  83.16, 26.55, 77.96, 8.05, 120.0, 
  57.0, 12.47, 135.63, 55.0, 153.46, 
  512.33, 30.0, 55.44, 512.33, 262.38, 
  25.93, 78.27, 26.28, 83.47, 89.1, 
  26.55, 26.55, 247.52, 262.38, 13.0, 
  30.0, 86.5, 55.9, 51.48, 26.0, 
  263.0, 25.93, 91.08, 10.5, 146.52, 
  69.3, 10.5, 227.53, 77.96, 151.55
  ]
# td_non_survive_fare 为泰坦尼克号部分遇难者的船票价格
td_non_survive_fare = [
  151.55, 110.88, 61.98, 263.0, 52.0, 
  38.5, 77.29, 247.52, 32.32, 26.55, 
  26.55, 79.65, 34.65, 66.6, 33.5, 
  106.42, 25.59, 26.55, 7.65, 0.0, 
  10.46, 27.75, 30.7, 113.28, 108.9, 
  77.29, 29.7, 35.5, 10.5, 30.0, 
  79.2, 211.5, 30.5, 40.12, 5.0
  ]
# 请计算 td_survive_fare 的极差，赋值给变量 range_survive_fare
range_survive_fare = max(td_survive_fare) - min(td_survive_fare)

# 请计算 td_non_survive_fare 的极差，赋值给变量 range_non_survive_fare
range_non_survive_fare = max(td_non_survive_fare) - min(td_non_survive_fare)

# 请计算 td_survive_fare 的均值，赋值给变量 mean_survive_fare
mean_survive_fare = sum(td_survive_fare) / len(td_survive_fare)

# 请计算 td_non_survive_fare 的均值，赋值给变量 mean_non_survive_fare
mean_non_survive_fare = sum(td_non_survive_fare) / len(td_non_survive_fare)

# 请计算 td_survive_fare 的方差和标准差，
# 分别存入变量 variance_survive_fare 和 stdev_survive_fare
sum_variance_survive_fare = 0
for fare in td_survive_fare:
    sum_variance_survive_fare += (fare - mean_survive_fare) ** 2
variance_survive_fare = sum_variance_survive_fare / (len(td_survive_fare) - 1)

stdev_survive_fare = variance_survive_fare ** 0.5

# 请计算 td_non_survive_fare 的方差和标准差，
# 分别存入变量 variance_non_survive_fare 和 stdev_non_survive_fare

sum_variance_non_survive_fare = 0
for fare in td_non_survive_fare:
    sum_variance_non_survive_fare += (fare - mean_non_survive_fare) ** 2
variance_non_survive_fare = sum_variance_non_survive_fare / (len(td_non_survive_fare) - 1)

stdev_non_survive_fare = variance_non_survive_fare ** 0.5

print("泰坦尼克号部分幸存者的船票价格统计：")
print("均值为：{}".format(round(mean_survive_fare,2)))
print("极差为：{}".format(round(range_survive_fare,2)))
print("方差为：{}".format(round(variance_survive_fare,2)))
print("标准差为：{}".format(round(stdev_survive_fare,2)))

print("泰坦尼克号部分遇难者的船票价格统计：")
print("均值为：{}".format(round(mean_non_survive_fare,2)))
print("极差为：{}".format(round(range_non_survive_fare,2)))
print("方差为：{}".format(round(variance_non_survive_fare,2)))
print("标准差为：{}".format(round(stdev_non_survive_fare,2)))
