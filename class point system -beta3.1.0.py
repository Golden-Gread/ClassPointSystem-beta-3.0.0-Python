import tkinter as tk
import time
import os
from datetime import datetime
import openpyxl as xl
import time

number = 50
record_list=[]
pointlist=[]


root = tk.Tk()
root.title("Class Point System beta3.1.0")
root.geometry("780x420")

label = tk.Label(root, text="""Class Point System 3.1.0
by 长郡天心以太星穹工作室
        loading...         """)
label.pack(pady=15)


if os.path.exists('log\logdata.log'):
    logfile = open('log\logdata.log','a',encoding='utf-8')
else:
    logfile = open('log\logdata.log','w',encoding='utf-8')


def show_log_window():
    log_win = tk.Toplevel(root)
    log_win.title("系统日志")
    
    text_widget = tk.Text(log_win, wrap=tk.WORD)
    scrollbar = tk.Scrollbar(log_win, command=text_widget.yview)
    text_widget.configure(yscrollcommand=scrollbar.set)
    
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_widget.pack(expand=True, fill=tk.BOTH)
    
    # 动态更新日志内容
    def update_log():
        try:
            with open('./log/logdata_temp.log', 'r',encoding='utf-8') as f:
                content = f.read()
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, content)
            text_widget.see(tk.END)  # 自动滚动到底部
        except FileNotFoundError:
            text_widget.insert(tk.END, "日志文件不存在")
        log_win.after(20, update_log)  
    
    update_log()  # 初始加载
show_log_window()


#临时函数加载
def pack_imformation():
    label1.pack(pady=15)
    system_information_button.pack_forget()
    button1.pack()
    add_point_button.pack_forget()
    search_point_button.pack_forget()
    restart_point_button.pack_forget()
    search_record_button.pack_forget()
    order_point_button.pack_forget()
    check_button.pack_forget()
    login('system','INFO','loading system information')

def pack_forget_imformation():
    label1.pack_forget()
    button1.pack_forget()
    add_point_button.pack(padx=10,side='left',pady=10)
    search_point_button.pack(padx=10,side='left',pady=10)
    restart_point_button.pack(padx=10,side='left',pady=10)
    search_record_button.pack(padx=10,side='left',pady=10)
    order_point_button.pack(padx=10,side='left',pady=10)
    system_information_button.pack(pady=20)
    check_button.pack(padx=10,side='left',pady=10)
    button1.pack_forget()
    login('system','INFO','exit system information')



def loading_word():
    label.destroy()
    word.pack(pady=15)
    word1.pack(pady=10)
    entry.pack(pady=10)
    word2.pack(pady=10)
    entry1.pack(pady=10)
    button2.pack(pady=10)
    login('system','INFO','loading word')

def logining():
    name=entry.get()    
    password=entry1.get()
    if not name or not password:
        window = tk.Toplevel(root)
        window.title('error')
        window.geometry("300x150")
        label = tk.Label(window, text="""Error:
账号或密码不能为空。""")
        label.pack(pady=15)
        button_error = tk.Button(window, text="确定", command=window.destroy,height=1)
        button_error.pack(pady=10)
        login('system','WARNING','account or password is empty')
    else:
        if name == "1" and password == "1":
            login('users','INFO','login successfully')
            window = tk.Toplevel(root)
            window.title('users')
            window.geometry("300x150")
            label = tk.Label(window, text="""登录成功""")
            label.pack(pady=15)
            button_ok = tk.Button(window, text="确定", command=window.destroy,height=1)
            button_ok.pack(pady=10)
            main_windows()
        else:
            window = tk.Toplevel(root)
            window.title('error')
            window.geometry("300x150")
            label = tk.Label(window, text="""Error:
账号或密码错误。""")
            label.pack(pady=15)
            button_error = tk.Button(window, text="确定", command=window.destroy,height=1)
            button_error.pack(pady=10)
            entry.delete(0,tk.END)
            entry1.delete(0,tk.END)
            login('system','WARNING','account or password is wrong')
    

