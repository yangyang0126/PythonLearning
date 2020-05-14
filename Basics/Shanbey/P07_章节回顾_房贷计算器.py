'''
房贷计算器 I 等额本息还款

老张打算买一套房子，贷款100万，计划分30年还完。

已知年利率在4.9%，假设老张用等额本息还款，每月要还多少钱？

注：等额本息还款是指：还款期内，每月偿还同等数额的贷款(包括本金和利息)，计算公式如下（也可参考代码中的注释部分）：

每月还款额度 =（贷款本金×月利率×（1+月利率）^还款月数） ÷（（1+月利率）^还款月数－1）

我们来建立一个计算 等额本息 还款的函数吧：

1.创建函数 pay_loan()，设置三个参数 loan，months，year_rate。分别对应贷款金额、还款月数、年利率；

2.函数主体内，创建变量 month_rate = year_rate/12；

3.创建变量 month_pay ，其值为每月还款额度。代码注释中有参考公式，供自行使用；

4.用 round() 函数取 month_pay 小数点后两位，可复制下方代码：month_pay = round(month_pay,2) ；

5.函数返回 month_pay；

6.输出 pay_loan(1000000,360,4.9) 的结果，看看老张每个月要还多少钱。
'''

# 我用 Python 计算等额本息还款额度
def pay_loan(loan,months,year_rate):
  month_rate=year_rate/12
  # 每月还款额度计算公式：
  month_pay = (loan * (month_rate/100)*(1 + (month_rate/100)) ** months)/((1+ (month_rate/100))**months-1)
  # 取小数点后两位
  month_pay=round(month_pay,2)
  return month_pay
print(pay_loan(1000000,360,4.9))
