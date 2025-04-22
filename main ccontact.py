from tkinter import*
import tkinter.messagebox
import countact
#phonebook2


class phone:

    def __init__(self,root):
        self.root=root
        self.root.title("phone book")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="steel blue")
        

        Firstname=StringVar()
        Lastname=StringVar()
        Tel=StringVar()
        Address=StringVar()
     #=============================Function==============================
        def iExit():
            iExit= tkinter.messagebox.askyesno("phone book","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def cleardata():
            self.txtFn.delete(0,END)
            self.txtLn.delete(0,END)
            self.txtTel.delete(0,END)
            self.txtAdr.delete(0,END)
            
        
        def addcontact():
            if (len(Firstname.get())!=0):
                  phonebook1.adddata(Firstname.get() ,Lastname.get(), Tel.get(), Address.get())   
                  Tellist.delete(0,END)
                  Tellist.insert(END,(Firstname.get() ,Lastname.get(), Tel.get(), Address.get()))


        def Displaycontact():
            Tellist.delete(0,END)
            for row in phonebook1.viewdata():
                Tellist.insert(END,row,str(""))

        def Phonecontact(event):
            global ph
            searchPh=Tellist.curselection()[0]
            ph=Tellist.get(searchPh)
            

            self.txtFn.delete(0,END)
            self.txtFn.insert(END,ph[1])
            self.txtLn.delete(0,END)
            self.txtLn.insert(END,ph[2])
            self.txtTel.delete(0,END)
            self.txtTel.insert(END,ph[3])
            self.txtAdr.delete(0,END)
            self.txtAdr.insert(END,ph[4])            
            
        def delcontact():
              if (len(Firstname.get())!=0):
                  phonebook1.deldata(ph[0])
                  cleardata()
                  Displaycontact()

        def searchcontact():
             Tellist.delete(0,END)
             for row in phonebook1.searchdata(Firstname.get() ,Lastname.get(),Tel.get(), Address.get()):
                     Tellist.insert(END,row,str(""))
                                                 

        def updatecontact ():             
             if (len(Firstname.get())!=0):
                  phonebook1.deldata(ph[0])
             if (len(Firstname.get())!=0):
                phonebook1.adddata(Firstname.get() ,Lastname.get(), Tel.get(), Address.get())
                Tellist.delete(0,END)
                Tellist. insert (END,(Firstname.get() , Lastname.get(),Tel.get(), Address.get()))          
                
           #=============================Frames==============================
        MainFrame=Frame(self.root,bg="steel blue")
        MainFrame.grid()

        TitFrame=Frame(MainFrame,bd=2,padx=54,pady=8, bg="white smoke" ,relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit=Label(TitFrame,font=('times new roman',40,'bold'),text='MY PHONE BOOK',bg="white smoke" )
        self.lblTit.grid()

        ButtonFrame=Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg="white smoke" ,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,relief=RIDGE ,bg="white smoke" )
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,relief=RIDGE,bg="white smoke" ,
                                 font=('times new roman',25,'bold'),text="Info Contact\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=1,width=450,height=300,padx=30,pady=3,relief=RIDGE,bg="white smoke" ,
                                 font=('times new roman',25,'bold'),text="Contact Details\n") 
        DataFrameRIGHT.pack(side=RIGHT)
        #=============================Labels and Entry widget========================    
        self.lblFn=Label(DataFrameLEFT,font=('times new roman',20,'bold'),text='Firstname',padx=2,pady=2,bg="white smoke" )
        self.lblFn.grid(row=0,column=0,sticky=W)
        self.txtFn=Entry(DataFrameLEFT,font=('times new roman',20,'bold'),textvariable=Firstname,width=40)
        self.txtFn.grid(row=0,column=1)

        self.lblLn=Label(DataFrameLEFT,font=('times new roman',20,'bold'),text='Lastname',padx=2,pady=2,bg="white smoke" )
        self.lblLn.grid(row=1,column=0,sticky=W)
        self.txtLn=Entry(DataFrameLEFT,font=('times new roman',20,'bold'),textvariable=Lastname,width=40)
        self.txtLn.grid(row=1,column=1)

        self.lblTel=Label(DataFrameLEFT,font=('times new roman',20,'bold'),text='Tel',padx=2,pady=2,bg="white smoke" )
        self.lblTel.grid(row=2,column=0,sticky=W)
        self.txtTel=Entry(DataFrameLEFT,font=('times new roman',20,'bold'),textvariable=Tel,width=40)
        self.txtTel.grid(row=2,column=1)

        self.lblAdr=Label(DataFrameLEFT,font=('times new roman',20,'bold'),text='Address',padx=2,pady=2,bg="white smoke" )
        self.lblAdr.grid(row=3,column=0,sticky=W)
        self.txtAdr=Entry(DataFrameLEFT,font=('times new roman',20,'bold'),textvariable=Address,width=40)
        self.txtAdr.grid(row=3,column=1)
        #=============================ListBox & ScrolBar Widget==========================
        scrollbar=Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        Tellist=Listbox(DataFrameRIGHT,width=40,height=16,font=('times new roman',12,'bold'),yscrollcommand=scrollbar.set)
        Tellist.bind('<<ListboxSelect>>',Phonecontact)
        Tellist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=Tellist.yview)
       #=============================Buttom widget==========================
        self.btnAdd=Button(ButtonFrame,text='Add',font=('times new roman',22,'bold'),height=1,width=10,bd=4,command=addcontact)
        self.btnAdd.grid(row=0,column=0)

        self.btnDisplay=Button(ButtonFrame,text='Display',font=('times new roman',22,'bold'),height=1,width=10,bd=4,command=Displaycontact )
        self.btnDisplay.grid(row=0,column=1)

        self.btnClear=Button(ButtonFrame,text='Clear',font=('times new roman',22,'bold'),height=1,width=10,bd=4,command=cleardata)
        self.btnClear.grid(row=0,column=2)  

        self.btnDel=Button(ButtonFrame,text='Delete',font=('times new roman',22,'bold'),height=1,width=10,bd=4,command=delcontact)
        self.btnDel.grid(row=0,column=3)

        self.btnSearch=Button(ButtonFrame,text='Search',font=('times new roman',22,'bold'),height=1,width=10,bd=4,command=searchcontact )
        self.btnSearch.grid(row=0,column=4)

        self.btnupdate=Button(ButtonFrame,text='Update',font=('times new roman',22,'bold'),height=1,width=10,bd=4,command=updatecontact)
        self.btnupdate.grid(row=0,column=5)

        self.btnExit=Button(ButtonFrame,text='Exit',font=('times new roman',22,'bold'),height=1,width=10,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=6)


if __name__=="__main__":
    root=Tk()
    application=phone(root)
    root.mainloop()



        


