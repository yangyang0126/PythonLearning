class Famous:
  def __init__(self,name):
    self.name = name

  def __repr__(self):
    # 下方判断 self.name 是否为 "鲁迅"
    if self.name == "鲁迅":
      return "{}：在我的后园，可以看见墙外有两株树。".format(self.name)
    # 下方判断 self.name 是否为 "海明威"
    if self.name == "海明威":
      return "{}：世界是个美好的地方，值得为它奋斗。".format(self.name)
    if self.name == "维特根斯坦":
      return "{}：语言的边界就是世界的边界。".format(self.name)

lu_xun = Famous("鲁迅")
# 下方创建对象，name 属性为 "海明威" 
hemingway = Famous("海明威")
wittgenstein = Famous("维特根斯坦")
print(lu_xun)
print(hemingway)
print(wittgenstein)
