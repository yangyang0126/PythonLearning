'''
下方变量 goal_record 是2018年俄罗斯世界杯64场球赛的比分（不包含淘汰赛点球大战）

创建字典 wc_2018_goal，记录32支球队的各自进球数。
'''

goal_record = """Russia 5–0 Saudi Arabia;
Egypt 0–1 Uruguay;
Russia 3–1 Egypt;
Uruguay 1–0 Saudi Arabia;
Uruguay 3–0 Russia;
Saudi Arabia 2–1 Egypt;
Morocco 0–1 Iran;
Portugal 3–3 Spain;
Portugal 1–0 Morocco;
Iran 0–1 Spain;
Iran 1–1 Portugal;
Spain 2–2 Morocco;
France 2–1 Australia;
Peru 0–1 Denmark;
Denmark 1–1 Australia;
France 1–0 Peru;
Denmark 0–0 France;
Australia 0–2 Peru;
Argentina 1–1 Iceland;
Croatia 2–0 Nigeria;
Argentina 0–3 Croatia;
Nigeria 2–0 Iceland;
Nigeria 1–2 Argentina;
Iceland 1–2 Croatia;
Costa Rica 0–1 Serbia;
Brazil 1–1 Switzerland;
Brazil 2–0 Costa Rica;
Serbia 1–2 Switzerland;
Serbia 0–2 Brazil;
Switzerland 2–2 Costa Rica;
Germany 0–1 Mexico;
Sweden 1–0 South Korea;
South Korea 1–2 Mexico;
Germany 2–1 Sweden;
South Korea 2–0 Germany;
Mexico 0–3 Sweden;
Belgium 3–0 Panama;
Tunisia 1–2 England;
Belgium 5–2 Tunisia;
England 6–1 Panama;
England 0–1 Belgium;
Panama 1–2 Tunisia;
Colombia 1–2 Japan;
Poland 1–2 Senegal;
Japan 2–2 Senegal;
Poland 0–3 Colombia;
Japan 0–1 Poland;
Senegal 0–1 Colombia;
France 4–3 Argentina;
Uruguay 2–1 Portugal;
Spain 1–1 Russia;
Croatia 1–1 Denmark;
Brazil 2–0 Mexico;
Belgium 3–2 Japan;
Sweden 1–0 Switzerland;
Colombia 1–1 England;
Uruguay 0–2 France;
Brazil 1–2 Belgium;
Sweden 0–2 England;
Russia 2–2 Croatia;
France 1–0 Belgium;
Croatia 2–1 England;
Belgium 2–0 England;
France 4–2 Croatia"""

team_goal = []
for match in goal_record.split(";\n"):
    for team in match.split("–"):
        team_goal.append(team)
wc_2018_goal = {}
for num in range(len(team_goal)):
    if num % 2 == 0:
        wc_2018_goal[team_goal[num][:-2]] = 0
    else:
        wc_2018_goal[team_goal[num][2:]] = 0
        
for num in range(len(team_goal)):
    if num % 2 == 0:
        wc_2018_goal[team_goal[num][:-2]] += int(team_goal[num][-1])
    else:
        wc_2018_goal[team_goal[num][2:]] += int(team_goal[num][0])

for key,value in wc_2018_goal.items():
  print(key,value)
