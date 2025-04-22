from tkinter import *
from tkinter import ttk
import sqlite3
#import form
# import form
global price1
price1 = 0
global price2
price2 = 0
global list1
list1 = ''
global list2
list2 = ''
#the first page
def menu():
    root = Tk()
    root.geometry('1365x1280')
    def destroy():
         root.destroy()
    h = Label(root,text='pick your restaurant',font=('Helvetica',40),fg='#091a40',bg='#1c5253',width=45).pack(side=TOP)
    h1 = Button(root,text='KFC',font=('Helvetica',40),fg='#218380',width=22,height=20,activebackground='#218380',bg='#00171f',
    activeforeground='#00171f',borderwidth=10,command=lambda : [KFC_hover(),destroy()]).pack(side=RIGHT)
    h2 = Button(root,text='Mc Donalds',font=('Helvetica',40),fg='#218380',bg='#00171f',width=22,height=20,activebackground='#218380',
    activeforeground='#00171f',borderwidth=10,command=lambda : [Mc_Donald_hover(),destroy()]).pack(side=LEFT)
    root.mainloop()
#_____________________________

# KFC's page
def KFC_hover():
    root = Tk()
    root.geometry('1370x1280')
    root.configure(bg='#1c5253')
    def destroy():
        root.destroy()
    a = Button(root, text='----->', width=10, height=4, fg='#00171f', bg='#218380',command=lambda: [destroy(), menu()]).place(x=1290)
    h1 = Button(root, text='Chickens', font=('Helvetica', 40), fg='#218380', width=13, height=5, bg='#00171f',
    activebackground='#218380',activeforeground='#00171f', borderwidth=10, command=lambda: [KFCchicken(), destroy()]).grid(row=0,column=1)
    h2 = Button(root, text='Hamburgers', font=('Helvetica', 40), fg='#218380', width=13, height=5, bg='#00171f',
    activebackground='#218380',activeforeground='#00171f', borderwidth=10, command=lambda: [KFChamburger(), destroy()]).grid(row=0,column=2)
    h3 = Button(root, text='Rice Bowls', font=('Helvetica', 40), fg='#218380', width=13, height=5, bg='#00171f',
    activebackground='#218380',activeforeground='#00171f', borderwidth=10, command=lambda: [KFCRice_Bowls(), destroy()]).grid(row=1, column=2)
    h4 = Button(root, text='Drinks', font=('Helvetica', 40), fg='#218380', width=13, height=5, bg='#00171f',
    activebackground='#218380',activeforeground='#00171f', borderwidth=10, command=lambda: [KFCdrinks(), destroy()]).grid(row=1,column=1)
    def sabt():
        root = Tk()
        root.geometry('800x900')
        root.configure(bg='#1c5253')
        message = Label(root, text='''your list:%s      
    the total price is:%0.1f''' % (list1,price1),wraplength=600,justify=LEFT,bg='#1c5253',fg='#00171f',
    font=('Helvetica', 30)).place(x=0,y=0)
    buttonsabt = Button(root, width=23, height=4, text='sabt', font=('Helvetica', 30), fg='#218380', bg='#00171f',
    activebackground='#218380',activeforeground='#00171f', command=lambda: [destroy(), sabt()]).place(x=860, y=490)
# ____________________________________

