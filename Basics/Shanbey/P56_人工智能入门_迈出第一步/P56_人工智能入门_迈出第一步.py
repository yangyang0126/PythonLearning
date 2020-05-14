'''
继续拿之前的房屋价格与面积的数据集来做线性回归的梯度下降训练
观察不同大小的学习率对下降幅度的影响。
'''
price = []
size = []
with open("price_size.txt") as price_size:
  data = price_size.readlines()
  for d in data:
    price.append(float(d.split(" ")[0]))
    size.append(float(d.split(" ")[1].split("\n")[0]))

def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

# 计算下降梯度函数
def step_gradient(x, y, b_current, m_current, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]


# 当前的截距预期值:
b = 0
# 当前的斜率预期值:
m = 0

b1, m1 = step_gradient(price, size, b, m, 0.01)
b2, m2 = step_gradient(price, size, b, m, 0.001)
print(b1, m1)
print(b2, m2)
