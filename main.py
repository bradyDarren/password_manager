from tkinter import * 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk() 
window.title("Password Manager")
window.config(padx=20)

canvas = Canvas(width=200, height=200, highlightthickness= 0)
lock_img = PhotoImage(file= 'logo.png')
canvas.create_image(100,100,image = lock_img) 
canvas.grid(column=0, row=0)

window.mainloop()