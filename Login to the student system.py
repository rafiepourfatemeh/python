from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3  

addrFileDB = 'aysan.db'  


def selectItem():

    selectWindow = Toplevel()
    selectWindow.geometry("350x350")
    selectWindow.title("انتخاب")
    selectWindow.grab_set()
    selectWindow.configure(bg='#0d0c38')

    def singupWindow():


        def resetform():
            listtaskDeleat = [
                Tname, Tfamily, Tnamefather, Tsex,
                TdateD, TdateM, TdateY, TnationalCode,
                Tnumber, Temail, Tusername, Tpass
            ]
            for i in listtaskDeleat:
                i.set('')


        def sending():
            nameUser = Tname.get()
            familyUser = Tfamily.get()
            fatherUser = Tnamefather.get()
            sexUser = Tsex.get()
            dateDUser = TdateD.get()
            dateMUser = TdateM.get()
            dateYUser = TdateY.get()
            nationalCodeUser = TnationalCode.get()
            numberUser = Tnumber.get()
            emailUser = Temail.get()
            usernameUser = Tusername.get()
            passUser = Tpass.get()

            listtask = [
                (
                    nameUser, familyUser, fatherUser, sexUser,
                    dateDUser, dateMUser, dateYUser, nationalCodeUser,
                    numberUser, emailUser, usernameUser, passUser,
                )
            ]





            # start Database

            conn = sqlite3.connect(addrFileDB)  

            c = conn.cursor()                   
                                                
            c.execute('''CREATE TABLE IF NOT EXISTS students(       
                                    namee ,
                                    family ,
                                    dadyname ,
                                    sex ,
                                    birthd ,
                                    birthm ,
                                    birthy ,
                                    codemeli ,
                                    mobile ,
                                    email ,
                                    username ,
                                    password
                                     )''')

        

        

            c.executemany('INSERT INTO students VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', listtask);

            conn.commit()
            conn.close()


            


            resetform()



        selectWindow.destroy()

        singWindow = Toplevel()
        singWindow.geometry("700x680")
        singWindow.title("ثبت نام دانشجو")
        singWindow.grab_set()
        singWindow.configure(bg='#0d0c38')

        Label(singWindow, text="فرم ثبت نام دانشجو", fg='white', bg='#4949b2', ).grid(row = 0, pady = 2, padx=5)
        Label(singWindow, text="مجتمع فني تهران", font=("Tahoma", 35), bg='#0d0c38', fg='white', width=20, justify=CENTER).grid(row = 1, pady = 2, padx=5)
        Label(singWindow, text="www.mftplus.com", font=("Tahoma", 13), bg='#0d0c38', fg='white', width=55, justify=CENTER).grid(row = 2, pady = 2, padx=5)
        Label(singWindow, text=":نام", bg='#0d0c38', font=("Tahoma", 15), fg='white', width=0, justify=CENTER).grid(row = 3, column = 1, pady = 2, padx=0)
        Label(singWindow, text=":نام خانوادگي", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row = 4, column = 1, pady = 2, padx=0)
        Label(singWindow, text=":نام پدر", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row = 5, column = 1, pady = 2, padx=0)
        Label(singWindow, text=":جنسيت", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row = 6, column = 1, pady = 2, padx=0)
        Label(singWindow, text=":تاريخ تولد", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row = 7, column = 1, pady = 2, padx=0)
        Label(singWindow, text=":روز -", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row = 8, column = 1, pady = 2, padx=0)
        Label(singWindow, text=":ماه -", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row = 9, column = 1, pady = 2, padx=0)
        Label(singWindow, text=":سال -", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0,  justify=CENTER).grid(row = 10, column = 1, pady = 2, padx=0)


        Label(singWindow, font=("Tahoma", 15), text=":کد ملي", bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row = 11, column = 1, pady = 2, padx=0)
        Label(singWindow, font=("Tahoma", 15), text=":شماره همراه", bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row = 12, column = 1, pady = 2, padx=0)
        Label(singWindow, font=("Tahoma", 15), text=":ايميل", bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row = 13, column = 1, pady = 2, padx=0)
        Label(singWindow, font=("Tahoma", 15), text=":نام کاربري", bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row = 14, column = 1, pady = 2, padx=0)
        Label(singWindow, font=("Tahoma", 15), text=":رمز عبور", bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row = 15, column = 1, pady = 2, padx=0)

        Tname = StringVar()
        Entry(singWindow, textvariable=Tname, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 3, column = 0, pady = 2, padx=5)

        Tfamily = StringVar()
        Entry(singWindow, textvariable=Tfamily, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 4, column = 0, pady = 2, padx=5)

        Tnamefather = StringVar()
        Entry(singWindow, textvariable=Tnamefather, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 5, column = 0, pady = 2, padx=5)

        Tsex = StringVar()
        Entry(singWindow, textvariable=Tsex, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 6, column = 0, pady = 2, padx=5)

        TdateD = StringVar()
        Entry(singWindow, textvariable=TdateD, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 8, column = 0, pady = 2, padx=5)

        TdateM = StringVar()
        Entry(singWindow, textvariable=TdateM, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 9, column = 0, pady = 2, padx=5)

        TdateY = StringVar()
        Entry(singWindow, textvariable=TdateY, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 10, column = 0, pady = 2, padx=5)


        TnationalCode = StringVar()
        Entry(singWindow, textvariable=TnationalCode, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 11, column = 0, pady = 2, padx=5)

        Tnumber = StringVar()
        Entry(singWindow, textvariable=Tnumber, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 12, column = 0, pady = 2, padx=5)

        Temail = StringVar()
        Entry(singWindow, textvariable=Temail, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 13, column = 0, pady = 2, padx=5)

        Tusername = StringVar()
        Entry(singWindow, textvariable=Tusername, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 14, column = 0, pady = 2, padx=5)

        Tpass = StringVar()
        Entry(singWindow, textvariable=Tpass, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 15, column = 0, pady = 2, padx=5)

        Button(singWindow, text="ثبت نام", font=("Tahoma"), bg='#2a2a3f', fg='white',command=sending).grid(row = 16, column = 0, pady = 2, padx=5)

        def goBack():
            singWindow.destroy()
            selectItem()

        Button(singWindow, text="برگشت", font=("Tahoma"), bg='#2a2a3f', fg='white', command=goBack).grid(row=17, column=0, pady=2, padx=5)




    def lessonSubmitWindow():

        def resetform():
            listtaskDeleat = [Tlesson, Tunit, Tteacher, Tpre]
            for i in listtaskDeleat:
                i.set('')

        def sending():
            lesson = Tlesson.get()
            unit = Tunit.get()
            teacher = Tteacher.get()
            pre= Tpre.get()

            listtask = [(lesson, unit,teacher, pre)]


            conn = sqlite3.connect(addrFileDB)
            c = conn.cursor()   
            c.execute('''CREATE TABLE IF NOT EXISTS Lesson(       
                                    lesson ,
                                    unit ,
                                    teacher ,
                                    pre
                                     )''')

            

        

            c.executemany('INSERT INTO Lesson VALUES(?,?,?,?)', listtask);

            conn.commit()
            conn.close()
            resetform()



        selectWindow.destroy()

        lessonWindow = Toplevel()
        lessonWindow.geometry("500x400")
        lessonWindow.title("ثبت درس")
        lessonWindow.grab_set()
        lessonWindow.configure(bg='#0d0c38')

        Label(lessonWindow, text="فرم ثبت درس", fg='white', bg='#4949b2', justify=CENTER).grid(row = 1, pady = 2)
        Label(lessonWindow, font=("Tahoma", 35), text="مجتمع فني تهران", bg='#0d0c38', fg='white', justify=CENTER).grid(row = 1, pady = 2)
        Label(lessonWindow, font=("Tahoma", 13), text="www.mftplus.com", bg='#0d0c38', fg='white', justify=CENTER).grid(row = 2, pady = 2)

        Label(lessonWindow, font=("Tahoma", 15), text="نام درس ", bg='#0d0c38', fg='white', justify=CENTER).grid(row = 3, column = 1, pady = 2, padx=5)
        Label(lessonWindow, font=("Tahoma", 15), text="تعداد واحد ", bg='#0d0c38', fg='white', justify=CENTER).grid(row = 4, column = 1, pady = 2, padx=5)
        Label(lessonWindow, font=("Tahoma", 15), text="اساتید مدرس ", bg='#0d0c38', fg='white', justify=CENTER).grid(row = 5, column = 1, pady = 2, padx=5)
        Label(lessonWindow, font=("Tahoma", 15), text="پیشنیاز ها ", bg='#0d0c38', fg='white', justify=CENTER).grid(row = 6, column = 1, pady = 2, padx=5)

        Tlesson = StringVar()
        Entry(lessonWindow, textvariable=Tlesson, font=("Tahoma"), bg='gray', justify=RIGHT).grid(row = 3, column = 0, pady = 2, padx=5)

        Tunit = StringVar()
        Entry(lessonWindow, textvariable=Tunit, font=("Tahoma"), bg='gray', justify=RIGHT).grid(row = 4, column = 0, pady = 2, padx=5)

        Tteacher = StringVar()
        Entry(lessonWindow, textvariable=Tteacher, font=("Tahoma"), bg='gray', justify=RIGHT).grid(row = 5, column = 0, pady = 2, padx=5)

        Tpre = StringVar()
        Entry(lessonWindow, textvariable=Tpre, font=("Tahoma"), bg='gray', justify=RIGHT).grid(row = 6, column = 0, pady = 2, padx=5)

        Button(lessonWindow, text="ثبت درس", font=("Tahoma"), bg='#2a2a3f', fg='white',command=sending).grid(row = 7, pady = 2, padx=5)

        def goBack():
            lessonWindow.destroy()
            selectItem()

        Button(lessonWindow, text="برگشت", font=("Tahoma"), bg='#2a2a3f', fg='white', command=goBack).grid(row=17, column=0, pady=2, padx=5)


    def editAshowWindow():

        def resetform():
            listtaskDeleat = [
                Tname, Tfamily, Tnamefather, Tsex,
                TdateD, TdateM, TdateY, TnationalCode,
                Tnumber, Temail, Tusername, Tpass
            ]
            for i in listtaskDeleat:
                i.set('')



        def openNewWindow():


            newWindow = Toplevel(root)
            newWindow.title("انتخاب از دیتابیس")
            newWindow.geometry("300x350")
            Label(newWindow, text="برای ویرایش یا حذف انتخاب کنید").pack()
            newWindow.grab_set()

            lb = Listbox(newWindow, font=(12))
            lb.pack(expand=True, fill=BOTH, padx=20)
            sb = Scrollbar(newWindow, orient=HORIZONTAL)
            sb.pack(fill=X)
            lb.configure(xscrollcommand=sb.set, justify=CENTER, font=("tahoma"))
            sb.config(command=lb.xview)

            conn = sqlite3.connect(addrFileDB)
            cur = conn.cursor()
            cur.execute("select * from students")
            gos = cur.fetchall()

            iii = 1
            for go in gos:
                lb.insert(iii, go[0] + ' ' + go[1] + ' ')
                iii += 1


            conn.close()


            def selectRecordForEdit():
                conn = sqlite3.connect(addrFileDB)
                cur = conn.cursor()
                x = str(int(lb.curselection()[0] + 1))
                cur.execute(f"select * from students WHERE rowid == {x}")
                record = cur.fetchall()
                conn.close()


                lrowid.set(f'آیدی : {x}')
                Tname.set(record[0][0])
                Tfamily.set(record[0][1])
                Tnamefather.set(record[0][2])
                Tsex.set(record[0][3])
                TdateD.set(record[0][4])
                TdateM.set(record[0][5])
                TdateY.set(record[0][6])
                TnationalCode.set(record[0][7])
                Tnumber.set(record[0][8])
                Temail.set(record[0][9])
                Tusername.set(record[0][10])
                Tpass.set(record[0][11])

                newWindow.destroy()

            Button(newWindow, text='ویرایش', font=("tahoma"), width=10, justify=CENTER,
                   command=selectRecordForEdit).pack()
            Button(newWindow, text='حذف', font=("tahoma"), width=10, justify=CENTER,
                   command=selectRecordForEdit).pack()


        def editRecord():

            nameUser = Tname.get()
            familyUser = Tfamily.get()
            fatherUser = Tnamefather.get()
            sexUser = Tsex.get()
            dateDUser = TdateD.get()
            dateMUser = TdateM.get()
            dateYUser = TdateY.get()
            nationalCodeUser = TnationalCode.get()
            numberUser = Tnumber.get()
            emailUser = Temail.get()
            usernameUser = Tusername.get()
            passUser = Tpass.get()

            conn = sqlite3.connect(addrFileDB)
            cur = conn.cursor()
            x = int(lrowid.get().split()[2])
            listdata = (nameUser, familyUser, fatherUser, sexUser, dateDUser,
                        dateMUser, dateYUser, nationalCodeUser, numberUser, emailUser,
                        usernameUser, passUser, x)

            cur.execute('''UPDATE students
                                      SET 
                                      namee =? ,
                                      family =? ,
                                      dadyname=? ,
                                      sex=?,
                                      birthd=? ,
                                      birthm=? ,
                                      birthy=?,
                                      codemeli=? ,
                                      mobile=?,
                                      email=? ,
                                      username=? ,
                                      password=?
                                      WHERE rowid == ? ;''', listdata)
            conn.commit()
            resetform()
            conn.close()

        def deleteRecord():
            conn = sqlite3.connect(addrFileDB)
            cur = conn.cursor()
            x = int(lrowid.get().split()[2])
             
            query=('DELETE FROM students WHERE rowid=={x}'.format(x=x))
            cur.execute(query)
            conn.commit()
            cur.execute("VACUUM;")
            conn.close()
            resetform()


        selectWindow.destroy()

        eAsWindow = Toplevel()
        eAsWindow.geometry("700x700")
        eAsWindow.title("نمایش و ویرایش")
        eAsWindow.grab_set()
        eAsWindow.configure(bg='#0d0c38')

        Label(eAsWindow, text="فرم نمایش و اطلاعات کاربر", fg='white', bg='#4949b2', ).grid(row=0, pady=2, padx=5)
        Label(eAsWindow, text="مجتمع فني تهران", font=("Tahoma", 35), bg='#0d0c38', fg='white', width=20,justify=CENTER).grid(row=1, pady=2, padx=5)
        Label(eAsWindow, text="www.mftplus.com", font=("Tahoma", 13), bg='#0d0c38', fg='white', width=55,justify=CENTER).grid(row=2, pady=2, padx=5)

        lrowid = StringVar()
        Label(eAsWindow, font=("tahoma"), textvariable=lrowid, width=10, justify=CENTER).grid(row=16, column=1, pady=2, padx=0)

        Label(eAsWindow, text=":نام", bg='#0d0c38', font=("Tahoma", 15), fg='white', width=0, justify=CENTER).grid(row=3, column=1, pady=2, padx=0)
        Label(eAsWindow, text=":نام خانوادگي", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0,justify=CENTER).grid(row=4, column=1, pady=2, padx=0)
        Label(eAsWindow, text=":نام پدر", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row=5, column=1, pady=2, padx=0)
        Label(eAsWindow, text=":جنسيت", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row=6, column=1, pady=2, padx=0)
        Label(eAsWindow, text=":تاريخ تولد", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0,justify=CENTER).grid(row=7, column=1, pady=2, padx=0)
        Label(eAsWindow, text=":روز -", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row=8, column=1, pady=2, padx=0)
        Label(eAsWindow, text=":ماه -", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row=9, column=1, pady=2, padx=0)
        Label(eAsWindow, text=":سال -", font=("Tahoma", 15), bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row=10, column=1, pady=2, padx=0)

        Label(eAsWindow, font=("Tahoma", 15), text=":کد ملي", bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row=11, column=1, pady=2, padx=0)
        Label(eAsWindow, font=("Tahoma", 15), text=":شماره همراه", bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row=12, column=1, pady=2, padx=0)
        Label(eAsWindow, font=("Tahoma", 15), text=":ايميل", bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row=13, column=1, pady=2, padx=0)
        Label(eAsWindow, font=("Tahoma", 15), text=":نام کاربري", bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row=14, column=1, pady=2, padx=0)
        Label(eAsWindow, font=("Tahoma", 15), text=":رمز عبور", bg='#0d0c38', fg='white', width=0, justify=CENTER).grid(row=15, column=1, pady=2, padx=0)

        Tname = StringVar()
        Entry(eAsWindow, textvariable=Tname, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row=3, column=0, pady=2, padx=5)

        Tfamily = StringVar()
        Entry(eAsWindow, textvariable=Tfamily, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row=4, column=0, pady=2, padx=5)

        Tnamefather = StringVar()
        Entry(eAsWindow, textvariable=Tnamefather, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row=5, column=0, pady=2, padx=5)

        Tsex = StringVar()
        Entry(eAsWindow, textvariable=Tsex, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row = 6, column = 0, pady = 2, padx=5)

        TdateD = StringVar()
        Entry(eAsWindow, textvariable=TdateD, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row=8, column=0, pady=2, padx=5)

        TdateM = StringVar()
        Entry(eAsWindow, textvariable=TdateM, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row=9, column=0, pady=2, padx=5)

        TdateY = StringVar()
        Entry(eAsWindow, textvariable=TdateY, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row=10, column=0, pady=2, padx=5)

        TnationalCode = StringVar()
        Entry(eAsWindow, textvariable=TnationalCode, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row=11, column=0, pady=2, padx=5)

        Tnumber = StringVar()
        Entry(eAsWindow, textvariable=Tnumber, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row=12, column=0, pady=2, padx=5)

        Temail = StringVar()
        Entry(eAsWindow, textvariable=Temail, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row=13, column=0, pady=2, padx=5)

        Tusername = StringVar()
        Entry(eAsWindow, textvariable=Tusername, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row=14, column=0, pady=2, padx=5)

        Tpass = StringVar()
        Entry(eAsWindow, textvariable=Tpass, font=("Tahoma"), bg='gray', width=30, justify=RIGHT).grid(row=15, column=0, pady=2, padx=5)

        Button(eAsWindow, text="ویرایش", font=("Tahoma"), bg='#2a2a3f', fg='white',command=openNewWindow).grid(row=16, column=0, pady=2, padx=5)

        def goBack():
            eAsWindow.destroy()
            selectItem()

        Button(eAsWindow, text="برگشت", font=("Tahoma"), bg='#2a2a3f', fg='white', command=goBack).grid(row=17, column=0, pady=2, padx=5)
        Button(eAsWindow, text="ثبت تغییرات", font=("Tahoma"), bg='#2a2a3f', fg='white', command=editRecord).grid(row=18, column=0, pady=2, padx=5)
        Button(eAsWindow, text="حذف از ديتابيس", font=("Tahoma"), bg='#2a2a3f', fg='white', command=deleteRecord).grid(row=19, column=0, pady=2, padx=5)
 



    Label(selectWindow, text="انتخاب کنید", fg='white', bg='#4949b2', padx=10, pady=10, width=10).pack(padx=10, pady=10)

    Button(selectWindow, text='ثبت نام دانشجو', padx=10, pady=10, width=25, command=singupWindow).pack(padx=10, pady=10)
    Button(selectWindow, text='ثبت درس', padx=10, pady=10, width=25, command=lessonSubmitWindow).pack(padx=10, pady=10)
    Button(selectWindow, text='مشاهده و ویرایش اطلاعات دانشجو', padx=10, pady=10, width=25, command=editAshowWindow).pack(padx=10, pady=10)






