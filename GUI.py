# -*- coding: utf-8 -*-
from Tkinter import *

class Application(Frame):
    def createWidgets(self, sidebar_width):
        height = self.master.winfo_height()
        input_window_width = self.master.winfo_width() - sidebar_width
        
        #Create the instance, THEN call the grid() method. 
        self.sidebar = Frame(self,height=height, width=sidebar_width)
        self.sidebar.grid_propagate(0)
        self.sidebar.grid(row=0, column=0)

        self.input_window = Frame(self, background = "midnight blue",height=height, width = input_window_width)
        self.input_window.grid(row=0, column=1)

    def fill_sidebar(self):
        
        ## HOW DO YOU CENTER THESE
        self.chapters_label = Label(self.sidebar, text = "Select chapters from Genki:",anchor = CENTER)
        self.chapters_label.grid(row=0)

        self.chapters_list = Listbox(self.sidebar,height=6,selectmode=EXTENDED)
        self.chapters_list.grid(row=1)
        for i in range(0,25):
            self.chapters_list.insert(i, "Chapter %d" %(i+1)) 
        

    def disable_sidebar(self):
        pass
    
    def enable_sidebar(self):
        pass
        
    def __init__(self, master=None, height=500, width = 1000):
        Frame.__init__(self, master)
        master.geometry("%dx%d" %(width, height))
        master.update()
        self.grid()
 
        self.createWidgets(sidebar_width = 350)
        self.fill_sidebar()
        print dir(self.sidebar)


        
    

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