def main_windows():
    add_point_button.pack(padx=10,side='left',pady=10)
    search_point_button.pack(padx=10,side='left',pady=10)
    restart_point_button.pack(padx=10,side='left',pady=10)
    search_record_button.pack(padx=10,side='left',pady=10)
    order_point_button.pack(padx=10,side='left',pady=10)
    check_button.pack(padx=10,side='left',pady=10)
    system_information_button.pack(pady=200)    
    entry.destroy()
    entry1.destroy()
    button2.destroy()
    word.destroy()
    word1.destroy()
    word2.destroy()
    login('system','INFO','loading main windows')

def add_point_window():
    window = tk.Toplevel(root)
    window.title('add point')
    window.geometry("500x300")
    label = tk.Label(window, text="""加减分""")
    label.pack(pady=15)
    label1 = tk.Label(window, text="""姓名：""")
    label1.pack(pady=10)
    entry1 = tk.Entry(window, width=20)
    entry1.pack(pady=10)
    label2 = tk.Label(window, text="""加减分：""")
    label2.pack(pady=10)
    entry2 = tk.Entry(window, width=20)
    entry2.pack(pady=10)
    def add_point_confirm():
        name=entry1.get()
        point=entry2.get()
        if not name or not point:
            window1 = tk.Toplevel(window)
            window1.title('error')
            window1.geometry("300x100")
            label1 = tk.Label(window1, text="""Error:
姓名或加减分不能为空。""")
            label1.pack(pady=15)
            button_error = tk.Button(window1, text="确定", command=window1.destroy,height=1)
            button_error.pack(pady=10)
            login('system','WARNING','name or point is empty')
        else:
            try:
                point=int(point)
            except ValueError:
                window1 = tk.Toplevel(window)
                window1.title('error')
                window1.geometry("300x100")
                label1 = tk.Label(window1, text="""Error:
加减分必须为整数。""")
                label1.pack(pady=15)
                button_error = tk.Button(window1, text="确定", command=window1.destroy,height=1)
                button_error.pack(pady=10)
                login('system','WARNING','point is not integer')
            else:
                if add_point(name,point):
                    window1 = tk.Toplevel(window)
                    window1.title('success')
                    window1.geometry("300x100")
                    label1 = tk.Label(window1, text="""加减分成功。""")
                    label1.pack(pady=15)
                    button_ok = tk.Button(window1, text="确定", command=window1.destroy,height=1)
                    button_ok.pack(pady=10)
                    login('system','INFO','add point successfully')
                else:
                    window1 = tk.Toplevel(window)
                    window1.title('error')
                    window1.geometry("300x100")
                    label1 = tk.Label(window1, text="""Error:
加减分失败。""")
                    label1.pack(pady=15)
                    button_error = tk.Button(window1, text="确定", command=window1.destroy,height=1)
                    button_error.pack(pady=10)
                    login('system','WARNING','add point failed')
    button1 = tk.Button(window, text="确认", command=add_point_confirm,width=10, height=2)
    button1.pack(pady=10)

def search_point_window():
    window = tk.Toplevel(root)
    window.title('search point')
    window.geometry("500x300")
    label = tk.Label(window, text="""查询分数""")
    label.pack(pady=15)
    label1 = tk.Label(window, text="""姓名：""")
    label1.pack(pady=10)
    entry1 = tk.Entry(window, width=20)
    entry1.pack(pady=10)
    def search_point_confirm():
        name=entry1.get()
        if not name:
            window1 = tk.Toplevel(window)
            window1.title('error')
            window1.geometry("300x100")
            label1 = tk.Label(window1, text="""Error:
姓名不能为空。""")
            label1.pack(pady=15)
            button_error = tk.Button(window1, text="确定", command=window1.destroy,height=1)
            button_error.pack(pady=10)
            login('system','WARNING','name is empty')
        else:
            point = search_point(pointlist,name)
            if point == 'None':
                window1 = tk.Toplevel(window)
                window1.title('error')
                window1.geometry("300x100")
                label1 = tk.Label(window1, text="""Error:
找不到该姓名的记录。""")
                label1.pack(pady=15)
                button_error = tk.Button(window1, text="确定", command=window1.destroy,height=1)
                button_error.pack(pady=10)
                login('system','WARNING','do not find data with value {}'.format(name))
            else:
                window1 = tk.Toplevel(window)
                window1.title('success')
                window1.geometry("300x100")
                label1 = tk.Label(window1, text="""{}的分数为{}分。""".format(name,point))
                label1.pack(pady=15)
                button_ok = tk.Button(window1, text="确定", command=window1.destroy,height=1)
                button_ok.pack(pady=10)
                login('system','INFO','find data with value {}'.format(name))
    button1 = tk.Button(window, text="确认", command=search_point_confirm,width=10, height=2)
    button1.pack(pady=10)

