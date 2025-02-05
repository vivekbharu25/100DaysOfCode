from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_box.insert(0,password)
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password Copied")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = web_box.get()
    email = eu_box.get()
    password = pass_box.get()

    new_data = {
        website: {
            "email":email,
            "password":password
        }
    }

    if len(website)==0 or len(password) == 0:
        messagebox.showwarning(title="OOPs", message="The fields shouldn't be empty")
    else:
        try:
            with open ("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file, indent = 4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data,data_file, indent = 4)
        finally:
            web_box.delete(0,END)
            pass_box.delete(0, END)

#--------------------------Search Details-------------------------#
def search_details():
    website = web_box.get()
    try:
        with open ("data.json", "r") as pm:
            data = json.load(pm)
    except FileNotFoundError:
        messagebox.showinfo(title="Add Data", message="Add some data")
    try:
        messagebox.showinfo(title=website, message=f"Email:{data[website]["email"]}\nPassword:{data[website]["password"]}")
    except KeyError:
        messagebox.showinfo(title="No Data",message="There is no data")
    except UnboundLocalError:
        pass
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(pady=30, padx=50)

canvas = Canvas(width=200,height=200)
lock_img =PhotoImage(file="logo.png")
canvas.create_image(100,100,image = lock_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row = 1, column = 0)

web_box = Entry(width=30)
web_box.grid(row=1,column = 1)
web_box.focus()

eu_label = Label(text="Email/Username:")
eu_label.grid(row = 2, column = 0)

eu_box = Entry(width=50)
eu_box.grid(row=2,column = 1, columnspan = 2)
eu_box.insert(0,'vivek@gmail.com')

pass_label =  Label(text="Password:")
pass_label.grid(row = 3, column = 0)

pass_box = Entry(width=30)
pass_box.grid(row=3,column = 1)

gen_pass_button = Button(text="Generate Password", command=pass_gen)
gen_pass_button.grid(row=3, column = 2)

add_button = Button(text="Add", width=45, command=save_pass)
add_button.grid(row=4, column = 1, columnspan=2)

search_button = Button(text="Search", command=search_details)
search_button.grid(row = 1, column = 2)

window.mainloop()