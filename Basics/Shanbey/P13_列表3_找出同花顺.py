your_card = ["大鬼","红桃A","红桃K","红桃Q","黑桃Q","梅花J","方片J","红桃J","梅花10","红桃10","黑桃9"]
# tong_tian_shun 为 your_card 中的第2~4张牌
tong_tian_shun = your_card[1:4]

tong_tian_shun.append("红桃J")
# 用 + 或者 += 将 
# tong_tian_shun 和 ["红桃10"] 联结起来
tong_tian_shun += ["红桃10"]

# 输出 tong_tian_shun
print(tong_tian_shun)
