# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:40:01 2019

@author: YangYang
"""

import math

# 输入数据，假设这是一组订单的金额
order = [27.0, 15.0, 19.0, 68.0, 32.0, 19.0, 19.0, 120.0, 20.0, 32.0, 12.0]
print("输入数组：")
print(order)

# 【1】计算均值
get_mean = sum(order)/len(order)  # 计算平均值
get_mean = round(get_mean,2)  # round取小数位后两位
print('\n')
print("平均数：get_mean =",get_mean)

# 【2】中位数
def get_median(numbers):  #找到numbers最中间的数    
    length = len(numbers)  #length 为numbers中数值的个数    
    sorted_numbers = sorted(numbers)  #将numbers排序，存入sorted_numbers
    mid_point = int(length/2) #中位数的位置，需要是int类型    
    if length % 2 == 1: # 如果数值个数为奇数
        median = sorted_numbers[mid_point]
    else: # 如果数值个数为偶数，中位数为中间两个数 mid_a 和 mid_b 的均值
        mid_a = sorted_numbers[mid_point-1]
        mid_b = sorted_numbers[mid_point]
        median = (mid_a + mid_b)/2    
    return median  # 函数返回 median
median_order = get_median(order)
print('\n')
print("中位数：get_median =",median_order)

# 【3】分位数
def find_nperc(numbers,n): #返回numbers中，n分位对应的数值是多少    
    sorted_numbers = sorted(numbers) # 先将数值排序     
    n_index = int(n/100 * len(sorted_numbers)) # 找到n分位数值在sorted_numbers中的索引位置    
    return sorted_numbers[n_index]  #函数返回n分位数数值
print('\n')
print("95分位数：find_nperc = {}".format(find_nperc(order,95)))
print('\n')
# 【4】众数
def get_mode(numbers):  #返回 numbers中出现次数最多的数值（众数）及其出现次数
    count_num = {}
    max_count_num = []
    # 循环numbers，建立字典 count_num {数值：出现次数}
    for num in numbers:
        count_num[num] = numbers.count(num)
    # 循环count_num
    # 用max() 得到数值出现次数的最大值，赋值给 max_count
    # 将出现次数最大值的数值（众数）放入 max_count_num
    for num,count in count_num.items():
        if count == max(count_num.values()):
            max_count = count
            max_count_num.append(num)
    return max_count_num,max_count
#将order作为函数 get_mode 的参数    
mode_num, times = get_mode(order)
for num in mode_num:
  print("众数：get_mode = {}".format(num))
#print("众数出现次数为{}".format(times))

# 【5】极差
def get_range(data):
    # get_range 为 data 的极差
    cal_range = max(data) - min(data)
    return cal_range
order_range = get_range(order)
print('\n')
print("极差：get_rang = {}".format(order_range))

# 【6】方差
def get_variance(data):
    # 均值在上面已经求解过 get_mean
    get_mean = sum(order)/len(order)
    sum_sqr = 0
    for num in order:
        sum_sqr += (num - get_mean) ** 2
    # 求方差 variance，其为 sum_sqr 的均值
    variance = sum_sqr / (len(order) -1)
    return variance
variance = get_variance(order)
variance = round(variance,2)
print('\n')
print("方差：get_variance =",variance)


# 【7】标准差
# 用 math 中的 .sqrt() 方法求 std_dev,sqrt表示平方根
get_std_dev = math.sqrt(variance)  # variance ** 0.5
get_std_dev = round(get_std_dev,2)
print('\n')
print("标准差：get_std_dev =",get_std_dev)
print('\n')

# 【8】异常值
# 25分位数值为 q1_num
q1_num = find_nperc(order,25)
# 75分位数值为 q3_num
q3_num = find_nperc(order,75)
# 计算 IQR
iqr = q3_num - q1_num
for o in order:
    if o < (q1_num - iqr * 1.5) or o > (q3_num + iqr * 1.5):
        print("{}是异常值".format(o))

# 【9】数据调整
'''
订单大于等于 60 元，标记为 "***"；
订单小于 60元并且大于等于 20元，标记为 "**"；
其他情况下，订单标记为 "*"。
'''
update_order = []
for o in order:
    if o >= 60:
        update_order.append("***")
    elif o >= 20:
        update_order.append("**")
    else:
        update_order.append("*")
print('\n')
print("数据标记：")
print("订单大于等于 60 元，标记为 ***")
print("订单小于 60元并且大于等于 20元，标记为 **")
print("其他情况下，订单标记为 *")
print('\n')
print(list(zip(update_order,order)))

print('\n')
input("数据分析完毕")









