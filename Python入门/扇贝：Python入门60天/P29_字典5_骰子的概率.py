'''
我们随机抛掷一个六面骰子1000次，每个面会有怎样的概率分布？
'''
import random
side_num = range(0,6)
side_count = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
roll_time = 1000
for play in range(0,roll_time):
    dice = random.choice(list(side_count.keys()))
    side_count[dice] += 1

for side, count in side_count.items():    
    print("数字{}的概率为{}".format(side,count/roll_time))
