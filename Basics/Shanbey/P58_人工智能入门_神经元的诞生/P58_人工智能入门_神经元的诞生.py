from flower import flower_data
for length, flower in flower_data.items():
  # 如果 flower 是 1，代表 山鸢尾
  if flower == 1:
    print("山鸢尾花萼长度{}，花瓣长度{}".format(length[0], length[1]))
  # 如果 flower 是 -1，代表 变色鸢尾
  elif flower == -1:
    print("变色鸢尾花萼长度{}，花瓣长度{}".format(length[0], length[1]))

