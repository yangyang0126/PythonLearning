'''
小李今天接了几单？

drive_record 中是专车司机小李昨日一天的行车记录，其中包括了乘客上车时间（10:03:12）和订单行驶公里数（里程：3.2公里）。

请按照下列代码的注释完成要求，我们看看小李昨天订单的行驶总里程和每小时内的接单数。
'''

drive_record = \
"""
   10:03:12                   里程：3.2公里；
   10:23:18                   里程：6.7公里；
   10:40:32                   里程：2.1公里；
   10:52:02                   里程：4.2公里；
   11:21:23                   里程：5.2公里；
   12:23:57                   里程：7.3公里；
   13:03:12                   里程：3.0公里；
   13:22:02                   里程：13.2公里；
   14:08:43                   里程：6.1公里；
   14:43:52                   里程：7.2公里；
   15:13:32                   里程：3.2公里；
   15:37:12                   里程：10.6公里；
   16:43:22                   里程：3.4公里；
   17:20:01                   里程：3.2公里；
   17:33:15                   里程：7.3公里；
   18:03:17                   里程：10.2公里；
   19:02:12                   里程：5.8公里；
   19:33:43                   里程：3.7公里；
   19:53:52                   里程：6.2公里；
   20:28:21                   里程：6.6公里；
   21:03:12                   里程：15.2公里；
   22:03:12                   里程：3.9公里；
   22:23:12                   里程：6.2公里
"""
# 将drive_record 以 ；分割，组成列表 drive_record_list
# 请在下方补全代码：
drive_record_list = drive_record.split("；")
# 昨日小李的接单总数：
print("昨日小李接到的订单数为{}单".format(len(drive_record_list)))

# for循环 drive_record_list，提取出每个元素中的公里数（如第一个元素为 3.2），组成列表 drive_kms
drive_kms = []
for record in drive_record_list:
    drive_kms.append(record.split("里程：")[1].split("公里")[0])

# 计算小李昨日的订单总里程：
drive_sum = 0
for kms in drive_kms:
    drive_sum += float(kms)
# 请在下方…处补全代码    
print("昨日里程数为{}公里".format(drive_sum))

# 遍历drive_record_list，提取出每个元素中的小时数（如第一个元素为 10），组成列表 hours
hours = []
for record in drive_record_list:
    hour = record.split(":")[0].split("\n")[1].strip()
    hours.append(hour)

# 在 hours 中找出不重复的小时数：
unique_hour = []
for hour in hours:
    if hour not in unique_hour:
        unique_hour.append(hour)
    else:
        pass

# 订单时间不重复的小时数为 ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
# 创建函数 count_hour，参数 hour。
# 计算 hour 在列表 hours 中的出现次数：
def hour_count(hour):
    count = 0
    for h in hours:
        if h == hour:
            count += 1
    return count
# 遍历 unique_hour，
# 输出每个元素在 hours 中的出现次数，
# 例如： 10点有4单

for hour in unique_hour:
    # 请将下行……处代码补全
    print("{}点有{}单".format(hour,hour_count(hour)))

