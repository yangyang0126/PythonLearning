'''
在本课程的后期，我们会学习用 Python 爬取网页上的数据，这些信息往往以字符串的形式呈现在我们面前。我们需要对它们进行清洗，以获得想要的数据格式。

今天我们体验一下如何清洗爬取下来的数据吧，请补全注释行代码：

下列变量 text 中存储了我们从“买书网”（虚构）上抓取的网页HTML信息，请用你在本课中学到的知识，先分析下段代码是如何将 text 中的字符串 "Python爬虫实战" 截取存至变量 book_name。参考此代码将 text 中的 "30.0元" 存入变量price 。

最后输出book_name 与 price。
'''

# 我用 Python 清洗网站爬取数据
text = """
<!DOCTYPE html>
<html>
<head>
  <title>买书网</title>
</head>
<body>
<p id="item">  Python爬虫实战  </p>
<p id="price">30.0元</p>
</body>
</html>
"""
book_name = text.split("</p>")[0].split(">")[-1].strip()
price = text.split("</p")[1].split(">")[-1]
print(book_name)
print(price)
