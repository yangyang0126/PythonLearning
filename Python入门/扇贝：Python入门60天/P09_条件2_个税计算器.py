# 我用Python计算个税
def tax(income):
  if income < 0:
    tax = 0
  elif income <= 36000:
    tax = income * 0.03
  elif income <= 144000:
    tax = income * 0.1 - 2520
  elif income <= 300000:
    tax = income * 0.2 - 16920
  elif income <= 420000:
    tax = income * 0.25 - 31920
  elif income <= 660000:
    tax = income * 0.3 - 52920
  elif income <= 960000:
    tax = income * 0.35 - 85920
  else :
    tax = income * 0.45 - 181920
  return "应缴个人所得税：" + str(tax) + "元"

print("200000元"+tax(200000))
print("100000元"+tax(100000))
print("50000元"+tax(50000))
