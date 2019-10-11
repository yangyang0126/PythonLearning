import pygal
line_chart = pygal.Line()
# 请为图表添加标题：泰坦尼克号不同上船点乘客幸存数据
line_chart.title = "泰坦尼克号不同上船点乘客幸存数据"
#将横坐标标记为依次登船点："Queenstown","Cherbourg","Southampton"
line_chart.x_labels = map(str, ["Queenstown","Cherbourg","Southampton"])
line_chart.add('幸存者',[30, 93, 217])
#添加 "遇难者" 的数据线：人数依次为 [47, 75, 427]
line_chart.add('遇难者',[47, 75, 427])
line_chart.render_to_file("P45_数据可视化_不同的登船点.svg")
