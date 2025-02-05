from tkinter import *

window = Tk()
window.title("Miles to KMs Converter")
window.minsize(width=200, height=100)
window.config(padx=40, pady=20)

miles_label = Label(text="Miles", font=("Arial",10, "italic"))
miles_label.grid(row = 0, column = 2)

km_label = Label(text="KMs", font=("Arial",10, "italic"))
km_label.grid(row = 1, column = 2)

km_value = Label(text="0",font=("Arial",10, "italic"))
km_value.grid(row = 1, column = 1)

equals = Label(text="is equal to",font=("Arial",10, "italic"))
equals.grid(row = 1, column = 0)

entry = Entry(width=10)
entry.grid(column = 1, row = 0)

def calculate():
    mile_input = int(entry.get())
    km_output = round(mile_input*1.60934,2)
    km_value.config(text=km_output)

button = Button(text = "Calculate", command=calculate)
button.grid(row = 2, column = 1)

window.mainloop()