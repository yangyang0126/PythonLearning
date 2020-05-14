# -*- coding: utf-8 -*-
"""
Created on Tue May 28 2019

@author: YangYang

将一串数组以“Z 形”放入 n 个桶中
首先实现功能：第一列正着放，第二列倒着放
"""
# 方法一
def ListZ(data,step):
    #补充矩阵
    for i in range(step):
        if len(data) % step != 0:
            data.append(None)
            
    # 翻转偶数列
    for i in range(0,len(data),step):
        if (i/step) % 2 != 0:        
            data[i:i+step] = data[i+step-1:i-1:-1]   
            
    # 重新排列数组
    Zdata = []  
    for i in range(step):    
        data_ramp = [data[j] for j in range(i,len(data),step)]
        if None in data_ramp:
            data_ramp.remove(None)
        Zdata.append(data_ramp)
    return Zdata

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
step = 4
Zdata = ListZ(data,step)
print(Zdata)
        

# 方法二
def split_bucket(array, n):
    buckets = [[] for _ in range(n)]
    for i ,num in enumerate(array):
        if (i // n) % 2 == 0:
            bucket = buckets[i % n]
        else:
            bucket = buckets[-(i % n) - 1]
        bucket.append(num)
    return buckets
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    step = 4
    Zdata = split_bucket(data,step)
    print(Zdata)

# 进阶
# 将一串数组以“Z 形”放入 n 个桶中
def split_bucket(array, step):
    array_step = [array[i:i+2*step-2] for i in range(0,len(array),2*step-2)] 
    buckets = [[] for _ in range(step)]
    for i, num1 in enumerate(array_step):
        for j, num2 in enumerate(num1):    
            if (j // step)  == 0:
                bucket = buckets[j % step]
                bucket.append(num2)
            else:
                for k in range(step):
                    if k == (j%step+1):
                        bucket = buckets[-k-1]
                        bucket.append(str(num2))
                    else:
                        bucket = buckets[-k-1]
                        bucket.append(" ")
    return buckets
if __name__ == '__main__':
    array = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    array = list(array)
    step = 6    
    Zdata = split_bucket(array,step)
    for i in range(step):
        print("".join('%s' %id for id in Zdata[i]))

    
    
    
    
    
    
    
    