class StudentGroup:
  def __init__(self, students, status):
    self.student_list = students
    self.status = status

  def __iter__(self):
    return iter(self.student_list)

  def __len__(self):
    return len(self.student_list)

  def __contains__(self, student):
    return student in self.student_list


class Student:
  def __init__(self, name):
    self.name = name

a_qiang = Student('阿强')
lao_wang = Student('老王')
xiao_ming = Student('小明')
niu_niu = Student("妞妞")

completed = StudentGroup([a_qiang, lao_wang, xiao_ming], {'任务完成': True})
not_completed = StudentGroup([niu_niu], {'任务完成': False})

print("完成的同学有{}个".format(len(completed)))
print("未完成的同学有{}个".format(len(not_completed)))


