# -*- coding: utf-8 -*-
from Tkinter import *

class Application(Frame):
    def createWidgets(self, sidebar_width):
        height = self.master.winfo_height()
        input_window_width = self.master.winfo_width() - sidebar_width
        
        #Create the instance, THEN call the grid() method. 
        self.sidebar = Frame(self,height=height, width=sidebar_width, background="papaya whip")
        #quick and dirty way of centering could be setting this to 1..would this work with other frames?
        self.sidebar.grid_propagate(0)
        self.sidebar.grid(row=0, column = 0)

        self.input_window = Frame(self, background = "pale turquoise",height=height, width = input_window_width)
        self.input_window.grid(row=0, column=1)

    def fill_sidebar(self, sidebar_width):
        
        self.chapters_label = Label(self.sidebar, text = "Select chapters from Genki:", background = "lemon chiffon")
        self.chapters_label.grid(row=0)
        #Centers within current size of sidebar, not sure how to standardize height/if even possible
        self.chapters_label.place(x=sidebar_width/2, y=10, anchor="center")
        
        self.chapters_list = Listbox(self.sidebar,height=4,selectmode=EXTENDED, background = "lemon chiffon")
        #PROB CAN DELETE
        #self.chapters_list.grid(row=1)
        #Centers within current size of sidebar
        self.chapters_list.place(x=sidebar_width/2, y=55, anchor="center")
        for i in range(2,25):
            self.chapters_list.insert(i, "Chapter %d" %(i+1))

        self.aspect_label = Label(self.sidebar, text = "Select Verb Aspect(s):",  background = "lemon chiffon")
    
        self.aspect_label.place(x=sidebar_width/2, y=105, anchor="center")    

        self.aspect_list = Listbox(self.sidebar,height=4,selectmode=EXTENDED, background = "lemon chiffon")
        self.aspect_list.place(x=sidebar_width/2, y=155, anchor="center")

        for item in ["Potential","Passive", "Causative", "Causative passive","Regular"]:
            self.aspect_list.insert(END, item)

        
        self.form_label = Label(self.sidebar, text = "Select Verb Form(s):",  background = "lemon chiffon")
        self.form_label.place(x=sidebar_width/2, y=205, anchor="center")    

        self.form_list = Listbox(self.sidebar,height=4,selectmode=EXTENDED, background = "lemon chiffon")
        self.form_list.place(x=sidebar_width/2, y=255, anchor="center")

        for item in ["Masu","Te", "Tai", "Tara","Ba","Volitional", "Imperfective"]:
            self.form_list.insert(END, item)

        self.polarity_label = Label(self.sidebar, text = "Select Polarity:",  background = "lemon chiffon")
        self.polarity_label.place(x=sidebar_width/4, y=305, anchor="center")  
        self.pos_checkbox = Checkbutton(self.sidebar, text="Pos.",onvalue="RGB", offvalue="L",  background = "lemon chiffon")
        self.neg_checkbox = Checkbutton(self.sidebar, text="Neg.",onvalue="RGB", offvalue="L",  background = "lemon chiffon")
        self.pos_checkbox.place(x=sidebar_width-85, y=305, anchor="center")
        self.neg_checkbox.place(x=sidebar_width-35, y=305, anchor="center")

        self.tense_label = Label(self.sidebar, text = "Select Tense:",  background = "lemon chiffon")
        self.tense_label.place(x=sidebar_width/4.5, y=330, anchor="center")  
        self.past_checkbox = Checkbutton(self.sidebar, text="Past",onvalue="RGB", offvalue="L",  background = "lemon chiffon")
        self.present_checkbox = Checkbutton(self.sidebar, text="Present",onvalue="RGB", offvalue="L",  background = "lemon chiffon")
        self.past_checkbox.place(x=sidebar_width-95, y=330, anchor="center")
        self.present_checkbox.place(x=sidebar_width-35, y=330, anchor="center")

        self.display_label = Label(self.sidebar, text = "Display:",  background = "lemon chiffon")
        self.display_label.place(x=sidebar_width/6, y=355, anchor="center")  
        self.kana_checkbox = Checkbutton(self.sidebar, text="Kana",onvalue="RGB", offvalue="L",  background = "lemon chiffon")
        self.kanji_checkbox = Checkbutton(self.sidebar, text="Kanji",onvalue="RGB", offvalue="L",  background = "lemon chiffon")
        self.kana_checkbox.place(x=sidebar_width-100, y=355, anchor="center")
        self.kanji_checkbox.place(x=sidebar_width-40, y=355, anchor="center")
        
        self.type_label = Label(self.sidebar, text = "Select Type:",  background = "lemon chiffon")
        self.type_label.place(x=sidebar_width/5, y=380, anchor="center")  
        self.u_checkbox = Checkbutton(self.sidebar, text="U",onvalue="RGB", offvalue="L",  background = "lemon chiffon")
        self.ru_checkbox = Checkbutton(self.sidebar, text="Ru",onvalue="RGB", offvalue="L",  background = "lemon chiffon")
        self.irr_checkbox =  Checkbutton(self.sidebar, text="Irr.",onvalue="RGB", offvalue="L", background = "lemon chiffon")
        self.u_checkbox.place(x=sidebar_width-110, y=380, anchor="center")
        self.ru_checkbox.place(x=sidebar_width-70, y=380, anchor="center")
        self.irr_checkbox.place(x=sidebar_width-25, y=380, anchor="center")

        self.number_label = Label(self.sidebar, text = "Number to Practice:",  background = "lemon chiffon")
        self.number_label.place(x=sidebar_width-145, y=415, anchor="center")

        self.num_user_entry = Entry(self.sidebar, width=5,background = "lemon chiffon")

        self.num_user_entry.delete(0, END)
        self.num_user_entry.insert(0, "15")
        self.num_user_entry.place(x=sidebar_width-40, y=415, anchor="center")

        # To fetch the current entry text, use the get method:
        # s = e.get()
        

    def disable_sidebar(self):
        pass
    
    def enable_sidebar(self):
        pass
        
    def __init__(self, master=None, height=450, width = 700):
        Frame.__init__(self, master)
        master.geometry("%dx%d" %(width, height))
        master.update()
        self.grid()
 
        self.createWidgets(sidebar_width = 210)
        self.fill_sidebar(sidebar_width = 210)
        print dir(self.sidebar)


        
    

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
