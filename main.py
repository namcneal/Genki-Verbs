#!/usr/bin/python
from Tkinter import Tk
from GUI import Application

if __name__ == '__main__':
    root = Tk()
    root.resizable(0, 0)
    app = Application(master=root)
    app.mainloop()
    root.destroy()
