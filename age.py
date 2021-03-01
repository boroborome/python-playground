#!/usr/bin/python
# coding=utf-8

gradeDict = {'6':'1年级',
    '7':'2年级',
    '8':'3年级',
    '9':'4年级',
    '10':'5年级',
    '11':'6年级',} #年级字典
while 1:
    nextP = 0
    age = ""
    answer = raw_input("你几岁了？\n") #判断岁数
    if answer=='我就不告诉你':
        print ('@{hh}拜拜！')
        break #如果是“我就不告诉你”退出循环
    while nextP < len(answer): 
            if answer[nextP]>="0" and answer[nextP]<="9":
                age = age + answer[nextP]
            nextP = nextP + 1 #看这个有多长
            
    print gradeDict.get(age,"我不懂？")  #看不看的懂
#0-9 = 48-59