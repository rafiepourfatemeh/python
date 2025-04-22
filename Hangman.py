import string
import os
import random
from tkinter import *
import tkinter as tk
from tkinter import messagebox


# Game Logic

class hangman:
    Current_Word = ""
    Hidden_Word = []
    Shown_Word = []
    guess = ''
    Guessed_List = ['Guessed:']
    lives = ['Lives(5):']
    end_state = False
    
    word_list = ["constantinople","constantine","hangman","reptile","undertaker","chemistery","assassin","astronaut","gemini","ginger","comet","superman","battery","graphite","mouse","goose","combat","madagascar","zorro","zebra","arrangement","xanax","example","practice","potential","panama","future","foniture","shock","godzilla","knot","horoscope","inception","prestige","interstellar","mayhem","android","robot","gamble","mafia"]
 

    def Get_Word(self):
        self.Current_Word = random.choice(self.word_list)

    def Revealed_Word(self,word):
        self.Shown_Word =list(word)

    def Hidden_Word(self,word):
        self.Hidden_Word = ['_'] * len(word)

    def Reveal_Word(self,guess,location):
        self.Hidden_Word[location] = guess

    def Get_Guess(self,player_guess):
        if(player_guess in self.Guessed_List):
            print("You have already tried to play " + player_guess)
        elif(player_guess in self.Shown_Word):
            for position,char in enumerate(self.Shown_Word):
                if char == player_guess:
                    self.Reveal_Word(self,player_guess,position)
            self.Guessed_List.append(player_guess)
        else:
            self.lives.append('x')
            self.Guessed_List.append(player_guess)


    def get_eg_status(self):
        if(len(self.lives) == 6):
            os.system('cls' if os.name == 'nt' else 'clear')
            self.end_state = True
            messagebox.showinfo("GAME OVER!", "GAME OVER: Thanks for playing! \n Answer:\t" + str(''.join([str(elem) for elem in self.Shown_Word])))
            main_form.quit()
        elif(self.Hidden_Word == self.Shown_Word):
            os.system('cls' if os.name == 'nt' else 'clear')
            self.end_state = True
            messagebox.showinfo("Congrats!", "You won! Thanks for playing!")
            main_form.quit()


    def get_user_guess(self,letter):
        char = str(letter)
        if(len(char) == 1 and char.isalpha()):
            self.Get_Guess(self,char.lower())
        else:
            print("Guess must be a single letter!")
            
game = hangman
game.Get_Word(game)
game.Hidden_Word(game,game.Current_Word)
game.Revealed_Word(game,game.Current_Word) 


# GUI

main_form = Tk()
main_form.title("Hangman")
main_form.geometry("600x310")

alphaList = list(string.ascii_lowercase)
game.Hidden_Word


GUI_Hidden_Word = tk.Label(main_form, text=game.Hidden_Word ,font = "Tahoma 30 bold")
GUI_Hidden_Word.pack(side="top")

gui_Guessed_List = tk.Label(main_form, text=game.Guessed_List ,font = "Tahoma 12")
gui_Guessed_List.pack()
gui_Guessed_List.place(bordermode=OUTSIDE, x=200, y=260)

gui_lives = tk.Label(main_form, text=game.lives ,font = "Tahoma 12")
gui_lives.pack()
gui_lives.place(bordermode=OUTSIDE, x=200, y=280)

def btn_Click(self,letter):
    self.config(state="disabled")
    game.get_user_guess(game,letter.lower())
    GUI_Hidden_Word['text'] = game.Hidden_Word
    gui_Guessed_List['text'] = game.Guessed_List
    gui_lives['text'] = game.lives
    game.get_eg_status(game)
    print(letter)    

def create_button(letter,xpos,ypos,index):
    letter = tk.Button(main_form, text=(alphaList[index].upper()),command = lambda: btn_Click(letter,alphaList[index].upper()))
    letter.pack()
    letter.place(bordermode=OUTSIDE, height=50, width=100,x=xpos,y=ypos)

def Letter_Board():
    c = 0
    startpos = 60
    xpos = 0
    ypos = startpos
    while(c < 26):
        if(c == 6):
            ypos = startpos + 50
            xpos = 0
        elif(c == 12):
            ypos = startpos + 100
            xpos = 0
        elif(c == 18):
            ypos = startpos + 150
            xpos = 0
        elif(c == 24):
            ypos = startpos + 200
            xpos = 0

        create_button(alphaList[c],xpos,ypos,c)
        xpos = xpos + 100
        c = c + 1 
Letter_Board()
main_form.mainloop()