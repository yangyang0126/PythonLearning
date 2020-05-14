'''
让我们来创建佩奇一家！

佩奇喜欢踩泥坑，她的好朋友是小羊苏西；

佩奇的弟弟叫乔治，乔治喜欢恐龙；

佩奇的爸爸喜欢读报纸；

佩奇的妈妈喜欢裙子。

1.创建类 Peppa_family；

2.Peppa_family 内创建 __init()__ ，参数 self, called, like；

3.__init()__ 内，self.called 为 called，self.like 为 like；

4.创建Peppa_family的四个对象：peppa_pig，george，daddy_pig和 mummy_pig，对象 called，like属性分别为："佩奇","泥坑"；"乔治","恐龙"；"爸爸","报纸"；"妈妈","裙子"；

5.为对象 peppa_pig 创建对象变量 friend，值为 "小羊苏西"。
'''
class Peppa_family:
    def __init__(self,called,like):
        self.called = called
        self.like = like
peppa_pig = Peppa_family("佩奇","泥坑")
george = Peppa_family("乔治","恐龙")
daddy_pig = Peppa_family("爸爸","报纸")
mummy_pig = Peppa_family("妈妈","裙子")
peppa_pig.friend = "小羊苏西"

print("{}喜欢{}，她的朋友是{}".format(peppa_pig.called,peppa_pig.like,peppa_pig.friend))
