from tkinter import *
from tkinter import messagebox


bits_num = 8
last = ""
#-----------------
root = Tk()
root.maxsize(width = 425, height = 530)
root.minsize(width = 425, height = 530)
root.title('8-битный сумматор')
root.withdraw()
root.geometry('+830+200')

#-----------------
def info(): 
    messagebox.showinfo("Информация", "Автор: Миронов Григорий"+"\n"+
                       "Программа: 8-ми разрядный сумматор")

def help_me():
    messagebox.showinfo("Помощь", "1. Вводить можно только символы " +
                        "представленные на экранной клавиатуре"+
                        "\n")

def clear(): 
    entryA.delete(0, END)
    labelA.config(text = '')

    entryB.delete(0, END)
    labelB.config(text = '')
    
    labelRes10.config(text = '')
    labelRes2.config(text = '')

#-----------------
def menu():
    m = Menu(root) 
    root.config(menu = m)
    
    # fm = Menu(m)
    # m.add_cascade(label='Действия', menu = fm)
    # fm.add_command(label='Очистить поля', command = clear) 
    
    hm = Menu(m)
    m.add_cascade(label='Справка',menu = hm)
    hm.add_command(label='Помощь', command = help_me)
    hm.add_command(label='Информация', command = info)

def buttons():
    control = Frame(root)

    Button(control, text = 7, height = 2, width = 5, command = lambda: ins(7))\
        .grid(row = 1, column = 0, padx = 5, pady = 5)
    Button(control, text = 8, height = 2, width = 5, command = lambda: ins(8))\
        .grid(row = 1, column = 1, padx = 5, pady=5)
    Button(control, text = 9, height = 2, width = 5, command = lambda: ins(9))\
        .grid(row = 1, column = 2, padx=5, pady=5)
    Button(control, text = 4, height = 2, width = 5, command = lambda: ins(4))\
        .grid(row = 2, column = 0, padx=5, pady=5)
    Button(control, text = 5, height = 2, width = 5, command = lambda: ins(5))\
        .grid(row = 2, column = 1, padx=5, pady=5)
    Button(control, text = 6, height = 2, width = 5, command = lambda: ins(6))\
        .grid(row = 2, column = 2, padx=5, pady=5)
    Button(control, text = 1, height = 2, width = 5, command = lambda: ins(1))\
        .grid(row = 3, column = 0, padx=5, pady=5)
    Button(control, text = 2, height = 2, width = 5, command = lambda: ins(2))\
        .grid(row = 3, column = 1, padx=5, pady=5)
    Button(control, text = 3, height = 2, width = 5, command = lambda: ins(3))\
        .grid(row = 3, column = 2, padx=5, pady=5)
    Button(control, text = 0, height = 2, width = 5, command = lambda: ins(0))\
        .grid(row = 4, column = 1, padx=5, pady=5)

    Button(control, text = "AC", height = 2, width = 5, command = clear)\
    .grid(row = 0, column = 0, padx=5, pady=5)

    Button(control, text = "<-", height = 2, width = 5, command = backspace)\
    .grid(row = 0, column = 1, padx=5, pady=5)

    Button(control, text = " + ", height = 5, width = 4, command = sum)\
    .grid(row = 1, column = 3, rowspan = 2, padx=5)

    Button(control, text = " - ", height = 5, width = 4, command = dif)\
    .grid(row = 3, column = 3, rowspan = 2, padx=5)

    control.grid(row=1, column=0, columnspan = 2, padx=5, pady=20)
#-----------------
def ins(number):
    widget = root.focus_get()
    if isinstance(widget, Entry):
        widget.insert(END, number)
    
def backspace():
    widget = root.focus_get()
    if isinstance(widget, Entry):
        widget.delete(len(widget.get())-1, END)

def event_by_keyboard(event):
    if labelRes10['text'] != '' and last != '':
        if last == "sum":
            sum()
        elif last == "dif":
            dif()
#-----------------
def twos_complement(n, bits=32):
    mask = (1 << bits) - 1
    if n < 0:
        n = ((abs(n) ^ mask) + 1)

    res = ""

    while n > 0:
        res = str(n % 2) + res
        n //= 2

    return bin(int(res, 2) & mask)