def restart_point_confirm_1(name):
        record_list_temp = record_list.copy()
        for i in record_list_temp:
            if i.split(',')[0] == name:
                record_list.remove(i)
                login('system','INFO','delete record with value {},record is {}'.format(name,i))
                
def restart_point_window():
    window = tk.Toplevel(root)
    window.title('restart point')
    window.geometry("500x300")
    label = tk.Label(window, text="""重置分数""")
    label.pack(pady=15)
    label1 = tk.Label(window, text="""姓名：""")
    label1.pack(pady=10)
    entry1 = tk.Entry(window, width=20)
    entry1.pack(pady=10)
    def restart_point_confirm():
        name=entry1.get()
        if not name:
            window1 = tk.Toplevel(window)
            window1.title('error')
            window1.geometry("300x100")
            label1 = tk.Label(window1, text="""Error:
姓名不能为空。""")
            label1.pack(pady=15)
            button_error = tk.Button(window1, text="确定", command=window1.destroy,height=1)
            button_error.pack(pady=10)
            login('system','WARNING','name is empty')
        else:
            code = False
            restart_point_confirm_1(name)
            for data in pointlist:
                if data.value == name:
                    data.restart()
                    login('system','INFO','restart {} point with value {}'.format(data.data,data.value))
                    code = True
                    break
            if not code:
                window1 = tk.Toplevel(window)
                window1.title('error')
                window1.geometry("300x100")
                label1 = tk.Label(window1, text="""Error:
找不到该姓名的记录。""")
                label1.pack(pady=15)
                button_error = tk.Button(window1, text="确定", command=window1.destroy,height=1)
                button_error.pack(pady=10)
                login('system','WARNING','do not find data with value {}'.format(name))
            else:
                window1 = tk.Toplevel(window)
                window1.title('success')
                window1.geometry("300x100")
                label1 = tk.Label(window1, text="""{}的分数已重置为0分。""".format(name))
                label1.pack(pady=15)
                button_ok = tk.Button(window1, text="确定", command=window1.destroy,height=1)
                button_ok.pack(pady=10)
                login('system','INFO','restart point successfully')
    
    def restart_all_point():
        window2 = tk.Toplevel(window)
        window2.title('restart all point')
        window2.geometry("500x300")
        label2 = tk.Label(window2, text="""确认重置全部分数？""")
        label2.pack(pady=15)
        
        def code():
            for data in pointlist:
                data.restart()
                login('system','INFO','restart {} point with value {}'.format(data.data,data.value))
            window3 = tk.Toplevel(window)
            window3.title('success')
            window3.geometry("300x100")
            label1 = tk.Label(window3, text="""重置成功""")
            label1.pack(pady=15)
            button_ok = tk.Button(window3, text="确定", command=window3.destroy,height=1)
            button_ok.pack(pady=10)
            window2.destroy()

        def cancel():
            login('system','INFO','cancel restart all point')
            window2.destroy()

        button3 = tk.Button(window2, text="确认", command=code,width=10, height=2)
        button3.pack(pady=10,side='left',padx=10)

        button4 = tk.Button(window2, text="取消", command=cancel,width=10, height=2)
        button4.pack(pady=10,side='left',padx=30)

    button1 = tk.Button(window, text="确认", command=restart_point_confirm,width=10, height=2)
    button1.pack(pady=10)

    button2 = tk.Button(window, text="全部重置", command=restart_all_point,width=10, height=2)
    button2.pack(pady=10)


