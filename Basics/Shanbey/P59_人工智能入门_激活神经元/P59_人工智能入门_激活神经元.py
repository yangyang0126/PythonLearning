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
    else:
      return -1
  def training(self, training_set):
    error_set = []
    for data in training_set:                   
      predict = self.activation(self.weighted_sum(data))
      actual = training_set[data]
      error = actual - predict
      error_set.append(error)
    return error_set
one_perceptron = Perceptron()
error_sum = 0
for error in one_perceptron.training(flower_data):
    error_sum += error
print("误差总值为{}".format(error_sum))
