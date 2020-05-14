# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:00:48 2019

@author: Administrator
"""


import aiml
import sys
import os
 
# 获取aiml的安装路径 
def get_module_dir(name):
    #print(sys.modules[name])
    
    # __file__ is the pathname of the file from which the module was loaded, if it was loaded from a file
    path = getattr(sys.modules[name], '__file__', None)
    #print(path)
    if not path:
        raise AttributeError('module %s has not attribute __file__' % name)
    return os.path.dirname(os.path.abspath(path))
 
# 补充路径名称 
alice_path = get_module_dir('aiml') + '\\botdata\\alice'

# 切换到语料库所在工作目录 
os.chdir(alice_path) 

# 创建机器人alice对象 
alice = aiml.Kernel() 

print("准备加载语料库")

# 这里做一个判断
# 如果是第一次加载语料库，就进入else部分，读取数据，同时保存资料至bot_brain.brn
# 如果是之后再加载语料库，就不需要读取所有数据了，直接读取保存数据bot_brain.brn
if os.path.isfile("bot_brain.brn"):
    alice.bootstrap(brainFile = "bot_brain.brn")
else:
    alice.learn("startup.xml") # 加载...\\botdata\\alice\\startup.xml
    alice.respond('LOAD ALICE') # 加载...\\botdata\\alice目录下的语料库
    alice.saveBrain("bot_brain.brn")
print("数据加载完毕，开始对话\n")

# 正式开始聊天 
while True:
    message = input("Enter your message >> ")    
    if ("exit" == message):# 如果输入exit，程序退出
        exit()
        response = alice.respond(message) # 机器人应答
        print(response)
        break # 结束循环
    response = alice.respond(message) # 机器人应答
    print(response)
 