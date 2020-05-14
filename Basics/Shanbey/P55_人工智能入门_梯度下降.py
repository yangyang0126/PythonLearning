def calculate_loss(x,y,m,b):
    y_predicted = [m * x_value + b for x_value in x]
    loss = 0
    for i in range(len(y)):
        loss += (y[i] - y_predicted[i]) ** 2
    return loss
x_values = [4, 3, 2]
y_values = [6, 2, 4]

print(calculate_loss(x_values,y_values,1,0))
print(calculate_loss(x_values,y_values,2,1))
