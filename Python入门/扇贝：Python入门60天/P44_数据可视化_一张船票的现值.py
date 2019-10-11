td_price = [
  56.5, 7.75, 133.65, 8.85, 7.9, 
  15.5, 10.5, 7.9, 7.75, 27.75, 
  7.9, 30.5, 8.65, 13.0, 27.72, 
  18.0, 15.74, 23.0, 30.5, 9.59, 
  7.05, 7.72, 120.0, 10.5, 7.75, 
  151.55, 7.9, 7.9, 89.1, 34.38, 
  8.03, 73.5, 7.8, 7.78, 7.22, 
  52.0, 24.15, 8.05, 7.9, 39.0, 
  9.5, 7.75, 15.85, 17.8, 21.68, 
  7.75, 7.55, 7.75, 10.5, 7.05
  ]
# 第一步：将 td_price 中的异常值剔除
# 求n分位函数
def find_nperc(numbers,n):
    """
    返回numbers中，n分位对应的数值是多少
    """
    # 先将数值排序 
    sorted_numbers = sorted(numbers)
    
    # 找到n分位对应数值的索引位置
    n_index = int(n/100 * len(sorted_numbers))
    
    return sorted_numbers[n_index]

# 25分位数值为 q1_price
q1_price = find_nperc(td_price,25)

# 75分位数值为 q3_price
q3_price = find_nperc(td_price,75)

iqr = q3_price - q1_price

for price in td_price:
    if price > q3_price + 1.5 * iqr or price < q1_price - 1.5 * iqr:
        td_price.remove(price)
        print("删去异常值{}".format(price))

# 第二步：计算 td_price 的均值
mean_td_price = round(sum(td_price) / len(td_price),2)
print("票价均值（英镑）为{}".format(mean_td_price))

# 第三步：将 mean_td_price 乘以 1000，得到人民币均价
td_price_rmb = mean_td_price * 1000
print("票价均值（人民币）为{}".format(td_price_rmb))
