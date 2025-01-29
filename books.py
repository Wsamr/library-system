import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
import customtkinter as ctk
import constants as c
import widgets as w
import database as db

padding = 100
genres = (
    "Fiction",
    "Fantasy",
    "Romance",
    "Thriller",
    "Mystery",
    "Horror",
    "Non-fiction",
    "Biography",
    "Poetry",
    "Adventure",
    "Classic",
    "Drama",
    "Dystopian",
    "Utopian",
    "Crime",
    "Paranormal",
    "Steampunk",
    "Cyberpunk",
)
genres = sorted(genres)
def field(parent,text,hint, variable):

    frame=ctk.CTkFrame(parent,fg_color=c.backgroundColor)
    frame.rowconfigure(0,weight=1,uniform="a")
    frame.columnconfigure(0,weight=1,uniform="a")
    frame.columnconfigure(1,weight=3,uniform="a")
    
    label=tk.Label(frame,text=text,bg=c.backgroundColor,font=(c.family,22, 'bold'), foreground=c.fontColor)
    label.grid(row=0,column=0,sticky='ws',padx=c.padding)
    
    entry=w.my_entry_var(frame,hint=hint,font=ctk.CTkFont(c.family), variable=variable)
    entry.grid(row=0,column=1,sticky="wen")
    return frame

def combobox(parent,text, variable):

    frame=ctk.CTkFrame(parent,fg_color=c.backgroundColor)
    frame.rowconfigure(0,weight=1,uniform="a")
    frame.columnconfigure(0,weight=1,uniform="a")
    frame.columnconfigure(1,weight=3,uniform="a")

    label=tk.Label(frame,text=text,bg=c.backgroundColor,font=(c.family,22, 'bold'), foreground=c.fontColor)
    label.grid(row=0,column=0,sticky='ws',padx=c.padding)
    
    combobox=w.my_combobox(frame, genres, variable)
    combobox.grid(row=0,column=1,sticky="wen")
    return frame


def buttons(parent, insert, clear, update, delete):

    frame=ctk.CTkFrame(parent,fg_color=c.backgroundColor)
    frame.columnconfigure((0,1),weight=1,uniform="a")
    frame.rowconfigure(0,weight=1,uniform="a")
    frame.rowconfigure(1,weight=1,uniform="a")
    
    clear_button=w.my_button(frame,"Clear",font=ctk.CTkFont(c.family,size=18, weight = 'bold'),command=clear)
    clear_button.grid(row=0,column=0, sticky = 'e', padx = c.padding, pady = 5)
    
    add_button=w.my_button(frame,"Add",font=ctk.CTkFont(c.family,size=18, weight = 'bold'),command=insert)
    add_button.grid(row=0,column=1, sticky = 'w', padx = c.padding, pady = 5)
    
    delete_button=w.my_button(frame,"Delete",font=ctk.CTkFont(c.family,size=18, weight = 'bold'),command=delete)
    delete_button.grid(row=1,column=0, sticky = 'e', padx = c.padding, pady = 5)
    
    update_button=w.my_button(frame,"Update",font=ctk.CTkFont(c.family,size=18, weight = 'bold'),command=update)
    update_button.grid(row=1,column=1, sticky = 'w', padx = c.padding, pady = 5)
    
    return frame