#KFC chiken's page
def KFCchicken():
    root = Tk()
    root.geometry('1370x1280')
    root.configure(bg='#1c5253')
    def destroy():
        root.destroy()
    def Price(x):
        global price1
        price1 += x
    def List(x):
        global list1
        list1 += ' '+x+'_'
    a = Button(root, text='----->', width=10, height=5,fg='#00171f',bg='#218380', command=lambda : [KFC_hover(),destroy()]).place(x=1290)
    b = Label(root,text='choose what your heart desire',font=('Tohoma',30),width=56,height=2,fg='#218380',bg='#00171f').place(x=2,y=-10)
    first = Label(root,text='''2 Pc Chicken & Fries meal price:44.9$''',fg='#218380',bg='#00171f',font=('Tohoma',18) ).place(x=660,y=100)
    buttonfirst = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff',font=('Tohoma',13), width=8, height=2,
    command=lambda : [Price(44.9),List('2 Pc Chicken & Fries meal')]).place(x=680, y=200)
    second = Label(root,text='''Chicken & Wings Combo price:52.9$''',fg='#218380',bg='#00171f',
    font=('Tohoma',18) ).place(x=0,y=100)
    buttonsecond = Button(root,  text='add to cart',fg='#2f2f2f',bg='#1b99ff',font=('Tohoma',13), width=8, height=2,
    command=lambda : [Price(52.9),List('Chicken & Wings Combo')]).place(x=10, y=200)
    third = Label(root,text='''2 Pc Hot & Crispy Chicken price:29.9$''',fg='#218380',bg='#00171f',
    font=('Tohoma', 18)).place(x=675,y=300)
    buttonthird = Button(root,  text='add to cart',fg='#2f2f2f',bg='#1b99ff',font=('Tohoma',13), width=8, height=2,
    command=lambda : [Price(29.9),List('2 Pc Hot & Crispy Chicken')]).place(x=680, y=400)
    fourth = Label(root, text='4 Pc Chickens & Fries meal price:74.9$',fg='#218380',bg='#00171f',
    font=('Tohoma', 18) ).place(y=300)
    buttonfourth = Button(root,  text='add to cart',fg='#2f2f2f',bg='#1b99ff',font=('Tohoma',13), width=8, height=2,
    command=lambda : [Price(74.9),List('4 Pc Chickens & Fries meal')]).place(x=10, y=400)
    fifth = Label(root, text='6 Pc Boneless Strips price:48.9$',fg='#218380',bg='#00171f',
    font=('Tohoma', 18)).place(x=660,y=490)
    buttonfifth = Button(root,  text='add to cart',fg='#2f2f2f',bg='#1b99ff',font=('Tohoma',13), width=8, height=2,
    command=lambda : [Price(48.9),List('6 Pc Boneless Strips')]).place(x=680, y=600)
    sixth = Label(root, text='8 Pc Hot & Crispy Chicken price:109.9$',fg='#218380',bg='#00171f',
    font=('Tohoma', 18) ).place(y=490)
    buttonsixth = Button(root,  text='add to cart',fg='#2f2f2f',bg='#1b99ff',font=('Tohoma',13), width=8, height=2,
    command=lambda : [Price(109.9),List('8 Pc Hot & Crispy Chicken')]).place(x=10, y=600)
#______________________________

# hamburger's page
def KFChamburger():
    root = Tk()
    root.geometry('1370x1280')
    root.configure(bg='#1c5253')
    def destroy():
        root.destroy()
    def Price(x):
        global price1
        price1 += x
    def List(x):
        global list1
        list1 += ' ' + x + '_'
    a = Button(root, text='----->', width=10, height=5,fg='#00171f',bg='#218380', command= lambda : [KFC_hover(),destroy()]).place(x=1290)
    b = Label(root,text='choose what your heart desire',font=('Tohoma',30),width=56,height=2,fg='#218380',bg='#00171f').place(x=2,y=-10)
    first = Label(root, text='Classic Zinger price:30.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660, y=100)
    buttonfirst = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(30.9),List('Classic Zinger')]).place(x=680, y=200)
    second = Label(root, text='Zing & Fries Meal price:39.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=0, y=100)
    buttonsecond = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(39.9),List('Zing & Fries Meal')]).place(x=10, y=200)
    third = Label(root, text='Classic Zinger with Cheese price:34.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=675, y=300)
    buttonthird = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(34.9),List('Classic Zinger with Cheese')]).place(x=680, y=400)
    fourth = Label(root, text='Big Zing Trio price:54.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(y=300)
    buttonfourth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(54.9),List('Big Zing Trio')]).place(x=10, y=400)
    fifth = Label(root, text='2 Classic Zinger Meal  price:94.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660, y=490)
    buttonfifth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(94.9),List('2 Classic Zinger Meal')]).place(x=680, y=600)
    sixth = Label(root, text='Spicy Znger price:32.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(y=490)
    buttonsixth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(32.9),List('Spicy Znger')]).place(x=10, y=600)
#_______________________________

