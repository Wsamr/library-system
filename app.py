import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import constants as c
import widgets as w
import home_frame as home
import books
import users
import report
import loans

class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)

        # app window size attributes
        display_width = self.winfo_screenwidth()
        display_height = self.winfo_screenheight()
        left = int(display_width / 2 - size[0] / 2)
        top = int(display_height / 2 - size[1] / 2)

        # app window size
        self.geometry(f'{size[0]}x{size[1]}+{left}+{top}')
        self.minsize(size[0],size[1])
        # self.resizable(False,False)

        # window configure
        self.configure(fg_color=c.backgroundColor)
        self.iconbitmap(c.icon)

        # window attributes
        # self.attributes('-alpha', 0.9) # window opacity

        # grid configure
        self.columnconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure(1, weight = 9, uniform = 'a')
        self.rowconfigure(0, weight = 1, uniform = 'a')

        # frames
        frames = [
            home.Home(self),
            books.BookCU(self),
            loans.Loan(self),
            users.Users(self),
            report.Report(self),
        ]
        frames[0].lift()
        
        # navigation bar
        navigation = Navigation(self, 
            fg_color=c.primaryColor,
            frames=frames).grid(column = 0, row = 0, sticky ='nsew')

        # app frames
        for frame in frames:
            frame.grid(column = 1, row = 0, sticky='nsew')

        # quit app
        self.bind('<Escape>', lambda event: self.quit()) 
        
        # run
        self.mainloop()

# app logo
class AppLogo(tk.Label):
    def __init__(self, parent, image_path):
        super().__init__(parent, bg=c.primaryColor)
        self.image = tk.PhotoImage(file=image_path).subsample(10,10)
        self.config(image=self.image)

class Navigation(ctk.CTkFrame):
    def __init__(self, parent, fg_color, frames):
        super().__init__(parent, fg_color = fg_color, corner_radius = 0)

        # frame grid configuration
        self.columnconfigure(0, weight = 1, uniform = 'b')
        self.rowconfigure((0,2), weight = 1, uniform = 'b')
        self.rowconfigure(1, weight = 4, uniform = 'b')

        # content
        # row 0
        app_icon = AppLogo(self, image_path=c.book_and_clouds).grid(row=0, sticky = 'new')

        # row 1
        NavigationButtons(self, frames=frames).grid(row = 1, padx= 5)

        # row 2
        # w.sign_out_button(self).grid(row = 2, sticky='sn', padx = 15, pady = 20)

# navigation items
# navigation buttons
class NavigationButtons(ctk.CTkFrame):
    def __init__(self, parent, frames):
        super().__init__(parent, fg_color = 'transparent')
        
        # HOME
        home =   w.nav_button(self, 
            text = 'HOME',
            command = lambda : frames[0].lift(),
            img_path= c.cupcake).pack()
        
        # BOOKS
        books =  w.nav_button(self, 
            text = 'BOOKS',
            command = lambda : frames[1].lift(),
            img_path= c.book).pack()
        
        # LOANS
        loans =  w.nav_button(self, 
            text = 'LOANS',
            command = lambda : frames[2].lift(),
            img_path= c.donate).pack()

        # USERS
        users =  w.nav_button(self, 
            text = 'USERS',
            command = lambda : frames[3].lift(),
            img_path= c.heart).pack()
        
        # REPORTS
        report = w.nav_button(self, 
            text = 'REPORT',
            command = lambda : frames[4].lift(),
            img_path= c.lightbulb).pack()

# # app begin
# if __name__ == '__main__':
#     # worth checking way of moving
#     # auth.isSigned = False 
#     # auth.Auth(title='Library',size=(800,600))
#     # if (auth.isSigned):
# App(title='The Heart of the City', size=(800, 600))