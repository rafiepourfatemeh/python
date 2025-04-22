import time
from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
dispose = False
card_in_hand = ""

data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")


def show_front(card_in_hand):
    card.itemconfig(card_image, image=card_front)
    card.itemconfig(card_label, text="French", fill="black")
    card.itemconfig(card_text, text=card_in_hand["French"], fill="black")


def show_back(card_in_hand):
    card.itemconfig(card_image, image=card_back)
    card.itemconfig(card_label, text="English", fill="white")
    card.itemconfig(card_text, text=card_in_hand["English"], fill="white")


def take_card():
    global card_in_hand
    card_in_hand = random.choice(data_dict)
    show_front(card_in_hand)
    window.update()
    window.after(3000, show_back(card_in_hand))


def dispose_of_card():
    try:
        data_dict.remove(card_in_hand)
        data = pandas.DataFrame(data_dict)
        data.to_csv("data/words_to_learn.csv", index=False)
    except ValueError:
        pass
    finally:
        take_card()

# TODO: Create Window


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# TODO: Create Widgets:

# Cards:
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = card.create_image(400, 266, image=card_front)
card_label = card.create_text(400, 133, text="Press Any Button To Begin", font=("Arial", 28, "italic"))
card_text = card.create_text(400, 266, text="", font=("Arial", 28, "italic"))
card.grid(column=0, row=0, columnspan=2)

# Buttons:
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=dispose_of_card)
right_button.grid(column=1, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=take_card)
wrong_button.grid(column=0, row=1)

window.mainloop()

