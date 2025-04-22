from tkinter import*
from tkinter import ttk
from tkinter import messagebox

def callback():
    val=entry.get()
    x=0
    n=10
    sum=0
    s=0
    a=0
    b=0
    i=0
    while x<9:
        s=val[x]
        a=int(s)*n
        sum+=a

        s=0
        n=n-1
        x=x+1

    b=sum%11
    i=int(val[9])

    if b<=1 :
        if i==b :
           p1=ttk.Label(text="Your ID code is correct .")
           p1.grid(row=4,column=0,sticky='W',pady=10)
        else :
           p1=ttk.Label(text="Your ID code is incorrect .")
           p1.grid(row=4,column=0,sticky='W',pady=10)
     
    elif b>=2 :
        totall=11-b
        if i==totall :
           p1=ttk.Label(text="Your ID code is correct .")
           p1.grid(row=4,column=0,sticky='W',pady=10)
        else :
           p1=ttk.Label(text="Your ID code is incorrect .")
           p1.grid(row=4,column=0,sticky='W',pady=10)




m=Tk()
m.geometry("512x512")
m.title('ID code')
w=Label(m,text="Verify ID Code :",font="Khmer 16")
w.grid(row=0,column=1)
entry=Entry(m,width=30)
lblentry=Label(text="Enter Your ID Code :")
lblentry.grid(row=1,column=0,sticky='W',pady=10)
entry.grid(row=1,column=1,sticky=W)
#name=entry.gets()

button=Button(m,text='Verify',command=callback)
button.grid(row=3,column=1,padx=100,sticky='W',pady=6)

    

m.mainloop()
