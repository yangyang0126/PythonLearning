import pygal
bar_chart = pygal.Bar()
bar_chart.title = '泰坦尼克号乘客所在船舱统计'
bar_chart.x_labels = map(str, ["一等舱","二等舱","三等舱"])
bar_chart.add('幸存者', [136,87,119])
bar_chart.add('遇难者', [80,97,372])
bar_chart.render_to_file("P47_数据可视化_船舱的分布.svg")
