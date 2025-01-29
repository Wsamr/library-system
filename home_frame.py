import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import constants as c
import widgets as w
import database as db


class Home(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = c.backgroundColor)

        # variables
        search_var = tk.StringVar()

        # font
        font_main = ctk.CTkFont(family=c.family, size = 18, weight = 'bold')
        
        # frame : search area
        self.search_area = ctk.CTkFrame(self, fg_color = c.backgroundColor)
        self.search_area.grid(row = 0 , column = 0, sticky = 'nsew')

        # frame : summary area
        self.summary = w.frame_colored(self)
        self.summary.grid(row = 2, sticky = 'nsew', padx = c.padding, pady = c.padding)
        
        # grid configuration : whole frame
        self.rowconfigure((0,1), weight = 1, uniform = 'c')
        self.rowconfigure(2, weight = 2, uniform = 'c')
        self.columnconfigure(0, weight = 1, uniform = 'c')

        # grid configuration : search area
        self.search_area.columnconfigure(0 , weight = 8, uniform = 'd')
        self.search_area.columnconfigure(1 , weight = 2, uniform = 'd')
        self.search_area.rowconfigure((0, 1), weight = 1)

        # grid configuration : summary area
        self.summary.columnconfigure((0, 1, 2), weight = 1, uniform = 'summary')
        self.summary.rowconfigure((0, 1), weight = 1, uniform = 'summary')

        # row 1 : filter

        # row 1.1 : search

        # :: search bar 
        self.search_bar = w.my_entry_var(self.search_area, hint = 'Search for books', font = font_main, variable=search_var)
        self.search_bar.grid(row = 0 , column = 0, sticky = 'new', padx = (c.padding, 5), pady = c.padding)

        def search():
            global new_window 
            new_window = tk.Toplevel()
            # app window size attributes
            display_width = new_window.winfo_screenwidth()
            display_height = new_window.winfo_screenheight()
            left = int(display_width / 2 - 800 / 2)
            top = int(display_height / 2 - 500 / 2)

            # app window size
            new_window.geometry(f'{800}x{500}+{left}+{top}')
            new_window.minsize(800,500)
            tree = ttk.Treeview(new_window, columns = ("ISBN", "Title", "Author", "Genre"), show = 'headings')
            tree.heading("ISBN", text = "ISBN")
            tree.heading("Title", text = "Title")
            tree.heading("Author", text = "Author")
            tree.heading("Genre", text = "Genre")
            tree.pack(expand =True , fill = 'both')
            books = db.show_book(search_var.get())
            for book in books:
                tree.insert('', 'end', values= book[0:4])

        # :: search button
        self.search_button = w.my_button(self.search_area, text = 'search', font = font_main, command= search)
        self.search_button.grid(row = 0, column = 1, sticky = 'new', padx = (5, c.padding), pady = c.padding)

        # row 1.2 : categories
        

        # row 2: popular
        shelf = ctk.CTkLabel(self, text='', image = ctk.CTkImage(light_image = Image.open(c.shelf1), size = (556, 196)))
        shelf.grid(row = 1, column = 0)

        # row 3: summary
        # items
        books = db.show_book('')
        books_length = len(books)
        loans = db.show_loan('')
        loans_length = len(loans)
        summary_image = ctk.CTkLabel(self.summary, text='', image = ctk.CTkImage(light_image = Image.open(c.cat1), size = (300, 300)), fg_color = 'transparent', corner_radius = c.radius)
        summary_image.grid(row = 0, rowspan = 2, column = 0, columnspan = 2, padx = (c.padding,0))
        self.summary_item_books = SummaryItem(self.summary, text = 'books:', number = books_length)
        self.summary_item_loans = SummaryItem(self.summary, text = 'loans:', number = loans_length)
        # self.summary_item_due_loans = SummaryItem(self.summary, text = 'due loans', number = 4)

        # grid
        self.summary_item_books.grid(column = 2, row = 0, sticky = 'nsew', padx = 10, pady = 10)
        self.summary_item_loans.grid(column = 2, row = 1, sticky = 'nsew', padx = 10, pady = 10)
        # self.summary_item_due_loans.grid(column = 2, row = 0, sticky = 'nsew', padx = c.padding, pady = c.padding)

class SummaryItem(ctk.CTkFrame):
    def __init__(self, parent, text, number):
        super().__init__(parent, fg_color = c.backgroundColor, corner_radius = c.radius)
        
        # attributes
        self.number = ctk.CTkLabel(self, text = f'{number}', font = ctk.CTkFont('Gabriola', size = 30, weight = 'bold'))
        self.text = ctk.CTkLabel(self, text = text, font = ctk.CTkFont('Gabriola', size = 30))
        
        # grid configuration
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure((0,1), weight = 1, uniform = 'a')

        # widgets
        self.number.grid(row = 0, column = 1, sticky = 'ns')
        self.text.grid(row = 0, column = 0, sticky = 'nse')