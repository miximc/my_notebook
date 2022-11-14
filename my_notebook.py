from tkinter import *
from tkinter import ttk
from datetime import datetime
current_date = datetime.now().date()

col = 0
strok = 1
i = 0
h = 0

window = Tk()
window.title('Ежедневник')

file = open('test_2.txt', 'a')
file.write(f'\nДата: {current_date}\n')
file.close()

file_2 = open('dela.txt')
dela_2 = []
for b in file_2:
    a = b[:-1]
    dela_2.append(a)
file_2.close()

def history():      # функция для пополнения дел из прошлых записей и работы с ними
    global strok, i
    file_2 = open('dela.txt')
    file = open('test_2.txt', 'a')
    def m():
        global h
        if ch_1_s.get() == 1:
            m = dela_2[h]
            file = open('test_2.txt', 'a')
            plus = 'сделано'
            file.write(f'{dela_2[h]} - {plus}\n')
            h += 1
        else:
            m = str(dela_2[h])
            file = open('test_2.txt', 'a')
            plus = 'не сделано'
            file.write(f'{dela_2[h]} - {plus}\n')
            h += 1

    try:
        lbl = Label(window, text=dela_2[i].split()).grid(column=col, row=strok+1)
        bt_chek = Button(window, text='Save', command=m).grid(column=col + 2, row=strok+1)
        ch_1_s = IntVar()
        ch_1 = Checkbutton(bg='lightgrey', var=ch_1_s).grid(column=col + 1, row=strok+1)
        strok += 1
        i += 1
    except IndexError:
        lbl = Label(window, text='Cписок окончен').grid(column=4, row=1)
    file.close()
    file_2.close()

def general():   # функция для пополнения в файл с делами, а также отметка о проделанных делах
    global strok
    pole_lbl = pole.get()
    lbl_pole = Label(window,text=pole_lbl).grid(column=col,row=strok+1)
    ch_1_s = IntVar()
    plus = ''
    def m():
        file = open('test_2.txt', 'a')
        if ch_1_s.get() == 1:
            plus = 'сделано'
            file.write(f'{pole_lbl} - {plus}\n')
            print(plus)
        else:
            plus = 'не сделано'
            file.write(f'{pole_lbl} - {plus}\n')
            print(plus)
        file.flush()

    ch_1 = Checkbutton(bg='lightgrey',var=ch_1_s).grid(column=col+1, row=strok+1)
    bt_chek = Button(window,text='Save', command=m ).grid(column=col+2,row=strok+1)
    strok += 1
    f2 = open('dela.txt', 'a')
    f2.write(f'{pole_lbl}\n')
    f2.close()
    pole.delete(0, END)
date = f'Сегодня {current_date}'
today = Label(window, text =date).grid(column=0,row=0)
pole = Entry(window, width=25)
pole.grid(column=0,row=1)
use = Button(window,text='add',command=general).grid(column=1,row=1)
his_btn = Button(window,text='History',command=history).grid(column=2,row=1)

window.geometry('500x500')
window.mainloop()