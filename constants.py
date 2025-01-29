# import tkinter as tk
# from tkinter import ttk, font

# window = tk.Tk()
# window.title('Styling')
# window.geometry('400x300')

# for i in font.families():
#     print(i)
# print(font.families())

# window.mainloop()

# colors
primaryColor = '#EEE5DA'
backgroundColor = '#FBF8F5'
buttonColor = '#F26B6D'
buttonHoverColor = '#FF6B6D'
navButtonColor = '#FAF2E9'
fontColor = '#6C5148'
randomColors = ['#415F7A', '#74699C', '#74699C', '#598D5B', '#598D5B']

# constants
padding = 25
radius = 20
widget_height = 40

# images
book_and_clouds = 'images\\book_alone.png'
book_stack = 'images\\book_stack.png'
purple_book = 'images\\purple_book.png'
sign_out = 'images\\sign_out.png'
books = 'images\\books1.png'
books_and_trees = 'images\\books_trees.png'
book_cover = 'images\\book_cover.png'
girl_reading = 'images\\girl_reading.png'

cat1 = 'images\\cat1.png'
cat2 = 'images\\cat2.png'
shelf1 = 'images\\shelf1.png'
shelf2 = 'images\\shelf2.png'
shelf3 = 'images\\shelf3.png'
shelfs = 'images\\shelfs.png'

# button icons
book = 'images\\button\\book.png'
candle = 'images\\button\\book.png'
cupcake = 'images\\button\\cupcake.png'
donate = 'images\\button\\donate.png'
flower = 'images\\button\\flower.png'
heart_pop = 'images\\button\\heart_pop.png'
heart = 'images\\button\\heart.png'
lightbulb = 'images\\button\\lightbulb.png'
notification = 'images\\button\\notification.png'
strawberry = 'images\\button\\strawberry.png'

# icon image
icon = 'images\\book_stack.ico'

# font
family = 'Gabriola'

class report:
    def __init__(self):
        self.issued_book = 'Issued Book'
        self.overdue_book = 'Overdue Book'
        self.returned_book = 'Returned Book'
        self.added_user = 'Added User'
        self.deleted_user = 'Deleted User'
        self.updated_user = 'Updated User'
        self.added_book = 'Added Book'
        self.deleted_book = 'Deleted Book'
        self.updated_book = 'Updated Book'