def search_record_window():
    window = tk.Toplevel(root)
    window.title('search record')
    window.geometry("500x300")

    label = tk.Label(window, text="""查询记录""")
    label.pack(pady=15)

    label1 = tk.Label(window, text="""姓名：""")
    label1.pack(pady=10)

    entry1 = tk.Entry(window, width=20)
    entry1.pack(pady=10)

    def search_record_confirm():
        name=entry1.get()

        if not name:
            window1 = tk.Toplevel(window)
            window1.title('error')
            window1.geometry("300x100")
            label1 = tk.Label(window1, text="""Error:
姓名不能为空。""")
            label1.pack(pady=15)
            button_error = tk.Button(window1, text="确定", command=window1.destroy,height=1)
            button_error.pack(pady=10)
            login('system','WARNING','name is empty')
        else:
            strs = search_point_record(name)

            if strs == 'None':
                window1 = tk.Toplevel(window)
                window1.title('error')
                window1.geometry("300x100")
                label1 = tk.Label(window1, text="""Error:
找不到该姓名的记录。""")
                label1.pack(pady=15)
                button_error = tk.Button(window1, text="确定", command=window1.destroy,height=1)
                button_error.pack(pady=10)
                login('system','WARNING','do not find data with value {}'.format(name))
            else:
                window1 = tk.Toplevel(window)
                window1.title('success')
                window1.geometry("500x300")
                label1 = tk.Label(window1, text="""{}的加减分记录：""".format(name))
                label1.pack(pady=15)
                text = tk.Text(window1, width=80, height=10)
                text.pack(pady=10)
                text.insert(tk.END,strs)
                button_ok = tk.Button(window1, text="确定", command=window1.destroy,height=1)
                button_ok.pack(pady=10)
                login('system','INFO','find data with value {}'.format(name))

    button1 = tk.Button(window, text="确认", command=search_record_confirm,width=10, height=2)
    button1.pack(pady=10)

def order_point_window():
    window = tk.Toplevel(root)
    window.title('order point')
    window.geometry("300x100")
    label = tk.Label(window, text="""排序分数""")
    label.pack(pady=15)

    def order_point_confirm():
        global pointlist
        strs = order_point(pointlist)
        window1 = tk.Toplevel(window)
        window1.title('success')
        window1.geometry("930x400")
        label1 = tk.Label(window1, text="""排序成功。""")
        label1.pack(pady=15)
        text = tk.Text(window1, width=100, height=15)
        text.pack(pady=10)
        text.insert(tk.END,strs)
        button_ok = tk.Button(window1, text="确定", command=window1.destroy,height=1)
        button_ok.pack(pady=10)
        login('system','INFO','order point successfully')

    button1 = tk.Button(window, text="确认", command=order_point_confirm,width=10, height=2)
    button1.pack(pady=10)


def check_point():
    window = tk.Toplevel(root)
    window.title('check point')
    window.geometry("300x100")
    label = tk.Label(window, text="""检查分数""")
    label.pack(pady=15)
    def loading_backup_point_windows():
        window1 = tk.Toplevel(window)
        window1.title('success')
        window1.geometry("500x300")

        def code():
            window2 = tk.Toplevel(window1)
            window2.title('success')
            window2.geometry("300x100")
            window1.after(10,loading_backup_point)
            label1 = tk.Label(window2, text="""启用备份成功。""")
            label1.pack(pady=15)
            button_ok = tk.Button(window2, text="确定", command=window2.destroy,height=1)
            button_ok.pack(pady=10)
            login('system','INFO','backup system start successfully')
        label1 = tk.Label(window1, text="""是否启用备份？
警告：启用备份将会覆盖当前分数记录，请确认是否启用。""")
        label1.pack(pady=15)
        button = tk.Button(window1, text="启用备份", command=code,width=10, height=2)
        button.pack(pady=10)
        button1 = tk.Button(window1, text="取消", command=window1.destroy,width=10, height=2)
        button1.pack(pady=10)

    def check_point_confirm():
        global pointlist
        strs = ''
        for i in pointlist:
            strs += i.__str__()+'\n'
        window1 = tk.Toplevel(window)
        window1.title('success')
        window1.geometry("930x400")
        label1 = tk.Label(window1, text="""检查成功。""")
        label1.pack(pady=15)
        text = tk.Text(window1, width=100, height=15)
        text.pack(pady=10)
        text.insert(tk.END,strs)
        button_ok = tk.Button(window1, text="确定", command=window1.destroy,height=1)
        button_ok.pack(pady=10)
        login('system','INFO','check point successfully')

    def backup_point_confirm():
        window1 = tk.Toplevel(window)
        window1.title('success')
        window1.geometry("300x400")
        label1 = tk.Label(window1, text="""正在启用备份，请选择备份途径。""")
        label1.pack(pady=15)
        button = tk.Button(window1, text="启用cps备份文件", command=None,width=10, height=2)
        button.pack(pady=10)
        button1 = tk.Button(window1, text="启用cps记录文件", command=loading_backup_point_windows,width=10, height=2)
        button1.pack(pady=10)
        button2 = tk.Button(window1, text="取消", command=window1.destroy,width=10, height=2)
        button2.pack(pady=10)
    def code():
        check_point_confirm()
        backup_point_confirm()

    button1 = tk.Button(window, text="确认", command=code,width=10, height=2)
    button1.pack(pady=10)




