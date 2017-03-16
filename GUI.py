# -*- coding: utf-8 -*-
from Tkinter import *
from FileIO import get_verb_array


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
        
        self.chapters_list = Listbox(self.sidebar,height=4,selectmode=EXTENDED, background = "lemon chiffon", exportselection=False)
        #PROB CAN DELETE
        #self.chapters_list.grid(row=1)
        #Centers within current size of sidebar
        self.chapters_list.place(x=sidebar_width/2, y=55, anchor="center")
        for i in range(0,22):
            self.chapters_list.insert(i, "Chapter %d" %(i+3))

        self.aspect_label = Label(self.sidebar, text = "Select Verb Aspect(s):",  background = "lemon chiffon")
    
        self.aspect_label.place(x=sidebar_width/2, y=105, anchor="center")    

        self.aspect_list = Listbox(self.sidebar,height=4,selectmode=EXTENDED, background = "lemon chiffon", exportselection=False)
        self.aspect_list.place(x=sidebar_width/2, y=155, anchor="center")

        for item in ["Regular","Potential","Passive", "Causative", "Causative passive"]:
            self.aspect_list.insert(END, item)

        
        self.form_label = Label(self.sidebar, text = "Select Verb Form(s):",  background = "lemon chiffon")
        self.form_label.place(x=sidebar_width/2, y=205, anchor="center")    

        self.form_list = Listbox(self.sidebar,height=4,selectmode=EXTENDED, background = "lemon chiffon", exportselection=False)
        self.form_list.place(x=sidebar_width/2, y=255, anchor="center")

        for item in ["Non-past","Past","Te", "Tai","Volitional", "Tara","Ba"]:
            self.form_list.insert(END, item)
        
        self.pos_var = IntVar()
        self.neg_var = IntVar()
        self.polarity_label = Label(self.sidebar, text = "Select Polarity:",  background = "lemon chiffon")
        self.polarity_label.place(x=sidebar_width/4, y=305, anchor="center")  
        self.pos_checkbox = Checkbutton(self.sidebar, text="Pos.", background = "lemon chiffon", variable=self.pos_var)
        self.neg_checkbox = Checkbutton(self.sidebar, text="Neg.", background = "lemon chiffon",variable=self.neg_var)
        self.pos_checkbox.place(x=sidebar_width-85, y=305, anchor="center")
        self.neg_checkbox.place(x=sidebar_width-35, y=305, anchor="center")
        
        self.past_var = IntVar()
        self.present_var = IntVar()
        self.tense_label = Label(self.sidebar, text = "Select Tense:",  background = "lemon chiffon")
        self.tense_label.place(x=sidebar_width/4.5, y=330, anchor="center")  
        self.past_checkbox = Checkbutton(self.sidebar, text="Past", background = "lemon chiffon",variable=self.past_var)
        self.present_checkbox = Checkbutton(self.sidebar, text="Present", background = "lemon chiffon",variable=self.present_var)
        self.past_checkbox.place(x=sidebar_width-95, y=330, anchor="center")
        self.present_checkbox.place(x=sidebar_width-35, y=330, anchor="center")
        
        self.kana_var = IntVar()
        self.kanji_var= IntVar()
        self.display_label = Label(self.sidebar, text = "Display:",  background = "lemon chiffon")
        self.display_label.place(x=sidebar_width/6, y=355, anchor="center")  
        self.kana_checkbox = Checkbutton(self.sidebar, text="Kana", background = "lemon chiffon", variable=self.kana_var)
        self.kanji_checkbox = Checkbutton(self.sidebar, text="Kanji", background = "lemon chiffon",variable=self.kanji_var)
        self.kana_checkbox.place(x=sidebar_width-100, y=355, anchor="center")
        self.kanji_checkbox.place(x=sidebar_width-40, y=355, anchor="center")
        
        self.u_var = IntVar()
        self.ru_var = IntVar()
        self.irr_var = IntVar()
        self.type_label = Label(self.sidebar, text = "Select Type:",  background = "lemon chiffon")
        self.type_label.place(x=sidebar_width/5, y=380, anchor="center")  
        self.u_checkbox = Checkbutton(self.sidebar, text="U", background = "lemon chiffon",variable=self.u_var)
        self.ru_checkbox = Checkbutton(self.sidebar, text="Ru", background = "lemon chiffon",variable=self.ru_var)
        self.irr_checkbox =  Checkbutton(self.sidebar, text="Irr.",background = "lemon chiffon",variable=self.irr_var)
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
        
    def collect_sidebar_data(self):
        selected_chapters = [x+3 for x in list(self.chapters_list.curselection())]
        if selected_chapters == tuple():
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select chapters from Genki.",width=200)
            msg.pack()

            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
            return
            
        selected_aspects = self.aspect_list.curselection()
        if selected_aspects == tuple():
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select between regular, potential, etc.",width=200)
            msg.pack()

            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
            return 

        selected_forms = self.form_list.curselection()
        if selected_forms == tuple():
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select verb forms to practice.",width=200)
            msg.pack()

            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
            return 
    
        positive = self.pos_var.get()
        negative = self.neg_var.get()
        if not (negative or positive):
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select positive, negative, or both.",width=200)
            msg.pack()

            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
            return
        
        past = self.past_var.get()
        present = self.present_var.get()
        if not(past or present):
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select a tense(s) to practice.",width=200)
            msg.pack()
            
            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
            return
        
        kana = self.kana_var.get()
        kanji = self.kanji_var.get()
        if not(kana or kanji):
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select kana, kanji, or both to display.",width=200)
            msg.pack()
            
            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
            return
            
        u = self.u_var.get()
        ru = self.ru_var.get()
        irr = self.irr_var.get()
        if not(u or (ru or irr)):
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select the types of verbs to practice.",width=200)
            msg.pack()
            
            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
            return
            
        try:
            num_verbs = int(self.num_user_entry.get())
            if (num_verbs < 1):
                top = Toplevel()
                top.title("Error")
            
                msg = Message(top, text="Please enter the number of verbs to practice.",width=200)
                msg.pack()
            
                button = Button(top, text="Dismiss", command=top.destroy)
                button.pack()
        except:
            ValueError
            top = Toplevel()
            top.title("Error")
                
            msg = Message(top, text="Please enter the number of verbs to practice.",width=200)
            msg.pack()
                
            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
            return
            
            #TODO: Implement polite and plain
            #TODO: Implement the rest of the function to get the list of conjugated verbs
    
        
        verbs_to_conjugate = get_verb_array(selected_chapters, u, ru, irr)
            
            
        
        return
    
    def fill_input_window(self, input_window_width, height):
            # MAKE LARGER
            self.dictionary_marker = Label(self.input_window, text = "Dictionary", background = "pale turquoise")
            self.dictionary_marker.place(x=input_window_width/2, y=height/3 -10, anchor="center")
    
    
            self.meaning_marker = Label(self.input_window, text = "Meaning", background = "pale turquoise")
            self.meaning_marker.place(x=input_window_width/2, y=height/3 + 30, anchor="center")
    
    
            self.user_entry = Entry(self.input_window, width=30,background = "lemon chiffon")
            self.user_entry.delete(0, END)
            self.user_entry.insert(0, "")
            self.user_entry.place(x=input_window_width/2,y=height/2, anchor="center")
    
    
            self.aspect_marker = Label(self.input_window, text = "Aspect", background = "pale turquoise")
            self.aspect_marker.place(x=input_window_width/3 -10, y=height/2 +40, anchor="center")
            
            
            self.form_marker = Label(self.input_window, text = "Form", background = "pale turquoise")
            self.form_marker.place(x=input_window_width/3 -10, y=height/2 + 60, anchor="center")
            
            self.polarity_marker = Label(self.input_window, text = "Polarity", background = "pale turquoise")
            self.polarity_marker.place(x=input_window_width/3 -10, y=height/2 + 80, anchor="center")
            
            
            self.tense_marker = Label(self.input_window, text = "Tense", background = "pale turquoise")
            self.tense_marker.place(x=input_window_width/3 - 10, y=height/2 + 100, anchor="center")

            self.speech_level_marker = Label(self.input_window, text = "Speech Level", background = "pale turquoise")
            self.speech_level_marker.place(x=input_window_width/3 - 10, y=height/2 + 120, anchor="center")
            
            
            self.restart_button = Button(self.input_window, text="Restart", command=self.collect_sidebar_data)
            self.restart_button.place(x=input_window_width/2 - 10, y=height/2 + 140, anchor="center")


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
        self.fill_input_window(input_window_width = width - 210, height = height)
        print dir(self.sidebar)


        
    

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
