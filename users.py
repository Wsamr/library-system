import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import constants as c
import widgets as w
import customtkinter as ctk
import database as db
import datetime

class Users(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=c.backgroundColor)

        # variables
        ssn_var = tk.StringVar(value='')
        name_var = tk.StringVar(value='')
        email_var = tk.StringVar(value='')
        number_var = tk.StringVar(value='')

        # grid configuration : main frame
        self.rowconfigure((0,1,2,3), weight = 1)
        self.rowconfigure(4, weight = 2)
        self.rowconfigure(5, weight = 10)
        self.columnconfigure((0,1,2,3), weight = 1)

        # labels
        name_label = tk.Label(self, text = "Name",font=(c.family, 18, 'bold'), foreground = c.fontColor, background=c.backgroundColor)
        name_label.grid(row = 0, column = 0, padx = 10, pady = 10,sticky='e')
        email_label = tk.Label(self, text = "Email",font=(c.family, 18, 'bold'), foreground = c.fontColor, background=c.backgroundColor)
        email_label.grid(row = 1, column = 0, padx = 10, pady = 10,sticky='e')
        phone_label = tk.Label(self, text = "Phone Number",font=(c.family, 18, 'bold'), foreground = c.fontColor, background=c.backgroundColor)
        phone_label.grid(row = 2, column = 0, padx = 10, pady = 10,sticky='e')
        ssn_label = tk.Label(self, text = "SSN",font=(c.family, 18, 'bold'), foreground = c.fontColor, background=c.backgroundColor)
        ssn_label.grid(row = 3, column = 0, padx = 10, pady = 10,sticky='e')

        # entries
        name_entry = w.my_entry_var(self,font=ctk.CTkFont(c.family,size=16),hint="Enter user name", variable=name_var)
        name_entry.grid(row = 0, column = 1, columnspan= 3, padx = (10,200), pady = 10, sticky='we')
        email_entry = w.my_entry_var(self,font=ctk.CTkFont(c.family,size=16),hint="Enter user email", variable=email_var)
        email_entry.grid(row = 1, column = 1, columnspan= 3, padx = (10,200), pady = 10, sticky='we')
        phone_entry = w.my_entry_var(self,font=ctk.CTkFont(c.family,size=16),hint="Enter user phone number",variable=number_var)
        phone_entry.grid(row = 2, column = 1, columnspan= 3, padx = (10,200), pady = 10, sticky='we')
        ssn_entry = w.my_entry_var(self,font=ctk.CTkFont(c.family,size=16),hint="Enter user SSN",variable=ssn_var)
        ssn_entry.grid(row = 3, column = 1, columnspan= 3, padx = (10,200), pady = 10, sticky='we')

        # table
        tree = ttk.Treeview(self, columns = ("SSN","Name", "Email", "Phone Number"), show = 'headings')
        tree.heading("SSN", text = "SSN")
        tree.heading("Name", text = "Name")
        tree.heading("Email", text = "Email")
        tree.heading("Phone Number", text = "Phone Number")
        tree.grid(row = 5, column = 0, columnspan = 4, padx = 10, pady = 10)

        def on_tree_click(event):
            selected_item = tree.selection()[0]  # Get the first selected item
            item_values = tree.item(selected_item)["values"]

            # set variables
            ssn_var.set(item_values[0])
            name_var.set(item_values[1])
            email_var.set(item_values[2])
            number_var.set(item_values[3])

        # bind tree event
        tree.bind("<ButtonRelease-1>", on_tree_click)

        users = db.show_user('')
        for user in users:
            tree.insert('', 'end', values= user[0:4])

        def insert():
            if email_var.get()!='' and ssn_var.get()!='' and number_var.get()!='' and name_var.get()!='':
                if db.user_exist():
                    messagebox.showwarning(message='User already exists', title='User Exists')
                    return
                db.add_user(email=email_var.get(), ssn=ssn_var.get(),name=name_var.get(), number=number_var.get())
                db.add_report(report_type=c.report().added_user,
                            generated_on=datetime.datetime.now(),
                            report_data=f'On {datetime.datetime.now()} A User with SSN: {ssn_var.get()}, Name: {name_var.get()}, Email: {email_var.get()}, Phone Number: {number_var.get()} was Added')
                tree.insert('', 'end', values= (ssn_var.get(), name_var.get(),email_var.get(), number_var.get()))
            else:
                message = messagebox.showwarning(message='Please fill all fields', title='Empty Fields')
                return

        def clear():
            ssn_var.set(value='')
            name_var.set(value='')
            email_var.set(value='')
            number_var.set(value='')

        def update():
            selected_item = tree.selection()[0]
            if selected_item:
                ssn = ssn_var.get()
                name = name_var.get()
                email = email_var.get()
                number = number_var.get()
                if ssn and email and number and name:
                    tree.item(selected_item, values = (ssn, name, email, number))
                    db.update_user(ssn = ssn, name= name, email=email, number = number)
                    db.add_report(report_type=c.report().updated_user,
                            generated_on=datetime.datetime.now(),
                            report_data=f'On {datetime.datetime.now()} A User with SSN: {ssn_var.get()} was Updated to Name: {name_var.get()}, Email: {email_var.get()}, Phone Number: {number_var.get()}')
                    clear()
                else:
                    messagebox.showwarning("Input Error", "Please fill all fields")
            else:
                messagebox.showwarning("Selection Error", "Please select an item to update")
        
        def delete():
            selected_item = tree.selection()[0]
            if selected_item :
                tree.delete(selected_item)
                db.delete_user(ssn=ssn_var.get())
                db.add_report(report_type=c.report().deleted_user,
                            generated_on=datetime.datetime.now(),
                            report_data=f'On {datetime.datetime.now()} A User with SSN: {ssn_var.get()}, Name: {name_var.get()}, Email: {email_var.get()}, Phone Number: {number_var.get()} was Deleted')
            else :
                messagebox.showwarning("Selection Error", "Please select an item to delete")

        # buttons
        clear_button = w.my_button(self,text="Clear",font=ctk.CTkFont(c.family,size=20, weight = 'bold'),command=clear)
        clear_button.grid(row = 4, column = 0, padx = 10, pady = 20,sticky='e')
        add_button = w.my_button(self,text="Add",font=ctk.CTkFont(c.family,size=20, weight = 'bold'),command=insert)
        add_button.grid(row = 4, column = 1, padx = 10, pady = 20,sticky='e')
        update_button = w.my_button(self,text="Update",font=ctk.CTkFont(c.family,size=20, weight = 'bold'),command=update)
        update_button.grid(row = 4, column = 2, padx = 10, pady = 10)
        delete_button = w.my_button(self,text="Delete",font=ctk.CTkFont(c.family,size=20, weight = 'bold'),command=delete)
        delete_button.grid(row = 4, column = 3, padx = 10, pady = 10,sticky='w')




# test Users class
# root = tk.Tk()
# root.title("CRUD Users")
# root.geometry("800x600")

# Users(root).pack()

# root.mainloop()