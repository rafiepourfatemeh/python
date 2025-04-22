#Scientific Calculator



from tkinter import *
#import tkinter as tk
import math as m
import random as rd

root = Tk()
root.title('Scientific Calculator')
root.geometry("680x500+450+90")

eq = StringVar()
var1 = IntVar()
var2 = IntVar()

Label(root,textvariable = eq, font =('Times',20),pady = 20, padx = 20).grid(columnspan = 8)
# functions
def set_num(num):
    try:
        if eq.get()=='0':
            if num.isdigit() or num=='(':
                a = num
            else:
                a = eq.get()+num
        else:
            a = eq.get()+num
        if len(a)>=2:
            if not a[-2].isdigit() and a[-1]=='(':
                pass
            elif a[-2]=='(' or a[-2]==')' and not a[-1].isdigit():
               # a = a[:-2]+a[-1]
               pass
            elif not a[-2].isdigit() and not a[-1].isdigit():
                a = a[:-2]+a[-1]
        eq.set(a)
    except:
        eq.set('sth is wrong here, press C')
def calc_eq():# normal computation
    try:
        leq = eq.get()
        result = eval(leq)
        eq.set(result)
    except ZeroDivisionError:
        eq.set('division by zero, press C')


def blog10():
    a = float(eq.get())
    try:
        eq.set(m.log10(a))
    except:
        eq.set('log is not defined, press C')
def blog():
    a = float(eq.get())
    try:
        eq.set(m.log(a))
    except:
        eq.set('log is not defined, press C')

def bfact(): # n!
    count = 1
    a = eq.get()
    try:
        for i in range(int(a)):
            count*=(i+1)
        eq.set(count)
    except ValueError:
        eq.set('input is wrong, press C')
    
def bpowy():# x^y
    #input('import y')
   # eq.set('import y: ') # need to ask on the screen of calculator
    y = eq.get()
    eq.set(m.pow(float(y),float(y)))

def bsqrt():
    a = float(eq.get())
    try:
        eq.set(m.sqrt(a))
    except:
        eq.set('input is wrong, press C')
def bminus():
    a = eq.get()
    if a=='0':
        pass
    elif a[0]=='-':
        a= a[1:]
    else:
        a= '-'+a        
    eq.set(a)


def binverse():
    try:
        a = float(eq.get())
        eq.set(1/a)
    except:
        eq.set('division by zero!, press C')
def backspace():
    a = eq.get()
    if a=='0':
        pass
    else:
        a = a[:-1]
    eq.set(a)

# numbers
btn1 = Button(root,text='1',font =('Times',20),width = 5,height = 2,command=lambda:set_num('1')).grid(row=5,column=4)
btn2 = Button(root,text='2',font =('Times',20),width = 5,height = 2,command=lambda:set_num('2')).grid(row=5,column=5)
btn3 = Button(root,text='3',font =('Times',20),width = 5,height = 2,command=lambda:set_num('3')).grid(row=5,column=6)
btn4 = Button(root,text='4',font =('Times',20),width = 5,height = 2,command=lambda:set_num('4')).grid(row=4,column=4)
btn5 = Button(root,text='5',font =('Times',20),width = 5,height = 2,command=lambda:set_num('5')).grid(row=4,column=5)
btn6 = Button(root,text='6',font =('Times',20),width = 5,height = 2,command=lambda:set_num('6')).grid(row=4,column=6)
btn7 = Button(root,text='7',font =('Times',20),width = 5,height = 2,command=lambda:set_num('7')).grid(row=3,column=4)
btn8 = Button(root,text='8',font =('Times',20),width = 5,height = 2,command=lambda:set_num('8')).grid(row=3,column=5)
btn9 = Button(root,text='9',font =('Times',20),width = 5,height = 2,command=lambda:set_num('9')).grid(row=3,column=6)
bDot = Button(root,text='.',font =('Times',20),width = 5,height = 2,command=lambda:set_num('.')).grid(row=6,column=6)
btn0 = Button(root,text='0',font =('Times',20),width = 5,height = 2,command=lambda:set_num('0')).grid(row=6,column=5)


#simple and one line part: 
bSin = Button(root,text='sin',font =('Times',20),width = 5,height = 2,command= lambda: eq.set(m.sin(m.radians(float(eq.get()))))).grid(row=2,column=0)# degree input
bCos = Button(root,text='cos',font =('Times',20),width = 5,height = 2,command=lambda: eq.set(m.cos(m.radians(float(eq.get()))))).grid(row=3,column=0)
bTg = Button(root,text='tan',font =('Times',20),width = 5,height = 2,command=lambda: eq.set(m.tan(m.radians(float(eq.get()))))).grid(row=4,column=0)

