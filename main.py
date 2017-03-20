# -*- coding: utf-8 -*-
from GUI import Application

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()
