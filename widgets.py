import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import constants as c
import io

def sign_out_button(parent):
    sign_out_button = ctk.CTkButton(parent, 
            text = '',
            corner_radius = 15,
            image = ctk.CTkImage(light_image = Image.open(c.sign_out)),
            compound = 'top',
            fg_color = c.primaryColor,
            text_color = 'black',
            hover_color = c.backgroundColor)
    return sign_out_button

def nav_button(parent, command, img_path, text):
    photo = Image.open(img_path).resize((100,100))
    button = ctk.CTkButton(parent,
            text= '',
            font = ctk.CTkFont(size = 8),
            image = ctk.CTkImage(light_image= photo, size=(55, 55)),
            text_color = 'black',
            hover_color = c.backgroundColor,
            fg_color = c.primaryColor,
            compound = 'top',
            command = command)
    return button

def my_entry(parent, hint, font, isHidden = False, height = c.widget_height):
    char = ''
    if (isHidden == True):
        char = '*'
    search_bar = ctk.CTkEntry(parent, 
            placeholder_text = hint,
            font = font,
            corner_radius = c.radius, 
            fg_color = c.primaryColor,
            placeholder_text_color = c.fontColor,
            border_width = 0,
            height = height, 
            text_color = c.fontColor,
            show = char
            # lambda : '*' if isHidden else '*'
        )
    return search_bar

def my_entry_var(parent, hint, font, variable, isHidden = False, height = c.widget_height):
    char = ''
    if (isHidden == True):
        char = '*'
    search_bar = ctk.CTkEntry(parent, 
            placeholder_text = hint,
            font = font,
            corner_radius = c.radius, 
            fg_color = c.primaryColor,
            placeholder_text_color = c.fontColor,
            border_width = 0,
            text_color = c.fontColor,
            height = height, 
            show = char,
            textvariable = variable
            # lambda : '*' if isHidden else '*'
        )
    return search_bar

def my_button(parent, text, font, command):
    button = ctk.CTkButton(parent, 
            height = c.widget_height, 
            text = text,
            font = font,
            fg_color = c.buttonColor,
            hover_color = c.buttonHoverColor, 
            text_color = 'white',
            corner_radius = c.radius,
            command = command
        )
    return button

def frame_colored(parent):
    frame = ctk.CTkFrame(parent, fg_color = c.primaryColor, corner_radius = c.radius)
    return frame

def book_frame(parent, title, author, genre):
    frame = ctk.CTkFrame(parent, fg_color = c.backgroundColor)

    # grid configuration
    frame.rowconfigure(0, weight = 10, uniform = 'a')
    frame.rowconfigure((1,2), weight = 1, uniform = 'a')
    frame.columnconfigure(0, weight = 1, uniform = 'a')
    
    image_label = ctk.CTkLabel(frame,
                font=(c.family , 18, 'bold'),
                text=title,
                fg_color=c.backgroundColor,
                width=25,
                text_color = c.fontColor,
                image=ctk.CTkImage(light_image = Image.open(c.book_cover), size = (150,200)),
                compound = TOP,
                wraplength = 100)
    image_label.grid(row=0, column=0, sticky='nsew')
    tk.Label(frame, background=c.backgroundColor, width=25, font=(c.family , 12), text=author).grid(row=1, column=0, sticky='sew')
    tk.Label(frame, background=c.backgroundColor, width=25, font=(c.family , 10), text=genre).grid(row=2, column=0, sticky='new')

    return frame

def my_combobox(parent, values, variable):
    combobox = ctk.CTkComboBox(parent, 
                        width=200,
                        height = 35,
                        fg_color = 'white', 
                        border_color = c.primaryColor, 
                        button_color = c.primaryColor,
                        corner_radius = c.radius,
                        dropdown_fg_color = c.backgroundColor,
                        state='readonly', 
                        values=values,
                        variable =variable,
                        text_color = c.fontColor,
                        dropdown_text_color = c.fontColor,
                        dropdown_hover_color = c.primaryColor,
                        )
    return combobox
class SearchArea(ctk.CTkFrame):
    def __init__(self, parent, command, hint):
        super().__init__(parent, fg_color = c.backgroundColor)

        # grid configuration
        self.columnconfigure(0, weight = 8, uniform = 'a')
        self.columnconfigure(1, weight = 2, uniform = 'a')

        # :: search bar 
        self.search_bar = my_entry(self, hint = f'Search for {hint}', font = ctk.CTkFont(c.family, size = 20))
        self.search_bar.grid(row = 0 , column = 0, sticky = 'new', padx = (c.padding, 5), pady = c.padding)

        # :: search button
        self.search_button = my_button(self, text = 'search', font = ctk.CTkFont(c.family, size = 20), command= command)
        self.search_button.grid(row = 0, column = 1, sticky = 'new', padx = (5, c.padding), pady = c.padding)

class ScrollFrame(ttk.Frame):
    def __init__(self, parent, data, item_height):
        super().__init__(master = parent)

        # grid configuration
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 19, uniform = 'a')
        self.columnconfigure(1, weight = 1, uniform = 'a')

        # widget data
        self.data = data
        self.item_number = len(data)
        self.list_height = self.item_number * item_height

        # canvas 
        self.canvas = tk.Canvas(self, background = 'red', scrollregion = (0,0,self.winfo_width(),self.list_height))
        self.canvas.grid(row=0, column=0, sticky='nsew')

        # display frame
        self.frame = ttk.Frame(self)

        for item in self.data:
        	self.create_item(item).pack(expand = True, fill = 'both', pady =  4, padx = 10)
            
        # scrollbar 
        self.scrollbar = ttk.Scrollbar(self, orient = 'vertical', command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='nsew')

        # events
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
        self.bind('<Configure>', self.update_size)

    def update_size(self, event):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
            self.scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')
        else:
            height = self.winfo_height()
            self.canvas.unbind_all('<MouseWheel>')
            self.scrollbar.place_forget()

        self.canvas.create_window(
            (0,0), 
            window = self.frame, 
            anchor = 'nw', 
            width = self.winfo_width(), 
            height = height)

    def create_item(self, item):
        frame = ttk.Frame(self.frame)

        # grid layout
        frame.rowconfigure(0, weight = 1)
        frame.columnconfigure((0,1,2,3,4), weight = 1, uniform = 'a')

        # widgets 
        ttk.Label(frame, text = '5').grid(row = 0, column = 0)
        ttk.Label(frame, text = f'{item[0]}').grid(row = 0, column = 1)
        ttk.Button(frame, text = f'{item[1]}').grid(row = 0, column = 2, columnspan = 3, sticky = 'nsew')

        return frame

# # setup
# window = tk.Tk()
# window.geometry('500x400')
# window.title('Scrolling')

# text_list = [('label', 'button'),('thing', 'click'),('third', 'something'),('label1', 'button'),('label2', 'button'),('label3', 'button'),('label4', 'button')]
# list_frame = ScrollFrame(window, text_list, 100).pack(expand = True, fill = 'both')

# # run 
# window.mainloop()