root = tk.Tk()
root.geometry("550x200")
root.title("وارد شوید")
root.configure(bg='#0d0c38')


Label1 = Label(root, font=("Tahoma", 20), text="ورود به سامانه دانشجو", bg='#0d0c38', fg='white', width=20, justify=CENTER).grid(row = 0, column = 0, pady = 2, padx=5)
Label2 = Label(root, font=("Tahoma", 15), text=":نام کاربري", bg='#0d0c38', fg='white', width=20, justify=CENTER).grid(row = 1, column = 1, pady = 2, padx=5)
Label3 = Label(root, font=("Tahoma", 15), text=":رمز عبور", bg='#0d0c38', fg='white', width=20, justify=CENTER).grid(row = 2, column = 1, pady = 2, padx=5)

Tname = StringVar()
user_name = Entry(root, textvariable=Tname, font=("Tahoma"), bg='gray', width=20, justify=RIGHT).grid(row = 1, column = 0, pady = 2, padx=5)

Tpassword = StringVar()
user_password = Entry(root, textvariable=Tpassword, font=("Tahoma"), bg='gray', width=20, justify=RIGHT).grid(row = 2, column = 0, pady = 2, padx=5)

btn1 = Button(root, text="ورود", bg='#2a2a3f', font=("Tahoma"), fg='white',width=5,pady = 5, padx=10, command=selectItem).grid(row = 3, pady = 2, padx=5)

root.mainloop()






