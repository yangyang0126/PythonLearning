import pygal

"""
对891名泰坦尼克号乘客统计（人数）：
女性幸存者：223
男性幸存者：109
女性遇难者：81
男性遇难者：468
"""

survive_female = 223
non_survive_female = 81
survive_male = 109
non_survive_male = 468

line_chart = pygal.Bar()
line_chart.title = '泰坦尼克号生存统计'
line_chart.x_labels = map(str, ["幸存者","遇难者"])
line_chart.add('女性',  [survive_female, non_survive_female])
line_chart.add('男性',  [survive_male, non_survive_male])
line_chart.render_to_file('P41_数据可视化_幸存者的性别.svg')
