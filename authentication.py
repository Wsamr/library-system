import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk
import customtkinter as ctk
import constants as c
import widgets as w
import app
import database as db


def go_home(self):
    self.destroy()
    app.App('The Heart of the City', (800,600))

def login(self, email, password):
    if email== '' or password=='':
        message = messagebox.showwarning(message='Please fill all fields', title='Empty Fields')
        return
    if not db.admin_exist(email):
        message = messagebox.showwarning(message='Admin doesn\'t exist, please Sign Up', title='Admin doesn\'t exist')
        return
    admin_data = db.get_admin(email)
    if admin_data[0][2] != password:
        message = messagebox.showwarning(message='Your password is incorrect', title='Incorrect Password')
        return
    go_home(self)

def sign_up(self, name, email, password, confirm_password):
    if email== '' or name=='' or password=='' or confirm_password=='':
        message = messagebox.showwarning(message='Please fill all fields', title='Empty Fields')
        return
    if db.admin_exist(email):
        message = messagebox.showwarning(message='Admin already exists, please Login', title='Admin exists')
        return
    if password != confirm_password:
        message = messagebox.showwarning(message='You didn\'t confirm password', title='Password Confirmation')
        return
    db.add_admin(name, email, password)
    go_home(self)

class Auth(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)

        # window geometry
        window_width = size[0]
        window_height = size[1]

        # to position screen in the center
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.configure(fg_color = c.backgroundColor)
        self.iconbitmap(c.icon)

        # grid configuration : self
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')

        # frames
        frame_sign_up = SignUp(self, login=lambda: frame_login.lift())
        frame_login = Login(self, register=lambda: frame_sign_up.lift())

        # login
        frame_login.grid(row = 0, column = 0, sticky = 'nsew')

        # sign up
        frame_sign_up.grid(row = 0, column = 0, sticky = 'nsew')

        # run
        self.mainloop()


class Login(ctk.CTkFrame):
    def __init__(self, parent, register):
        super().__init__(parent, fg_color = c.backgroundColor)

        # grid configuration : self
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure((0,1), weight = 1, uniform = 'a')

        # frame : form
        self.frame_form = ctk.CTkFrame(self, fg_color = c.backgroundColor)
        self.frame_form.grid(column = 0, row = 0, sticky = 'nsew', pady= c.padding, padx= c.padding)
        
        # grid configuration : form frame
        self.frame_form.rowconfigure(0, weight = 2, uniform = 'a')
        self.frame_form.rowconfigure((1,2,3,4,5,6,7), weight = 1, uniform = 'a')
        self.frame_form.columnconfigure(0, weight = 1, uniform = 'a')
        self.frame_form.columnconfigure(1, weight = 2, uniform = 'a')

        # content : image frame
        photo = ctk.CTkImage(light_image=Image.open(c.books_and_trees), size = (700, 1070))
        frame_image = ctk.CTkLabel(self, image=photo, fg_color = c.backgroundColor, text= '')
        frame_image.grid(row = 0, column = 1, sticky = 'nsew')

        # content : form frame
        # row 1 : title
        title = ctk.CTkLabel(self.frame_form, text="The Heart of the City", fg_color=c.backgroundColor, font=(c.family, 44, "bold"), corner_radius = c.radius)
        title.grid(row = 0, column = 0, columnspan = 2, sticky ='nsew', pady = c.padding)

        # row 2 : welcome message
        welcome = ctk.CTkLabel(self.frame_form, text="Welcome!", fg_color=c.backgroundColor, font=(c.family, 30, "bold"))
        welcome.grid(row = 1, column = 0, columnspan = 2, sticky ='new')

        # row 3 : username
        username = ctk.CTkLabel(self.frame_form, text="E-Mail:    ", fg_color=c.backgroundColor, font=(c.family, 20, "bold"))
        username.grid(row = 2, column = 0, sticky = 'e')
        # field
        username_entry = w.my_entry(self.frame_form, font=(c.family, 13), hint = 'Enter your Username')
        username_entry.grid(row = 2, column = 1, sticky = 'ew')

        # row 4 : password
        password = ctk.CTkLabel(self.frame_form, text="Password:    ", fg_color=c.backgroundColor, font=(c.family, 20, "bold"), height = c.widget_height)
        password.grid(row = 3, column = 0, sticky = 'ne')
        # field
        password_entry = w.my_entry(self.frame_form, font=(c.family, 13), hint = 'Enter your Password', isHidden=True)
        password_entry.grid(row = 3, column = 1, sticky = 'new')

        # row 5 : login button
        login_button = w.my_button(self.frame_form, 
                        text= 'Log in', 
                        command= lambda: login(parent, email= username_entry.get(), password=password_entry.get()),
                        font= ctk.CTkFont(family = c.family, size = 18, weight = 'bold'),
                        )
        login_button.grid(row = 4, column = 0, columnspan = 2, sticky = 'n')
        
        # row 6 : sign up button
        sign_up = ctk.CTkLabel(self.frame_form, text="If you don't have an account, Sign Up Now", fg_color=c.backgroundColor, font=(c.family, 20, "bold"))
        sign_up.grid(row = 5, column = 0, columnspan = 2, sticky = 'new')
        sign_up.bind('<Button-1>', lambda event: register())


