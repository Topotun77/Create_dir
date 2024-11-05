import os
import tkinter as tk
from tkinter import filedialog as fd, scrolledtext
from tkinter import messagebox as mb
import subprocess
from tkinter.constants import (SUNKEN, FLAT, RAISED, GROOVE,
                               RIDGE, END, NW, X, CENTER, S, E, W, N)


def to_str(c):
    s = str(c)
    if len(s) < 2:
        s = "0" + s
    return s


def get_path():
    file_ = file_entry.get()
    if '/' not in file_:
        dir_ = dir_entry.get()
        file_ = (dir_+'/'+file_).replace("\\", "/")
    return os.path.abspath(file_)


def read_list():
    file_full = get_path()
    text_box.delete(0.0, END)
    try:
        with open(file_full, 'r') as fl:
            text = fl.read()
            text_box.insert(0.0, chars=text)
    except FileNotFoundError as err:
        text_box.insert(0.0, chars=f'Файл {file_full} не найден!')


def save_list():
    file_full = get_path()
    try:
        text = text_box.get(0.0, END)
        with open(file_full, 'w') as fl:
            fl.write(text)
            mb.showinfo('Файл сохранен', f'Файл {file_full} сохранен успешно!', parent=window)
    except FileNotFoundError as err:
        mb.showerror('Error', f'Файл {file_full} не найден!', parent=window)


def create_dir():
    c = 1
    file_ = file_entry.get()
    dir_ = dir_entry.get()
    try:
        if dir_:
            os.chdir(dir_)
        with open(file_, "r") as fl:
            while True:
                ln = fl.readline()
                if not ln:
                    break
                os.mkdir(to_str(c) + " " + ln.strip())
                c += 1
    except FileNotFoundError or OSError as err:
        mb.showerror('Error', f'Файл {file_} не найден!')
    # fd.askdirectory()
    dir_full = os.path.abspath(dir_)
    print(dir_full)
    subprocess.Popen(f'explorer "{dir_full}"')


def choice_dir():
    dir_ = dir_entry.get()
    txt = fd.askdirectory(initialdir=dir_)
    if txt:
        dir_entry.delete(0, 'end')
        dir_entry.insert(0, txt)
    read_list()


def choice_list():
    file_ = file_entry.get()
    if '/' in file_:
        dir_ = file_[0:file_.rfind('/')]
    else:
        dir_ = dir_entry.get()
    txt = fd.askopenfilename(initialdir=dir_)
    if txt:
        file_entry.delete(0, 'end')
        file_entry.insert(0, txt)
    read_list()


window = tk.Tk()
window.title('Создание папок по списку из файла')
try:
    window.iconbitmap(default="./folders-2.ico")
except:
    pass
window.geometry("500x500")
window.minsize(460,200)
# window.columnconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)


frame1 = tk.Frame(
    window,
    padx=10,
    pady=10,
    relief=SUNKEN,
    border=1
)
frame1.pack()

number2 = tk.Label(frame1, text="Директория вывода:", justify='right')
number2.grid(row=0, column=0)

number1 = tk.Label(frame1, text="Файл со списком:", justify='right')
number1.grid(row=1, column=0)

dir_entry = tk.Entry(frame1, width=50)
dir_entry.grid(row=0, column=1)
txt = './'
dir_entry.insert(0, txt)

file_entry = tk.Entry(frame1, width=50)   #, justify='center')
file_entry.grid(row=1, column=1)
txt = 'list.txt'
file_entry.insert(0, txt)

button_dir = tk.Button(frame1, text="/", width=1, height=0, command=choice_dir)
button_dir.grid(row=0, column=2)

button_file = tk.Button(frame1, text="...", width=1, height=0, command=choice_list)
button_file.grid(row=1, column=2)

frame2 = tk.Frame(
    window,
    padx=5,
    pady=5,
    relief=RIDGE,
    border=1
)
frame2.pack(fill="both", expand=True)

frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1)
frame2.rowconfigure(0, weight=1)

text_box = scrolledtext.ScrolledText(frame2, width=3000,  height=3000)
text_box.grid(row=0, column=0, columnspan=2, rowspan=1)

button_save = tk.Button(frame2, text="Сохранить файл", width=20, height=2, command=save_list)
button_save.grid(row=1, column=0, sticky=E)

button_create = tk.Button(frame2, text="Создать директории", width=20, height=2, command=create_dir)
button_create.grid(row=1, column=1, sticky=W)

read_list()

window.mainloop()
