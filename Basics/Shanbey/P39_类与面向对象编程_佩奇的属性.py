class Pig:    
    def __init__(self):
      self.eye = 2
      self.foot = 4
      self.tail = 1
    def sing(self):
        # 猪可不会唱歌哦
        return False
    def speak(self):
        # 猪也不会说话！
        return False

# Peppa 继承 Pig
class Peppa(Pig):
    # 佩奇会唱歌
    def sing(self):
        return "啦啦啦"
    # 佩奇会说话    
    def speak(self):
        return "我是佩奇，这是我的弟弟乔治"

peppa_pig = Peppa()

print("佩奇有{}只眼睛".format(peppa_pig.eye))
print("佩奇有{}只蹄子".format(peppa_pig.foot))
print("佩奇有{}条尾巴".format(peppa_pig.tail))
print("佩奇唱："+peppa_pig.sing())
print("佩奇说："+peppa_pig.speak())
