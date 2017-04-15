#!/usr/bin/python
from Tkinter import Tk
from GUI import Application

if __name__ == '__main__':
    root = Tk()
    root.resizable(0, 0)
    root.iconbitmap(default='conj_icon.ico') 
    app = Application(master=root)
    root.wm_title("Genki Verb! Conjugation Practice Program")
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    app.mainloop()
    
