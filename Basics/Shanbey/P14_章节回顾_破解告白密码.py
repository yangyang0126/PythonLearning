letter = ['7', 'u', 'b', 'u', 'r', 'l', 'n', ' ', '5', 'o', 'j', 'c', '3', \
      '7', '1', 'x', 'd', 'x', 'm', '8', 'a', 'v', 'f', 'd', 'z', 'z', \
      'd', 'l', 'v', 'o', 'q', 'j', 'u', '2', 'o', 'l', 'v', '6', 'i', \
      'o', 'i', '5', '9', 'b', 'c', 'i', 's', 'a', 'i', '!', 'd', '8', \
      's', 't', '9', 'r', 'x', 'w', 'j', '1', '5', '5', '3', 'm', '9', \
      '6', 'r', 'w', '9', 'd', 'd', 'r', 'y', '3', 'p', 'h', 'f', '9', '1', 'b', 'w', 'u', \
      'c', 'e', 'r', '3', 'i', 'i', 'x', '7', 'x', '2', 'n', 'p', 'a', '4', 'b', 'f', 'w', ' ']

# 用 append() 在 letter 末尾加上英文"!"
letter.append("!")

# 取 letter 第7，8，9 位元素，
# 存入新变量 secret
secret = letter[6:9]

# 计算 letter 中 "x" 元素出现的次数，
# 并将数值存入变量 x_times
x_times = letter.count("x")


secret.append(str(x_times))
secret += letter[int(len(letter)/2)-1]

# 取 letter 最后三位元素
# 存入新列表 letter_end
letter_end = letter[-3:]

secret += letter_end
print(''.join(secret))
# TA 的回应究竟是什么呢？
