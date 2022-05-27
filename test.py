from tkinter import *

root = Tk()
root.geometry('640x640')
root1 = Tk()
root1.geometry('640x640')

root.title('1')
root1.title('2')

A = '(a + b)²:'
B = '(a - b)²'
C = 'a² + b²'
D = 'a² + b²'
E = 'a² + 1/a²'
F = 'a² + 1/a²'
G = '(a + b)(a - b)'
H = '(x + a)(x + b)'

AA = 'a² + 2ab + b²'
BB = 'a² - 2ab + b²'
CC = '(a + b)² - 2ab'
DD = '(a - b)² + 2ab'
EE = '(a + 1/a)² - 2'
FF = '(a - 1/a)² + 2'
GG = 'a² + b²'
HH = 'x² + (a + b)x + ab'

correct = '맞히셨습니다.'
incorrect = '틀리셨습니다. 계속 시도하세요'

entry1 = Entry(root, bg='yellow')
entry1.pack()

entry2 = Entry(root, bg='yellow')
entry2.pack()

entry1.grid(row=0, column=0)
entry2.grid(row=1, comumn=0)

def correct_check1():
    input1 = entry1.get()
    print(input1)
    if (input1 == AA):
        print(correct)
    elif (input != AA):
        print(incorrect)

def correct_check2():
    input2 = entry2.get()
    print(input2)
    if (input2 == BB):
        print(correct)
    else:
        print(incorrect)

btn1 = Button(root, text=A, bg='skyblue', command=correct_check1)
btn1.pack()

btn2 = Button(root, text=B, bg='skyblue', command=correct_check2)
btn2.pack()

root.mainloop()