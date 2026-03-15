import random
import time
import os
import easygui as gui 
ways = gui.diropenbox('选择安装目录')
if os.path.exists('./record') == False:
    os.mkdir('./record')
    f = open('./record/record.cps','w')
    f.close()
else:
    pass
time.sleep(1)
print('record文件夹初始化完毕_')
list1 = os.listdir(ways)
print(list1)
if 'point.cps' not in list1:
    f = open('./point.cps','w')
    f.write('0')
    for i in range(0,48):
        f.write(',0')
    f.close()
time.sleep(1)
print('目录文件初始化完毕_')
if os.path.exists('./password.cps') == False:
    while True:
        password = gui.passwordbox('请输入密码')
        if password == '':
            print('密码不能为空，请重新输入')
        else:
            break
    f = open('./password.cps','w')
    f.write(password)
    f.close()
print('密码文件初始化完毕_')
if os.path.exists('./backup') == False:
    os.mkdir('./backup')
    f1 = open('./backup/back_up_point.cps','w')
    f1.close()
else:
    pass
time.sleep(1)
print('backup文件夹初始化完毕_')
if os.path.exists('./log/logdata.log') == False:
    os.makedirs('./log')
    f = open('./log/logdata.log','w',encoding='utf-8')
    f.close()
gui.msgbox('初始化完成！')