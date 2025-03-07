from tkinter import * 
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():    
    letters = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
    numbers = [1,2,3,4,5,6,7,8,9,0]
    symbols = ['!','@','#','$','%','^','&','*','(',')']

    nr_letters = random.randint(8,10)
    nr_numbers = random.randint(2,4)
    nr_symbols = random.randint(2,4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]

    numbers_list = [str(random.choice(numbers)) for _ in range(nr_numbers)]

    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
    
def add_pass():
    website = website_entry.get()
    email = uname_entry.get()
    password = password_entry.get()
    new_data = {
         website:{
              'email':email,
              'password':password
         }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Empty', message="Please don't leave any fields empty.")
    else:
        with open (file='data.json', mode='w') as file:
                json.dump(new_data, file)
                website_entry.delete(first=0, last=END)
                password_entry.delete(first=0, last=END)

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
website_entry.focus()
uname_entry = Entry(width=38)
uname_entry.grid(column=1, row=2, columnspan=2)
uname_entry.insert(0, 'sample@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Buttons
generate_button = Button(text="Generate Password", command=gen_pass)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=add_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()