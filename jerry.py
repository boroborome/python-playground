#!/usr/bin/python
# coding=utf-8
print(repr([22,23,24,25]))
abc = 20 + \
      30 + \
      59 + \
      1
# 你是卧底
if abc==500:
    print('500')
    if abc==600:
        print('600')
    else:
        print(abc)
else:
    if abc==110:
        print('''aa
bb''')
    else:
        print('''cc
dd''') #啊啊阿迪哥
'''
啊啊啊
你你你
是是是
卧卧卧
底底底
'''

names = []

dd = raw_input("你叫啥？\n")
name = dd[6:]
names += [name] # names = names + name
if name=='高杰睿':
    print('你太好了👍，' + name)
else:
    if name=='妈妈':
        print('做点吃的🍚，' + name)
    else:
        if name=='高玉山':
            print('你太坏了🔥，' + name)
        else:
            print('你好，' + name)


dd = raw_input("你叫啥？\n")
name = dd[6:]
names += [name] # names = names + name
if name=='高杰睿':
    print('你太好了👍，' + name)
else:
    if name=='妈妈':
        print('做点吃的🍚，' + name)
    else:
        if name=='高玉山':
            print('你太坏了🔥，' + name)
        else:
            print('你好，' + name)


dd = raw_input("你叫啥？\n")
name = dd[6:]
names += [name] # names = names + name
if name=='高杰睿':
    print('你太好了👍，' + name)
else:
    if name=='妈妈':
        print('做点吃的🍚，' + name)
    else:
        if name=='高玉山':
            print('你太坏了🔥，' + name)
        else:
            print('你好，' + name)


dd = raw_input("你叫啥？\n")
age = int(dd,2)
name = dd[6:]
names += [name] # names = names + name
if name=='高杰睿':
    print('你太好了👍，' + name)
else:
    if name=='妈妈':
        print('做点吃的🍚，' + name)
    else:
        if name=='高玉山':
            print('你太坏了🔥，' + name)
        else:
            print('你好，' + name)

dd = raw_input("你叫啥？\n")
name = dd[6:]
names += [name] # names = names + name
if name=='高杰睿':
    print('你太好了👍，' + name)
else:
    if name=='妈妈':
        print('做点吃的🍚，' + name)
    else:
        if name=='高玉山':
            print('你太坏了🔥，' + name)
        else:
            print('你好，' + name)
# 打印：你们好，xxx
print("你们好，" + ",".join(names))