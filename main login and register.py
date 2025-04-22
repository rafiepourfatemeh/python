from tkinter import *
import tkinter.messagebox as messagebox
import sqlite3 
import os



root=Tk()
root.geometry('1000x500')
root.title('Main Page')

enterL=Label(root,text='register or login to your account',bg='yellow',font=('Arial',12),pady=10,width=30)
enterL.place(relx=0.5,rely=0.1, anchor=CENTER)



def register():
    root.destroy()
    os.system('register.py')

def login():
    root.destroy()
    os.system('login.py')
    

registerB=Button(root,text='register',command=register,font=('Arial',12), width=8,pady=5,bg='green')
registerB.place(relx=0.4,rely=0.2, anchor=CENTER)

loginB=Button(root,text='login' ,command=login ,font=('Arial',12), width=8,pady=5,bg='green')
loginB.place(relx=0.6,rely=0.2, anchor=CENTER)

root.mainloop()
