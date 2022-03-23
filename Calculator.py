from tkinter import *

window = Tk()
window.resizable(0, 0)
window.title("Simple Calculator")

e = Entry(window, width="26", borderwidth="15", justify="right", font="arial")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_pn():
    current = e.get()
    if current >= '0':
        e.delete(0, END)
        e.insert(0, str('-') + str(current))
    else:
        e.delete(0, END)
        e.insert(0, abs(float(current)))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "multiplication":
        e.insert(0, f_num * float(second_number))

    if math == "division":
        e.insert(0, f_num / float(second_number))


button_1 = Button(window, text='1', padx=30, pady=10, command=lambda: button_click(1), font='arial', borderwidth="5")
button_2 = Button(window, text='2', padx=30, pady=10, command=lambda: button_click(2), font='arial', borderwidth="5")
button_3 = Button(window, text='3', padx=30, pady=10, command=lambda: button_click(3), font='arial', borderwidth="5")
button_4 = Button(window, text='4', padx=30, pady=10, command=lambda: button_click(4), font='arial', borderwidth="5")
button_5 = Button(window, text='5', padx=30, pady=10, command=lambda: button_click(5), font='arial', borderwidth="5")
button_6 = Button(window, text='6', padx=30, pady=10, command=lambda: button_click(6), font='arial', borderwidth="5")
button_7 = Button(window, text='7', padx=30, pady=10, command=lambda: button_click(7), font='arial', borderwidth="5")
button_8 = Button(window, text='8', padx=30, pady=10, command=lambda: button_click(8), font='arial', borderwidth="5")
button_9 = Button(window, text='9', padx=30, pady=10, command=lambda: button_click(9), font='arial', borderwidth="5")
button_0 = Button(window, text='0', padx=30, pady=10, command=lambda: button_click(0), font='arial', borderwidth="5")
button_clear = Button(window, text='AC', padx=114, pady=10, command=button_clear, font='arial', borderwidth="5")
button_pn = Button(window, text='+/-', padx=23, pady=10, command=button_pn, font='arial',
                   borderwidth="5")
button_period = Button(window, text='.', padx=32, pady=9, command=lambda: button_click("."), font=('arial', 0, 'bold'),
                       borderwidth="5")
button_add = Button(window, text='+', padx=25, pady=10, command=button_add, font='arial', borderwidth="5")
button_subtract = Button(window, text='-', padx=27, pady=10, command=button_subtract, font=('arial', 0, 'bold'),
                         borderwidth="5")
button_multiply = Button(window, text='*', padx=27, pady=10, command=button_multiply, font='arial', borderwidth="5")
button_divide = Button(window, text='/', padx=28, pady=10, command=button_divide, font='arial', borderwidth="5")
button_equal = Button(window, text='=', padx=25, pady=10, command=button_equal, font='arial', borderwidth="5")

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=1)
button_period.grid(row=5, column=2)
button_pn.grid(row=5, column=0)
button_add.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)
button_equal.grid(row=5, column=3)
button_clear.grid(row=1, column=0, columnspan=3)

window.mainloop()
