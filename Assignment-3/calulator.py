from tkinter import * 

root = Tk()
root.title("Simple Calculator")
e = Entry(root,width=25,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

try:
    def button_click(number):
       
        current = e.get().strip()
        e.delete(0,END)
        e.insert(0,str(current)+str(number))

    def add():
        first_number = e.get()
        global fnum
        fnum = float(first_number)
        e.delete(0,END)
        number = e.get()
        global operation
        operation = 'addition'
        e.delete(0,END)
    
    def sub():
        first_number = e.get()
        global fnum
        fnum = float(first_number)
        e.delete(0,END)
        global operation
        operation = 'subtraction'
        e.delete(0,END)

    def mul():
        first_number = e.get()
        global fnum
        fnum = float(first_number)
        e.delete(0,END)
        global operation
        operation = 'multiplication'
        e.delete(0,END)

    def div():
        first_number = e.get()
        global fnum
        fnum = float(first_number)
        e.delete(0,END)
        global operation
        operation = 'division'
        e.delete(0,END)

    def mod():
        first_number = e.get()
        global fnum
        fnum = float(first_number)
        e.delete(0,END)
        global operation
        operation = 'modulus'
        e.delete(0,END) 

    def equal12():
        second_number = e.get()
        e.delete(0,END)

        if operation == 'addition':
            e.insert(0,fnum + float(second_number))
        
        if operation == 'subtraction':
            e.insert(0,fnum-float(second_number))
        
        if operation == 'division':
            e.insert(0,fnum/float(second_number))

        if operation == 'multiplication':
            e.insert(0,fnum*float(second_number))

        if operation == 'modulus':
            e.insert(0,fnum%float(second_number))

    def clear():
        e.delete(0,END)
        exp=0
        r=0
except ValueError:
    pass
try:
    clear1 = Button(root,text="AC",padx=15,pady=2,command=clear)
    clear1.grid(row=1,column=3)
    one = Button(root,text='1',padx=20,pady=2,command=lambda: button_click(1))
    one.grid(row=1,column=0)
    two = Button(root,text="2",padx=20,pady=2,command=lambda: button_click(2))
    two.grid(row=1,column=1)
    three = Button(root,text='3',padx=20,pady=2,command=lambda: button_click(3))
    three.grid(row=1,column=2)
    four = Button(root,text='4',padx=20,pady=2,command=lambda: button_click(4))
    four.grid(row=2,column=0)
    five = Button(root,text='5',padx=20,pady=2,command=lambda: button_click(5))
    five.grid(row=2,column=1)
    six = Button(root,text='6',padx=20,pady=2,command=lambda: button_click(6))
    six.grid(row=2,column=2)
    seven = Button(root,text='7',padx=20,pady=2,command=lambda: button_click(7))
    seven.grid(row=3,column=0)
    eight = Button(root,text='8',padx=20,pady=2,command=lambda: button_click(8))
    eight.grid(row=3,column=1)
    nine = Button(root,text='9',padx=20,pady=2,command=lambda: button_click(9))
    nine.grid(row=3,column=2)
    add1 = Button(root,text='+',padx=20,pady=2,command=add)
    add1.grid(row=2,column=3)
    sub1 = Button(root,text='-',padx=20,pady=2,command=sub)
    sub1.grid(row=3,column=3)
    mul1 = Button(root,text='x',padx=20,pady=2,command= mul)
    mul1.grid(row=4,column=1)
    div1 = Button(root,text='/',padx=20,pady=2,command= div)
    div1.grid(row=4,column=2)
    mod1 = Button(root,text='%',padx=20,pady=2,command= mod)
    mod1.grid(row=4,column=3)
    zero = Button(root,text='0',padx=20,pady=2,command=lambda: button_click(0))
    zero.grid(row=4,column=0)
    equals = Button(root,text='=',padx=20,pady=2,command=equal12)
    equals.grid(row=5,column=1)
    decimal = Button(root,text='.',padx=20,pady=2,command=lambda: button_click("."))
    decimal.grid(row=5,column=2)
except ValueError:
    pass


root.mainloop()