from urllib.request import urlopen
page = "https://assets.baydn.com/baydn/public/codetime/1/shanbay_news.html"
# 爬取page数据存入shanbay_news
shanbay_news = urlopen(page)
news_data = shanbay_news.read()
print(news_data)
# 输出news_data 的长度
print(len(news_data))

# 虽然现在看到的 
# news_data 是杂乱不堪的
# 不过不用着急
# 我们在后面的课程中
# 教你如何清洗抓取数据