def Convert_A():
    global curr
    curr = "A"
    txt = svA.get()
    labelA.config(text = '')
    if txt.isdigit() or txt.startswith('-') and txt[1:].isdigit():
        res = str(twos_complement(int(txt), bits_num))
        labelA.config(text = "0"*(bits_num - len(res[2:])) + res[2:])

def Convert_B():
    global curr
    curr = "B"
    txt = svB.get()
    labelB.config(text = '')
    if txt.isdigit() or txt.startswith('-') and txt[1:].isdigit():
        res = str(twos_complement(int(txt), bits_num))
        labelB.config(text = "0"*(bits_num - len(res[2:])) + res[2:])
        
def work(a, b):
        res = str(twos_complement(a + b, bits_num))
        labelRes2.config(text = "0" * (bits_num - len(res[2:])) + res[2:])

        a1 = int(int(res, 2))
        b1 = -((int(int(res, 2)) - 1) ^ ((1 << 8) - 1))
        if -128 <= a1 <= 127:
            labelRes10.config(text = a1)
        else:
            labelRes10.config(text = b1)

def sum():
    global last
    if labelRes10['text'] != '' and last == 'sum':
        entryA.delete(0, END)
        entryA.insert(0, labelRes10['text'])

    if (labelA['text'].isdigit() and labelB['text'].isdigit()):
        last = 'sum'
        a = int(labelA['text'], 2)
        b = int(labelB['text'], 2)

        work(a, b)
        
def dif():
    global last
    if labelRes10['text'] != '' and last == 'dif':
        entryA.delete(0, END)
        entryA.insert(0, labelRes10['text'])

    if (labelA['text'].isdigit() and labelB['text'].isdigit()):
        last = 'dif'
        a = int(labelA['text'], 2)
        b = int(labelB['text'], 2)
        
        work(a, -b)
#-----------------

menu()
buttons()
# Поля ввода в 10-ой
inputNum = Frame(root)

Label(inputNum, text = "Числа в 10-ой СС", font = 18, justify = CENTER)\
    .grid(row = 0, column = 0, padx=5, pady=5)

svA = StringVar()
svA.trace_add("write", lambda *args : Convert_A())
entryA = Entry(inputNum, font = 16, textvariable = svA, justify = RIGHT)
entryA.grid(row = 1, column = 0, padx=5, pady=5)
entryA.focus_set()

svB = StringVar()
svB.trace_add("write", lambda *args : Convert_B())
entryB = Entry(inputNum, font = 16, textvariable = svB, justify = RIGHT)
entryB.grid(row = 2, column = 0, padx=5, pady=5)

labelRes10Ans = Label(inputNum, font = 16, justify = RIGHT)
labelRes10Ans.grid(row = 3, column = 0, padx=5, pady=5)
labelRes10Ans.config(text = 'Ответ:')

labelRes10 = Label(inputNum, font = 16, justify = RIGHT)
labelRes10.grid(row = 4, column = 0, padx=5, pady=5)

inputNum.grid(row=0,column=0, padx=5, pady=5)

# Результат ввода в 2-ой
inputRes = Frame(root)

Label(inputRes, text = " Числа в 2-ой СС ", font = 18, justify = CENTER)\
    .grid(row = 0, column = 0, padx=5, pady=5)
labelA = Label(inputRes, font = 16, justify = RIGHT)
labelA.grid(row = 1, column = 0, padx=5, pady=5)

labelB = Label(inputRes, font = 16, justify = RIGHT)
labelB.grid(row = 2, column = 0, padx=5, pady=5)

labelRes2Ans = Label(inputRes, font = 16, justify = RIGHT)
labelRes2Ans.grid(row = 3, column = 0, padx=5, pady=5)
labelRes2Ans.config(text = 'Ответ:')

labelRes2 = Label(inputRes, font = 16, justify = RIGHT)
labelRes2.grid(row = 4, column = 0, padx=5, pady=5)

inputRes.grid(row=0, column=1, padx=5, pady=5)

root.bind('<Return>', event_by_keyboard)

root.deiconify()
root.mainloop()