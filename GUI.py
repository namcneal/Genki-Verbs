# -*- coding: utf-8 -*-
from Tkinter import *
import FileIO
import random
from Conjugation import get_random_conjugation

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
    
    def get_available_chapters(self):
        import glob, os
        chapters = list()
        for file_name in glob.glob("*.csv"):
            file_name = file_name[20:][:-4]
            chapters.append(int(file_name))
        chapters.sort()
        return chapters

    def fill_sidebar(self, sidebar_width):
        
        self.chapters_label = Label(self.sidebar, text = "Select chapters from Genki:", background = "lemon chiffon")
        self.chapters_label.grid(row=0)
        #Centers within current size of sidebar, not sure how to standardize height/if even possible
        self.chapters_label.place(x=sidebar_width/2, y=10, anchor="center")
        
        self.chapters_list = Listbox(self.sidebar,height=4,selectmode=EXTENDED, background = "lemon chiffon", exportselection=False)
        self.chapters_list.select_set(0)
        self.chapters_list.place(x=sidebar_width/2, y=55, anchor="center")
        
        for i in self.get_available_chapters():
            self.chapters_list.insert(i-3, "Chapter %d" %i)

        self.aspect_label = Label(self.sidebar, text = "Select Verb Aspect(s):",  background = "lemon chiffon")
    
        self.aspect_label.place(x=sidebar_width/2, y=105, anchor="center")    

        self.aspect_list = Listbox(self.sidebar,height=4,selectmode=EXTENDED, background = "lemon chiffon", exportselection=False)
        self.aspect_list.place(x=sidebar_width/2, y=155, anchor="center")
        self.aspect_list.select_set(0)

        for item in ["Regular","Potential","Passive", "Causative", "Causative passive"]:
            self.aspect_list.insert(END, item)

        
        self.form_label = Label(self.sidebar, text = "Select Verb Form(s):",  background = "lemon chiffon")
        self.form_label.place(x=sidebar_width/2, y=205, anchor="center")    

        self.form_list = Listbox(self.sidebar,height=4,selectmode=EXTENDED, background = "lemon chiffon", exportselection=False)
        self.form_list.place(x=sidebar_width/2, y=255, anchor="center")
        self.form_list.select_set(0)

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
        self.past_checkbox.place(x=sidebar_width-35, y=330, anchor="center")
        self.present_checkbox.place(x=sidebar_width-95, y=330, anchor="center")
        
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
        
        self.polite_var = IntVar()
        self.plain_var = IntVar()
        self.speech_level_label = Label(self.sidebar, text = "Speech Level:",  background = "lemon chiffon")
        self.speech_level_label.place(x=sidebar_width/4 - 05, y=405, anchor="center")
        self.polite_checkbox = Checkbutton(self.sidebar, text="Polite", background = "lemon chiffon", variable=self.polite_var)
        self.plain_checkbox = Checkbutton(self.sidebar, text="Plain", background = "lemon chiffon",variable=self.plain_var)
        self.polite_checkbox.place(x=sidebar_width-85, y=405, anchor="center")
        self.plain_checkbox.place(x=sidebar_width-30, y=405, anchor="center")

        self.number_label = Label(self.sidebar, text = "Number to Practice:",  background = "lemon chiffon")
        self.number_label.place(x=sidebar_width-145, y=432, anchor="center")

        self.num_user_entry = Entry(self.sidebar, width=5,background = "lemon chiffon")
        
        self.num_user_entry.delete(0, END)
        self.num_user_entry.insert(0, "15")
        self.num_user_entry.place(x=sidebar_width-40, y=432, anchor="center")
    
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

        self.number_marker = Label(self.input_window, text = "Completed: /", background = "pale turquoise")
        self.number_marker.place(x=input_window_width/2, y=height/2 + 160, anchor="center")
        
        self.restart_button = Button(self.input_window, text="Restart", background= "papaya whip")
        self.restart_button.place(x=input_window_width/2 - 150, y=height/2 + 200, anchor="center")
    
        self.skip_button = Button(self.input_window, text="Skip for Now", background= "papaya whip")
        self.skip_button.place(x=input_window_width/2, y=height/2 + 200, anchor="center")

        self.show_answer_button = Button(self.input_window, text="Show Answer", background= "papaya whip")
        self.show_answer_button.place(x=input_window_width/2+150, y=height/2 + 200, anchor="center")



    
    def get_and_display_current_conjugation(self):
        self.user_entry.delete(0, END)
        self.dictionary_marker.config(text = self.verbs[0][0])
        self.dictionary_marker.update()

        self.meaning_marker.config(text = self.verbs[0][1])
        self.meaning_marker.update()

        self.aspect_marker.config(text = self.verbs[0][2])
        self.aspect_marker.update()

        self.form_marker.config(text = self.verbs[0][3])
        self.form_marker.update()

        self.polarity_marker.config(text = self.verbs[0][4])
        self.polarity_marker.update()
        
        self.tense_marker.config(text = self.verbs[0][5])
        self.tense_marker.update()

        casual = ""
        if self.verbs[0][6] == u"Plain": casual = u"/Casual" 
        self.speech_level_marker.config(text = self.verbs[0][6]+casual)
        self.speech_level_marker.update()

        self.number_marker.config(text = "Completed: %d/%d" %(self.num_verbs-len(self.verbs), self.num_verbs))
        

    def is_conjugation_correct(self):
        if (self.user_entry.get() == self.verbs[0][7][0]) or \
            self.user_entry.get() == self.verbs[0][7][1]:
            return True
        else: return False

    def display_end_screen(self):
        self.user_entry.delete(0, END) 
        self.user_entry.insert(0, u"やった！")
        self.input_window.configure(background = "pale green")
        self.dictionary_marker.config(background = "pale green",text = u"やった！")
        self.dictionary_marker.update()

        self.meaning_marker.config(background = "pale green",text = u"やった！")
        self.meaning_marker.update()

        self.aspect_marker.config(background = "pale green",text = u"やった！")
        self.aspect_marker.update()

        self.form_marker.config(background = "pale green",text = u"やった！")
        self.form_marker.update()

        self.polarity_marker.config(background = "pale green",text = u"やった！")
        self.polarity_marker.update()
        
        self.tense_marker.config(background = "pale green",text = u"やった！")
        self.tense_marker.update()

        self.speech_level_marker.config(background = "pale green",text = u"やった！")
        self.speech_level_marker.update()

        self.number_marker.config(background = "pale green", text = "Press restart to play again!")


    def progress_game(self, event=None):
        if self.is_conjugation_correct() :
            if len(self.verbs)==1:
                self.display_end_screen()
            else:
                del self.verbs[0]
                self.user_entry.delete(0,'end')
                self.get_and_display_current_conjugation()

    def restore_skip_button(self, event=None):
        self.skip_button.config(state = NORMAL)
        pass
        
    def skip_verb(self, event=None):
        self.user_entry.delete(0, END) 
        self.skip_button.config(state = DISABLED)

        try:
            self.verbs.append(self.verbs.pop(0))
            self.user_entry.delete(0,'end')
            self.get_and_display_current_conjugation()
        except:
            IndexError
        self.master.after(3000, self.restore_skip_button)

    def show_answer(self, event = None):
        try:
            self.user_entry.delete(0, END) 
            self.user_entry.insert(0, self.verbs[0][7][1])
        except IndexError:
            pass

    def collect_sidebar_data(self, event=None):
        selected_chapters = [x+3 for x in list(self.chapters_list.curselection())]
        if selected_chapters == tuple():
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select chapters from Genki.",width=200, background="alice blue")
            msg.pack()

            button = Button(top, text="Dismiss", command=top.destroy, background= "pale turquoise")
            button.pack()
            return
            
        selected_aspects = self.aspect_list.curselection()
        if selected_aspects == tuple():
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select between regular, potential, etc.",width=200,  background="alice blue")
            msg.pack()

            button = Button(top, text="Dismiss", command=top.destroy, background= "pale turquoise")
            button.pack()
            return 

        selected_forms = self.form_list.curselection()
        if selected_forms == tuple():
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select verb forms to practice.",width=200, background="alice blue")
            msg.pack()

            button = Button(top, text="Dismiss", command=top.destroy, background= "pale turquoise")
            button.pack()
            return 
    
        positive = self.pos_var.get()
        negative = self.neg_var.get()
        if not (negative or positive):
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select positive, negative, or both.",width=200, background="alice blue")
            msg.pack()

            button = Button(top, text="Dismiss", command=top.destroy, background= "pale turquoise")
            button.pack()
            return
        
        past = self.past_var.get()
        present = self.present_var.get()
        if not(past or present):
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select a tense(s) to practice.",width=200, background="alice blue")
            msg.pack()
            
            button = Button(top, text="Dismiss", command=top.destroy, background= "pale turquoise")
            button.pack()
            return
        
        kana = self.kana_var.get()
        kanji = self.kanji_var.get()
        if not(kana or kanji):
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select kana, kanji, or both to display.",width=200, background="alice blue")
            msg.pack()
            
            button = Button(top, text="Dismiss", command=top.destroy, background= "pale turquoise")
            button.pack()
            return
            
        u = self.u_var.get()
        ru = self.ru_var.get()
        irr = self.irr_var.get()
        if not(u or (ru or irr)):
            top = Toplevel()
            top.title("Error")
            
            msg = Message(top, text="Please select the types of verbs to practice.",width=200, background="alice blue")
            msg.pack()
            
            button = Button(top, text="Dismiss", command=top.destroy, background= "pale turquoise")
            button.pack()
            return
            
        try:
            num_verbs = int(self.num_user_entry.get())
            if (num_verbs < 1) or (num_verbs > 500):
                top = Toplevel()
                top.title("Error")
            
                msg = Message(top, text="Please enter the number (1-500) of verbs to practice.",width=200, background="alice blue")
                msg.pack()
            
                button = Button(top, text="Dismiss", command=top.destroy, background= "pale turquoise")
                button.pack()
                return
        except:
            ValueError
            top = Toplevel()
            top.title("Error")
                
            msg = Message(top, text="Please enter the number of verbs to practice.",width=200, background="alice blue")
            msg.pack()
                
            button = Button(top, text="Dismiss", command=top.destroy, background= "pale turquoise")
            button.pack()
            return
            
            
        polite = self.polite_var.get()
        plain = self.plain_var.get()
        if not(polite or plain):
            top = Toplevel()
            top.title("Error")
                            
            msg = Message(top, text="Please select the speech level(s) to practice.",width=200, background="alice blue")
            msg.pack()
                                    
            button = Button(top, text="Dismiss", command=top.destroy, background= "pale turquoise")
            button.pack()
            return
                                                

            #TODO: Implement the rest of the function to get the list of conjugated verbs
        
        # Clear old list and prepare for a new list of verbs based on current selection
        random.seed()
        self.game_params = {'aspect_indices' : selected_aspects, 
                            'form_indices' : selected_forms, 
                            'plain' : plain, 'polite' :polite, 
                            'pos' : positive, 'neg': negative, 
                            'past' : past, 'pres' : present, 
                            'kana' : kana, 'kanji' : kanji}
        self.num_verbs = num_verbs
        all_verbs = FileIO.get_verb_array(selected_chapters, u, ru, irr)
        for i in range(0, num_verbs):
            self.verbs.append(get_random_conjugation(random.choice(all_verbs),
                              **self.game_params))
        
        self.get_and_display_current_conjugation()

    def restart_game(self, event=None):
        self.skip_button.config(state = DISABLED)
        self.restart_button.config(state = DISABLED)
        
        self.num_verbs = -1
        self.game_params = dict()
        self.verbs = list()
        
        self.input_window.configure(background = "pale turquoise")
        self.dictionary_marker.config(background = "pale turquoise")
        self.dictionary_marker.update()

        self.meaning_marker.config(background = "pale turquoise")
        self.meaning_marker.update()

        self.aspect_marker.config(background = "pale turquoise")
        self.aspect_marker.update()

        self.form_marker.config(background = "pale turquoise")
        self.form_marker.update()

        self.polarity_marker.config(background = "pale turquoise")
        self.polarity_marker.update()
        
        self.tense_marker.config(background = "pale turquoise")
        self.tense_marker.update()

        self.speech_level_marker.config(background = "pale turquoise")
        self.speech_level_marker.update()

        self.number_marker.config(background = "pale turquoise")

        self.current_index = 0
        self.collect_sidebar_data()
        self.skip_button.config(state = NORMAL)
        self.restart_button.config(state = NORMAL)
        
    def __init__(self, master=None, height=450, width = 700):
        self.num_verbs = -1
        self.verbs = list()
        self.game_params = dict()
        self.current_index = 0
        self.current_conjugation = list()

        Frame.__init__(self, master)
        self.master.geometry("%dx%d" %(width, height))
        self.master.update()
        self.grid()
        self.createWidgets(sidebar_width = 210)
        self.fill_sidebar(sidebar_width = 210)
        self.fill_input_window(input_window_width = width - 210, height = height)

        # Bind all the buttons and keys
        self.master.bind('<Return>', self.progress_game)
        self.restart_button.config(command= self.restart_game)
        self.skip_button.config(command= self.skip_verb)
        self.show_answer_button.config(command=self.show_answer)
