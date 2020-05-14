find_reviews = [
 '读后感：<!-- /react-text --><!-- react-text: 46 --><i>32</i>',
 '读后感：<!-- /react-text --><i>268</i>',
 '读后感：<!-- /react-text --><i>221</i>',
 '读后感：<!-- /react-text --><i>32</i>',
 '读后感：<!-- /react-text --><i>72</i>',
 '读后感：<!-- /react-text --><i>39</i>',
 '读后感：<!-- /react-text --><i>60</i>',
 '读后感：<!-- /react-text --><i>23</i>',
 '读后感：<!-- /react-text --><i>469</i>',
 '读后感：<!-- /react-text --><i>686</i>'
 ]
 
import re
count = 1
for review in find_reviews:
    """
    找到 review 中，以 > 开头
    以 < 结尾，并且 > 与 < 之间包含
    至少一个阿拉伯数字的部分，存入 news_review
    """
    news_review = re.findall(">([0-9]+)<",review)
    """
    news_review 中只有一个元素
    类似为 ">32<" 这样的字符串
    我们用 [1:-1] 取字符串中间的数字部分
    """
    print("第{}篇读后感数量：{}".format(count,news_review[0]))
    count += 1
