'''
我们来计算一段文本中，各个字符的出现次数。

比如在 "我是我自己" 这段文本中，"我" 出现2次，"是"、"自"、"己" 各出现1次。

1.创建空字典 char_count；

2.用for循环遍历 text，令其中元素为 char_count 的键，值为 0；

3.再次for循环遍历 text，每到一个元素，令 char_count[元素] += 1；

4.输出：char_count。
'''


text = "上海自来水来自海上"
char_count = {}
for char in text:
    char_count[char] = 0
for char in text:
    char_count[char] += 1
print(char_count)
