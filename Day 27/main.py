from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=600, height=400)

#label
my_label = Label(text="I'm a label", font=("Arial",25, "italic"))
# my_label["text"] = "New Text"
my_label.config(text="new text")
my_label.grid(column = 0, row = 0)

entry = Entry(width=15)
entry.grid(column = 3, row = 2)

def button_clicked():
    new_text = entry.get()
    my_label.config(text=new_text)

def action():
    my_label.config(text="New Button Got Clicked!")

button = Button(text="Click Me!", command=button_clicked)
button.grid(column = 1, row = 1)

new_button = Button(text="hahah!", command=action)
new_button.grid(column = 2, row = 0)



window.mainloop()