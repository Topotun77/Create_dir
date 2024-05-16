import os
import tkinter as tk
from tkinter import filedialog as fd

# print(help(tk))


def ToStr(c):
    s=str(c)
    if len(s)<2:
        s = "0"+s
    return s


def create_dir():
    c=1
    file_ = file_entry.get()
    dir_ = dir_entry.get()
    os.chdir(dir_)
    fl = open(file_, "r")

    while True:
        ln = fl.readline()
        if not ln:
            break
        #print(ln.strip())
        os.mkdir(ToStr(c)+" "+ln.strip())
        c+=1
    fd.askdirectory()

def choice_dir():
    # txt = './Verstka'
    dir_ = dir_entry.get()
    txt = fd.askdirectory(initialdir=dir_)
    dir_entry.delete(0, 'end')
    dir_entry.insert(0, txt)


#os.chdir(Ndir)

window = tk.Tk()
window.configure(bg='orange')
# window['bg'] = 'yellow'   #(tuple([255, 255, 0]))
window.title('Создание директориев по списку')
window.geometry("500x200")
window.resizable(False, False)

button_create = tk.Button(window, text="Создать директории", width=55, height=2, command=create_dir)
button_create.place(x=35, y=100)

file_entry = tk.Entry(window, width=50)
file_entry.place(x=140, y=50)
txt = 'list.txt'
file_entry.insert(0, txt)

dir_entry = tk.Entry(window, width=50)
dir_entry.place(x=140, y=25)
txt = './'
# txt = './Verstka'
dir_entry.insert(0, txt)

button_dir = tk.Button(window, text="/", width=1, height=0, command=choice_dir)
button_dir.place(x=450, y=22)

number1 = tk.Label(window, text="Файл со списком: ")
number1.place(x=22, y=50)
number2 = tk.Label(window, text="Директория вывода: ")
number2.place(x=10, y=25)

window.mainloop()


# вывести текущую директорию
# print("Текущая деректория:", os.getcwd())