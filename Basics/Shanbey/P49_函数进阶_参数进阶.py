'''
公司入职了一批新人，我们需要自动为他们创建企业邮箱。
企业邮箱遵循固定的格式，请参照要求，
分别用位置参数与关键字参数调用函数 address_generator，
为员工张小明和陈阿强创建邮箱。
'''

def address_generator(first_name,last_name,company,domain = ".cn"):
    email_address = "{}.{}@{}{}".format(first_name,last_name,company,domain)
    return email_address
email_xiaoming = address_generator("xiaoming","zhang","shanbay",".com")
email_aqiang = address_generator(company = "learnpython",last_name = "chen",first_name = "aqiang")
print(email_xiaoming)
print(email_aqiang)