#KFC Rice Bowls's page
def KFCRice_Bowls():
    root = Tk()
    root.geometry('1370x1280')
    root.configure(bg='#1c5253')
    def destroy():
        root.destroy()
    def Price(x):
        global price1
        price1 += x
    def List(x):
        global list1
        list1 += ' '+x+'_'
    a = Button(root, text='----->', width=10, height=5,fg='#00171f',bg='#218380', command= lambda : [KFC_hover(),destroy()]).place(x=1290)
    b = Label(root,text='choose what your heart desire',font=('Tohoma',30),width=56,height=2,fg='#218380',bg='#00171f').place(x=2,y=-10)
    first = Label(root, text='Hot & Crispy Rice Bowl price:24.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660, y=100)
    buttonfirst = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(24.9),List('Hot & Crispy Rice Bowl')]).place(x=680, y=200)
    second = Label(root, text='Popcorn Rice Bowl price:32.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=0, y=100)
    buttonsecond = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(32.9),List('Popcorn Rice Bowl')]).place(x=10, y=200)
    third = Label(root, text='Hot Wings Rice Bowl price:29.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=675, y=300)
    buttonthird = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(29.9),List('Hot Wings Rice Bowl')]).place(x=680, y=400)
    fourth = Label(root, text='Rice Box price:34.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(y=300)
    buttonfourth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(34.9),List('Rice Box')]).place(x=10, y=400)
    fifth = Label(root, text='Strips Rice Combo price:49.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660, y=490)
    buttonfifth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(49.9),List('Strips Rice Combo')]).place(x=680, y=600)
    sixth = Label(root, text='Buudy Rice Combo price:69.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(y=490)
    buttonsixth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(69.9),List('Buudy Rice Combo')]).place(x=10, y=600)
#___________________________________

#KFC drinks's page
def KFCdrinks():
    root = Tk()
    root.geometry('1370x1280')
    root.configure(bg='#1c5253')
    def destroy():
        root.destroy()
    def Price(x):
        global price1
        price1 += x
    def List(x):
        global list1
        list1 += ' '+x+'_'
    a = Button(root, text='----->', width=10, height=5,fg='#00171f',bg='#218380', command= lambda : [KFC_hover(),destroy()]).place(x=1290)
    b = Label(root,text='choose what your heart desire',font=('Tohoma',30),width=56,height=2,fg='#218380',bg='#00171f').place(x=2,y=-10)
    first = Label(root, text='Pepsi(500ml) price:3.0$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660, y=100)
    buttonfirst = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(3.0),List('Pepsi(500ml)')]).place(x=680, y=200)
    second = Label(root, text='7UP(500ml) price:3.5$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=0, y=100)
    buttonsecond = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(3.5),List('7UP(500ml)')]).place(x=10, y=200)
    third = Label(root, text='Pepsi(800ml) price:3.5$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=675, y=300)
    buttonthird = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(3.5),List('Pepsi(800ml)')]).place(x=680, y=400)
    fourth = Label(root, text='7UP(800ml) price:4.0$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(y=300)
    buttonfourth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(4.0),List('7UP(800ml)')]).place(x=10, y=400)
    fifth = Label(root, text='Mountain Dew price:4.0$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660, y=490)
    buttonfifth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(4.0),List('Mountain Dew')]).place(x=680, y=600)
    sixth = Label(root, text='Aquafina Water price:1.5$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(y=490)
    buttonsixth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(1.5),List('Aquafina water')]).place(x=10, y=600)
#____________________________________

#Mac_Donalds's page
def Mc_Donald_hover():
    root = Tk()
    root.geometry('1370x1280')
    root.configure(bg='#1c5253')
    def destroy():
        root.destroy()
    a = Button(root,text='----->',width=10,height=4,fg='#00171f',bg='#218380',command=lambda : [destroy(),menu()]).place(x=1290)
    h1 = Button(root, text='Breakfast', font=('Helvetica', 40), fg='#218380',bg='#00171f', width=13, height=5, activebackground='#218380',
    activeforeground='#00171f', borderwidth=10,command=lambda : [Mc_Donald_Breakfast(),destroy()]).grid(row=0,column=1)
    h2 = Button(root, text='Hamburger', font=('Helvetica', 40),fg='#218380',bg='#00171f', width=13, height=5,
    activebackground='#218380',
    activeforeground='#00171f', borderwidth=10,command=lambda : [Mac_Donald_hamburger(),destroy()]).grid(row=0,column=2)
    h3 = Button(root, text='Chicken&Sandwich', font=('Helvetica', 40),fg='#218380',bg='#00171f', width=13, height=5,
    activebackground='#218380',
    activeforeground='#00171f', borderwidth=10,command=lambda : [Mac_Donald_Chicken_Sandwich(),destroy()]).grid(row=1,column=2)
    h4 = Button(root, text='drinks', font=('Helvetica', 40),fg='#218380',bg='#00171f', width=13, height=5,
    activebackground='#218380',
    activeforeground='#00171f', borderwidth=10,command=lambda : [Mc_Donald_drinks(),destroy()]).grid(row=1,column=1)
    def sabt2():
        root = Tk()
        root.geometry('800x900')
        root.configure(bg='#1c5253')
        message = Label(root,text='''your list:%s      
    the total price is:%0.1f''' % (list2,price2),wraplength=600,justify=LEFT,bg='#1c5253',fg='#00171f', font=('Helvetica', 30)).place(x=0,y=0)
    buttonsabt = Button(root,width=23,height=4,text='sabt',fg='#218380',bg='#00171f',activeforeground='#00171f',
    activebackground='#218380',font=('Helvetica',30),command=lambda : [destroy(),sabt2()]).place(x=860,y=490)
