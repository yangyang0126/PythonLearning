'''
请按照下方要求，补全注释行…处代码：

1.调用 random 模块；

2.用 range() 创建 numbers，包含元素 —— 0,1,2,3,4,5,6,7（数值类数据）；

3.将 random.choice(numbers) 赋值给变量 ans_num：random.choice() 将从 numbers 中随机抽取一个元素；

4.创建列表 answers ，包含以下8个元素："当然，毫无疑问" , "很有可能" , "我想是的" , "或许吧" , "让我想想" , "我的答案是不" , "真让人怀疑" , "这不可能"；

5.输出：answers[ans_num]

上方代码完成之后，请你心中默想一个只能由“是”或“否”来回答的问题，虔诚地运行上述代码。查看运行结果。

Just for fun.
'''

import random
numbers = range(8)
ans_num = random.choice(numbers)
answers = ["当然，毫无疑问","很有可能","我想是的","或许吧","让我想想","我的答案是不","真让人怀疑","这不可能"]
print(answers[ans_num])
