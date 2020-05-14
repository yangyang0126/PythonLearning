'''
质数是指：在大于1的自然数中，除了1和该数自身外，无法被其他自然数整除的数

1.创建函数 prime()， 参数 number；
2.令 number 为 int 类数据：number = int(number)；
3.建一个列表range()，从2开始，止于参数 number；
4.求 number 与上述列表每个元素之间的余数；
5.一旦出现余数为0的情况，说明 number 可以被该元素整除，那么number 不是质数。
函数输出："{number}不是质数"，{number}为参数数值，并停止循环；
6.如果 number 除以所有元素的余数都不为0，函数输出："{number}是质数"，{number}为参数数值；
7.调用 prime(2019)
'''

# 我用 Python 判断质数
def prime(number):
    number = int(number)
    for num in range(2,number):
        if number % num == 0:
            print(str(number) + "不是质数")
            break
    else:
        print(str(number) + "是质数")
prime(2019)
