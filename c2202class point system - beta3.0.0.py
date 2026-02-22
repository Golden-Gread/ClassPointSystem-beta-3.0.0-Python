from datetime import datetime
import time
import os
import easygui as gui
import sys
import openpyxl as xl
number = 50
pointlist=[]
record_list=[]
#定义数据类型

class point:
    def __init__(self,data,value):
        self.data=data
        self.value=value
    def restart(self):
        self.data=0
    def __str__(self):
        return '{}:{}分'.format(self.value,self.data)

#日志函数

def login(users_name,level:str,data:str):
    logfile.write('[{}][{}][{}]{}\n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),users_name,level,data))

def record(users_name,data):
    global record_listo
    record_list.append('{},加减分记录:{},{}'.format(users_name,data,datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

if os.path.exists('./log/logdata.log'):
    logfile = open('./log/logdata.log','a',encoding='utf-8')
else:
    logfile = open('./log/logdata.log','w',encoding='utf-8')
logfile.write('-------------------------------------------\n')
login('system','INFO','class point system loaded')

#前置文件加载区域


#加载积分文件
namelist = []
if os.path.exists('point.cps'):
    point_file = open('point.cps','r',encoding='utf-8')
    point_data_list = point_file.read().split(',')
    point_file.close()
    login('system','INFO','loading point file completely')
else:
    gui.msgbox('找不到积分文件,请检查文件是否丢失或损坏',title='错误')
    login('system','ERROR','do not find point file')
    login('system','INFO','class point system exit')
    logfile.close()
    sys.exit()
#加载姓名文件

if os.path.exists('name.xlsx'):
    name_file = xl.load_workbook('name.xlsx')
    name_sheet = name_file['Sheet1']
    for i in range(number):
        namelist.append(name_sheet['A'+str(i+1)].value)
    login('system','INFO','loading name file completely')
    name_file.close()
else:
    gui.msgbox('找不到姓名文件,请检查文件是否丢失或损坏',title='错误')
    login('system','ERROR','do not find name file')
    login('system','INFO','class point system exit')
    logfile.close()
    sys.exit()
print(namelist,point_data_list,pointlist)
for i in range(len(point_data_list)):
    pointlist.append(point(point_data_list[i],namelist[i]))

if os.path.exists('record/record.cps'):
    record_file = open('record/record.cps','r',encoding='utf-8')
    record_data = record_file.readlines()
    record_file.close()
    login('system','INFO','loading record file completely')
    for i in record_data:
        record_list.append(i.strip())
else:
    gui.msgbox('找不到记录文件,请检查文件是否丢失或损坏',title='错误')
    login('system','ERROR','do not find record file')
    login('system','INFO','class point system exit')
    logfile.close()
    sys.exit()



#前置文件加载区域结束

print("""class point system beta3.0.0
system version:beta3.0.0(oct 14 2024, 12:30:44)
system encoding:UTF-8""")
print("""温馨提示:请不要在程序运行时强制结束该进程,该行为会造成班级积分表丢失
在操作时请不要违规操作,该行为会造成班级积分表丢失且会造成程序报错""")

def order_point(datalist:list):
    data = []
    strs = ''
    for i in datalist:
        data.append(i.data)
    for i in range(min(data),max(data)+1):
        data1 = []
        for i1 in datalist:
            if i.data == i:
                data1.append(i1.value)
        strs += '{}分，{}：共{}人\n'.format(i,data1,len(data1))
    login('system','INFO','order point data')
    return strs  


def add_point(value,point):
    global pointlist
    code = False
    for data in pointlist:
        if data.value == value:
            data.data += point
            login('system','INFO','add {} point to {} with value {}'.format(point,data.data,data.value))
            record(value,point)
            code = True
            break
    if not code:
        login('system','WARNING','do not find data with value {}'.format(value))

def search_point(datalist:list,value):
    for data in datalist:
        if data.value == value:
            login('system','INFO','find data with value {}'.format(value))
            return data.data
    login('system','WARNING','do not find data with value {}'.format(value))
    gui.msgbox('找不到该数据',title='错误')
    return 'None'

#主程序
code=True
while code != False:
    b = (input('列表查询按1,列表输出按2,列表重置按3,加减分按4,查询记录按5,积分排名按6\n>>>'))
    if b == '1':
        name=input('请输入姓名>>>')
        point_data = search_point(pointlist,name)
        print('{}的积分为{}'.format(name,point_data))
    elif b == '2':
        for i in pointlist:
            print('{}的积分为{}'.format(i.value,i.data))
            login('system','INFO','output point data,value:{},data:{}'.format(i.value,i.data))
    elif b == '3':
        for i in pointlist:
            i.restart()
            login('system','INFO','reset point data,value:{},data:{}'.format(i.value,i.data))
    elif b == '4':
            name=input('请输入姓名>>>')
            point=int(input('请输入加减分数>>>'))
            add_point(pointlist,name,int(point))