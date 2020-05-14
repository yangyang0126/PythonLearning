'''
回文是一个有趣的语言学现象：一段文字自右至左与自左至右是完全一样的。

比如：上海自来水来自海上

请补全注释行中的代码，使得函数 huiwen_check() 可以判断一个字符串是否是回文。
'''

# 我用 Python 判断回文
def huiwen_check(chars):
    for i in range(len(chars)):
        if chars[i] == chars[-i-1]:
            continue
        else:
            print(chars+"<<这不是回文")
            break
    else:
        print(chars+"<<这是回文")
huiwen_check("黄山落叶松叶落山黄")
huiwen_check("level")
huiwen_check("abcdabcd")
