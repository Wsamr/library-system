import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk
import customtkinter as ctk
import widgets as w
import constants as c
import database as db
import datetime


class LoanTable(ctk.CTkFrame):
    def __init__(self, parent, isbn_var, ssn_var, issue_var, due_var, id_var):
        super().__init__(parent, fg_color = c.backgroundColor)

        loaned_books_label = tk.Label(self, text="List of Loaned Books", font=(c.family, 16, 'bold'), bg=c.backgroundColor)
        loaned_books_label.pack(anchor="w")

        loaned_books_list = ttk.Treeview(self, columns=("Title", "User Name", "Issue Date", "Due Date"), show="headings")

        loaned_books_list.heading("Title", text="Book ISBN",)
        loaned_books_list.heading("User Name", text="User SSN")
        loaned_books_list.heading("Issue Date", text="Issue Date")
        loaned_books_list.heading("Due Date", text="Due Date")

        loaned_books_list.column('Title', width = 190)
        loaned_books_list.column('User Name', width = 190)
        loaned_books_list.column('Issue Date', width = 190)
        loaned_books_list.column('Due Date', width = 190)

        loaned_books_list.pack(fill=tk.X)

        def on_tree_click(event):
            selected_item = loaned_books_list.selection()[0]  # Get the first selected item
            item_values = loaned_books_list.item(selected_item)["values"]

            # set variables
            isbn_var.set(item_values[0])
            ssn_var.set(item_values[1])
            issue_var.set(item_values[2])
            due_var.set(item_values[3])


        # bind loaned_books_list event
        loaned_books_list.bind("<ButtonRelease-1>", on_tree_click)

        loans = db.show_loan('')
        for loan in loans:
            loaned_books_list.insert('', 'end', values= loan[0:4])

        def insert():
            if isbn_var.get()!='' and ssn_var.get()!='' and issue_var.get()!='' and due_var.get()!='':
                if not db.book_available(isbn_var.get()):
                    messagebox.showwarning("Book Unavailable", "The book you are trying to issue is unavailable")
                    return
                db.add_loan(book_id=isbn_var.get(),user_id=ssn_var.get(), due_date=due_var.get(),issue_date=issue_var.get())
                db.add_report(report_type=c.report().issued_book,
                            generated_on=datetime.datetime.now(),
                            report_data=f'On {datetime.datetime.now()} A Book with ISBN: {isbn_var.get()}, was issued to User of SSN: {ssn_var.get()}')
                loaned_books_list.insert('', 'end', values= (isbn_var.get(), ssn_var.get(),issue_var.get(), due_var.get()))
            else:
                message = messagebox.showwarning(message='Please fill all fields', title='Warning')
                return

        def return_book():
            selected_item = loaned_books_list.selection()[0]
            if ((db.book_available)) and selected_item:
                loaned_books_list.delete(selected_item)
                db.delete_loan(book_id=isbn_var.get())
                db.add_report(report_type=c.report().returned_book,
                            generated_on=datetime.datetime.now(),
                            report_data=f'On {datetime.datetime.now()} A Book with ISBN: {isbn_var.get()}, was Returned')
            else: messagebox.showwarning("Selection Error", "Please select an item")
        
        self.insert = insert
        self.return_book = return_book


def field(parent, text, hint, variable):
    frame = ctk.CTkFrame(parent, fg_color = c.backgroundColor)
    
    # frame grid configuration
    frame.columnconfigure(0, weight = 1, uniform = 'a')
    frame.columnconfigure(1, weight = 2, uniform = 'a')
    frame.rowconfigure(0, weight = 1, uniform = 'a')

    # label
    label = tk.Label(frame, text=text, background=c.backgroundColor, font=(c.family, 22, 'bold'), foreground=c.fontColor)
    label.grid(row=0, column=0, sticky='e')

    # entry
    entry = w.my_entry_var(frame, hint, (c.family, 20), variable)
    entry.grid(row = 0, column = 1, sticky = 'we', padx = (10, 0))

    # return
    return frame

class Loan(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = c.backgroundColor)

        # variables
        id_var = tk.StringVar(value = '')
        isbn_var = tk.StringVar(value = '')
        ssn_var = tk.StringVar(value = '')
        issue_var = tk.StringVar(value = '')
        due_var = tk.StringVar(value = '')
        
        # grid configuration
        self.rowconfigure((0), weight = 1, uniform = 'a')
        self.rowconfigure(1, weight = 5, uniform = 'a')
        self.rowconfigure(2, weight = 4, uniform = 'a')
        self.columnconfigure((0,1), weight = 1, uniform = 'a')

        # search area
        frame_label = ctk.CTkLabel(self, text = 'Loaned Books', fg_color = c.backgroundColor, font = (c.family, 37, 'bold'), text_color = c.fontColor)
        frame_label.grid(row = 0, column = 0,columnspan = 2, padx= c.padding)

        # loans table
        table = LoanTable(self, isbn_var, ssn_var, issue_var, due_var, id_var)
        table.grid(row = 2, column = 0, columnspan = 2,padx= 10)

        # issue book frame
        issue_book_frame = ctk.CTkFrame(self, fg_color = c.backgroundColor)
        issue_book_frame.grid(row = 1, column= 0, sticky='nsew')


        # grid configuration
        issue_book_frame.rowconfigure((0,1,2,3), weight = 1, uniform = 'a')
        issue_book_frame.rowconfigure(4, weight = 2, uniform = 'a')
        issue_book_frame.columnconfigure((0,1), weight = 1, uniform = 'a')
        
        # frame items
        book_title = field(issue_book_frame, 'Book ISBN', 'Enter Book ISBN', isbn_var)
        book_title.grid(row = 0, column = 0, columnspan = 2, sticky= 'we')

        user_name = field(issue_book_frame, 'User SSN', 'Enter User SSN', ssn_var)
        user_name.grid(row = 1, column = 0, columnspan = 2, sticky= 'we')

        issue_date = field(issue_book_frame, 'Issue Date', 'Enter Issue Date', issue_var)
        issue_date.grid(row = 2, column = 0, columnspan = 2, sticky= 'we')

        due_date = field(issue_book_frame, 'Due Date', 'Enter Due Date', due_var)
        due_date.grid(row = 3, column = 0, columnspan = 2, sticky= 'we')

        # buttons
        cancel_button = w.my_button(issue_book_frame, 'Return', (c.family, 20, 'bold'), command= table.return_book)
        cancel_button.grid(row = 4, column = 0, sticky = 'e')

        issue_button = w.my_button(issue_book_frame, 'Issue Book', (c.family, 20, 'bold'), command= table.insert)
        issue_button.grid(row = 4, column = 1, sticky = 'e')

        # image
        image_label = ctk.CTkLabel(self, text= '', image = ctk.CTkImage(light_image = Image.open(c.girl_reading), size =(320,352)))
        image_label.grid(row=1, column = 1, sticky = 'nsew')