#______________________________


#Mc_Donald Breakfast's page
def Mc_Donald_Breakfast():
    root = Tk()
    root.geometry('1370x1280')
    root.configure(bg='#1c5253')
    def destroy():
        root.destroy()
    def Price(x):
        global price2
        price2 += x
    def List(x):
        global list2
        list2 += ' '+x+'_'
    a = Button(root, text='----->', width=10, height=5,fg='#00171f',bg='#218380', command=lambda : [Mc_Donald_hover(),destroy()]).place(x=1290)
    b = Label(root,text='choose what your heart desire',font=('Tohoma',30),width=56,height=2,fg='#218380',bg='#00171f').place(x=2,y=-10)
    first = Label(root, text='Bacon&egg price:24.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660, y=100)
    buttonfirst = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(24.9),List('Bacon&egg ')]).place(x=680, y=200)
    second = Label(root, text='Chicken McMuffin price:22.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=0, y=100)
    buttonsecond = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(22.9),List('Chicken McMuffin')]).place(x=10, y=200)
    third = Label(root, text='Egg MacMuffin price:29.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=675, y=300)
    buttonthird = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(29.9),List('Egg MacMuffin')]).place(x=680, y=400)
    fourth = Label(root, text='Hash Brown price:19.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(y=300)
    buttonfourth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(19.9),List('Hash Brown')]).place(x=10, y=400)
    fifth = Label(root, text='MacMuffin Deluxe price:34.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660, y=490)
    buttonfifth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(34.9),List('MacMuffin Deluxe')]).place(x=680, y=600)
    sixth = Label(root, text='Scramblrd Eggs price:109.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(y=490)
    buttonsixth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(109.9),List('Scramblrd Eggs')]).place(x=10, y=600)
#______________________________

#Mac_Donald_hamburger's page
def Mac_Donald_hamburger():
    root = Tk()
    root.geometry('1370x1280')
    root.configure(bg='#1c5253')
    def destroy():
         root.destroy()
    def Price(x):
        global price2
        price2 += x
    def List(x):
        global list2
        list2 += ' '+x+'_'
    a = Button(root, text='----->', width=10, height=5,fg='#00171f',bg='#218380', command= lambda : [Mc_Donald_hover(),destroy()]).place(x=1290)
    b = Label(root,text='choose what your heart desire',font=('Tohoma',30),width=56,height=2,fg='#218380',bg='#00171f').place(x=2,y=-10)
    first = Label(root, text='Big Mac price:39.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660, y=100)
    buttonfirst = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(39.9),List('Big Mac')]).place(x=680, y=200)
    second = Label(root, text='Big Tasty price:42.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=0, y=100)
    buttonsecond = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
     command=lambda: [Price(42.9),List('Big Tasty')]).place(x=10, y=200)
    third = Label(root, text='Cheeseburger price:44.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=675, y=300)
    buttonthird = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(44.9),List('Cheeseburger')]).place(x=680, y=400)
    fourth = Label(root, text='Chicken Mayo price:48.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(y=300)
    buttonfourth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
     command=lambda: [Price(48.9),List('Chicken Mayo')]).place(x=10, y=400)
    fifth = Label(root, text='Crispy McBacon  price:50.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660, y=490)
    buttonfifth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(50.9),List('Crispy McBacon')]).place(x=680, y=600)
    sixth = Label(root, text='McRib price:39.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(y=490)
    buttonsixth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(39.9),List('McRib')]).place(x=10, y=600)
#_______________________________

