from datetime import datetime
from tkinter import *
import tkinter.font as TkFont
from tkinter import ttk
from tkinter import messagebox
import os
from prettytable import PrettyTable
#++++++++++++++++++++++++++++++++++++++++++++
"""creating the window, menubar and title"""
class EventApp():
    def __init__(self):
        #creating instance
        self.root=Tk()
        self.root.title("Schedule")
        self.tkMessageBox=messagebox
        self.ttk=ttk
        headerFormat = ["Start Time","EndTime","Day","Event"]
        self.mains=PrettyTable(headerFormat)
        self.main1=PrettyTable(headerFormat)
        self.main2=PrettyTable(headerFormat)
        self.main3=PrettyTable(headerFormat)
        self.main4=PrettyTable(headerFormat)
        self.main5=PrettyTable(headerFormat)
        self.main6=PrettyTable(headerFormat)
        self.main7=PrettyTable(headerFormat)
        self.customFont = TkFont.Font(family="Helvetica", size=12)       
        
        self.root.resizable(0,0)
        self.createMenu()
        self.MainTabs()
        self.TabContent()
        self.retrieveTab()
        self.deleteEvent()
        
   #menu bar
    def createMenu(self):
        self.menuBar=Menu(self.root)
        self.root.configure(menu= self.menuBar)
        self.FileMenu = Menu(self.menuBar,tearoff=0)
        self.FileMenu.add_command(label="info",command=self.show_info)
        self.FileMenu.add_command(label="Exit", command=self.show_ask)
        self.HelpMenu= Menu(self.menuBar,tearoff=0)
        self.HelpMenu.add_command(label="About", command=self._about)
        self.menuBar.add_cascade(label="File", menu=self.FileMenu)
        self.menuBar.add_cascade(label="Help", menu=self.HelpMenu)

    def show_info(self):
         messagebox.showinfo('programmer','written by maryam naderpour')
    def show_ask(self):
        res=messagebox.askquestion('q/a','are sure want to exit')
        if res == 'yes':
            self.root.destroy()
        elif res == 'no':
             messagebox.showinfo('Response', 'thanks for staying')
        else:
             messagebox.showwarning('error', 'Something went wrong!')   
    def _about(self):
        self.tkMessageBox.showinfo('About the App','This app creates a schedule for the days of the week and the time with an hour  between the times.you can see the schedule for each day of a week')
    #tabs
    def MainTabs(self):
        self.AddingEventTab=ttk.Notebook(self.root)
        self.tab1= ttk.Frame(self.AddingEventTab)
        self.tab2= ttk.Frame(self.AddingEventTab)
        self.tab3= ttk.Frame(self.AddingEventTab)
        self.AddingEventTab.add(self.tab1, text="ADD EVENT")
        self.AddingEventTab.add(self.tab2, text="SEE EVENT")
        self.AddingEventTab.add(self.tab3, text="DELETE EVENT")
        self.AddingEventTab.pack(expand=1,pady=5, fill="both")
#**********************************************************************************************************
    """Add event tab"""
    def TabContent(self):
        root1= ttk.LabelFrame(self.tab1, text="Add Event")
        root1.grid(column=0, row=0,padx=8,pady=4,sticky="W")
        Day=ttk.Label(root1, text="Please Choose The Day").grid(column=0,row=0,sticky='W')
        self.days=StringVar()
        self.times=StringVar()
        self.times2=StringVar()
        self.bgenda=StringVar()
        option1=self.ttk.Combobox(root1, width=20, textvariable=self.days,state="readonly")
        option1['values']=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        option1.grid(column=0,row=1,sticky='W')
        option1.current(0)