bsinh = Button(root,text = 'sinh',font =('Times',20),width = 5,height = 2,command= lambda: eq.set(m.sinh(m.radians(float(eq.get()))))).grid(row=2,column=1)
bcosh = Button(root,text = 'cosh',font =('Times',20),width = 5,height = 2,command= lambda: eq.set(m.cosh(m.radians(float(eq.get()))))).grid(row=3,column=1)
btgh = Button(root,text='tanh',font =('Times',20),width = 5,height = 2,command= lambda: eq.set(m.tanh(m.radians(float(eq.get()))))).grid(row=4,column=1)

bLn = Button(root,text='Ln',font =('Times',20),width = 5,height = 2,command=lambda: blog()).grid(row=5,column=0)
bLog = Button(root,text='log',font =('Times',20),width = 5,height = 2,command=lambda: blog10()).grid(row=6,column=0)
bExp = Button(root,text='exp',font =('Times',20),width = 5,height = 2,command=lambda: eq.set(m.exp(float(eq.get())))).grid(row=5,column=1)# correct
bPow_10 = Button(root,text='10^x',font =('Times',20),width = 5,height = 2,command=lambda: eq.set(10**(float(eq.get())))).grid(row=6,column=1)# correct


bxPow3 = Button(root,text='x^3',font =('Times',20),width = 5,height = 2,command=lambda: eq.set(m.pow(float(eq.get()),3))).grid(row=4,column=2)
bxPow2 = Button(root,text='x^2',font =('Times',20),width = 5,height = 2,command=lambda: eq.set(m.pow(float(eq.get()),2))).grid(row=5,column=2)
bot_pi = Button(root,text='\u03C0',font =('Times',20),width = 5,height = 2,command=lambda: eq.set(m.pi)).grid(row=6,column=2)
bX_sqrt_2 = Button(root,text='x^(1/2)',font =('Times',20),width = 5,height = 2,command=lambda: bsqrt()).grid(row=3,column=3)
bX_sqrt_3 = Button(root,text='$x^(1/3)$',font =('Times',20),width = 5,height = 2,command=lambda: eq.set(float(eq.get())**(1./3.))).grid(row=4,column=3)
bFact = Button(root,text='n!',font =('Times',20),width = 5,height = 2,command=lambda:bfact()).grid(row=5,column=3)
b1_x = Button(root,text='1/x',font =('Times',20),width = 5,height = 2,command=lambda:binverse()).grid(row=6,column=3)



plus= Button(root,text='+',font =('Times',20),width = 5,height = 2,command=lambda:set_num('+')).grid(row=2,column=7)
minus= Button(root,text='-',font =('Times',20),width = 5,height = 2,command=lambda:set_num('-')).grid(row=3,column=7)
mult= Button(root,text='*',font =('Times',20),width = 5,height = 2,command=lambda:set_num('*')).grid(row=4,column=7)
divis= Button(root,text='/',font =('Times',20),width = 5,height = 2,command=lambda:set_num('/')).grid(row=5,column=7)
equla = Button(root,text='=',font =('Times',20),width = 5,height = 2,command=lambda:calc_eq()).grid(row=6,column=7)


# complex part
bCE = Button(root,text='CE',font =('Times',20),width = 5,height = 2,command=lambda:eq.set('0')).grid(row=2,column=5)
bC = Button(root,text='C',font =('Times',20),width = 5,height = 2,command=lambda:eq.set('0')).grid(row=2,column=6)


btnPlNe = Button(root,text='+/-',font =('Times',20),width = 5,height = 2,command=lambda: bminus()).grid(row=6,column=4)
bParL = Button(root,text='(',font =('Times',20),width = 5,height = 2,command=lambda:set_num('(')).grid(row=2,column=2)
bParR = Button(root,text=')',font =('Times',20),width = 5,height = 2,command=lambda:set_num(')')).grid(row=2,column=3)
bBack = Button(root,text='BACK',font =('Times',20),width = 5,height = 2,command=lambda:backspace()).grid(row=2,column=4)


bxPowy = Button(root,text='x^x',font =('Times',20),width = 5,height = 2,command=lambda: bpowy()).grid(row=3,column=2)# need function




