#Mac_Donald_Chicken&Sandwich's page
def Mac_Donald_Chicken_Sandwich():
    root = Tk()
    root.geometry('1370x1280')
    root.configure(bg='#1c5253')
    def destroy():
        root.destroy()
    def Price(x):
        global price2
        price2 += x
    def List(x):
        global list2
        list2 += ' '+x+'_'
    a = Button(root, text='----->', width=10, height=5,fg='#00171f',bg='#218380', command= lambda : [Mc_Donald_hover(),destroy()]).place(x=1290)
    b = Label(root,text='choose what your heart desire',font=('Tohoma',30),width=56,height=2,fg='#218380',bg='#00171f').place(x=2,y=-10)
    first = Label(root, text='Hot & Crispy Rice Bowl price:24.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660, y=100)
    buttonfirst = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(24.9),List('Hot & Crispy Rice Bowl')]).place(x=680, y=200)
    second = Label(root, text='Popcorn Rice Bowl price:32.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=0, y=100)
    buttonsecond = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(32.9),List('Popcorn Rice Bowl')]).place(x=10, y=200)
    third = Label(root, text='Hot Wings Rice Bowl price:29.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=675, y=300)
    buttonthird = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(29.9),List('Hot Wings Rice Bowl')]).place(x=680, y=400)
    fourth = Label(root, text='Rice Box price:34.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(y=300)
    buttonfourth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(34.9),List('Rice Box')]).place(x=10, y=400)
    fifth = Label(root, text='Strips Rice Combo price:49.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660, y=490)
    buttonfifth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(49.9),List('Strips Rice Combo')]).place(x=680, y=600)
    sixth = Label(root, text='Buudy Rice Combo price:69.9$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(y=490)
    buttonsixth = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff', font=('Tohoma', 13), width=8, height=2,
    command=lambda: [Price(69.9),List('Buudy Rice Combo')]).place(x=10, y=600)
#___________________________________
#Mc_Donald_drinks's page
def Mc_Donald_drinks():
    root = Tk()
    root.geometry('1370x1280')
    root.configure(bg='#1c5253')
    def destroy():
        root.destroy()
    def Price(x):
        global price2
        price2 += x
    def List(x):
        global list2
        list2 += ' '+x+'_'
    a = Button(root, text='----->', width=10, height=5,fg='#00171f',bg='#218380', command= lambda : [Mc_Donald_hover(),destroy()]).place(x=1290)
    b = Label(root,text='choose what your heart desire',font=('Tohoma',30),width=56,height=2,fg='#218380',bg='#00171f').place(x=2,y=-10)
    first = Label(root,text='Pepsi(500ml) price:3.0$',fg='#218380',bg='#00171f',font=('Tohoma',18) ).place(x=660,y=100)
    buttonfirst = Button(root, text='add to cart',fg='#2f2f2f',bg='#1b99ff',font=('Tohoma',13), width=8, height=2,
    command=lambda : [Price(3.0),List('Pepsi(500ml)')]).place(x=680, y=200)
    second = Label(root,text='7UP(500ml) price:3.5$',fg='#218380',bg='#00171f',font=('Tohoma',18) ).place(x=0,y=100)
    buttonsecond = Button(root,  text='add to cart',fg='#2f2f2f',bg='#1b99ff',font=('Tohoma',13), width=8, height=2,
    command=lambda : [Price(3.5),List('7UP(500ml)')]).place(x=10, y=200)
    third = Label(root,text='Pepsi(800ml) price:3.5$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=675,y=300)
    buttonthird = Button(root,  text='add to cart',fg='#2f2f2f',bg='#1b99ff',font=('Tohoma',13), width=8, height=2,
    command=lambda : [Price(3.5),List('Pepsi(800ml)')]).place(x=680, y=400)
    fourth = Label(root, text='7UP(800ml) price:4.0$',fg='#218380',bg='#00171f', font=('Tohoma', 18) ).place(y=300)
    buttonfourth = Button(root,  text='add to cart',fg='#2f2f2f',bg='#1b99ff',font=('Tohoma',13), width=8, height=2,
    command=lambda : [Price(4.0),List('7UP(800ml)')]).place(x=10, y=400)
    fifth = Label(root, text='Mountain Dew price:4.0$',fg='#218380',bg='#00171f', font=('Tohoma', 18)).place(x=660,y=490)
    buttonfifth = Button(root,  text='add to cart',fg='#2f2f2f',bg='#1b99ff',font=('Tohoma',13), width=8, height=2,
    command=lambda : [Price(4.0),List('Mountain Dew')]).place(x=680, y=600)
    sixth = Label(root, text='Aquafina Water price:1.5$',fg='#218380',bg='#00171f', font=('Tohoma', 18) ).place(y=490)
    buttonsixth = Button(root,  text='add to cart',fg='#2f2f2f',bg='#1b99ff',font=('Tohoma',13), width=8, height=2,
    command=lambda : [Price(1.5),List('Aquafina Water')]).place(x=10, y=600)
#____________________________________
menu()
