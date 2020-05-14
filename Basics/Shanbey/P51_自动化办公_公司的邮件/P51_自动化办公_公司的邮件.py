with open('shanbaypro_email.txt') as email_doc:
  mails = email_doc.read()
  mails_list = mails.split("\n")
  for mail in mails_list:
    if "neil@shanbaypro.com" in mail.split("收件者")[0]:
      print(mail)
