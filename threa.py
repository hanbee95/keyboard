import tkinter as tk
import time
import threading
from pynput import keyboard
import sys
from tkinter import messagebox

root = tk.Tk()
root.title('ctrl z counter')
root.geometry('300x300')
root.bind('<Escape>', lambda e: sys.exit(1))
cnt = 0

def on_activate_z():
    global cnt
    cnt = cnt + 1
    print(cnt)  
def activate_esc():
    sys.exit('end')
def print_numbers(end): #  no capitals for functions in python
    with keyboard.GlobalHotKeys({
            '<ctrl>+z': on_activate_z,
            '<ctrl>+<shift>': activate_esc}) as h:
        h.join()

def print_hello():
    name_entry = tk.Label(root,text = cnt, font=('calibre',10,'normal'))
    name_entry.grid(row=1,column=3)
    print(cnt)

def background(func, args):
    name_entry = tk.Label(root,text = 'started', font=('calibre',10,'normal'))
    name_entry.grid(row=0,column=3)    
    th = threading.Thread(target=func, args=args)
    th.start()

def quit():
    sys.exit('end')

b1 = tk.Button(root,text='start',command = lambda : background(print_numbers, (50,))) #args must be a tuple even if it is only one
b1.grid(row=0,column=1)

b2 = tk.Button(root,text='write',command = print_hello)
b2.grid(row=1,column=1)

# b3 = tk.Button(root,text='close',command = quit)
# b3.grid(row=2,column=1)
root.protocol("WM_DELETE_WINDOW", quit)
root.mainloop()