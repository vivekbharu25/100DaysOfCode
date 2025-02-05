from cytoolz import remove

FONT = "Ariel"

from tkinter import *
import pandas as pd
import random

current_card = {}

#------------------------------------#
try:
    words = pd.read_csv("data/words_to_learn.csv", header=0)
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv", header=0)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = words.to_dict(orient="records")


#------------------#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(lang_text, text = "French", fill = "black")
    current_card = random.choice(to_learn)
    canvas.itemconfig(text,text=current_card["French"], fill = "black")
    canvas.itemconfig(card_background,image = card_front)
    flip_timer = window.after(3000,func = flip_card)

def flip_card():
    canvas.itemconfig(card_background, image= card_back)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(text, text = current_card["English"], fill = "white")

def update_csv():
    try:
        to_learn.remove(current_card)
    except ValueError:
        print("You Learnt them all")
        pass
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Fr-En Flash Cards")
window.config(padx= 100, pady=50, bg ="#99EDC3")

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg ="#99EDC3",
                highlightthickness=0 )

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

card_background = canvas.create_image(400,268,image= card_front)

lang_text = canvas.create_text(400, 150, text="Title", fill="black",
                               font=(FONT,40,"italic"))
text = canvas.create_text(400,268, text="word",fill = "black", font=(FONT,60,"bold"))
canvas.grid(row = 0, column = 0, columnspan= 2)

right_button = Button(image=right_img, highlightthickness=0, command=update_csv)
right_button.grid(row=1, column = 1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column = 0)

next_card()

window.mainloop()