# -*- coding: utf-8 -*-
from Tkinter import Tk
from GUI import Application

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()