#组件加载
system_information_button = tk.Button(root, text="系统详情", 
                  command=pack_imformation,
                  width=10, height=2)

button1 = tk.Button(root, text="退出", 
                  command=pack_forget_imformation,
                  width=10, height=2)

button2 = tk.Button(root, text="登录", 
                  command=logining,
                  width=10, height=2)

add_point_button = tk.Button(root, text="加减分", 
                             command=add_point_window,
                             width=10, height=2)

search_point_button = tk.Button(root, text="查询分数", 
                             command=search_point_window,
                             width=10, height=2)

restart_point_button = tk.Button(root, text="重置分数", 
                             command=restart_point_window,
                             width=10, height=2)

search_record_button = tk.Button(root, text="查询记录", 
                             command=search_record_window,
                             width=10, height=2)

order_point_button = tk.Button(root, text="排序分数", 
                             command=order_point_window,
                             width=10, height=2)

check_button = tk.Button(root, text="检查分数", 
                          command=check_point,
                          width=10, height=2)

entry = tk.Entry(root, width=20)

entry1=tk.Entry(root, width=20,show='*')

word = tk.Label(root, text="""登录界面""")

word1= tk. Label(root, text="""账号：""")

word2= tk. Label(root, text="""密码：""")

label1=tk.Label(root,text="""class point system beta3.0.0
system version:beta3.1.0(oct 14 2024, 12:30:44)
system encoding:UTF-8""")





#主程序函数加载
class point:
    def __init__(self,data,value):
        self.data=data
        self.value=value
    def restart(self):
        self.data=0
    def __str__(self):
        return '{}:{}分'.format(self.value,self.data)

