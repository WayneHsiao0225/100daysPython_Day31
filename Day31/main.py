from tkinter import *
import pandas
import random

BACKGROUND_COLOR="#B1DDC6"
current={ }
data_dict={}

## load data
try:
    data=pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    data=pandas.read_csv("data/french_words.csv")
    data_dict=data.to_dict(orient="records")
else:
    data_dict=data.to_dict(orient="records")


## next word
def next():
    global current,flip_timer
    window.after_cancel(flip_timer)
    current=random.choice(data_dict)
    print(current)
    canvas.itemconfig(title,text="French",fill="Black")
    canvas.itemconfig(word,text=current["French"],fill="Black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=window.after(3000, func=flip)


## flip
def flip():
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=current["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)


## remove known
def remove():
    data_dict.remove(current)
    next()
    print(len(data_dict))
    data_output=pandas.DataFrame(data_dict)
    data_output.to_csv("data/word_to_learn.csv",index=False)


## window and canvas
window=Tk()
window.title("Flasky")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000, func=flip)

canvas=Canvas(width=800,height=526)
card_front_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front_img)
title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
word=canvas.create_text(400,260,text="word",font=("Airiel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


##button
wrong_image=PhotoImage(file="images/wrong.png")
button_unknown=Button(image=wrong_image,highlightthickness=0,command=next)
button_unknown.grid(row=1,column=0)

right_image=PhotoImage(file="images/right.png")
button_known=Button(image=right_image,highlightthickness=0,command=remove)
button_known.grid(row=1,column=1)


next()

window.mainloop()