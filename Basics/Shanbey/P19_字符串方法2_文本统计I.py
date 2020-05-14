#我用 Python 统计文本不重复字数
poem = "迢迢牵牛星，皎皎河汉女，纤纤擢素手，札札弄机杼。终日不成章，泣涕零如雨。河汉清且浅，相去复几许。盈盈一水间，脉脉不得语。"
def unique(chars):
    uni_words = []
    for char in chars:
        if char in uni_words:
            continue
        else:
            uni_words.append(char)
    return uni_words
print(unique("吃葡萄不吐葡萄皮"))
# poem 中不重复单个字数为：
print(len(unique(poem)))
