'''
制作一副扑克牌

一副扑克牌共有 54 张，其中四种花色 红心、梅花、黑桃、方块 各有13 张牌（A、2、3、4、5、6、7、8、9、10、J、Q、K）。此外，还有一张“大鬼”，一张“小鬼”。

请补充注释行 ... 处代码，制作一副扑克牌：

1.创建空列表 poke；

2.创建列表 numbers，包含元素："A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"；

3.创建列表 numbers_52 = numbers * 4；

4.创建列表 card_suit，包含元素： "红心"， "梅花"， "黑桃"， "方块"；

5.创建列表 card_suit_52 = card_suit * 13；

6.创建变量 number_and_suit = zip(numbers_52, card_suit_52)；

7.令列表 poke 等于list(number_and_suit)；

8.为 poke 添加 “大鬼”，“小鬼” 两张牌：poke += ；

9.输出 poke。
'''
poke = []
numbers = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
numbers_52 = numbers * 4
card_suit = ["红心","梅花","黑桃","方块"]
card_suit_52 = card_suit * 13
number_and_suit = zip(numbers_52,card_suit_52)
poke = list(number_and_suit)
poke += ["大鬼","小鬼"]
print(poke)
