# Hare Krishna
from tkinter import *

root = Tk()
root.maxsize(365, 400)
root.minsize(365, 400)
root.title('Calculator by Jony')
root.wm_iconbitmap('logo.ico')


def click(event):
    global scValue
    text = event.widget.cget('text')
    if text == "=":
        if scValue.get().isdigit():
            value = int(scValue.get())
        else:
            try:
                value = eval(scValue.get())

            except Exception as e:
                print(e)
                value = "Error"

        scValue.set(value)
        screen.update()

    elif text == 'AC':
        scValue.set('')
        screen.update()
    else:

        scValue.set(scValue.get() + text)
        screen.update()


scValue = StringVar()
scValue.set('')
screen = Entry(root, textvariable=scValue, font='arial 20 bold', bd=30, insertwidth=4, bg='powder blue', justify='right')
screen.grid(columnspan=4)


# Buttons

b7 = Button(root, text='7', padx=16, bd=8, font='arial 20 bold', bg='powder blue')
b7.grid(row=1, column=0)
b7.bind("<Button-1>", click)
b8 = Button(root, text='8', padx=16, bd=8, font='arial 20 bold', bg='powder blue')
b8.grid(row=1, column=1)
b8.bind("<Button-1>", click)
b9 = Button(root, text='9', padx=16, bd=8, font='arial 20 bold', bg='powder blue')
b9.grid(row=1, column=2)
b9.bind("<Button-1>", click)
b_plus = Button(root, text='+', padx=16, bd=8, font='arial 20 bold', bg='powder blue')
b_plus.grid(row=1, column=3)
b_plus.bind("<Button-1>", click)

'''.................................................................................................'''

b4 = Button(root, text='4', padx=16, bd=8, font='arial 20 bold', bg='powder blue')
b4.grid(row=2, column=0)
b4.bind("<Button-1>", click)
b5 = Button(root, text='5', padx=16, bd=8, font='arial 20 bold', bg='powder blue')
b5.grid(row=2, column=1)
b5.bind("<Button-1>", click)
b6 = Button(root, text='6', padx=16, bd=8, font='arial 20 bold', bg='powder blue')
b6.grid(row=2, column=2)
b6.bind("<Button-1>", click)
b_minus = Button(root, text='-', padx=16, bd=8, font='arial 20 bold', bg='powder blue')
b_minus.grid(row=2, column=3)
b_minus.bind("<Button-1>", click)
'''.................................................................................................'''

b1 = Button(root, text='1', padx=16, bd=8, font='arial 20 bold', bg='powder blue')
b1.grid(row=3, column=0)
b1.bind("<Button-1>", click)
b2 = Button(root, text='2', padx=16, bd=8, font='arial 20 bold', bg='powder blue')
b2.grid(row=3, column=1)
b2.bind("<Button-1>", click)
b3 = Button(root, text='3', padx=16, bd=8, font='arial 20 bold', bg='powder blue')
b3.grid(row=3, column=2)
b3.bind("<Button-1>", click)
b_multiply = Button(root, text='*', padx=16, bd=8, font='arial 20 bold', bg='powder blue')
b_multiply.grid(row=3, column=3)
b_multiply.bind("<Button-1>", click)


'''.................................................................................................'''
b0 = Button(root, text='0', padx=16, bd=8, pady=16, font='arial 20 bold', bg='powder blue')
b0.grid(row=4, column=0)
b0.bind("<Button-1>", click)
b_divide = Button(root, text='/', padx=16, pady=16, bd=8, font='arial 20 bold', bg='powder blue')
b_divide.grid(row=4, column=1)
b_divide.bind("<Button-1>", click)
b_equal = Button(root, text='=', padx=16, pady=16, bd=8, font='arial 20 bold', bg='powder blue')
b_equal.grid(row=4, column=2)
b_equal.bind("<Button-1>", click)
b_all_clear = Button(root, text='AC', padx=1, pady=16, bd=8, font='arial 20 bold', bg='powder blue')
b_all_clear.grid(row=4, column=3)
b_all_clear.bind("<Button-1>", click)


root.mainloop()