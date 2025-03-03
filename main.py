from tkinter import * 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk() 
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness= 0)
lock_img = PhotoImage(file= 'logo.png')
canvas.create_image(100,100,image = lock_img) 
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
uname = Label(text="Email/Username:")
uname.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

#Entries
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
uname_entry = Entry(width=38)
uname_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Buttons
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()