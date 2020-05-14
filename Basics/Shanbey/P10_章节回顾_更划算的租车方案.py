'''
哪种租车方式更划算？
你打算从北京去一个城市旅游（不考虑往返）：
天津，距北京150公里；
济南，距北京400公里；
上海，距北京1250公里；
为了方便出行，你打算租一辆车。
租车公司给了你两套方案：
1. 长途方案
里程（公里）， 单价（元/公里）， 固定服务费（元）
200（含） ，3 ，500
200～600（含） ，2 ，500
600～1000（含） ，1.5 ，500
1000～ ，1 ， 500
2. 短途方案
里程（公里） ，单价（元/公里） ，固定服务费（元）
200（含） ，3.5 ，100
200～600（含） ，3 ，100
600～1000（含） ，2.25 ，100
1000～ ， 2 ， 100
'''
def long_cost(km):
  if km <=200:
    cost = 3 * km + 500
  elif km <=600:
    cost = 2 * km + 500
  elif km<=1000:
    cost = 1.5 * km + 500
  else:
    cost = 1 * km +500
  return cost

def short_cost(km):
  if km <=200:
    cost = 3.5 * km + 100
  elif km <=600:
    cost = 3 * km + 100
  elif km<=1000:
    cost = 2.25 * km + 100
  else:
    cost = 2 * km + 100
  return cost



def cheapest(km):
  l = long_cost(km)
  s = short_cost(km)
  if l > s:
    return "短途方案最划算："+str(km)+"公里花费 "+str(s)+"元"
  elif l < s:
    return  "长途方案最划算："+str(km)+"公里花费 "+str(l)+"元"
  else:
    return "两种方案价格一样："+str(km)+"公里需要花费 " +str(s)+"元"


print("去上海"+cheapest(1250))
print("去济南"+cheapest(400))
print("去天津"+cheapest(150))