def login(users_name,level:str,data:str):
    if os.path.exists('./log/logdata.log'):
        logfile = open('./log/logdata.log','a',encoding='utf-8')
    else:
        logfile = open('./log/logdata.log','w',encoding='utf-8')
    if os.path.exists('./log/logdata_temp.log'):
        logfile_1 = open('./log/logdata_temp.log','a',encoding='utf-8')
    else:
        logfile_1 = open('./log/logdata_temp.log','w',encoding='utf-8')
    logfile.write('[{}][{}][{}]{}\n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),users_name,level,data))
    logfile_1.write('[{}][{}][{}]{}\n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),users_name,level,data))
    logfile_1.close()
    logfile.close()

def record(users_name,data):
    global record_list
    record_list.append('{},加减分记录:{},{}\n'.format(users_name,data,datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


logfile.write('-------------------------------------------\n')
logfile.close()
login('system','INFO','class point system loaded')

namelist = []
if os.path.exists('point.cps'):
    point_file = open('point.cps','r',encoding='utf-8')
    point_data_list = point_file.read().split(',')
    point_file.close()
    login('system','INFO','loading point file completely')
else:
    window = tk.Toplevel(root)
    window.title('error')
    window.geometry("300x100")
    label = tk.Label(window, text="""Error:
找不到积分文件，请检查文件是否丢失或损坏。""")
    label.pack(pady=15)
    login('system','ERROR','do not find point file')
    login('system','INFO','class point system exit')
    logfile.close()
    root.after(3000)
    root.quit()


if os.path.exists('name.xlsx'):
    name_file = xl.load_workbook('name.xlsx')
    name_sheet = name_file['Sheet1']
    for i in range(number):
        namelist.append(str(name_sheet['A'+str(i+1)].value))
    login('system','INFO','loading name file completely')
    name_file.close()
else:
    window = tk.Toplevel(root)
    window.title('error')
    window.geometry("300x100")
    label = tk.Label(window, text="""Error:
找不到姓名文件，请检查文件是否丢失或损坏。""")
    label.pack(pady=15)
    login('system','ERROR','do not find name file')
    login('system','INFO','class point system exit')
    logfile.close()
    root.after(3000)
    root.quit()

for i in range(len(point_data_list)):
    pointlist.append(point(int(point_data_list[i]),namelist[i]))

if os.path.exists('record/record.cps'):
    record_file = open('record/record.cps','r',encoding='utf-8')
    record_data = record_file.readlines()
    record_file.close()
    login('system','INFO','loading record file completely')
    for i in record_data:
        record_list.append(i)
else:
    window = tk.Toplevel(root)
    window.title('error')
    window.geometry("300x100")
    label = tk.Label(window, text="""Error:
找不到加减分记录文件，请检查文件是否丢失或损坏。""")
    label.pack(pady=15)
    login('system','ERROR','do not find record file')
    login('system','INFO','class point system exit')
    logfile.close()
    root.after(3000)
    root.quit()

if os.path.exists('backup/back_up_point.cps'):
    backup_file = open('backup/back_up_point.cps','r',encoding='utf-8')
    backup_data = backup_file.read().split(',')
    backup_file.close()
    login('system','INFO','loading backup file completely')
else:
    window = tk.Toplevel(root)
    window.title('error')
    window.geometry("300x100")
    label = tk.Label(window, text="""Error:
找不到备份文件，请检查文件是否丢失或损坏。""")
    label.pack(pady=15)
    login('system','ERROR','do not find backup file')
    login('system','INFO','class point system exit')
    logfile.close()
    root.after(3000)
    root.quit()

def order_point(datalist:list):
    data = []
    strs = ''
    for i in datalist:
        data.append(i.data)
    for i in range(min(data),max(data)+1):
        data1 = []
        for i1 in datalist:
            if i1.data == i:
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
        return False
    return True


def search_point(datalist:list,value):
    for data in datalist:
        if data.value == value:
            login('system','INFO','find data with value {}'.format(value))
            return data.data
    login('system','WARNING','do not find data with value {}'.format(value))
    window = tk.Toplevel(root)
    window.title('error')
    window.geometry("300x100")
    label = tk.Label(window, text="""Error:
找不到该姓名的记录。""")
    label.pack(pady=15)
    root.after(3000)
    return 'None'

def search_point_record(value):
    global record_list
    strs = ''
    for i in record_list:
        if i.split(',')[0] == value:
            login('system','INFO','find record with value {}'.format(value))
            strs += i.strip() + '\n'
    if strs == '':
        login('system','WARNING','do not find record with value {}'.format(value))
        return 'None'
    return strs

            
def loading_backup_point():
    login('system','INFO','loading backup point data')
    global pointlist
    for i in pointlist:
        i.restart()
    record_file = open('record/record.cps','r',encoding='utf-8')
    backup_data = record_file.readlines()
    print(backup_data)
    for i in backup_data:
        value = i.split(',')[0]
        point = int(i.split(',')[1].split(':')[1])
        print(value,point)
        for i1 in pointlist:
            print(i1.value,i1.data)
            if i1.value == value:
                i1.data += point
                login('system','INFO','loading backup point data with value {}'.format(value))
    record_file.close()

root.after(3000, loading_word)







root.mainloop()




point_file.close()
name_file.close()
record_file.close()
point_file_1 = open('point.cps','w',encoding='utf-8')
strs = ''
for i in range(len(pointlist)):
    word = pointlist[i].data
    if i == len(pointlist)-1:
        strs += str(word)
    else:
        strs += str(word) + ','
point_file_1.write(strs)
point_file_1.close()
login('system','INFO','saving point file completely')




record_file_1 = open('record/record.cps','w',encoding='utf-8')
for i in record_list:
    record_file_1.write(i)
record_file_1.close()
login('system','INFO','saving record file completely')
login('system','INFO','class point system exit')
log_file = open('log/logdata_temp.log','w',encoding='utf-8')
log_file.write("")
log_file.close()
