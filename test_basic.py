import tkinter as tk
from tkinter import *
from tkinter import ttk
import colors as c
import customtkinter as ctk
import widgets as w
from PIL import Image, ImageTk

# window
window = ctk.CTk()
window.geometry('480x240')
window.title('Basics Test')
# window['background'] = c.backgroundColor

# style = ttk.Style()
# style.theme_use('alt')
# style.configure('TButton', 
#     background = c.buttonColor, 
#     foreground ='white', 
#     width = 20, borderwidth=1, 
#     focusthickness=3, 
#     focuscolor='none')
# style.map('TButton', background=[('active',c.buttonColor)])

# button
button = ttk.Button(window, text='A button')
button.pack()

# button image
image_button = ctk.CTkImage(light_image = Image.open( 'images\\purple_book.png').resize((600,600)),
                                # dark_image = Image.open( 'images\\book_stack.png')
                                )

# ctk button
ctk_button = ctk.CTkButton(window, 
    text = "Set Dark Theme", 
    corner_radius = 15, 
    command = lambda: ctk.set_appearance_mode('dark'))
ctk_button.pack()
ctk_button = ctk.CTkButton(window, 
    text = "",
    image= image_button,
    corner_radius = 15, 
    command = lambda: ctk.set_appearance_mode('light'))
ctk_button.pack()

ctk.CTkLabel(window, image = image_button, text='').pack()

w.red_button(window, text='Hello World').pack()

# label
labelVariable = tk.StringVar(value='Old Label Text')
label = ttk.Label(window, text='A ttk Label', textvariable=labelVariable)
label.pack()

# entry
entry = ttk.Entry(window)
entry.pack()

# text
text = tk.Text(window)
text.pack()

# close by escape
window.bind('<Escape>', lambda event: window.quit())

# run
window.mainloop()