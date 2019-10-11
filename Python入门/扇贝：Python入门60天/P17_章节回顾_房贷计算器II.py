'''
房贷计算器 II 等额本金还款

在讲函数时，我们设计了程序计算等额本息还款。本章中，我们用新学的循环知识计算等额本金还款。

等额本金还款是指：还款期内按期等额归还贷款本金，并同时还清当期未归还本金所产生的利息。

计算公式如下： 月还款额=贷款本金÷贷款期月数+（本金-已归还本金累计额）×月利率

老张又打算买一套房子，还是贷款100万，计划分30年还完。已知年利率4.9%。这次，老张打算用等额本金还款，每月要还多少钱？（考虑篇幅所限，我们只输出前12个月的月还款额）

请按照下方要求，补全注释行… 处代码：

1.创建函数 pay_loan()，参数 loan，months，year_rate。分别对应 贷款金额、还款月数、年利率；

2.函数pay_loan() 主体内，创建变量 month_rate ，其值等于 year_rate 除以 12 的值；

3.继续创建变量 month_principle（每月本金） ，它等于 loan 除以 months 的值；

4.由于我们只看前12个月的还款额，用for循环遍历 range(1,13) ：计算第n月的还款额 month_pay。

5.输出“第{n}月需还款：month_pay 元” (n为月数)，month_pay 需保留两位小数，参考：round(mont_pay,2)；

6.输出 pay_loan(1000000,360,4.9)。

看看老张（前12个月）每个月要还多少钱。
'''


# 我用 Python 计算等额本金还款
def pay_loan(loan,months,year_rate):
    month_rate = year_rate/12
    month_principle = loan/months
    for month in range(1,13):
        month_pay = (loan-month_principle*(month-1))*month_rate + month_principle
        print("第"+str(month)+"月需还款："+ str(round(month_pay,2))+"元")
pay_loan(1000000,360,0.049)
