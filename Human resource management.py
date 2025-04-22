from email import message
from html import entities
from sqlite3 import Cursor, Row
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from tkmacosx import Button
from tkinter import messagebox
# from PIL import ImageTk, Image
from db import Database



db=Database("Employee.db")


root = Tk()
root.title("مدیریت نیرو انسانی")
root.geometry("1240x615+0+0")
root.resizable(False, False)
root.configure(bg="#2c3e50")


logo = PhotoImage(file="belkaa.png")
lbl_logo = Label(root, image=logo, bg="#2c3e50")
lbl_logo.place(x=80, y=520)










name = StringVar()
age = StringVar()
job = StringVar()
gender = StringVar()
email = StringVar()
mobile = StringVar()

# --------- entries frame  ----------
entries_frame = Frame(root, bg="#2c3e50")
entries_frame.place(x=1, y=1, width=360, height=510)
title = Label(entries_frame, text="  کارمند شرکت", font=(
    "Calibri", 18, "bold"), bg="#2c3e50", fg="white")
title.place(x=10, y=1)
lblname = Label(entries_frame, text="اسم", font=(
    "Calibri", 16, "bold"), bg="#2c3e50", fg="white")
lblname.place(x=10, y=50)
textname = Entry(entries_frame, textvariable=name,
                 width=20, font=("Calibri", 16))
textname.place(x=120, y=50)
lbljob = Label(entries_frame, text="شغل", font=(
    "Calibri", 16, "bold"), bg="#2c3e50", fg="white")
lbljob.place(x=10, y=90)
textjob = Entry(entries_frame, textvariable=job,
                width=20, font=("Calibri", 16))
textjob.place(x=120, y=90)
lblgender = Label(entries_frame, text="جنسیت", font=(
    "Calibri", 16, "bold"), bg="#2c3e50", fg="white")
lblgender.place(x=10, y=130)
combogender = ttk.Combobox(entries_frame, textvariable=gender,
                           state="readonly", width=18, font=("Calibri", 16))
combogender["values"] = ("مذکر", "مونث")
combogender.place(x=120, y=130)
lblage = Label(entries_frame, text="سن", font=(
    "Calibri", 16, "bold"), bg="#2c3e50", fg="white")
lblage.place(x=10, y=170)
textage = Entry(entries_frame, textvariable=age,
                width=20, font=("Calibri", 16))
textage.place(x=120, y=170)
lblemail = Label(entries_frame, text=" ایمیل", font=(
    "Calibri", 16, "bold"), bg="#2c3e50", fg="white")
lblemail.place(x=10, y=210)
textemail = Entry(entries_frame, textvariable=email,
                  width=20, font=("Calibri", 16))
textemail.place(x=120, y=210)
lblmobile = Label(entries_frame, text="شماره موبایل", font=(
    "Calibri", 16, "bold"), bg="#2c3e50", fg="white")
lblmobile.place(x=10, y=250)
textmobile = Entry(entries_frame, textvariable=mobile,
                    width=20, font=("Calibri", 16))
textmobile.place(x=120, y=250)
lbladdress = Label(entries_frame, text=" :آدرس", font=(
    "Calibri", 16, "bold"), bg="#2c3e50", fg="white")
lbladdress.place(x=10, y=290)
textaddress = Text(entries_frame, width=20, height=2, font=("Calibri", 16))

textaddress.place(x=10, y=330)



# -----------Define-------------
def hide():
    root.geometry("360x510+0+0")
def show():
    root.geometry("1240x615+0+0")
btnhide=Button(entries_frame,text="HIDE",cursor="hand2",bd=1,bg="white",relief=SOLID,command=hide)
btnhide.place(x=270,y=10)
btnshow=Button(entries_frame,text="SHOW",bd=1,bg="white",relief=SOLID,cursor="hand2",command=show)
btnshow.place(x=170,y=10)





