window=ctk.CTk()
window.geometry("800x600")

window.rowconfigure(0,weight = 1)
window.columnconfigure(0,weight = 1)

frame = BookCU(window)
frame.grid(sticky = 'nsew')

window.mainloop()