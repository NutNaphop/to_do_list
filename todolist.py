from tkinter import *
from tkinter import messagebox

#fucntion newTask
def newTask():
    task = my_entry.get()
    if task != '':
        lb.insert(END,task)
        my_entry.delete(0,'end')
    else:
        messagebox.showwarning('warning','Please Enter Some Task')

#fucntion delTask 
def delTask():
      lb.delete(ANCHOR)  

#fucntion delAll
def delAll():
    lb.delete(0,END)

#fucntion Exit
def Exit():
    ws.destroy()
    
#window
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('TodoList')
ws.config(bg='#FFF8DC')
ws.resizable(width=False,height=False)

#frame
frame = Frame(ws)
frame.pack(pady=20)

#listbox
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times',18),
    bd = 0,
    fg = '#2F4F4F',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none',
)

#scroll
sb =Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
lb.pack(side=LEFT,fill=BOTH)

#task
task_list = [
]
for item in task_list:
    lb.insert(END,item)
    
#Entry Box
my_entry = Entry(
    ws,
    font = ('times',24)
)
my_entry.pack(pady=20)

#button frame
button_frame = Frame(ws)
button_frame.pack(pady=20)

#button adding add/del
add_btn = Button(
    button_frame,
    text = 'Add Task',
    font=('times 14'),
    bg='#98FB98',
    padx=5,
    pady=5,
    command = newTask
)
add_btn.pack(fill=BOTH,expand=True,side=LEFT)

del_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#FF7F50',
    padx=20,
    pady=5,
    command = delTask
)
del_btn.pack(fill=BOTH,expand=True,side=LEFT)

delA_btn = Button(
    button_frame,
    text='Delete All Task',
    font=('times 14'),
    bg='#B22222',
    padx=20,
    pady=5,
    command = delAll
)
delA_btn.pack(fill=BOTH,expand=True,side=LEFT)

exit_btn = Button(
    button_frame,
    text='Exit',
    font=('times 14'),
    bg='#FF6347',
    padx=10,
    pady=5,
    command = Exit
)
exit_btn.pack(fill=BOTH,expand=True,side=LEFT)

ws.mainloop()