def getData(event):

      selected_row=tv.focus()
      data=tv.item(selected_row)
      global row
      row=data["values"]
      textaddress.delete(1.0,END)
      textaddress.insert(END,row[0])
      mobile.set(row[1])
      gender.set(row[2])
      email.set(row[3])
      job.set(row[4])
      age.set(row[5])
      name.set(row[6])

def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)


def remove():
    db.remove(row[7])
    clear()
    displayall()


def clear():
    name.set("")
    age.set("")
    email.set("")
    job.set("")
    gender.set("")  
    mobile.set("")
    textaddress.delete(1.0,END)     

def add_employee():
    if textname.get()=="" or textage.get()=="" or textjob.get()=="" or textemail.get()==""  or combogender.get()=="" or textaddress.get(1.0,END)=="" or textmobile.get()=="" :
        messagebox.showerror("Error","لطفا جای خالی را پر کنید")
        return
    db.insert(
        textname.get(),
        textage.get(),
        textjob.get(),
        textemail.get(),
        combogender.get(),
        textmobile.get(),
        textaddress.get(1.0,END))
    messagebox.showinfo("success","کارمند جدید اضافه شد")
    clear()
    displayall()

def update():
    if textname.get()=="" or textage.get()=="" or textjob.get()=="" or textemail.get()==""  or combogender.get()=="" or textaddress.get(1.0,END)=="" or textmobile.get()=="" :
           messagebox.showerror("Error","لطفا جای خالی را پر کنید")
           return
    db.update(
        row[7],
        textname.get(),
        textage.get(),
        textjob.get(),
        textemail.get(),
        combogender.get(),
        textmobile.get(),
        textaddress.get(1.0,END))
    messagebox.showinfo("seccess","اطلاعات بروز رسانی شد")
    clear()
    displayall()




# ----------Buttons Frame دکمه ها----------
btn_frame = Frame(entries_frame, bg="#2c3e50", bd=1, relief=SOLID)
btn_frame.place(x=10, y=400, width=335, height=100)

btnadd = Button(btn_frame,
                text="اضافه کردن اطلاعات",
                font=("Calibri", 16),
                fg="white",
                bg="#16a085",
                bd=0,command=add_employee)
btnadd.place(x=4, y=5, width=150, height=30)

btnedit = Button(btn_frame,
                 text=" بروزرسانی اطلاعات ",
                 font=("Calibri", 16),
                 fg="white",
                 bg="#2980b9",
                 bd=0,
                 command=update)
btnedit.place(x=4, y=50, width=150, height=30)

btndelete = Button(btn_frame,
                   text=" حذف اطلاعات ",
                   font=("Calibri", 16),
                   fg="white",
                   bg="#c0392b",
                   bd=0,
                   command=remove)
btndelete.place(x=170, y=5, width=150, height=30)

btnclear = Button(btn_frame,
                   text=" حذف جای خالی ",
                   font=("Calibri", 16),
                   fg="white",
                   bg="#f39c12",
                   bd=0,
                   command=clear)
btnclear.place(x=170, y=50, width=150, height=30)





    
    
    


# ------------Table frame -------------
tree_frame = Frame(root, bg="white")
tree_frame.place(x=365, y=1, width=875, height=610)
style = ttk.Style()
style.configure("mystyle.Treeview", font=("Calibri", 13), rowheight=50)
style.configure("mystyle.Treeview.heading", font=("Calibri", 13))
tv = ttk.Treeview(tree_frame, columns=(
    1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("8", text="ID")
tv.column("8", width=60)

tv.heading("7", text="اسم")
tv.column("7", width=110)
tv.heading("6", text="سن")
tv.column("6", width=50)
tv.heading("5", text="شغل")
tv.column("5", width=120)
tv.heading("4", text="ایمیل")
tv.column("4", width=110)
tv.heading("3", text="جنسیت")
tv.column("3", width=90)
tv.heading("2", text="موبایل")
tv.column("2", width=150)
tv.heading("1", text="آدرس")
tv.column("1", width=190)
tv["show"] = "headings"
tv.bind("<ButtonRelease-1>",getData)
tv.place(x=0,y=0,height=610)

displayall()

root.mainloop()