class BookCU(ctk.CTkFrame):
    # , book_title, book_genre, book_author, is_update = False
    def __init__(self, parent):
        super().__init__(parent, fg_color=c.backgroundColor)

        # variables
        isbn_constant = ''
        title_var = tk.StringVar(value = '')
        isbn_var = tk.StringVar(value = '')
        author_var = tk.StringVar(value = '')
        genre_var = tk.StringVar(value = '')

        # grid configuration : main frame (self)
        self.rowconfigure((0,1,2,3,4),weight=1,uniform="a")
        self.rowconfigure(5,weight=2,uniform="a")
        self.rowconfigure(6,weight=8,uniform="a")
        self.columnconfigure(0,weight=1,uniform="a")
        self.columnconfigure(1,weight=2,uniform="a")

        # image
        w.book_frame(self, 'The Library', '', genre='').grid(row = 1, rowspan = 5, column = 0, padx= c.padding)

        # title : row 1
        title_frame=field(self,"Title","Enter book title", variable=title_var)
        title_frame.grid(row=1,column=1,sticky="we",padx=(0,padding))

        # author : row 2
        author_frame=field(self,"Author","Enter book author", variable=author_var)
        author_frame.grid(row=2,column=1,sticky="we",padx=(0,padding))

        # ISBN : row 3
        isbn_frame=field(self,"ISBN","Enter book ISBN", variable=isbn_var)
        isbn_frame.grid(row=3,column=1,sticky="we",padx=(0,padding))

        # category : row 4
        category_frame=combobox(self,"Genre",genre_var)
        category_frame.grid(row=4,column=1,sticky="we",padx=(0,padding))

        # table : row 6
        tree = ttk.Treeview(self, columns = ("ISBN", "Title", "Author", "Genre"), show = 'headings')
        tree.heading("ISBN", text = "ISBN")
        tree.heading("Title", text = "Title")
        tree.heading("Author", text = "Author")
        tree.heading("Genre", text = "Genre")
        tree.grid(row = 6, column = 0, columnspan = 2, padx = 10)

        def on_tree_click(event):
            selected_item = tree.selection()[0]  # Get the first selected item
            item_values = tree.item(selected_item)["values"]

            # set variables
            
            isbn_var.set(item_values[0])
            isbn_constant = item_values[0]
            
            title_var.set(item_values[1])
            author_var.set(item_values[2])
            genre_var.set(item_values[3])


        # bind tree event
        tree.bind("<ButtonRelease-1>", on_tree_click)

        books = db.show_book('')
        for book in books:
            tree.insert('', 'end', values= book[0:4])

        def clear():
            title_var.set(value='')
            isbn_var.set(value='')
            author_var.set(value='')
            genre_var.set(value='')
        
        def insert():
            if isbn_var.get()!='' and title_var.get()!='' and author_var.get()!='' and genre_var.get()!='':
                if db.book_exist(isbn_var.get()):
                    messagebox.showwarning(message='Book already exists', title='Book Exists')
                    return
                db.add_book(isbn= isbn_var.get(), title= title_var.get(), author=author_var.get(), genre=genre_var.get())
                db.add_report(report_type=c.report().added_book,
                            generated_on=datetime.datetime.now(),
                            report_data=f'On {datetime.datetime.now()} A Book with ISBN: {isbn_var.get()}, Title: {title_var.get()}, Author: {author_var.get()}, Genre: {genre_var.get()} was Added')
                tree.insert('', 'end', values= (isbn_var.get(), title_var.get(),author_var.get(), genre_var.get()))
                clear()
            else:
                message = messagebox.showwarning(message='Please fill all fields', title='Warning')
                return

        

        def update():
            selected_item = tree.selection()[0]
            item_values = tree.item(selected_item)["values"]
            isbn_constant = item_values[0]
            if selected_item:
                isbn = isbn_var.get()
                title = title_var.get()
                author = author_var.get()
                genre = genre_var.get()
                if title and author and genre and isbn:
                    if isbn_var.get() != isbn_constant:
                        isbn_var.set(value=isbn_constant)
                        messagebox.showwarning(title="ISBN Error", message="You changed ISBN Value, the value was reset")
                        return
                    tree.item(selected_item, values = (isbn, title, author, genre))
                    db.update_book(isbn = isbn, title = title, author= author, genre = genre)
                    db.add_report(report_type=c.report().updated_book, 
                                generated_on=datetime.datetime.now(), 
                                report_data=f'The book of ISBN: {isbn} was updated to Title: {title}, Author: {author}, Genre: {genre}')
                    clear()
                else:
                    messagebox.showwarning("Input Error", "Please fill all fields")
            else:
                messagebox.showwarning("Selection Error", "Please select an item to update")
        
        def delete():
            selected_item = tree.selection()[0]
            if selected_item:
                tree.delete(selected_item)
                db.delete_book(isbn=isbn_var.get())
                db.add_report(report_type=c.report().deleted_book,
                            generated_on=datetime.datetime.now(),
                            report_data=f'On {datetime.datetime.now()} A Book with ISBN: {isbn_var.get()}, Title: {title_var.get()}, Author: {author_var.get()}, Genre: {genre_var.get()} was Deleted')
            else :
                messagebox.showwarning("Selection Error", "Please select an item to delete")

        # buttons : row 5 (cancel and submit)
        buttons_frame=buttons(self, insert=insert, clear = clear, update=update, delete=delete)
        buttons_frame.grid(row=5,column=1,sticky="we")

