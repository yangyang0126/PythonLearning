'''
三角形内角和为 180度；
四边形内角和为 360度；
五边形内角和为 540度；
……

那么，n边形的内角和为多少度？

已知：n边形内角和公式 (n-2) * 180：
1.请写一个函数 degree()，参数为 side，当n边形的边数为 side 时，输出n边形内角和；
2.调用函数 degree()，令 side = 6。
'''

# 我用 Python 计算任意多变形内角和
def degree_n(side):
  angle = (side-2)*180
  print(angle)
degree_n(6)
