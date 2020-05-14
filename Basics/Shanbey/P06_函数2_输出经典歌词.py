'''
《外婆桥》是一首著名的童谣，请补全代码：

1.创建函数 repeat() ，参数为 yao，num，num 的默认值为 3；

2.repeat() 返回 yao * num；

3.调用 repeat() ，令yao = "摇啊摇，"，num = 2，将返回值赋值给新变量 lyrics；

4.将字符串 "摇到外婆桥。"添加至 lyrics 之后；

5.再次调用 repeat() 函数，这次令yao = lyrics，将返回值赋值给新变量 song；

6.输出 song。
'''


# 我用 Python 输出歌词
def repeat(yao, num = 3):
  return yao*num
  
lyrics = repeat(yao = "摇啊摇，", num = 2)
lyrics += "摇到外婆桥。"
song = repeat(yao = lyrics)
print(song)
