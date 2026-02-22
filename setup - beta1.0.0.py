import random
import time
import os
import easygui as gui 
ways = gui.diropenbox('选择安装目录')
if os.path.exists('./record') == False:
    os.mkdir('./record')
    f = open('./record/point_record.txt','w')
    f.close()
else:
    pass
time.sleep(1)
print('record文件夹初始化完毕_')
if os.path.exists('./restore') == False:
    os.mkdir('./restore')
    f = open('./restore/restorefile_point.txt','w')
    f1 = open('./restore/restorefile_record.txt','w')
    f2 = open('./restore/restorefile_code.txt','w')
    f.close()
    f1.close()
    f2.close()
else:
    pass
time.sleep(1)
print('restore文件夹初始化完毕_')
list1 = os.listdir(ways)
print(list1)
if 'point.cps' not in list1:
    f = open('./point.cps','w')
    f.close()
time.sleep(1)
print('目录文件初始化完毕_')
if os.path.exists('./password') == False:
    password = gui.enterbox('请输入密码\n')
    f = open('./password.cps','w')
    f.write(password)
    f.close()
print('密码文件初始化完毕_')
if os.path.exists('./backup') == False:
    os.mkdir('./backup')
    f = open('./backup/point_backup.txt','w')
    f1 = open('./backup/backup_file.txt','w')
    f.close()
    f1.close()
else:
    pass
time.sleep(1)
print('backup文件夹初始化完毕_')
print('安装完成，主程序运行环境就绪_')