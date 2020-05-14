from flower import flower_data
class Perceptron:
  def __init__(self, num_input=2, weight=[1,1]):
    self.num_input = num_input
    self.weight = weight
    
  def weighted_sum(self, inputs):
    weighted_sum = 0
    for i in range(self.num_input):
      weighted_sum += self.weight[i]*inputs[i]
    return weighted_sum
  
  def activation(self, weighted_sum):
    if weighted_sum >= 0:
      return 1
    if weighted_sum < 0:
      return -1
    
  def training(self, training_set):
    error_zero = False
    while not error_zero:
      error_sum = 0
      for inputs in training_set:
        prediction = self.activation(self.weighted_sum(inputs))
        actual = training_set[inputs]
        error = actual - prediction
        # abs(error)  取 error 的绝对值
        error_sum += abs(error)
        for i in range(self.num_input):
          # 权重调整公式  new_weight = old_weight + error * input
          self.weight[i] += error*inputs[i]
      print("误差为{}".format(error_sum))
      if error_sum == 0:
        error_zero = True
      
one_perceptron = Perceptron()
one_perceptron.training(flower_data)
print("更新后的权重为：{}".format(one_perceptron.weight))
