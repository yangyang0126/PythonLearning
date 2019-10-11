'''
请先点击运行，观察在默认的参数下，函数 gradient_descent 的模型表现。
之后，你可以自己尝试调整函数 gradient_descent 的后两个参数。
注意，为了避免由于计算量过大而造成的故障，请将学习率的范围控制在 0.001 ～ 0.005 之间；而迭代次数的范围控制在 10～100 之间。
'''
price = []
size = []
with open("price_size.txt") as price_size:
  data = price_size.readlines()
  for d in data:
    # 由于原始数据较大
    # 为便于计算，将房价和面积均除以 10000
    price.append(float(d.split(" ")[0])/10000)
    size.append(float(d.split(" ")[1].split("\n")[0])/10000)
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

def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]

# calculate_loss 计算每次迭代时，损失值的大小
def calculate_loss(x,y,m,b):
    y_predicted = [m * x_value + b for x_value in x]
    loss = 0
    for i in range(len(y)):
        loss += (y[i] - y_predicted[i]) ** 2
    return loss


# gradient_descent 参数中的 num_iterations 是我们可以选择的迭代次数
def gradient_descent(x, y, learning_rate, num_iterations):
  b = 0
  m = 0 
  count = 0
  for i in range(num_iterations):
    count += 1
    b, m = step_gradient(b, m, x, y, learning_rate)
    iter_loss = calculate_loss(x,y,b,m)
    print("第{}次迭代数据更新".format(count))
    print("斜率{}；截距{}；损失{}".format(m,b,iter_loss))
  return b,m

gradient_descent(price, size, 0.001, 100)
input("运行结束")
