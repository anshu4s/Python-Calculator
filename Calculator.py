from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root,width=35, borderwidth= 2)
e.grid(row=0,column=0,columnspan=3, padx =10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
    

def equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))

def clear():
    e.delete(0, END)


#defines buttons
button_1 = Button(root, text="1", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: button_click(1))
button_2 = Button(root, text="2", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: button_click(2))
button_3 = Button(root, text="3", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: button_click(3))
button_4 = Button(root, text="4", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: button_click(4))
button_5 = Button(root, text="5", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: button_click(5))
button_6 = Button(root, text="6", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: button_click(6))
button_7 = Button(root, text="7", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: button_click(7))
button_8 = Button(root, text="8", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: button_click(8))
button_9 = Button(root, text="9", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: button_click(9))
button_0 = Button(root, text="0", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: button_click(0))
button_00 = Button(root, text="00", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: button_click(00))

button_add = Button(root, text="+", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: add())
button_sub = Button(root, text="-", fg="red", bg="black", padx=51, pady=20,borderwidth= 5, command=lambda: sub())
button_mul = Button(root, text="x", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: mul())
button_div = Button(root, text="/", fg="red", bg="black", padx=50, pady=20,borderwidth= 5, command=lambda: div())


button_equal = Button(root, text="=", fg="white", bg="green", padx=50, pady=20,borderwidth= 5, command=lambda: equal())
button_clear = Button(root, text="Clear", fg="white", bg="red", padx=60, pady=20,borderwidth= 5, command=lambda: clear())

#ekhan theke amra row aar column e division korbo sob key gulo ke ....

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=5, column=2)
button_00.grid(row=6, column=1)

button_add.grid(row =4 , column =0 )
button_sub.grid(row =4 , column =1 )
button_mul.grid(row =4 , column =2 )
button_div.grid(row =6 , column =0 )



button_equal.grid(row =5 , column =0 )
button_clear.grid(row =5 , column =1 )

root.mainloop()