class SignUp(ctk.CTkFrame):
    def __init__(self, parent, login):
        super().__init__(parent, fg_color = c.backgroundColor)
        # frame : form
        self.frame_form = ctk.CTkFrame(self, fg_color = c.backgroundColor)
        self.frame_form.grid(column = 0, row = 0, sticky = 'nsew', pady= c.padding, padx= c.padding)

        # grid configuration : self
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure((0,1), weight = 1, uniform = 'a')

        # grid configuration : form frame
        self.frame_form.rowconfigure(0, weight = 2, uniform = 'a')
        self.frame_form.rowconfigure((1,2,3,4,5,6,7), weight = 1, uniform = 'a')
        self.frame_form.columnconfigure(0, weight = 1, uniform = 'a')
        self.frame_form.columnconfigure(1, weight = 2, uniform = 'a')

        # content : image frame
        photo = ctk.CTkImage(light_image=Image.open(c.books_and_trees), size = (700, 1070))
        frame_image = ctk.CTkLabel(self, image=photo, fg_color = c.backgroundColor, text= '')
        frame_image.grid(row = 0, column = 1, sticky = 'nsew')

        # content : form frame
        # row 1 : title
        title = ctk.CTkLabel(self.frame_form, text="The Heart of the City", fg_color=c.backgroundColor, font=(c.family, 44, "bold"), corner_radius = c.radius)
        title.grid(row = 0, column = 0, columnspan = 2, sticky ='nsew', pady = c.padding)

        # row 2 : welcome message
        welcome = ctk.CTkLabel(self.frame_form, text="Welcome!", fg_color=c.backgroundColor, font=(c.family, 30, "bold"))
        welcome.grid(row = 1, column = 0, columnspan = 2, sticky ='new')
        
        # row 3 : name
        name = ctk.CTkLabel(self.frame_form, text="Full Name:    ", fg_color=c.backgroundColor, font=(c.family, 20, "bold"), height = c.widget_height)
        name.grid(row = 2, column = 0, sticky = 'se', pady = 5)
        # field
        name_entry = w.my_entry(self.frame_form, font=(c.family, 13), hint = 'Enter your full name')
        name_entry.grid(row = 2, column = 1, sticky = 'sew', pady = 5)

        # row 4 : email
        e_mail = ctk.CTkLabel(self.frame_form, text="E-Mail:    ", fg_color=c.backgroundColor, font=(c.family, 20, "bold"))
        e_mail.grid(row = 3, column = 0, sticky = 'e')
        # field
        e_mail_entry = w.my_entry(self.frame_form, font=(c.family, 13), hint = 'Enter your E_mail')
        e_mail_entry.grid(row = 3, column = 1, sticky = 'ew')

        # row 5 : password
        password = ctk.CTkLabel(self.frame_form, text="Password:    ", fg_color=c.backgroundColor, font=(c.family, 20, "bold"), height = c.widget_height)
        password.grid(row = 4, column = 0, sticky = 'ne', pady = 5)
        # field
        password_entry = w.my_entry(self.frame_form, font=(c.family, 13), hint = 'Enter your Password', isHidden=True)
        password_entry.grid(row = 4, column = 1, sticky = 'new', pady = 5)
        
        # row 6 : confirm password

        confirm_password = ctk.CTkLabel(self.frame_form, text="Confirm:    ", fg_color=c.backgroundColor, font=(c.family, 20, "bold"), height = c.widget_height)
        confirm_password.grid(row = 5, column = 0, sticky = 'ne')
        # field
        confirm_password_entry = w.my_entry(self.frame_form, font=(c.family, 13), hint = 'Confirm your Password', isHidden=True)
        confirm_password_entry.grid(row = 5, column = 1, sticky = 'new')

        # row 7 : login button
        login_button = w.my_button(self.frame_form, 
                        text= 'Sign Up', 
                        command= lambda: sign_up(parent, name= name_entry.get(), email= e_mail_entry.get(), password=password_entry.get(), confirm_password=confirm_password_entry.get()),
                        font= ctk.CTkFont(family = c.family, size = 18, weight = 'bold'),
                        )
        login_button.grid(row = 6, column = 0, columnspan = 2, sticky = 'n')
        
        # row 8 : sign up button
        sign_up_label = ctk.CTkLabel(self.frame_form, text="If you have an account, Login Now", fg_color=c.backgroundColor, font=(c.family, 20, "bold"))
        sign_up_label.grid(row = 7, column = 0, columnspan = 2, sticky = 'new')
        sign_up_label.bind('<Button-1>', lambda event: login())

Auth(title='Library', size= (800, 600))