#**************************************************************************************************************
        ###start time
        Time=ttk.Label(root1, text="Please Choose a Time").grid(column=0,row=2,sticky='W')
        startTime=ttk.Label(root1, text="Start Time").grid(column=0,row=3,sticky='W')
        EndTime=ttk.Label(root1, text="End Time").grid(column=2,row=3)
        Timedrop=ttk.Combobox(root1, width=20, textvariable=self.times,state="readonly")
        Timedrop['values']=("12:00am","1:00am","2:00am","3:00am","4:00am","5:00am","6:00am","7:00am","8:00am","9:00am",
                            "10:00am","11:00am","12:00pm","1:00pm","2:00pm","3:00pm","4:00pm","5:00pm","6:00pm","7:00pm","8:00pm","9:00pm","10:00pm","11:00pm")
        Timedrop.grid(column=0,row=4,sticky='W')
        Timedrop.current(0)
        
        TimeEndDrop=ttk.Combobox(root1,width=20, textvariable=self.times2,state="readonly")
        TimeEndDrop['values']=("12:00am","1:00am","2:00am","3:00am","4:00am","5:00am","6:00am","7:00am","8:00am","9:00am",
                           "10:00am","11:00am","12:00pm","1:00pm","2:00pm","3:00pm","4:00pm","5:00pm","6:00pm","7:00pm","8:00pm","9:00pm","10:00pm","11:00pm")
        TimeEndDrop.grid(column=2,row=4)
        TimeEndDrop.current(0)
        ttk.Label(root1,text="Please enter a short discription for your plan").grid(column=0,row=6,pady=10,sticky='W')
        ttk.Label(root1,text="Examples are class, meeting, work, studying").grid(column=0,row=7,sticky='W')
        self.Agenda=ttk.Entry(root1,width=50,textvariable=self.bgenda)
        self.Agenda.grid(column=0,row=8,pady=5,sticky='W')
        showbiz2=Text(root1,width=75,height=15)
        showbiz2.grid(column=0,row=9)
        def viewPrint():
            showbiz2.delete(1.0,END)
            messagebox.showinfo("View","The View button shows all the Events")
            if os.stat("text.txt").st_size==0:
                showbiz2.insert(INSERT,"No Event Found")
            else:
                with open ("text.txt","r")as file_new:
                    contents=file_new.read()
                    showbiz2.insert(INSERT,contents)
                    showbiz2.see(INSERT)
        def clean():
            showbiz2.delete(1.0,END)
            messagebox.showinfo("Clear","note that the clear button only cleans the display field but not the schedule. Please use 'DELETE EVENT' if you want to delete event")
            
                
        creat=Button(self.tab1,text="CREATE  ",bg='#4d79ff',fg='white',font=("Helvetica",14),command=self.add_task).grid(column=0,ipadx=62,pady=5,row=10,sticky="W")
        view=Button(self.tab1, text="All Event",bg='#ff5050',fg='white',font=("Helvetica",14),command=viewPrint).grid(column=0,ipadx=70,row=11,pady=5,sticky="W")
        clear=Button(self.tab1,text="CLEAR   ",bg='#ffc34d',fg='white',font=("Helvetica",14),command=clean).grid(column=0,ipadx=66,row=12,pady=5,sticky="W")
    def add_task(self):
        def allEvent():
            messagebox.showinfo("Created","Event Created")
            self.Agenda.delete(0,'end')
            self.mains.add_row([self.times.get(),self.times2.get(),self.days.get(),self.bgenda.get()])
            file_new=open("text.txt","a")
            file_new.write(str("Created: " + datetime.now().strftime(' %Y-%m-%d %H:%M:%S'))+'\n')
            if self.days.get()=="Monday":
                file_new.write(str(self.main1)+'\n')
            elif self.days.get()=="Tuesday":
                file_new.write(str(self.main2)+'\n')
            elif self.days.get()=="Wednesday":
                file_new.write(str(self.main3)+'\n')
            elif self.days.get()=="Thursday":
                file_new.write(str(self.main4)+'\n')
            elif self.days.get()=="Friday":
                file_new.write(str(self.main5)+'\n')
            elif self.days.get()=="Saturday":
                file_new.write(str(self.main6)+'\n')
                
            elif self.days.get()=="Sunday":
                file_new.write(str(self.main7))
            file_new.close()
        def monday():
            self.main1.add_row([self.times.get(),self.times2.get(),self.days.get(),self.bgenda.get()])
            file_new=open("monday.txt","w")
            file_new.write(str(self.main1))
            file_new.close()
            allEvent()
        def tuesday():
            self.main2.add_row([self.times.get(),self.times2.get(),self.days.get(),self.bgenda.get()])
            file_new=open("tuesday.txt","w")
            file_new.write(str(self.main2))
            file_new.close()
            allEvent()
        def wednesday():
            self.main3.add_row([self.times.get(),self.times2.get(),self.days.get(),self.bgenda.get()])
            file_new=open("wednesday.txt","w")
            file_new.write(str(self.main3))
            file_new.close()
            allEvent()
        def thursday():
            self.main4.add_row([self.times.get(),self.times2.get(),self.days.get(),self.bgenda.get()])
            file_new=open("thursday.txt","w")
            file_new.write(str(self.main4))
            file_new.close()
            allEvent()
        def friday():
            self.main5.add_row([self.times.get(),self.times2.get(),self.days.get(),self.bgenda.get()])
            file_new=open("friday.txt","w")
            file_new.write(str(self.main5))
            file_new.close()
            allEvent()
        def saturday():
            self.main6.add_row([self.times.get(),self.times2.get(),self.days.get(),self.bgenda.get()])
            file_new=open("saturday.txt","w")
            file_new.write(str(self.main6))
            file_new.close()
            allEvent()
        def sunday():
            self.main7.add_row([self.times.get(),self.times2.get(),self.days.get(),self.bgenda.get()])
            file_new=open("sunday.txt","w")
            file_new.write(str(self.main7))
            file_new.close()
            allEvent()
        if self.days.get()=="Monday":
            monday()
        elif self.days.get()=="Tuesday":
            tuesday()
        elif self.days.get()=="Wednesday":
            wednesday()
        elif self.days.get()=="Thursday":
            thursday()
        elif self.days.get()=="Friday":
            friday()
        elif self.days.get()=="Saturday":
            saturday()
        elif self.days.get()=="Sunday":
            sunday()
    
    def retrieveTab(self):
        root2=ttk.LabelFrame(self.tab2, text="Retrieve")
        greetings=ttk.Label(self.tab2,text="Hello there!Please click on the day you want to see",font=self.customFont)
        greetings.grid(column=0,row=0,pady=5)
        
        def printAllEvent():
            showbiz.delete(1.0,END)
            file_new=open("text.txt",'a')
            if os.stat("text.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, No Event Found")
            else:
                with open ("text.txt","a")as file_new:
                    file_new=open("text.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
        def printMonday():
            showbiz.delete(1.0,END)
            file_new=open("monday.txt","a")
            if os.stat("monday.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, Monday is Empty")
            else:
                with open ("monday.txt","a")as file_new:
                    file_new=open("monday.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
        def printTuesday():
            showbiz.delete(1.0,END)
            file_new=open("tuesday.txt","a")
            if os.stat("tuesday.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, Tuesday is Empty")
            else:
                with open ("tuesday.txt","a")as file_new:
                    file_new=open("tuesday.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
        def printWednesday():
            showbiz.delete(1.0,END)
            file_new=open("wednesday.txt",'a')
            if os.stat("wednesday.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, Wednesday is Empty")
            else:
                with open ("wednesday.txt","a")as file_new:
                    file_new=open("wednesday.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
        def printThursday():
            showbiz.delete(1.0,END)
            file_new=open("thursday.txt",'a')
            if os.stat("thursday.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, Thursday is Empty")
            else:
                with open ("thursday.txt","a")as file_new:
                    file_new=open("thursday.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
        def printFriday():
            showbiz.delete(1.0,END)
            file_new=open("friday.txt",'a')
            if os.stat("friday.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, Friday is Empty")
            else:
                with open ("friday.txt","a")as file_new:
                    file_new=open("friday.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
        def printSaturday():
            showbiz.delete(1.0,END)
            file_new=open("saturday.txt",'a')
            if os.stat("saturday.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, Saturday is Empty")
            else:
                with open ("saturday.txt","a")as file_new:
                    file_new=open("saturday.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
        def printSunday():
            showbiz.delete(1.0,END)
            file_new=open("sunday.txt",'a')
            if os.stat("sunday.txt").st_size == 0:
                showbiz.insert(INSERT,"Sorry, Sunday is Empty")
            else:
                with open ("sunday.txt","a")as file_new:
                    file_new=open("sunday.txt")
                    contents=file_new.read()
                    showbiz.insert(INSERT,contents)
                    showbiz.see(INSERT)
       
        monday=Button(self.tab2, text="Monday",bg="#4d79ff",fg="white",font=("Helvetica",14),command=printMonday).grid(column=0,row=2,ipadx=18,pady=5)
        tuesday=Button(self.tab2, text="Tuesday",bg="#ff5050",fg="white",font=("Helvetica",14),command=printTuesday).grid(column=1,row=2,ipadx=11,pady=5)
        wednesday=Button(self.tab2, text="Wednesday",bg="#ffc34d",fg="white",font=("Helvetica",14),command=printWednesday).grid(column=0,row=3,pady=5)
        thursday=Button(self.tab2, text="Thursday",bg="#4d79ff",fg="white",font=("Helvetica",14),command=printThursday).grid(column=1,row=3,ipadx=10,pady=5)
        friday=Button(self.tab2, text="Friday",bg="#009900",fg="white",font=("Helvetica",14),command=printFriday).grid(column=0,row=4,pady=5,ipadx=24)
        saturday=Button(self.tab2, text="Saturday",bg="#ff5050",fg="white",font=("Helvetica",14),command=printSaturday).grid(column=1,row=4,ipadx=15,pady=5)
        sunday=Button(self.tab2, text="Sunday",bg="#ffc34d",fg="white",font=("Helvetica",14),command=printSunday).grid(column=0,row=5,pady=5,ipadx=20)
        showbiz=Text(self.tab2,width=97,height=22)
        showbiz.grid(columnspan=3)
        allEvent=Button(self.tab2, text="All Events",bg="orange",fg="white",font=("Helvetica",14),command=printAllEvent).grid(column=1,row=5,ipadx=8,pady=5)    
#***********************************************************************************************************************
    def deleteEvent(self):
        def deleteMonday():
            result=messagebox.askyesno("delete","Are you sure you want to delete Monday Event ?")
            if result is True:
                file_new=open("monday.txt","w").close()
                messagebox.showinfo("Deleted","Monday Event(s) Deleted")
        def deleteTuesday():
            result=messagebox.askyesno("delete","Are you sure you want to delete Tuesday Event ?")
            if result is True:
                file_new=open("tuesday.txt","w").close()
                messagebox.showinfo("Deleted","Tuesday Event(s) Deleted")
            
        def deleteWednesday():
            result=messagebox.askyesno("delete","Are you sure you want to delete Wednesday Event ?")
            if result is True:
                file_new=open("wednesday.txt","w").close()
                messagebox.showinfo("Deleted","Wednesday Event(s) Deleted")
        def deleteThursday():
            result=messagebox.askyesno("delete","Are you sure you want to delete thursday Event ?")
            if result is True:
                file_new=open("thursday.txt","w").close()
                messagebox.showinfo("Deleted","Thursday Event(s) Deleted")
        def deleteFriday():
            result=messagebox.askyesno("delete","Are you sure you want to delete Friday Event ?")
            if result is True:
                file_new=open("friday.txt","w").close()
                messagebox.showinfo("Deleted","Friday Event(s) Deleted")
        def deleteSaturday():
            result=messagebox.askyesno("delete","Are you sure you want to delete Saturday Event ?")
            if result is True:
                file_new=open("saturday.txt","w").close()
                messagebox.showinfo("Deleted","Saturday Event(s) Deleted")
        def deleteSunday():
            result=messagebox.askyesno("delete","Are you sure you want to delete Sunday Event ?")
            if result is True:
                file_new=open("sunday.txt","w").close()
                messagebox.showinfo("Deleted","Sunday Event(s) Deleted")
        def deleteAllEvent():
            result=messagebox.askyesno("delete","Are you sure you want to delete Monday Event ?")
            result=messagebox.askyesno("delete","Are you sure you want to delete All Events ?")
            files = ["text.txt", "monday.txt", "tuesday.txt", "wednesday.txt","thursday.txt","friday.txt" ,"saturday.txt" ,"sunday.txt"]
            if result is True:
                file_new=open("text.txt","w").close()
                file_new=open("monday.txt","w").close()
                file_new=open("tuesday.txt","w").close()
                file_new=open("wednesday.txt","w").close()
                file_new=open("thursday.txt","w").close()
                file_new=open("friday.txt","w").close()
                file_new=open("saturday.txt","w").close()
                file_new=open("sunday.txt","w").close()
                for file_name in files:
                    file_new=open(file_name,"w").close()
                messagebox.showinfo("Deleted","All Events Deleted")

        monday=Button(self.tab3, text="Delete Monday",bg='#4d79ff',fg='white',font=("Helvetica",14),command=deleteMonday).pack(fill=X,padx=100,ipady=10,pady=10)
        tuesday=Button(self.tab3, text="Delete Tuesday",bg='#ff5050',fg='white',font=("Helvetica",14),command=deleteTuesday).pack(fill=X,padx=100,ipady=10,pady=10)
        wednesday=Button(self.tab3, text="Delete Wednesday",bg='#ffc34d',fg='white',font=("Helvetica",14),command=deleteWednesday).pack(fill=X,padx=100,ipady=10,pady=10)
        thursday=Button(self.tab3, text="Delete Thursday",bg='#4d79ff',fg='white',font=("Helvetica",14),command=deleteThursday).pack(fill=X,padx=100,ipady=10,pady=10)
        friday=Button(self.tab3, text="Delete Friday",bg='#009900',fg='white',font=("Helvetica",14),command=deleteFriday).pack(fill=X,padx=100,ipady=10,pady=10)
        saturday=Button(self.tab3, text="Delete Saturday",bg='#ff5050',fg='white',font=("Helvetica",14),command=deleteSaturday).pack(fill=X,padx=100,ipady=10,pady=10)
        sunday=Button(self.tab3, text="Delete Sunday",bg='#ffc34d',fg='white',font=("Helvetica",14),command=deleteSunday).pack(fill=X,padx=100,ipady=10,pady=10)
        allEvent=Button(self.tab3, text="Delete all Events",bg='orange',fg='white',font=("Helvetica",14),command=deleteAllEvent).pack(fill=X,padx=100,ipady=10,pady=10)
app= EventApp()
app.root.mainloop()
