with open('shanbaypro_email.txt') as email_doc:
  mails = email_doc.read()
  email_split = mails.split("\n")

sender_receiver = {}
for email in email_split:
    sender = email.split("发件者：")[1].split(" ")[0]
    receiver = email.split("收件者：")[1]
    if sender not in sender_receiver:
        sender_receiver[sender] = []
        sender_receiver[sender].append(receiver)
    else:
        if receiver in sender_receiver[sender]:
            continue
        else:
            sender_receiver[sender].append(receiver)

def find_shortest_path(graph, start, end, shortestLength=-1, path=[]):
  path = path + [start]
  if start == end:
    return path

  shortest = None
  for node in graph[start]:
    if node not in path:
      if shortestLength==-1 or len(path)<(shortestLength-1):
        newpath = find_shortest_path(graph, node, end, shortestLength, path)
        if newpath:
          if not shortest or len(newpath) < len(shortest):
            shortest = newpath
            shortestLength = len(newpath)  
  return shortest        
        
member1="sahil@shanbaypro.com"
member2="holmes@shanbaypro.com"
print("成员 1: " + member1)
print("成员 2: " + member2)
print("找寻最短路径... ")
path=find_shortest_path(sender_receiver,member1,member2)
print("邮件链条: " + "{}层关系".format(len(path)-1))
print(path)

print("--------")
print("将结果写入 email_network.txt")

with open('email_network.txt', 'w') as network:
  net = ""
  for node in path:
    net += node
    net += "->"
  network.write(net)

print("写入成功！")
