'''
26个英文字母中，有的字母经常出现，比如e, a...；有的字母很少出现，比如z,q ...。

我们按照字母的出现频率为它们附上分值，频率越高的字母分值越低：
接着，我们令一个单词的总分等于构成它所有字母的分值之和。比如，red = r + e + d => 1 + 1 + 2 = 4。

请按照下方要求，补全注释行…处代码：

我们来创建一个函数，计算所给单词的分值吧！

1.将 letters 和 points 两个列表合并成字典 letter_to_point，字典的键为 letters，值为letters中各字母对应的分值；

2.创建函数 word_score，参数 word；

3.函数内变量 score = 0；

4.遍历 word ，将每个元素变为小写字母，并对应 letter_to_point 中的键，将值添加给 score；

5.函数返回 score；

6.输出：word_score("Agriculture")；

7.输出：word_score("pneumonoultramicroscopicsilicovolcanoconiosis")。

'''



letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_point = {key:value for key,value in zip(letters,points)}
def word_score(word):
    score = 0
    for char in word:
        score += letter_to_point[char.lower()]
    return score
print(word_score("Agriculture"))
# 下方是英文中最长的单词
print(word_score("pneumonoultramicroscopicsilicovolcanoconiosis"))
