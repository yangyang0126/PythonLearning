price = []
size = []
with open("price_size.txt") as price_size:
  data = price_size.readlines()
  for d in data:
    price.append(float(d.split(" ")[0]))
    size.append(float(d.split(" ")[1].split("\n")[0]))

mean_price = sum(price)/len(price)
mean_size = sum(size)/len(size)

print("房价均价：{}美元".format(round(mean_price,2)))
print("生活面积（均值）：{}英尺".format(round(mean_size,2)))
