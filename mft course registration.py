try: # python 3
    import tkinter as tk
    from tkinter import font as tkfont
    from tkinter import messagebox
    from PIL import Image, ImageTk
    from tkinter import ttk
    import re
    import sqlite3
except ImportError:# python 2
    import Tkinter as tk
    import tkFont as tkfont
    from tkinter import messagebox
    from PIL import Image, ImageTk
    from Tkinter import ttk
    import re
    import sqlite3

#global variables-----------------------------------
logkey_var = "" #code_melli need for login
menu_var = False #menu_var if you click it in menubar set true
rowname = [] #strings for user information that decrease access to database
rowict = [] #strings for user information
rowweb = [] #strings for user information
rownet1 = [] #strings for user information
rownet2 = [] #strings for user information
rowpro1 = [] #strings for user information
rowpro2 = [] #strings for user information
back = ['StartPage','StartPage']  #strings for menu btn
bk = ['StartPage','StartPage','StartPage','StartPage'] #strings for back btn
#Functions that change the global variables---------
def loginvar(code): #change the logkey_var
    global logkey_var
    logkey_var = code
    return logkey_var
#--------------------------------------------------
def logoutvar(): #change the logkey_var
    global logkey_var
    logkey_var = ""
    return logkey_var
#--------------------------------------------------
def menu_btn(boolean): #change the menu_var
    global menu_var
    menu_var = boolean
    return menu_var
#--------------------------------------------------
def namelist(alist): #change the rowname
    global rowname
    rowname = alist
    if rowname==None:
        rowname = []
    return rowname
#--------------------------------------------------
def ictlist(alist): #change the rowict
    global rowict
    rowict = alist
    if rowict==None:
        rowict = []
    return rowict
#--------------------------------------------------
def weblist(alist): #change the rowweb
    global rowweb
    rowweb = alist
    if rowweb==None:
        rowweb = []
    return rowweb
#--------------------------------------------------
def net1list(alist): #change the rownet1
    global rownet1
    rownet1 = alist
    if rownet1==None:
        rownet1 = []
    return rownet1
#--------------------------------------------------
def net2list(alist): #change the rownet2
    global rownet2
    rownet2 = alist
    if rownet2==None:
        rownet2 = []
    return rownet2
#--------------------------------------------------
def pro1list(alist): #change the rowpro1
    global rowpro1
    rowpro1 = alist
    if rowpro1==None:
        rowpro1 = []
    return rowpro1
#--------------------------------------------------
def pro2list(alist): #change the rowpro2
    global rowpro2
    rowpro2 = alist
    if rowpro2==None:
        rowpro2 = []
    return rowpro2
#--------------------------------------------------
def back_btn(page): #change the back
    global back
    back[0] = back[1]
    back[1] = page
    return back
#--------------------------------------------------
def back_crs(page): #change the bk
    global bk
    bk[0] = bk[1]
    bk[1] = bk[2]
    bk[2] = bk[3]
    bk[3] = page
    return bk
#Class parent: SampleApp -------------------------------------------------------------------------
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("600x780")
        self.title("سامانه آموزش مجتمع فنی تهران")
        self.resizable(False, False)
        #Fonts------------------------------------------------------------------------------------
        self.Blblfont = ("B nazanin",15,"bold")
        self.lblfont = ("B nazanin",15)
        self.btnfont = ("B nazanin",10,"bold")
        self.logfont = ("B nazanin",13)
        self.menufont = ("B nazanin",11)
        self.title_font = ("B nazanin",18,"bold","italic")

        self.english_font  = ("Times New Roman",14)
        self.english_lblfont  = ("Times New Roman",11)
        #Variables---------------------------------------------------------------------------------
        #Global Variables------------------
        global logkey_var
        self.ckbtnVR = tk.IntVar()
        #Variables for SigninPage----------
        self.signin_code = tk.StringVar()
        self.signin_psw = tk.StringVar()
        #Variables for SignupPage----------
        self.name_var = tk.StringVar()
        self.lname_var = tk.StringVar()
        self.fname_var = tk.StringVar()
        self.code_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.pw_var = tk.StringVar()
        self.pwagain_var = tk.StringVar()
        #Variables for Error text----------
        self.err_var = tk.StringVar()
        self.Err_lbl_email_txt = tk.StringVar()
        #Menu_btn_pictures--------------------------------------------------------------------------
        self.imgmft = Image.open("logo_mft_tra.png")
        self.imgmft = self.imgmft.resize((72,56))
        self.tkimgmft =  ImageTk.PhotoImage(self.imgmft)

        self.imgmenu = Image.open("logo_menu_tra.png")
        self.imgmenu = self.imgmenu.resize((40,40))
        self.tkimgmenu =  ImageTk.PhotoImage(self.imgmenu)

        self.imgsignin = Image.open("signin_logo_tra.png")
        self.imgsignin = self.imgsignin.resize((40,40))
        self.tkimgsignin =  ImageTk.PhotoImage(self.imgsignin)

        self.imgsignup = Image.open("logo_signup_tra.png")
        self.imgsignup = self.imgsignup.resize((40,40))
        self.tkimgsignup =  ImageTk.PhotoImage(self.imgsignup)

        #Header_pictures--------------------------------------------------------------------------
        self.header1 = Image.open("header1.jpeg")
        self.header1 = self.header1.resize((600,150))
        self.tkheader1 =  ImageTk.PhotoImage(self.header1)

        self.header2 = Image.open("header2.jpeg")
        self.header2 = self.header2.resize((600,150))
        self.tkheader2 =  ImageTk.PhotoImage(self.header2)

        self.header3 = Image.open("header3.jpeg")
        self.header3 = self.header3.resize((600,150))
        self.tkheader3 =  ImageTk.PhotoImage(self.header3)

        self.header4 = Image.open("header4.jpeg")
        self.header4 = self.header4.resize((600,150))
        self.tkheader4 =  ImageTk.PhotoImage(self.header4)

        self.header5 = Image.open("header5.jpeg")
        self.header5 = self.header5.resize((600,150))
        self.tkheader5 =  ImageTk.PhotoImage(self.header5)
        #signup_pictures-------------------------------------------------------------------------
        self.show = Image.open("logo_show.png")
        self.show = self.show.resize((25,25))
        self.tkshow =  ImageTk.PhotoImage(self.show)

        self.hide = Image.open("logo_hide.png")
        self.hide = self.hide.resize((25,25))
        self.tkhide =  ImageTk.PhotoImage(self.hide)
        #refresh_picture-------------------------------------------------------------------------
        self.imgrefresh = Image.open("refresh_logo.png")
        self.imgrefresh = self.imgrefresh.resize((40,40))
        self.tkimgrefresh =  ImageTk.PhotoImage(self.imgrefresh)
        #txt of footer--------------------------------------------------------------------------
        self.footer = """،آدرس دفتر مرکزی: سعادت آباد، بالاتر از ميدان كاج، خيابان دوم (شهيد عبقری) بلوار بهزاد شمالی، نبش باغستان يكم
| شماره دوازده | مشاوره آموزشی: ۰۲۱-۲۷۲۹| تلفن: ۰۲۱۲۲۰۹۰۰۰۱ | سامانه پیام کوتاه: ۱۰۰۰۲۷۲۹
 info@mftplus.com:پست الکترونیک"""
        #database_users-------------------------------------------------------------------------
        self.mftdb = sqlite3.connect('mft01.db')
        cursor = self.mftdb.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT(Melli_code text, Name text, Last_Name text,
        Father_Name text, Phone text, Email text, Password text,
        ICDL1 text, Algorithms text, Network text, Web text)''')
        try:
            cursor.execute('''SELECT * from STUDENT''')
            row = cursor.fetchall()
            #add_users if database is empty
            if row == []:
                cursor.execute('''CREATE TABLE IF NOT EXISTS NET1(Melli_code text,winlo text, server1 text,
                server2 text, server3 text, exchange text, vmware text, vdi text)''')
                cursor.execute('''CREATE TABLE IF NOT EXISTS NET2(Melli_code text,ccna text, ccna_security text,ccnp text,
                ceh text, lpic1 text, lpic2 text)''')
                cursor.execute('''CREATE TABLE IF NOT EXISTS pro1(Melli_code text,python text,ml text,deep_learning text,
                Image_proccessing text,c_plusplus text,c_sharp text,sql text,
                asp_net text,javascriPt text, block_chain text)''')
                cursor.execute('''CREATE TABLE IF NOT EXISTS pro2(Melli_code text,java text,java_se text,java_ee text,android text,
                android_with_kotlin text,android_with_java text,ios text)''')
                cursor.execute('''CREATE TABLE IF NOT EXISTS ict(Melli_code text,ICDL2 text,Excel_Expert text,Power_BI text)''')
                cursor.execute('''CREATE TABLE IF NOT EXISTS web(Melli_code text,web2 text,web3 text,React text,Node_JS text,
                PHP text,Django text,Wordpress text, Woocommerce text, UI_UX text,Seo text)''')

                record = [('0123456789', "ادمين","ادمين","ادمين","","admin@gmail.com",'123456789Admin','notregister','notregister','notregister','notregister'),
                          #-----------------------------------------------------------------------------------------------------------------------------------------
                          ('1234567101', "افسانه","زارع","علي","09121234499","afsaneh@gmail.com",'Mft1400sep','register','notregister','notregister','notregister'),
                          #-----------------------------------------------------------------------------------------------------------------------------------------
                          ('1234567102',"نيما","رهنما","عليرضا","09121234500","nima@gmail.com",'Mft1400sep','pass','notregister','notregister','notregister'),
                          ('1234567103',"فرهود","جمادي","احمد","09121234501","farhood@gmail.com",'Mft1400sep','pass','notregister','notregister','register'),
                          ('1234567104',"فريناز","چاوشي","پويا","09121234502","farinaz@gmail.com",'Mft1400sep','pass','notregister','register','notregister'),
                          ('1234567105',"فرهاد","باطني","پوريا","09121234503","farhad@gmail.com",'Mft1400sep','pass','notregister','register','register'),
                          ('1234567106',"سجاد","اميري","سياوش","09121234504","sajad@gmail.com",'Mft1400sep','pass','notregister','notregister','pass'),
                          ('1234567107',"ديبا","ذاکري","مراد","09121234505","diba@gmail.com",'Mft1400sep','pass','notregister','pass','notregister'),
                          ('1234567108',"آرمين","کمالي","کاوه","09121234506","armin@gmail.com",'Mft1400sep','pass','notregister','register','pass'),
                          ('1234567109',"علي","فرجي","محمد","09121234507","ali@gmail.com",'Mft1400sep','pass','notregister','pass','register'),
                          ('1234567110',"ندا","حميدي","حسين","09121234508","neda@gmail.com",'Mft1400sep','pass','notregister','pass','pass'),
                          #-----------------------------------------------------------------------------------------------------------------------------------------
                          ('1234567111',"جواد","کاظمي","احمد","09121234509","jaka@gmail.com",'Mft1400sep','pass','register','notregister','notregister'),
                          ('1234567112',"رضا","مجيدي","عباس","09121234510","rez_ds@gmail.com",'Mft1400sep','pass','register','notregister','register'),
                          ('1234567113',"الهه","کمالي","علي","09121234511","elah@gmail.com",'Mft1400sep','pass','register','register','notregister'),
                          ('1234567114',"مهتاب","حسيني","عبداله","09121234512","mahtaab@gmail.com",'Mft1400sep','pass','register','register','register'),
                          ('1234567115',"مريم","ناصري","رضا","09121234513","mary@gmail.com",'Mft1400sep','pass','register','notregister','pass'),
                          ('1234567116',"احمد","بابايي","جليل","09121234514","ahhh@gmail.com",'Mft1400sep','pass','register','pass','notregister'),
                          ('1234567117',"سينا","رضايي","قاسم","09121234515","sina@gmail.com",'Mft1400sep','pass','register','register','pass'),
                          ('1234567118',"مجيد","عباسي","رحمان","09121234516","majjjid@gmail.com",'Mft1400sep','pass','register','pass','register'),
                          ('1234567119',"سعيد","يوسفي","کمال","09121234517","sa_yoo@gmail.com",'Mft1400sep','pass','register','pass','pass'),
                          #-----------------------------------------------------------------------------------------------------------------------------------------
                          ('1234567120',"اکرم","رسولي","ناصر","09121234518","akram@gmail.com",'Mft1400sep','pass','pass','notregister','notregister'),
                          ('1234567121',"محبوبه","وحيدي","ابوالفضل","09121234519","mahboob@gmail.com",'Mft1400sep','pass','pass','notregister','register'),
                          ('1234567122',"منصوره","سعيدي","اکبر","09121234520","mansooreh@gmail.com",'Mft1400sep','pass','pass','register','notregister'),
                          ('1234567123',"سهيلا","اسعداللهي","سمد","09121234521","soh@gmail.com",'Mft1400sep','pass','pass','register','register'),
                          ('1234567124',"شهلا","سليماني","اصغر","09121234522","shahla@gmail.com",'Mft1400sep','pass','pass','notregister','pass'),
                          ('1234567125',"شيوا","محمدي","مسعود","09121234523","shiva@gmail.com",'Mft1400sep','pass','pass','pass','notregister'),
                          ('1234567126',"مليکا","بابايي","سپهر","09121234524","melika_b@gmail.com",'Mft1400sep','pass','pass','register','pass'),
                          ('1234567127',"فاطمه","صالحي","امير","09121234525","fati_sa@gmail.com",'Mft1400sep','pass','pass','pass','register'),
                          ('1234567128',"شبنم","عراقي","محمود","09121234526","shabnam_ar@gmail.com",'Mft1400sep','pass','pass','pass','pass'),
                          ('1234567129',"بهادر","عرفانيان","محمدرضا","09121234527","bah_er@gmail.com",'Mft1400sep','pass','pass','pass','pass'),
                          #-----------------------------------------------------------------------------------------------------------------------------------------
                        ]

                #add courses to new tables for sample users
                cursor.executemany('''INSERT INTO STUDENT values(?,?,?,?,?,?,?,?,?,?,?)''',record)

                net1_r = [('1234567107','pass','pass','pass','pass','pass','register','notregister'),
                          ('1234567109','pass','pass','pass','register','notregister','notregister','notregister')]
                cursor.executemany('''INSERT INTO NET1 values(?,?,?,?,?,?,?,?)''',net1_r)

                net2_r = [('1234567110','pass','register','notregister','notregister','pass','notregister'),
                          ('1234567116','pass','notregister','notregister','notregister','pass','notregister')]
                cursor.executemany('''INSERT INTO NET2 values(?,?,?,?,?,?,?)''',net2_r)

                pro1_r = [('1234567125','pass','pass','notregister','notregister','notregister','pass','register','notregister','pass','register'),
                          ('1234567127','notregister','notregister','notregister','notregister','pass','notregister','notregister','notregister','pass','pass'),
                          ('1234567128','pass','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister')]
                cursor.executemany('''INSERT INTO pro1 values(?,?,?,?,?,?,?,?,?,?,?)''',pro1_r)

                pro2_r = [('1234567121','pass','pass','pass','register','notregister','notregister','pass'),
                          ('1234567122','register','pass','pass','notregister','notregister','notregister','notregister')]
                cursor.executemany('''INSERT INTO pro2 values(?,?,?,?,?,?,?,?)''',pro2_r)

                ictrow = [('1234567109','pass','register','notregister'),
                          ('1234567110','pass','pass','register')]
                cursor.executemany('''INSERT INTO ict values(?,?,?,?)''',ictrow)

                webrow = [('1234567106','pass','pass','register','notregister','notregister','notregister','pass','register','notregister','notregister'),
                          ('1234567108','register','notregister','notregister','notregister','notregister','register','pass','pass','notregister','pass')]
                cursor.executemany('''INSERT INTO web values(?,?,?,?,?,?,?,?,?,?,?)''',webrow)

                self.mftdb.commit()
            else:
                pass
        except:
            pass
        #----container------------------------------------------------------------
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, HomePage, SigninPage, SignupPage, User,
                  Forgetpsw, Change_User, SET_CRS, ict, web, net, programming1,
                  programming2, Admin, Menu_Admin, Menu_login, Menu_logout):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        #----Open app------------------------------------------------------------
        self.show_frame("StartPage")
    #*--------------------------------------------------------------------------------------------------------------------------------
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        global back
        global bk
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "Menu_logout" or page_name == "Menu_login" or page_name == "Menu_Admin":
            menu_btn(True)
        else:
            if back[1] == page_name:
                menu_btn(False)
            else:
                if page_name == 'ict' or page_name == 'web' or page_name == 'net' or page_name == 'programming1' or page_name == 'programming2':
                    if bk[3]== 'ict' or bk[3] == 'web' or bk[3] == 'net' or bk[3] == 'programming1' or bk[3] == 'programming2':
                        bk[3] = page_name
                        back[1] = page_name
                    else:
                        back_crs(page_name)
                        back_btn(page_name)
                elif page_name == 'Admin' or page_name == 'Change_User' or page_name == 'Forgetpsw':
                    back_btn(page_name)
                else:
                    back_crs(page_name)
                    back_btn(page_name)
                menu_btn(False)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def gotopage(self,frame): #reset all the entrys then change the frame
        self.show_frame(frame)
        self.err_var.set("")

        self.signin_code.set("")
        self.signin_psw.set("")

        self.name_var.set("")
        self.lname_var.set("")
        self.fname_var.set("")
        self.code_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.pw_var.set("")
        self.pwagain_var.set("")
    #*--------------------------------------------------------------------------------------------------------------------------------
    def menubar(self,menubtn_fr): #menubar that eachpages use

        self.btn_logo = tk.Button(menubtn_fr, image=self.tkimgmft,
                             bd = 0, cursor='hand2',
                           command=lambda: self.menubar_btnmft())
        self.btn_logo.pack(side='right', padx =10, pady =5)

        self.btn_menu = tk.Button(menubtn_fr, image=self.tkimgmenu,
                             bd = 0, cursor='hand2',
                           command=lambda: self.menubar_btnmenu())
        self.btn_menu.pack(side='left', padx =10,pady =3)

        self.btn_signin = tk.Button(menubtn_fr, image=self.tkimgsignin,
                             bd = 0, cursor='hand2',
                           command=lambda:self.menubar_btnsignin())
        self.btn_signin.pack(side='left', padx =0, pady =3)

        self.btn_signup = tk.Button(menubtn_fr, image=self.tkimgsignup,
                             bd = 0, cursor='hand2',
                           command=lambda: self.menubar_btnsignup())
        self.btn_signup.pack(side='left', padx =10, pady =3)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def menubar_btnmft(self):
        
        global logkey_var
        if logkey_var=="0123456789":
            self.show_frame("Admin")
        elif logkey_var!="":
            self.show_frame("User")
        else:
            self.gotopage("HomePage")

    #*--------------------------------------------------------------------------------------------------------------------------------
    def menubar_btnsignup(self):
        
        global logkey_var
        if logkey_var=="0123456789":
            ertxt = "!لطفا ابتدا از پنل ادمين خارج شويد"
            tk.messagebox.showwarning("!اخطار",ertxt)
        elif logkey_var!="":
            ertxt = "!لطفا ابتدا از پنل کاربري خارج شويد"
            tk.messagebox.showwarning("!اخطار",ertxt)
        else:
            self.gotopage("SignupPage")

    #*--------------------------------------------------------------------------------------------------------------------------------
    def menubar_btnsignin(self):
        
        global logkey_var
        if logkey_var!="":
            msg = tk.messagebox.askquestion("ورود", "آيا قصد خروج داريد؟")
            if msg == 'yes':
                back_btn("StartPage")
                alist = []
                namelist(alist)
                ictlist(alist)
                weblist(alist)
                net1list(alist)
                net2list(alist)
                pro1list(alist)
                pro2list(alist)
                logoutvar()
                self.destroy()
                self.mftdb.commit()
                self.mftdb.close()
                app = SampleApp()
                app.mainloop()
            else:
                pass
        else:
            self.btn_signup.configure(state="normal")
            self.gotopage("SigninPage")

    #*--------------------------------------------------------------------------------------------------------------------------------
    def menubar_btnmenu(self):
        
        global logkey_var
        global menu_var
        global back

        if logkey_var=="0123456789":
            if menu_var==False:
                menu_btn(True)
                self.show_frame("Menu_Admin")
            else:
                menu_btn(False)
                self.show_frame(back[1])
        elif logkey_var!="":
            if menu_var==False:
                menu_btn(True)
                self.show_frame("Menu_login")
            else:
                menu_btn(False)
                self.show_frame(back[1])
        else:
            if menu_var==False:
                menu_btn(True)
                self.gotopage("Menu_logout")
            else:
                menu_btn(False)
                self.gotopage(back[1])

    #*--------------------------------------------------------------------------------------------------------------------------------
    def Footer(self,footer_fr): #footer that eachpages use
        
        tk.Label(footer_fr, text=self.footer, anchor='center',font=self.btnfont).pack(side="top", fill="x", pady=1,ipadx=50)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def signout(self): #close the program and openit again
        
        msg = tk.messagebox.askquestion("ورود", "آيا قصد خروج داريد؟")
        if msg == 'yes':
            back_btn("StartPage")

            alist = []
            namelist(alist)
            ictlist(alist)
            weblist(alist)
            net1list(alist)
            net2list(alist)
            pro1list(alist)
            pro2list(alist)

            logoutvar()
            self.destroy()
            self.mftdb.commit()
            self.mftdb.close()
            app = SampleApp()
            app.mainloop()
        else:
            pass
    #*--------------------------------------------------------------------------------------------------------------------------------
    def signout2(self): #close the program and openit again
        
        back_btn("StartPage")
        alist = []
        namelist(alist)
        ictlist(alist)
        weblist(alist)
        net1list(alist)
        net2list(alist)
        pro1list(alist)
        pro2list(alist)

        logoutvar()
        self.destroy()
        self.mftdb.commit()
        self.mftdb.close()

        app = SampleApp()
        app.mainloop()
    #*--------------------------------------------------------------------------------------------------------------------------------
    def close(self): #close the program
        
        msg = tk.messagebox.askquestion("ورود", "آيا قصد بستن برنامه را داريد؟")
        if msg == 'yes':
            self.mftdb.commit()
            self.mftdb.close()
            self.destroy()
        else:
            pass
    #*--------------------------------------------------------------------------------------------------------------------------------
    def login(self): #connect to the database to change the global variables
        self.dbname()
        self.dbict()
        self.dbweb()
        self.dbnet1()
        self.dbnet2()
        self.dbpro1()
        self.dbpro2()
    #*--------------------------------------------------------------------------------------------------------------------------------
    def change_image(self,label,image_list,nextindex): #change the header image for HomePage with after
        label.configure(image=image_list[nextindex])
        self.ckbtnVR.set(nextindex)
        self.after(3000,lambda: self.change_image(label,image_list,(nextindex+1)%len(image_list)))
    #*--------------------------------------------------------------------------------------------------------------------------------
    def change_image_btn(self,label,image_list,ckbtnVR): #change the header image for HomePage with check btn
        label.configure(image=image_list[ckbtnVR])
    #*--------------------------------------------------------------------------------------------------------------------------------
    def show_hide_psw(self,button,entry,nextindex): #function change the pictures btn show hide psw
        image_list=[self.tkhide,self.tkshow]
        entry_show = ['','*']
        entry.configure(show=entry_show[nextindex])
        button.configure(image=image_list[nextindex],command = lambda:self.show_hide_psw(button,entry,(nextindex+1)%len(image_list)))
    #*--------------------------------------------------------------------------------------------------------------------------------
    def dbict(self): #connect to the database ict to change the global variables
        global logkey_var
        rowict = []
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        cursor.execute('''SELECT * from ict''')
        row = cursor.fetchall()
        for r in row:
            if logkey_var==r[0]:
                ICDL2 = r[1]
                Excel = r[2]
                Power = r[3]
                rowict = [ICDL2,Excel,Power]
                break
            else: pass
        ictlist(rowict)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def dbweb(self): #connect to the database web to change the global variables
        global logkey_var
        rowweb = []
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        cursor.execute('''SELECT * from web''')
        row = cursor.fetchall()
        for r in row:
            if logkey_var==r[0]:
                web2 = r[1]
                web3 = r[2]
                React = r[3]
                Node = r[4]
                PHP = r[5]
                Django = r[6]
                Wordpress = r[7]
                Woocommerce = r[8]
                UIUX = r[9]
                Seo = r[10]
                rowweb = [web2,web3,React,Node,PHP,Django,Wordpress,Woocommerce,UIUX,Seo]
                break
            else: pass
        weblist(rowweb)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def dbnet1(self): #connect to the database net1 to change the global variables
        global logkey_var
        rownet1 = []
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        cursor.execute('''SELECT * from NET1''')
        row = cursor.fetchall()
        for r in row:
            if logkey_var==r[0]:
                Winlo = r[1]
                Server1 = r[2]
                Server2 = r[3]
                Server3 = r[4]
                Exchange = r[5]
                Vmware = r[6]
                VDI = r[7]
                rownet1 = [Winlo, Server1, Server2, Server3, Exchange, Vmware,VDI]
                break
            else: pass
        net1list(rownet1)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def dbnet2(self): #connect to the database net2 to change the global variables
        global logkey_var
        rownet2 = []
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        cursor.execute('''SELECT * from NET2''')
        row = cursor.fetchall()
        for r in row:
            if logkey_var==r[0]:
                CCNA = r[1]
                CCNA_S = r[2]
                CCNP = r[3]
                CEH = r[4]
                Lpic1 = r[5]
                Lpic2 = r[6]
                rownet2 = [CCNA, CCNA_S, CCNP, CEH, Lpic1, Lpic2]
                break
            else: pass
        net2list(rownet2)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def dbpro1(self): #connect to the database pro1 to change the global variables
        global logkey_var
        rowpro1 = []
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        cursor.execute('''SELECT * from pro1''')
        row = cursor.fetchall()
        for r in row:
            if logkey_var==r[0]:
                Python = r[1]
                ML = r[2]
                DeepL = r[3]
                ImagePro = r[4]
                Cplus = r[5]
                Csharp = r[6]
                SQL = r[7]
                ASP = r[8]
                JS = r[9]
                Block_C = r[10]
                rowpro1 = [Python,ML,DeepL,ImagePro,Cplus,Csharp,SQL,ASP,JS,Block_C]
                break
            else: pass
        pro1list(rowpro1)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def dbpro2(self): #connect to the database pro2 to change the global variables
        global logkey_var
        rowpro2 = []
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        cursor.execute('''SELECT * from pro2''')
        row = cursor.fetchall()
        for r in row:
            if logkey_var==r[0]:
                Java = r[1]
                SE = r[2]
                EE = r[3]
                Android = r[4]
                Kotlin = r[5]
                Android_Java = r[6]
                IOS = r[7]
                rowpro2 = [Java,SE,EE,Android,Kotlin,Android_Java,IOS]
                break
            else: pass
        pro2list(rowpro2)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def dbname(self): #connect to the database STUDENT to change the global variables
        global logkey_var
        rowname = []
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        cursor.execute('''SELECT * from STUDENT''')
        row = cursor.fetchall()
        for r in row :
            if logkey_var==r[0]:
                Melli_code = r[0]
                Name = r[1]
                Last_Name = r[2]
                Father_Name = r[3]
                Phone = r[4]
                Email = r[5]
                Password = ""
                ICDL1 = r[7]
                Algorithms = r[8]
                Network = r[9]
                web = r[10]
                rowname = [Melli_code,Name,Last_Name,Father_Name,Phone,Email,Password,ICDL1,Algorithms,Network,web]
                break
            else: pass
        namelist(rowname)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def pishniyaz(self,point):
        if point=='pass':
            return True
        else:
            return False
    #*--------------------------------------------------------------------------------------------------------------------------------
    def errpishniyaz(self,pishniyaz,dbname,darsname,darspishniyaz,point,course):
        global logkey_var
        global rowname
        user = rowname[1] +" "+ rowname[2] +" عزيز، شما "
        if pishniyaz == True and point=='pass':
            ertxt = "!را قبلا گذرانده ايد"+"  "+darsname+"  "+user
            tk.messagebox.showwarning("!اخطار",ertxt)
        elif pishniyaz == True and point=='register':
            ertxt = "!را قبلا ثبت نام کرده ايد"+"  "+darsname+"  "+user
            tk.messagebox.showwarning("!اخطار",ertxt)
        elif pishniyaz == True and point=='notregister':
            ertxt = ".با موفقيت ثبت شد "+darsname
            tk.messagebox.showinfo("ثبت درس",ertxt)
            mftdb = sqlite3.connect('mft01.db')
            cursor = mftdb.cursor()
            txt = "UPDATE "+dbname+" SET "+course+"='register'"+" WHERE Melli_code='"+logkey_var+"'"
            cursor.execute(txt)
            mftdb.commit()
            mftdb.close()
            if dbname=='ict':
                self.dbict()
            elif dbname=='web':
                self.dbweb()
            elif dbname=='pro1':
                self.dbpro1()
            elif dbname=='pro2':
                self.dbpro2()
            elif dbname=='NET1':
                self.dbnet1()
            elif dbname=='NET2':
                self.dbnet2()
            elif dbname=='STUDENT':
                self.dbname()
                
        elif pishniyaz == False:
            ertxt0 = "!را نگذرانده ايد"+"  "+darspishniyaz+"  "+user+"\n"
            ertxt1 =".هستید"+"  "+darspishniyaz+" "+"نیازمند به گذراندن"+"  "+darsname+"  "+"برای ثبت نام "
            ertxt = ertxt0 + ertxt1
            tk.messagebox.showwarning("عدم رعايت پيشنيازي",ertxt)
        else:
            pass

#Class child1: StartPage ------------------------------------------------------------------------------------------------------------------------------------------
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.err_var = controller.err_var
        self.Err_lbl_email_txt = controller.Err_lbl_email_txt
        global logkey_var
        self.homepagetxt = """این برنامه به عنوان پروژه پایان دوره برنامه نویسی به زبان پایتون است که به دانشپذیر
 امکان ثبت درس را می دهد و در صورت رعایت نکردن پیشنیاز به دانشپذیر پیغام اخطار
.را نمایش می دهد
،تقدیم به استاد گرامی
سرکار خانم فاطمه رفیع پور"""
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #----Space--------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #-----------------------------------------------------------------------
        hm_frmlbl = tk.LabelFrame(self,text = "  معرفي  ",labelanchor='ne',relief = 'ridge',font=controller.logfont)
        hm_frmlbl.pack(side="top", fill="x",padx=5,pady=5,ipadx=10,ipady=5,)

        start_lbl = tk.Label(hm_frmlbl,text = self.homepagetxt,justify='right',font=controller.logfont,width=41)
        start_lbl.pack(side="top", fill="x", pady=10)
        #----Space--------------------------------------------------------------
        login_btn = tk.Button(hm_frmlbl, text="اجراي برنامه", bg = "#316ba9",fg = "white",font=controller.Blblfont,cursor='hand2',
                            command=lambda: controller.show_frame("HomePage"))
        login_btn.pack(side="top",fill='x',padx = 20, ipadx=10,pady=20)
        #-----------------------------------------------------------------------
        hmlbl = tk.LabelFrame(self,text = "  راهنمايي  ",labelanchor='ne',relief = 'ridge',font=controller.logfont)
        hmlbl.pack(side="top", fill="x",padx=5,pady=5,ipadx=10,ipady=5,)
        #-----------------------------------------------------------------------
        fram1 = tk.Frame(hmlbl)
        fram2 = tk.Frame(hmlbl)
        fram3 = tk.Frame(hmlbl)
        fram4 = tk.Frame(hmlbl)
        fram5 = tk.Frame(hmlbl)
        fram6 = tk.Frame(self)
        #-----------------------------------------------------------------------
        frames = (fram1, fram2, fram3,fram4,fram5,fram6)
        for fram in frames:
            fram.pack(side="top", fill="x")
        #----Information--------------------------------------------------------
        lbl_menu = tk.Label(fram1, image=controller.tkimgmenu)
        txt_menu = tk.Label(fram1, font = controller.logfont, text = "دکمه منو: دسترسي سريع به صفحات")
        #-----------------------------------------------------------------------
        lbl_signin = tk.Label(fram2, image=controller.tkimgsignin)
        txt_signin = tk.Label(fram2, font = controller.logfont, text = "دکمه ساين اين: صفحه وارد شدن به پنل کاربر و ادمين و یا خارج شدن از پنل")
        #-----------------------------------------------------------------------
        lbl_signup = tk.Label(fram3, image=controller.tkimgsignup,)
        txt_signup = tk.Label(fram3, font = controller.logfont, text = "دکمه ساين آپ: ساختن اکانت کاربر",)
        #-----------------------------------------------------------------------
        lbl_refresh = tk.Label(fram4, image=controller.tkimgrefresh)
        txt_refresh = tk.Label(fram4, font = controller.logfont, text = "دکمه رفرش: پس از برداشتن درس، دروس کاربر را به روز رساني ميکند")
        #-----------------------------------------------------------------------
        lbl_logo = tk.Label(fram5, image=controller.tkimgmft)
        lbl_logo.pack(side='right', padx =30, pady =2)
        txt_logo = tk.Label(fram5, font = controller.logfont, text = "دکمه لوگو: دسترسي سريع به صفحه اصلي يا صفحه کاربر و يا صفحه ادمين")
        #-----------------------------------------------------------------------
        lbl = tk.Label(fram6, font = controller.english_lblfont , fg = "#316ba9",text = "Designed by: Farzaneh Ahmadi - 'https://www.linkedin.com/in/farzaneh-ahmadi' - 1400/mehr/19")
        lbl.pack(side='left', padx =16, pady =1)
        #-----------------------------------------------------------------------
        lbl1 = (lbl_menu, lbl_signin ,lbl_signup, lbl_refresh)
        for lblpic in lbl1:
            lblpic.pack(side='right', padx =45,pady =2)
        #-----------------------------------------------------------------------
        lbl2 = (txt_menu, txt_signin, txt_signup , txt_logo, txt_refresh)
        for lbltxt in lbl2:
            lbltxt.pack(side='right', padx =5, pady =5)
        #----Footer-------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
        
#Class child1: HomePage ------------------------------------------------------------------------------------------------------------------------------------------
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.err_var = controller.err_var
        self.Err_lbl_email_txt = controller.Err_lbl_email_txt
        self.chk_btn_var = controller.ckbtnVR
        self.chk_btn_var.set(1)
        global logkey_var
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #----Space------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top', pady = 1,ipadx = 5000, fill="y")
        #---------------------------------------------------------------------
        #----Header-----------------------------------------------------------
        hdr_fr = tk.Frame(self)
        hdr_fr.pack(side="top", fill="x")

        image_list = [controller.tkheader1,controller.tkheader2,controller.tkheader3,controller.tkheader4,controller.tkheader5]
        hdr1_lbl = tk.Label(self, image=controller.tkheader1,bg = "white")
        hdr1_lbl.pack(side="top", fill="x")
        controller.change_image(hdr1_lbl,image_list,0)
        #----Space------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #----Check_btn------------------------------------------------------------
        check_fr = tk.Frame(self)
        check_fr.pack(side="top", fill="x")

        tk.Label(check_fr,font=controller.btnfont).pack(side="right", padx=80)
        chk_btn1 = tk.Radiobutton(check_fr, variable=self.chk_btn_var, value=0,cursor='target',
                                  command= lambda: controller.change_image_btn(hdr1_lbl,image_list,0))
        chk_btn1.pack(side="right",anchor='center', padx=10)

        chk_btn2 = tk.Radiobutton(check_fr, variable=self.chk_btn_var, value=1,cursor='target',
                                  command= lambda: controller.change_image_btn(hdr1_lbl,image_list,1))
        chk_btn2.pack(side="right",anchor='center', padx=10)

        chk_btn3 = tk.Radiobutton(check_fr, variable=self.chk_btn_var, value=2,cursor='target',
                                  command= lambda: controller.change_image_btn(hdr1_lbl,image_list,2))
        chk_btn3.pack(side="right",anchor='center', padx=10)

        chk_btn4 = tk.Radiobutton(check_fr, variable=self.chk_btn_var, value=3,cursor='target',
                                  command= lambda: controller.change_image_btn(hdr1_lbl,image_list,3))
        chk_btn4.pack(side="right",anchor='center', padx=10)

        chk_btn5 = tk.Radiobutton(check_fr, variable=self.chk_btn_var, value=4,cursor='target',
                                  command= lambda: controller.change_image_btn(hdr1_lbl,image_list,4))
        chk_btn5.pack(side="right",anchor='center', padx=10)
        
        #-----------------------------------------------------------------------
        self.btnuser = tk.Button(self,font=controller.Blblfont, bg="#316ba9",fg="white",cursor='hand2',
                                     text = "  ثبت نام درس  ",command=lambda: controller.show_frame('SET_CRS'))
        self.btnuser.pack(side="top",fill='x',padx = 20, ipadx=10,pady=20)
        #----frame--------------------------------------------------------------
        fram1 = tk.Frame(self)
        fram2 = tk.Frame(self)
        fram3 = tk.Frame(self)
        fram4 = tk.Frame(self)
        fram5 = tk.Frame(self)
        #-----------------------------------------------------------------------
        for frame in (fram1, fram2, fram3, fram4, fram5):
            frame.pack(side="top", fill="x")
        #----Courses------------------------------------------------------------
        tk.Label(fram1,font=controller.btnfont).pack(side="right", padx=20)
        co1_lbl = tk.Label(fram1, text=" دوره هاي مهارت پايه ",font=controller.Blblfont)
        co1_lbl.pack(side="right", fill="x", padx = 1, pady = 13)

        co1_btn = tk.Button(fram1, text=" نمايش ", font=controller.btnfont, bg="#a9d9f4",fg="black",cursor='hand2',
                            command=lambda: controller.show_frame('ict'))
        co1_btn.pack(side="left", padx = 90, ipadx=60, ipady=5)

        tk.Label(fram2,font=controller.btnfont).pack(side="right", padx=20)
        co2_lbl = tk.Label(fram2, text=" دوره هاي وب ",font=controller.Blblfont)
        co2_lbl.pack(side="right", fill="x", padx = 1, pady = 13)

        co2_btn = tk.Button(fram2, text=" نمايش ", font=controller.btnfont, bg="#a9d9f4",fg="black",cursor='hand2',
                            command=lambda: controller.show_frame('web'))
        co2_btn.pack(side="left", padx = 90, ipadx=60, ipady=5)

        tk.Label(fram3,font=controller.btnfont).pack(side="right", padx=20)
        co3_lbl = tk.Label(fram3, text=" دوره هاي شبکه ",font=controller.Blblfont)
        co3_lbl.pack(side="right", fill="x", padx = 1, pady = 13)

        co3_btn = tk.Button(fram3, text=" نمايش ", font=controller.btnfont, bg="#a9d9f4",fg="black",cursor='hand2',
                            command=lambda: controller.show_frame('net'))
        co3_btn.pack(side="left", padx = 90, ipadx=60, ipady=5)

        tk.Label(fram4,font=controller.btnfont).pack(side="right", padx=20)
        co4_lbl = tk.Label(fram4, text="1 دوره هاي برنامه نويسي ",font=controller.Blblfont)
        co4_lbl.pack(side="right", fill="x", padx = 1, pady = 13)

        co4_btn = tk.Button(fram4, text=" نمايش ", font=controller.btnfont, bg="#a9d9f4",fg="black",cursor='hand2',
                            command=lambda: controller.show_frame('programming1'))
        co4_btn.pack(side="left", padx = 90, ipadx=60, ipady=5)

        tk.Label(fram5,font=controller.btnfont).pack(side="right", padx=20)
        co5_lbl = tk.Label(fram5, text="2 دوره هاي برنامه نويسي ",font=controller.Blblfont)
        co5_lbl.pack(side="right", fill="x", padx = 1, pady = 13)

        co5_btn = tk.Button(fram5, text=" نمايش ", font=controller.btnfont, bg="#a9d9f4",fg="black",cursor='hand2',
                            command=lambda: controller.show_frame('programming2'))
        co5_btn.pack(side="left", padx = 90, ipadx=60, ipady=5)
        #----Footer-------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)

#Class child2: SigninPage ------------------------------------------------------------------------------------------------------------------------------------------
class SigninPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.show_frame = controller.show_frame
        self.login = controller.login
        #---------------------------------------
        global logkey_var
        self.code_var = controller.signin_code
        self.pw_var = controller.signin_psw
        self.err_var = controller.err_var
        #---------------------------------------
        self.verifybool = tk.BooleanVar()
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #----Space--------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #----frames--------------------------------------------------------------
        SigninPage_lblfr = tk.LabelFrame(self,text = "  ورود به داشبورد  ",labelanchor='ne',relief = 'ridge',font=controller.logfont)
        SigninPage_lblfr.pack(side="top", fill="x",padx=5,pady=10,ipadx=10,ipady=5,)
        #-----------------------------------------------------------------------
        signin_fr = tk.Frame(SigninPage_lblfr)
        fram1 = tk.Frame(signin_fr)
        fram2 = tk.Frame(signin_fr)
        framE2 = tk.Frame(signin_fr)
        fram3 = tk.Frame(signin_fr)
        fram4 = tk.Frame(signin_fr)
        empty = tk.Frame(self)
        #-----------------------------------------------------------------------
        frames = (signin_fr,fram1,fram2,framE2,fram3,fram4,empty)
        for fram in frames:
            fram.pack(side="top", fill="x")
        #-----------------------------------------------------------------------
        validationInt = self.register(self.only_int)
        validationChreng = self.register(self.only_engchar)
        #----1st Frame for codemelli--------------------------------------------
        tk.Label(fram1,text = "  ",pady = 5).pack(side="top", fill="x",padx=50)
        lb_code = tk.Label(fram1,text = "  :کد ملي                  ", pady=5, font=controller.lblfont)
        lb_code.pack(side="right", fill="x",padx=4)

        lb = tk.Label(fram1,text = "  ",pady = 5, font=controller.lblfont)
        lb.pack(side="left", fill="x",padx=50)

        en_code = tk.Entry(fram1,textvariable = self.code_var, font=controller.btnfont, bd=2,
                           validate='key',validatecommand=(validationInt,'%S'))
        en_code.pack(side="left", fill="x", anchor="center", padx=1, ipadx=100)
        #----2nd Frame for psw-------------------------------------------------
        lb_psw = tk.Label(fram2,text = ":رمز عبور                  ",
                          pady = 5,
                          font=controller.lblfont)
        lb_psw.pack(side="right", fill="x",padx=4)
        #showpsw
        lb = tk.Label(fram2,text = "  ",pady = 5, font=controller.lblfont)
        lb.pack(side="left", fill="x",padx=35)

        show_btn1 = tk.Button(fram2,image=controller.tkshow, pady=5, bd =0,cursor='hand2',
                              command=lambda: controller.show_hide_psw(show_btn1,en_psw,0))
        show_btn1.pack(side="left", fill="x",padx = 1)

        en_psw = tk.Entry(fram2,textvariable = self.pw_var, bd=2,
                          font=controller.btnfont,show="*",
                          validate='key',validatecommand=(validationChreng ,'%S'))
        en_psw.pack(side="left", fill="x",anchor="center", padx=1, ipadx=100)
        #-----------------------------------------------------------------------
        self.Err_lbl_pw = tk.Label(framE2,text=self.err_var.get(),fg = "red",
                                 font=controller.lblfont)
        self.Err_lbl_pw.pack(side="bottom", fill="x",anchor="center")
        #----signin_btn---------------------------------------------------------
        # Button that will call the submit function
        self.signin_btn=tk.Button(fram3,text = 'ورود',font=controller.btnfont,
                                  bg="#316ba9",fg="#f0f0f0",cursor='hand2',
                                  disabledforeground = "#85b1da",
                                  command = lambda: self.signin(), state = 'disable')
        self.signin_btn.pack(side="left",anchor='e',padx = 25, ipadx=10,pady=10)

        self.code_var.trace('w',self.btn_enable_1)
        self.pw_var.trace('w',self.btn_enable_1)
        #----forgetpsw_btn------------------------------------------------------
        # Button that will call the forgetpsw function
        self.forgetpsw_btn=tk.Button(fram3,text = 'فراموشي رمز عبور',cursor='hand2',
                                     font=controller.btnfont,bg="#fad7dc",fg="black",
                                     command = lambda: controller.gotopage('Forgetpsw'), state = 'normal')
        self.forgetpsw_btn.pack(side="left",anchor='w',padx = 1, ipadx=10,pady=10)
        #-----------------------------------------------------------------------
        ttk.Separator(fram4,orient = 'horizontal').pack(side='top',anchor='center',pady = 10, ipadx = 1000)
        #----signup_btn------------------------------------------------------
        # Button that will call the signup function
        self.signup_btn=tk.Button(fram4,text = 'ثبت نام',cursor='hand2',
                                  font=controller.btnfont, bg="#a9d9f4",fg="black",
                                  command = lambda: controller.gotopage('SignupPage'), state = 'normal')
        self.signup_btn.pack(side="top",anchor='w',padx = 25, ipadx=73,pady=10)
        #----Footer-------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def only_int(self,Int):#function for don't let the wrong entry
        return Int.isdigit()
    #*--------------------------------------------------------------------------------------------------------------------------------
    def only_engchar(self,char):#function for don't let the wrong entry
        for i in char:
            if(32<=ord(i)<127):
                return True
            else:
                return False
    #*--------------------------------------------------------------------------------------------------------------------------------
    def btn_enable_1(self,*arg): #function enable disable btn
        a = self.code_var.get()
        b = self.pw_var.get()
        if a and b:
            self.signin_btn.configure(state = 'normal')
            self.signup_btn.configure(state = 'disable')
        else:
            self.signin_btn.configure(state = 'disable')
            self.signup_btn.configure(state = 'normal')
            self.err_var.set("")
            self.Err_lbl_pw.configure(text = self.err_var.get())    
    #*--------------------------------------------------------------------------------------------------------------------------------
    def signin(self): #function check the database
        global logkey_var
        global rowname
        global rowict
        global rowweb
        global rownet1
        global rownet2
        global rowpro1
        global rowpro2
        code = self.code_var.get()
        password = self.pw_var.get()
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        cursor.execute('''SELECT * from STUDENT''')
        row = cursor.fetchall()
        for r in row :
            #----------------------------------------------------------
            if r[0]==code and r[6]== password:
                self.pw_var.set("")
                self.verifybool.set(True)
                loginvar(code)
                Melli_code = r[0]
                Name = r[1]
                Last_Name = r[2]
                Father_Name = r[3]
                Phone = r[4]
                Email = r[5]
                Password = ""
                ICDL1 = r[7]
                Algorithms = r[8]
                Network = r[9]
                web = r[10]
                rowname = [Melli_code,Name,Last_Name,Father_Name,Phone,Email,Password,ICDL1,Algorithms,Network,web]
                namelist(rowname)
                self.login()
                self.Err_lbl_pw.configure(text = self.err_var.get())
                if code=='0123456789':
                    self.show_frame("Admin")
                else:
                    self.show_frame("User")
                break
            #----------------------------------------------------------
            elif r[0]==code and r[6]!= password:
                logoutvar()
                self.pw_var.set("")
                self.verifybool.set(True)
                self.err_var.set(".رمز عبور اشتباه است. لطفا دوباره رمز خود را وارد کنيد")
                self.Err_lbl_pw.configure(text = self.err_var.get())
                break
            #----------------------------------------------------------
            elif row==[]:
                logoutvar()
                tk.messagebox.showinfo("! خطا",".پايگاه داده پيدا نشد")
                break
            #----------------------------------------------------------
            else:
                logoutvar()
                self.verifybool.set(False)
        #----------------------------------------------------------------------------------------------------------------------------------
        if self.verifybool.get() == False:
            self.err_var.set(".شماره کد ملي شما قبلا در سامانه ثبت نشده است")
            self.Err_lbl_pw.configure(text = self.err_var.get())
            tk.messagebox.showinfo("! خطا",".شما قبلا در سامانه عضو نشده ايد")
            msg = tk.messagebox.askquestion("ورود", "آیا مایل به ثبت نام در سامانه هستید؟")
            if msg == 'yes':
                code = self.code_var.get()
                self.err_var.set("")
                self.Err_lbl_pw.configure(text = self.err_var.get())
                self.code_var.set("")
                self.pw_var.set("")
                self.show_frame("SignupPage")
            else:
                self.err_var.set("")
                self.Err_lbl_pw.configure(text = self.err_var.get())
                pass

#Class child3: SignupPage ------------------------------------------------------------------------------------------------------------------------------------------
class SignupPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.show_frame = controller.show_frame
        self.gotopage = controller.gotopage
        self.signout = controller.signout
        self.login = controller.login
        #---------------------------------------
        global logkey_var
        self.name_var = controller.name_var
        self.lname_var = controller.lname_var
        self.fname_var = controller.fname_var
        self.code_var = controller.code_var
        self.email_var = controller.email_var
        self.phone_var = controller.phone_var
        self.pw_var = controller.pw_var
        self.pwagain_var = controller.pwagain_var

        self.err_var = controller.err_var
        self.Err_lbl_email_txt = controller.Err_lbl_email_txt
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #----Space--------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #----frames-------------------------------------------------------------
        SignupPage_lblfr = tk.LabelFrame(self,text = "  ثبت نام در سامانه  ",labelanchor='ne',relief = 'ridge',font=controller.logfont)
        SignupPage_lblfr.pack(side="top", fill="x",padx=5,pady=10,ipadx=10,ipady=5,)

        signup_fr = tk.Frame(SignupPage_lblfr)
        signup_fr.pack(side="top", fill="x")
        #-----------------------------------------------------------------------
        fram1 = tk.Frame(signup_fr)
        fram2 = tk.Frame(signup_fr)
        fram3 = tk.Frame(signup_fr)
        fram4 = tk.Frame(signup_fr)
        fram5 = tk.Frame(signup_fr)
        fram6 = tk.Frame(signup_fr)
        fram7 = tk.Frame(signup_fr)
        fram8 = tk.Frame(signup_fr)
        framE = tk.Frame(signup_fr)
        fram9 = tk.Frame(signup_fr)
        frames = (fram1, fram2, fram3,fram4,fram5,fram6,fram7,fram8,framE,fram9)
        for fram in frames:
            fram.pack(side="top", fill="x")

        validationInt = self.register(self.only_int)
        validationChrper = self.register(self.only_perchar)
        validationChreng = self.register(self.only_engchar)
        #----1st Frame for name--------------------------------------------------------
        tk.Label(fram1,text = "  ",pady = 5).pack(side="top", fill="x",padx=50)
        lb_name = tk.Label(fram1,text = ":نام (فارسی)                  ",
                font=controller.lblfont)
        lb_name.pack(side="right", fill="x",padx=4)
        tk.Label(fram1,text = "  ",pady = 5).pack(side="left", fill="x",padx=50)

        en_name = tk.Entry(fram1,textvariable = self.name_var,
                           font=controller.btnfont,bd = 2,
                           validate='key',validatecommand=(validationChrper,'%S'))
        en_name.pack(side="left", fill="x",ipadx=60)
        #----2nd Frame for lastname---------------------------------------------------
        lb_lname = tk.Label(fram2,text = ":نام خانوادگی (فارسی)                  ",
                            font=controller.lblfont)
        lb_lname.pack(side="right", fill="x",padx=4)
        tk.Label(fram2,text = "  ",pady = 5).pack(side="left", fill="x",padx=50)

        en_lname = tk.Entry(fram2,textvariable = self.lname_var,
                            font=controller.btnfont,bd = 2,
                            validate='key',validatecommand=(validationChrper,'%S'))
        en_lname.pack(side="left", fill="x",ipadx=60)
        #----3rd Frame for fname------------------------------------------------------
        lb_fname = tk.Label(fram3,text = ":نام پدر (فارسی)                  ",
                            pady = 5, font=controller.lblfont)
        lb_fname.pack(side="right", fill="x",padx=4)
        tk.Label(fram3,text = "  ",pady = 5).pack(side="left", fill="x",padx=50)

        en_fname = tk.Entry(fram3,textvariable = self.fname_var,
                            font=controller.btnfont,bd = 2
                            ,validate='key', validatecommand=(validationChrper,'%S'))
        en_fname.pack(side="left", fill="x",ipadx=60)
        #----4th Frame for codemelli---------------------------------------------------
        lb_code = tk.Label(fram4,text = ":کد ملي                  ",
                           pady = 5,font=controller.lblfont)
        lb_code.pack(side="right", fill="x",padx=4)

        tk.Label(fram4,text = "  ",pady = 5).pack(side="left", fill="x",padx=50)

        en_code = tk.Entry(fram4,textvariable = self.code_var,
                           font=controller.btnfont,bd = 2,
                           validate='key', validatecommand=(validationInt,'%S'))
        en_code.pack(side="left", fill="x",ipadx=60)
        #----5th Frame for phonenumber-------------------------------------------------
        lb_phone = tk.Label(fram5,text = ":شماره همراه                  ",
                            pady = 5,
                            font=controller.lblfont)
        lb_phone.pack(side="right", fill="x",padx=4)
        tk.Label(fram5,text = "  ",pady = 5).pack(side="left", fill="x",padx=50)

        en_phone = tk.Entry(fram5,textvariable = self.phone_var,
                           font=controller.btnfont,bd = 2,
                           validate='key',validatecommand=(validationInt,'%S'))
        en_phone.pack(side="left", fill="x",ipadx=60)
        #----6th Frame for email---------------------------------------------------------
        lb_email = tk.Label(fram6,text = ":ايميل                   ",
                            pady = 5,font=controller.lblfont)
        lb_email.pack(side="right", fill="x")

        tk.Label(fram6,text = "  ",pady = 5).pack(side="left", fill="x",padx=35)

        self.Err_lbl_email = tk.Label(fram6,text="    ",fg = "red",
                                 font=controller.lblfont)
        self.Err_lbl_email.pack(side="left", fill="x",padx=2)

        en_email = tk.Entry(fram6,textvariable = self.email_var,
                            font=controller.btnfont, bd = 2,
                            validate='key',validatecommand=(validationChreng,'%S'))
        en_email.pack(side="left", fill="x",ipadx=60)
        #----7th Frame for psw------------------------------------------------------
        lb_psw = tk.Label(fram7,text = ":رمز عبور                  ",
                          pady = 5,
                          font=controller.lblfont)
        lb_psw.pack(side="right", fill="x",padx=4)
        tk.Label(fram7,text = "  ",pady = 5).pack(side="left", fill="x",padx=35)
        #showpsw
        show_btn1 = tk.Button(fram7,image=controller.tkshow,cursor='hand2',
                             command=lambda: controller.show_hide_psw(show_btn1,en_psw,0),
                             pady = 5, bd =0)
        show_btn1.pack(side="left", fill="x",padx = 1)
        en_psw = tk.Entry(fram7,textvariable = self.pw_var,font=controller.btnfont
                          ,show="*",bd = 2,
                          validate='key',validatecommand=(validationChreng,'%S'))
        en_psw.pack(side="left", fill="x",anchor="center",padx=1,ipadx=60)
        #----8th Frame for againpsw------------------------------------------------------
        lb_pswagain = tk.Label(fram8,text = ":تکرار رمز عبور                  ",
                pady = 5,font=controller.lblfont)
        lb_pswagain.pack(side="right", fill="x",padx=4)
        tk.Label(fram8,text = "  ",pady = 5).pack(side="left", fill="x",padx=35)

        #showagainpsw
        show_btn2 = tk.Button(fram8,image=controller.tkshow,cursor='hand2',
                             command=lambda: controller.show_hide_psw(show_btn2,en_pswagain,0),
                             pady = 5, bd =0)
        show_btn2.pack(side="left", fill="x",padx = 1)
        en_pswagain = tk.Entry(fram8,textvariable = self.pwagain_var,
                               font=controller.btnfont,bd = 2, show="*",
                               validate='key',validatecommand=(validationChreng,'%S'))
        en_pswagain.pack(side="left", fill="x",padx=1,ipadx=60)
         #----9th Frame for errors ------------------------------------------------------
        self.Err_lbl = tk.Label(framE,text=self.err_var.get(), fg = "red",
                                 font=controller.lblfont)
        self.Err_lbl.pack(side="top", fill="x",padx=2)
        #----Submit_btn---------------------------------------------------------
        # Button that will call the submit function
        self.sub_btn=tk.Button(fram9,text = 'ثبت نام',
                               fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9", font = controller.btnfont ,cursor='hand2',
                               command = lambda: self.submit(), state = 'disable')
        self.sub_btn.pack(side="left",anchor='w',padx = 85, ipadx=40,pady=10)
        #----signin_btn---------------------------------------------------------
        # Button that will call the signin function
        self.signin_btn=tk.Button(fram9,text = 'ورود به پنل کاربر',font=controller.btnfont,
                                  fg="black", disabledforeground = "#85b1da",cursor='hand2',
                                  bg="#a9d9f4",
                                  command = lambda: controller.gotopage("SigninPage"), state = 'normal')
        self.signin_btn.pack(side="left",anchor='w', ipadx=50,pady=10)
        #-----------------------------------------------------------------------
        self.name_var.trace('w',self.btn_enable)
        self.lname_var.trace('w',self.btn_enable)
        self.fname_var.trace('w',self.btn_enable)
        self.code_var.trace('w',self.btn_enable)
        self.email_var.trace('w',self.btn_enable)
        self.phone_var.trace('w',self.btn_enable)
        self.pw_var.trace('w',self.btn_enable)
        self.pwagain_var.trace('w',self.btn_enable)
        #----Footer-------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def only_perchar(self,char):
        if char.isalpha()==True:
            for i in char:
                if(1568<=ord(i)<1632 or 1649<=ord(i)<1752 or 1872<=ord(i)<1920):
                    return True
                else:
                    return False
        else:
            for i in char:
                if(ord(i)==32 or 48<=ord(i)<=57):
                    return True
                else:
                    return False
            return False
    #*--------------------------------------------------------------------------------------------------------------------------------
    def only_int(self,Int):
        return Int.isdigit()
    #*--------------------------------------------------------------------------------------------------------------------------------
    def only_engchar(self,char):
        for i in char:
            if(32<=ord(i)<127):
                return True
            else:
                return False
    #*--------------------------------------------------------------------------------------------------------------------------------
    def btn_enable(self,*arg):
        
        a = self.name_var.get()
        b = self.lname_var.get()
        c = self.fname_var.get()
        d = self.code_var.get()
        e = self.email_var.get()
        f = self.phone_var.get()
        g = self.pw_var.get()
        h = self.pwagain_var.get()
        if a and b and c and d and e and f and g and h:
            self.sub_btn.configure(state = 'normal')
            self.signin_btn.configure(state = 'disable')
            self.Err_lbl_email.configure(text = "    ")
            self.err_var.set("")
            self.Err_lbl.configure(text = self.err_var.get())
        else:
            self.sub_btn.configure(state = 'disable')
            self.signin_btn.configure(state = 'normal')
            self.Err_lbl_email.configure(text = "    ")
            self.err_var.set("")
            self.Err_lbl.configure(text = self.err_var.get())
    #*--------------------------------------------------------------------------------------------------------------------------------
    def submit(self):
        
        global logkey_var
        name = self.name_var.get()
        lname = self.lname_var.get()
        fname = self.fname_var.get()
        code = self.code_var.get()
        phone = self.phone_var.get()
        pw = self.pw_var.get()
        pwagain = self.pwagain_var.get()
        #------------------------------------------------------------
        if len(code)==10:
            codechecker = True
        else:
            codechecker = False
            tk.messagebox.showinfo("! خطا",".کد ملي بايد 10 رقمي باشد\nبه طور مثال : 0490112233")
        #------------------------------------------------------------
        if len(phone)==11:
            phonchecker = True
        else:
            phonchecker = False
            tk.messagebox.showinfo("! خطا",".شماره همراه بايد 11 رقمي باشد\nبه طور مثال : 09121010101")
        #------------------------------------------------------------
        #emailcheck and pswcheck:
        email_checker = False
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex,self.email_var.get()):
            email_checker = True
        else:
            email_checker = False
        #------------------------------------------------------------
        if pw == pwagain and email_checker and phonchecker and codechecker: 
            email = self.email_var.get()
            email = email.lower()
            password = self.pwagain_var.get()
            A = any(x.isupper() for x in password)
            B = any(x.islower() for x in password)
            C = any(x.isdigit() for x in password)
            D = any(x.isalpha() for x in password)
            E = len(password)>=8
            if A and B and C and D and E:
                self.submit_db(name,lname,fname,code,email,phone,password)
                self.email_var.set("")

                self.err_var.set("")
                self.Err_lbl.configure(text = self.err_var.get())
                self.Err_lbl_email.configure(text = "    ")
            if D==False:
                tk.messagebox.showinfo("! خطا",".رمز عبور بايد شامل حداقل دو حرف باشد")
                self.pwagain_var.set("")
                password = ""
            if D:
                if A==False:
                    tk.messagebox.showinfo("! خطا",".رمز عبور بايد شامل حداقل يک حرف بزرگ باشد")
                    self.pwagain_var.set("")
                    password = ""
                if B==False:
                    tk.messagebox.showinfo("! خطا",".رمز عبور بايد شامل حداقل يک حرف کوچک باشد")
                    self.pwagain_var.set("")
                    password = ""
                if C==False:
                    tk.messagebox.showinfo("! خطا",".رمز عبور بايد شامل حداقل يک عدد باشد")
                    self.pwagain_var.set("")
                    password = ""
            if E==False:
                tk.messagebox.showinfo("! خطا",".طول رمز عبور بايد بيشتر از 8 کاراکتر باشد")
                self.pwagain_var.set("")
                password = ""
                
        elif pw == pwagain and email_checker == False:
            self.email_var.set("")
            self.err_var.set("!لطفا دوباره ايميل خود را وارد کنيد")
            self.Err_lbl.configure(text = self.err_var.get())
            self.Err_lbl_email.configure(text = "**")

        elif pw != pwagain and email_checker == False:
            self.pwagain_var.set("")
            self.email_var.set("")
            self.err_var.set(". عدم تشابه رمز عبور و ایمیل اشتباه، لطفاً دوباره ایمیل و رمز عبور خود را وارد کنید")
            self.Err_lbl.configure(text = self.err_var.get())
            self.Err_lbl_email.configure(text = "**")

        elif pw != pwagain and email_checker == True:
            self.pwagain_var.set("")
            self.err_var.set(". عدم تشابه رمز، لطفاً دوباره رمز خود را وارد کنید")
            self.Err_lbl.configure(text = self.err_var.get())
            self.Err_lbl_email.configure(text = "    ")

        else:
            self.Err_lbl.configure(text = "")
    #*--------------------------------------------------------------------------------------------------------------------------------
    def submit_db(self,name,lname,fname,code,email,phone,password):
        
        global logkey_var
        global rowname
        global rowict
        global rowweb
        global rownet1
        global rownet2
        global rowpro1
        global rowpro2
        #Create database
        notindb = True
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT(Melli_code text, Name text, Last_Name text, Father_Name text, Phone int, Email text, Password text, ICDL1 number, Algorithms number, Network number, Web number)''')
        cursor.execute('''SELECT * from STUDENT''')
        row = cursor.fetchall()
        for r in row :
            #--------------------------------------------------
            if r[0]==code and r[6]== password:
                notindb = False
                tk.messagebox.showinfo("! خطا",".شما قبلا در سامانه عضو شده ايد")
                msg = tk.messagebox.askquestion("ورود", "آيا مايل هستيد که وارد سامانه شويد؟")
                if msg == 'yes':
                    self.name_var.set("")
                    self.lname_var.set("")
                    self.fname_var.set("")
                    self.code_var.set("")
                    self.email_var.set("")
                    self.phone_var.set("")
                    self.pw_var.set("")
                    self.pwagain_var.set("")
                    loginvar(code)
                    self.login()
                    self.show_frame("User")
                else:
                    logoutvar()
                    self.pwagain_var.set("")
                    mftdb.commit()
                    mftdb.close()
                break
            #--------------------------------------------------
            elif r[0]==code and r[6]!= password:
                notindb = False
                tk.messagebox.showinfo("! خطا",".شما قبلا در سامانه عضو شده ايد")
                msg = tk.messagebox.askquestion("ورود", "آیا رمز عبور خود را فراموش کرده اید؟")
                if msg == 'yes':
                    msg1 = tk.messagebox.askquestion("ورود", "آيا قصد ورود داريد؟")
                    if msg1 == 'yes':
                        logoutvar()
                        self.gotopage("Forgetpsw")
                    else:
                        self.pwagain_var.set("")
                else:
                    msg1 = tk.messagebox.askquestion("ورود", "آيا قصد ورود داريد؟")
                    if msg1 == 'yes':
                        logoutvar()
                        self.gotopage("SigninPage")
                    else:
                        logoutvar()
                        self.pwagain_var.set("")
                mftdb.commit()
                mftdb.close()
                break
            #--------------------------------------------------
            elif r[0]!=code and r[6]!= password:
                notindb = True
        #----------------------------------------------------------------------------------------------------------------
        if notindb or row==[]:
            loginvar(code)
            self.show_frame("User")

            alist = [code,name,lname,fname,phone,email,"",'notregister','notregister','notregister','notregister']
            record = [(code,name,lname,fname,phone,email,password,'notregister','notregister','notregister','notregister')]

            cursor.executemany('''INSERT INTO STUDENT values(?,?,?,?,?,?,?,?,?,?,?)''',record)
            mftdb.commit()
            mftdb.close()
            #--------------------------------------------------
            namelist(alist)

            self.name_var.set("")
            self.lname_var.set("")
            self.fname_var.set("")
            self.code_var.set("")
            self.email_var.set("")
            self.phone_var.set("")
            self.pw_var.set("")
            self.pwagain_var.set("")

#Class child4: Forgetpsw ------------------------------------------------------------------------------------------------------------------------------------------
class Forgetpsw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.show_frame = controller.show_frame
        self.login = controller.login
        self.gotopage = controller.gotopage
        #---------------------------------------
        global logkey_var
        self.code_var = controller.code_var
        self.email_var = controller.email_var
        self.phone_var = controller.phone_var
        self.pw_var = controller.pw_var
        self.pwagain_var = controller.pwagain_var

        self.err_var = controller.err_var
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #----Space--------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #----frames-------------------------------------------------------------
        forgetpsw_lblfr = tk.LabelFrame(self,text = "  فراموشي رمز عبور  ",labelanchor='ne',relief = 'ridge',font=controller.logfont)
        forgetpsw_lblfr.pack(side="top", fill="x",padx=5,pady=10,ipadx=10,ipady=5,)

        frgpsw_fr = tk.Frame(forgetpsw_lblfr)
        frgpsw_fr.pack(side="top", fill="x")

        fram1 = tk.Frame(frgpsw_fr)
        fram2 = tk.Frame(frgpsw_fr)
        fram3 = tk.Frame(frgpsw_fr)
        fram4 = tk.Frame(frgpsw_fr)
        fram5 = tk.Frame(frgpsw_fr)
        fram6 = tk.Frame(frgpsw_fr)
        framE = tk.Frame(frgpsw_fr)
        fram9 = tk.Frame(frgpsw_fr)
        frames = (fram1, fram2, fram3,fram4,fram5,fram6,framE,fram9)
        for fram in frames:
            fram.pack(side="top", fill="x")

        validationInt = self.register(self.only_int)
        validationChreng = self.register(self.only_engchar)
        #----1st Frame for codemelli---------------------------------------------------
        tk.Label(fram1,text = "  ",pady = 5).pack(side="top", fill="x",padx=50)
        lb_code = tk.Label(fram1,text = ":کد ملي                   ",
                           pady = 5,
                           font=controller.lblfont)
        lb_code.pack(side="right", fill="x",padx=4)
        lbl = tk.Label(fram1,text = "",pady = 5,font=controller.lblfont).pack(side="left", fill="x",padx=50)
        en_code = tk.Entry(fram1,textvariable = self.code_var,
                           font=controller.btnfont,bd = 2,
                           validate='key',validatecommand=(validationInt,'%S'))
        en_code.pack(side="left", fill="x",ipadx=60,padx = 2)
        #----2nd Frame for phonenumber-------------------------------------------------
        lb_phone = tk.Label(fram2,text = ":شماره همراه                   ",
                            pady = 5,
                            font=controller.lblfont)
        lb_phone.pack(side="right", fill="x",padx=4)
        lbl = tk.Label(fram2,text = "",pady = 5,font=controller.lblfont).pack(side="left", fill="x",padx=50)
        en_phone = tk.Entry(fram2,textvariable = self.phone_var,
                           font=controller.btnfont,bd = 2,
                           validate='key',validatecommand=(validationInt,'%S'))
        en_phone.pack(side="left", fill="x",ipadx=60,padx = 2)
        #----3rd Frame for email---------------------------------------------------------
        lb_email = tk.Label(fram3,text = ":ايميل                    ",
                            pady = 5,font=controller.lblfont)
        lb_email.pack(side="right", fill="x")

        lbl = tk.Label(fram3,text = "",pady = 5,font=controller.lblfont).pack(side="left", fill="x",padx=50)

        en_email = tk.Entry(fram3,textvariable = self.email_var,
                            font=controller.btnfont, bd = 2,
                            validate='key',validatecommand=(validationChreng,'%S'))
        en_email.pack(side="left", fill="x",ipadx=60,padx = 2)
        #----4th Frame for psw------------------------------------------------------
        lb_psw = tk.Label(fram5,text = ":رمز عبور جديد                   ",
                          pady = 5,
                          font=controller.lblfont)
        lb_psw.pack(side="right", fill="x",padx=4)
        lbl = tk.Label(fram5,text = "", pady = 5,font=controller.lblfont).pack(side="left", fill="x",padx=35)
        #showpsw
        show_btn1 = tk.Button(fram5,image=controller.tkshow,cursor="hand2",
                             command=lambda: controller.show_hide_psw(show_btn1,en_psw,0),
                             pady = 5, bd =0)
        show_btn1.pack(side="left", fill="x",padx=2)

        en_psw = tk.Entry(fram5,textvariable = self.pw_var,
                          font=controller.btnfont,show="*",bd = 2,
                          validate='key',validatecommand=(validationChreng,'%S'))
        en_psw.pack(side="left", fill="x",ipadx=60)
        #----5th Frame for againpsw------------------------------------------------------
        lb_pswagain = tk.Label(fram6,text = ":تکرار رمز عبور جديد                   ",
                pady = 5,
                font=controller.lblfont)
        lb_pswagain.pack(side="right", fill="x",padx=4)

        lbl = tk.Label(fram6,text = "",pady = 5,font=controller.lblfont).pack(side="left", fill="x",padx=35)
        #showagainpsw
        show_btn2 = tk.Button(fram6,image=controller.tkshow,cursor="hand2",
                             command=lambda: controller.show_hide_psw(show_btn2,en_pswagain,0),
                             pady = 5, bd =0)
        show_btn2.pack(side="left", fill="x",padx=2)

        en_pswagain = tk.Entry(fram6,textvariable = self.pwagain_var,
                               font=controller.btnfont, bd = 2, show="*",
                               validate='key',validatecommand=(validationChreng,'%S'))
        en_pswagain.pack(side="left", fill="x",ipadx=60)


        self.Err_lbl = tk.Label(framE,text=self.err_var.get(), fg = "red",
                                 font=controller.lblfont)
        self.Err_lbl.pack(side="top", fill="x",padx=2)
        #----Submit_btn---------------------------------------------------------
        # Button that will call the submit function
        tk.Label(fram9,text = "",font=controller.lblfont).pack(side="left", fill="x",padx=45)
        self.sub_btn=tk.Button(fram9,text = 'تغيير رمز عبور',
                               fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9", font = controller.btnfont ,cursor='hand2',
                               command = lambda: self.changepsw(), state = 'disable')
        self.sub_btn.pack(side="left",anchor='w', ipadx=30,pady=10)
        #----signin_btn---------------------------------------------------------
        # Button that will call the signin function
        tk.Label(fram9,text = "",font=controller.lblfont).pack(side="right", fill="x",padx=45)
        self.signin_btn=tk.Button(fram9,text = 'ورود به پنل کاربر',font=controller.btnfont,
                                  fg="black", disabledforeground = "#85b1da",
                                  bg="#a9d9f4",cursor='hand2',
                                  command = lambda: controller.gotopage("SigninPage"), state = 'normal')
        self.signin_btn.pack(side="right",anchor='w', ipadx=30,pady=10)
        #-----------------------------------------------------------------------
        self.code_var.trace('w',self.btn_enable)
        self.email_var.trace('w',self.btn_enable)
        self.phone_var.trace('w',self.btn_enable)
        self.pw_var.trace('w',self.btn_enable)
        self.pwagain_var.trace('w',self.btn_enable)
        #----Footer-------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def only_int(self,Int):
        return Int.isdigit()
    #*--------------------------------------------------------------------------------------------------------------------------------
    def only_engchar(self,char):
        for i in char:
            if(32<=ord(i)<127):
                return True
            else:
                return False
    #*--------------------------------------------------------------------------------------------------------------------------------
    def btn_enable(self,*arg):
        d = self.code_var.get()
        e = self.email_var.get()
        f = self.phone_var.get()
        g = self.pw_var.get()
        h = self.pwagain_var.get()
        if d and e and f and g and h:
            self.sub_btn.configure(state = 'normal')
            self.signin_btn.configure(state = 'disable')
            self.Err_lbl.configure(text = self.err_var.get())
        else:
            self.sub_btn.configure(state = 'disable')
            self.signin_btn.configure(state = 'normal')
            self.Err_lbl.configure(text = self.err_var.get())
    #*--------------------------------------------------------------------------------------------------------------------------------
    def changepsw(self):
        global logkey_var
        code = self.code_var.get()
        phone = self.phone_var.get()
        pw = self.pw_var.get()
        pwagain = self.pwagain_var.get()
        email = self.email_var.get()
        email = email.lower()
        #**------------------------------------------------------------
        if pw == pwagain:
            password = self.pwagain_var.get()
            mftdb = sqlite3.connect('mft01.db')
            cursor = mftdb.cursor()
            cursor.execute('''SELECT * from STUDENT''')
            row = cursor.fetchall()
            dbcheck = False
            for r in row:
                #------------------------------------------------------------
                if code==r[0] and phone==r[4] and email==r[5] and password==r[6]:
                    loginvar(code)
                    tk.messagebox.showinfo("تغيير رمز عبور","نياز به تغيير رمز عبور نيست. :)")
                    if code=='0123456789':
                        self.s("Admin")
                    else:
                        self.gotopage("User")
                    self.err_var.set("")
                    self.Err_lbl.configure(text = self.err_var.get())
                    alist = [r[0],r[1],r[2],r[3],r[4],r[5],"",r[7],r[8],r[9],r[10]]
                    namelist(alist)
                    self.login()
                    dbcheck = True
                    break
                #------------------------------------------------------------
                elif code==r[0] and phone==r[4] and email==r[5]:
                    A = any(x.isupper() for x in password)
                    B = any(x.islower() for x in password)
                    C = any(x.isdigit() for x in password)
                    D = any(x.isalpha() for x in password)
                    E = len(password)>=8
                    if A and B and C and D and E:
                        if code=='0123456789':
                            self.gotopage("Admin")
                        else:
                            self.gotopage("User")
                        loginvar(code)
                        txt = "UPDATE STUDENT SET Password='"+password+"' WHERE Melli_code='"+code+"'"
                        cursor.execute(txt)
                        tk.messagebox.showinfo("تغيير رمز عبور",".رمز با موفقیت عوض شد")
                        alist = [r[0],r[1],r[2],r[3],r[4],r[5],"",r[7],r[8],r[9],r[10]]
                        namelist(alist)
                        self.login()
                        mftdb.commit()
                        dbcheck = True
                        self.err_var.set("")
                        self.Err_lbl.configure(text = self.err_var.get())
                        break
                    if D==False:
                        tk.messagebox.showinfo("! خطا",".رمز عبور بايد شامل حداقل دو حرف باشد")
                        self.pwagain_var.set("")
                        password = ""
                    if D:
                        if A==False:
                            tk.messagebox.showinfo("! خطا",".رمز عبور بايد شامل حداقل يک حرف بزرگ باشد")
                            self.pwagain_var.set("")
                            password = ""
                        if B==False:
                            tk.messagebox.showinfo("! خطا",".رمز عبور بايد شامل حداقل يک حرف کوچک باشد")
                            self.pwagain_var.set("")
                            password = ""
                        if C==False:
                            tk.messagebox.showinfo("! خطا",".رمز عبور بايد شامل حداقل يک عدد باشد")
                            self.pwagain_var.set("")
                            password = ""
                    if E==False:
                        tk.messagebox.showinfo("! خطا",".طول رمز عبور بايد بيشتر از 8 کاراکتر باشد")
                        self.pwagain_var.set("")
                        password = ""
                    dbcheck = True
                    break
                #------------------------------------------------------------
                else: dbcheck = False
            #--------------------------------------------------------------------------------------------------------------------
            if dbcheck == False:
                tk.messagebox.showinfo("تغيير رمز عبور",".عدم هماهنگي اطلاعات کاربر، لطفا در وارد کردن اطلاعات دقت کنيد")
        #**------------------------------------------------------------
        else:
            self.err_var.set(". عدم تشابه رمز عبور، لطفاً دوباره رمز خود را وارد کنید")
            self.Err_lbl.configure(text = self.err_var.get())
            self.pwagain_var.set("")

#Class child5: User ------------------------------------------------------------------------------------------------------------------------------------------
class User(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.show_frame = controller.show_frame
        self.gotopage = controller.gotopage
        self.signout = controller.signout
        self.tkimgrefresh = controller.tkimgrefresh
        #Variables--------------------------------------------------------------
        global logkey_var
        self.txt_pass_beg = tk.StringVar()
        self.txt_pass_ict = tk.StringVar()
        self.txt_pass_web = tk.StringVar()
        self.txt_pass_net = tk.StringVar()
        self.txt_pass_pro = tk.StringVar()
        #---------------------
        self.txt_reg_beg = tk.StringVar()
        self.txt_reg_ict = tk.StringVar()
        self.txt_reg_web = tk.StringVar()
        self.txt_reg_net = tk.StringVar()
        self.txt_reg_pro = tk.StringVar()
        #Fonts-----------------------------------------------------------------------------------
        self.Blblfont = controller.Blblfont
        self.lblfont = controller.lblfont
        self.btnfont = controller.btnfont
        self.logfont = controller.logfont
        self.title_font = controller.title_font
        self.font = controller.english_font
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #----Space--------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #-----------------------------------------------------------------------
        self.user_lfr = tk.LabelFrame(self,text = "  داشبورد من  ",labelanchor='ne',relief = 'ridge',font=self.logfont)
        self.user_lfr.pack(side="top", fill="x",padx=5,pady=1,ipadx=10,ipady=5,)

        self.fram1 = tk.Frame(self.user_lfr )
        self.fram2 = tk.Frame(self.user_lfr )
        self.fram3 = tk.Frame(self.user_lfr )
        self.fram4 = tk.Frame(self.user_lfr )
        self.fram5 = tk.Frame(self.user_lfr )

        for frame in (self.fram1, self.fram2, self.fram3, self.fram4, self.fram5):
            frame.pack(side="top", fill="x")

        self.lbl1 = tk.Label(self.fram1, text=".سلام. براي وارد شدن به پنل کاربري لطفا دکمه زير را فشار دهید",
                             font=controller.Blblfont)
        self.lbl1.pack(side="top",fill='x',padx = 25, ipadx=10,pady=10)

        self.btnuser = tk.Button(self.fram1,font=self.Blblfont, bg="#316ba9",fg="white", cursor="hand2",
                                     text = "  ورود  ",command=lambda: self.update())
        self.btnuser.pack(side="bottom",fill='x',padx = 25, ipadx=10,pady=10)
        #----Footer-------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def update(self):
        global logkey_var
        self.btnuser.pack_forget()
        #---------------------------------------
        name = rowname[1]
        lname = rowname[2]
        #---------------------------------------
        lbl_txt ="!" + "سلام " + name +" "+ lname + " عزيز "+"      "
        self.lbl1.configure(text=lbl_txt,anchor="e",pady=1)
        
        self.my_courses_fr = tk.Frame(self.user_lfr)
        self.my_courses_fr.pack(side="top", fill="x")
        buttonfr = tk.Frame(self.my_courses_fr)
        #---------------------------------------
        lblfr1 = tk.LabelFrame(self.my_courses_fr,text = "  دروس گذرانده شده  ",labelanchor='ne',relief = 'ridge',font=self.logfont)
        lblfr1.pack(side="top", fill="x",padx=5,pady=1,ipadx=10,ipady=5,)

        lblfr2 = tk.LabelFrame(self.my_courses_fr,text = "  دروس ثبت نام شده  ",labelanchor='ne',relief = 'ridge',font=self.logfont)
        lblfr2.pack(side="top", fill="x",padx=5,pady=1,ipadx=10,ipady=5,)
        #---------------------------------------
        self.txt_pass_beg.set("    ")
        self.txt_pass_ict.set("    ")
        self.txt_pass_web.set("    ")
        self.txt_pass_net.set("    ")
        self.txt_pass_pro.set("    ")
        #----------------------------------------
        self.txt_reg_beg.set("    ")
        self.txt_reg_ict.set("    ")
        self.txt_reg_web.set("    ")
        self.txt_reg_net.set("    ")
        self.txt_reg_pro.set("    ")
        #---------------------------------------
        self.frm_pass_beg = tk.Frame(lblfr1)
        self.frm_pass_ict = tk.Frame(lblfr1)
        self.frm_pass_web = tk.Frame(lblfr1)
        self.frm_pass_net = tk.Frame(lblfr1)
        self.frm_pass_pro = tk.Frame(lblfr1)
        
        self.frm_reg_beg = tk.Frame(lblfr2)
        self.frm_reg_ict = tk.Frame(lblfr2)
        self.frm_reg_web = tk.Frame(lblfr2)
        self.frm_reg_net = tk.Frame(lblfr2)
        self.frm_reg_pro = tk.Frame(lblfr2)
        #-------------------------------------------------------
        self.lbl_pass_beg = tk.Label(self.frm_pass_beg,text = "    ",anchor='w',font=self.font,justify="left")
        self.lbl_pass_ict = tk.Label(self.frm_pass_ict,text = "    ",anchor='w',font=self.font,justify="left")
        self.lbl_pass_web = tk.Label(self.frm_pass_web,text = "    ",anchor='w',font=self.font,justify="left")
        self.lbl_pass_net = tk.Label(self.frm_pass_net,text = "    ",anchor='w',font=self.font,justify="left")
        self.lbl_pass_pro = tk.Label(self.frm_pass_pro,text = "    ",anchor='w',font=self.font,justify="left")
        #-------------------------------------------------------
        self.lbl_reg_beg = tk.Label(self.frm_reg_beg,text = "    ",anchor='w',font=self.font,justify="left")
        self.lbl_reg_ict = tk.Label(self.frm_reg_ict,text = "    ",anchor='w',font=self.font,justify="left")
        self.lbl_reg_web = tk.Label(self.frm_reg_web,text = "    ",anchor='w',font=self.font,justify="left")
        self.lbl_reg_net = tk.Label(self.frm_reg_net,text = "    ",anchor='w',font=self.font,justify="left")
        self.lbl_reg_pro = tk.Label(self.frm_reg_pro,text = "    ",anchor='w',font=self.font,justify="left")
        #-------------------------------------------------------
        labels = [self.lbl_pass_beg, self.lbl_pass_ict, self.lbl_pass_web, self.lbl_pass_net, self.lbl_pass_pro, self.lbl_reg_beg, self.lbl_reg_ict, self.lbl_reg_web, self.lbl_reg_net, self.lbl_reg_pro]
        for lbl in labels:
           lbl.pack(side="top", fill="x", ipadx=5, anchor ="w",pady=1)
        self.refresh()
        buttonfr.pack(side="top", fill="x")
        
        btnuser1 = tk.Button(buttonfr,font=self.Blblfont, bg="#316ba9",fg="white",cursor="hand2",
                                 text = "  ثبت نام درس  ",command=lambda: self.info_changeframe())
        btnuser1.pack(side="right",padx=5, ipadx=180,pady=10)
        btnref = tk.Button(buttonfr, image=self.tkimgrefresh,
                             bd = 0, cursor='hand2',
                           command=lambda: self.refresh())
        btnref.pack(side='left',padx=5, ipadx=15)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def info_changeframe(self):
        tk.messagebox.showinfo("! هشدار",".لطفا پس از برداشتن درس صفحه را رفرش کنيد")
        self.show_frame("SET_CRS")
    #*--------------------------------------------------------------------------------------------------------------------------------
    def refresh(self):
        global logkey_var
        global rowname
        global rowict
        global rowweb
        global rownet1
        global rownet2
        global rowpro1
        global rowpro2
        #---------------------------------------------------
        #for changeuser information
        name = rowname[1]
        lname = rowname[2]
        #---------------------------------------
        lbl_txt ="!" + "سلام " + name +" "+ lname + " عزيز "+"      "
        self.lbl1.configure(text=lbl_txt,anchor="e",pady=1)
        try:
            self.frm_pass_beg.pack_forget()
            self.frm_pass_ict.pack_forget()
            self.frm_pass_web.pack_forget()
            self.frm_pass_net.pack_forget()
            self.frm_pass_pro.pack_forget()
            #------------------------------
            self.frm_reg_beg.pack_forget()
            self.frm_reg_ict.pack_forget()
            self.frm_reg_web.pack_forget()
            self.frm_reg_net.pack_forget()
            self.frm_reg_pro.pack_forget()
        except:
            pass
        #-----------------------------------
        STUDENT = ['Melli_code','Name','Last_Name','Father_Name','Phone','Email','Password','ICDL1','Algorithms','Network','Web1']
        net1 = ['Winlo','Server1','Server2','Server3','Exchange','Vmware','VDI']
        net2 = ["CCNA", "CCNA security","CCNP","CEH", "Lpic1", "Lpic2"]
        STUDENT1 = ["ICDL1","Algorithms",'Network','Web']
        pro1 = ["Python", "ML", "Deep Learning","Image Proccessing","C++","C#","SQL","ASP.NET","Java Script", "Block Chain"]
        pro2 = ["Java","Java SE","Java EE","Android","Android with Kotlin","Android with Java","IOS"]
        ict = ["ICDL2","Excel Expert","Power BI"]
        web = ["Web2","Web3","React","Node JS","PHP","Django","Wordpress","Woocommerce","UI/UX","Seo"]
        #-----------------
        pass_crs_beg = []
        pass_crs_ict = []
        pass_crs_web = []
        pass_crs_net1 = []
        pass_crs_net2 = []
        pass_crs_pro1 = []
        pass_crs_pro2 = []
        #-----------------
        reg_crs_beg = []
        reg_crs_ict = []
        reg_crs_web = []
        reg_crs_net1 = []
        reg_crs_net2 = []
        reg_crs_pro1 = []
        reg_crs_pro2 = []
        #---------------------------------------
        for i in range(len(rowname)):
            if rowname[i] == 'register':
                if STUDENT[i] not in reg_crs_beg:
                    reg_crs_beg.append(STUDENT[i])
            elif rowname[i] == 'pass':
                if STUDENT[i] not in pass_crs_beg:
                    pass_crs_beg.append(STUDENT[i])
        #---------------------------------------
        for i in range(len(rowict)):
            if rowict[i] == 'register':
                if ict[i] not in reg_crs_ict:
                    reg_crs_ict.append(ict[i])
            elif rowict[i] == 'pass':
                if ict[i] not in pass_crs_ict:
                    pass_crs_ict.append(ict[i])
        #---------------------------------------
        for i in range(len(rowweb)):
            if rowweb[i] == 'register':
                if web[i] not in reg_crs_web:
                    reg_crs_web.append(web[i])
            elif rowweb[i] == 'pass':
                if web[i] not in pass_crs_web:
                    pass_crs_web.append(web[i])
        #---------------------------------------
        for i in range(len(rownet1)):
            if rownet1[i] == 'register':
                if net1[i] not in reg_crs_net1:
                    reg_crs_net1.append(net1[i])
            elif rownet1[i] == 'pass':
                if net1[i] not in pass_crs_net1:
                    pass_crs_net1.append(net1[i])
        #---------------------------------------
        for i in range(len(rownet2)):
            if rownet2[i] == 'register':
                if net2[i] not in reg_crs_net2:
                    reg_crs_net2.append(net2[i])
            elif rownet2[i] == 'pass':
                if net2[i] not in pass_crs_net2:
                    pass_crs_net2.append(net2[i])
        #---------------------------------------
        for i in range(len(rowpro1)):
            if rowpro1[i] == 'register':
                if pro1[i] not in reg_crs_pro1:
                    reg_crs_pro1.append(pro1[i])
            elif rowpro1[i] == 'pass':
                if pro1[i] not in pass_crs_pro1:
                    pass_crs_pro1.append(pro1[i])
        #---------------------------------------
        for i in range(len(rowpro2)):
            if rowpro2[i] == 'register':
                if pro2[i] not in reg_crs_pro2:
                    reg_crs_pro2.append(pro2[i])
            elif rowpro2[i] == 'pass':
                if pro2[i] not in pass_crs_pro2:
                    pass_crs_pro2.append(pro2[i])
        #---------------------------------------
        txt_pass_beg = "    "
        txt_pass_ict = "    "
        txt_pass_web = "    "
        txt_pass_net = "    "
        txt_pass_pro = "    "
        #---------------------
        txt_reg_beg = "    "
        txt_reg_ict = "    "
        txt_reg_web = "    "
        txt_reg_net = "    "
        txt_reg_pro = "    "
        #-----------------------------------------------------------------------------------------
        if pass_crs_beg!=[]:
            for i in pass_crs_beg:
                txt_pass_beg = txt_pass_beg + i +" - "
        #-------------------------------------------------
        if pass_crs_ict!=[]:
            txt_pass_ict = txt_pass_ict + "ICT: "
            for i in pass_crs_ict:
                txt_pass_ict = txt_pass_ict + i +" - "
        #-------------------------------------------------
        if pass_crs_web!=[]:
            n = 0
            txt_pass_web = txt_pass_web + "Web: "
            for i in pass_crs_web:
                if n%4!=0 or n==0:
                    txt_pass_web = txt_pass_web + i +" - "
                    n = n + 1
                else:
                    txt_pass_web = txt_pass_web + i +" \n"+"    "
                    n = n + 1
        #-------------------------------------------------
        if pass_crs_net1!=[]:
            n = 0
            txt_pass_net = txt_pass_net + "Network: "
            for i in pass_crs_net1:
                if n%5!=0 or n==0:
                    txt_pass_net = txt_pass_net + i +" - "
                    n = n + 1
                else:
                    txt_pass_net = txt_pass_net + i +" \n"+"    "
                    n = n + 1
        if pass_crs_net2!=[]:
            if txt_pass_net=="    ":
                n=0
                txt_pass_net = txt_pass_net + "Network: "
            elif txt_pass_net!="    " and n>5 and n%5!=0:
                pass
            else:
                n=0
                txt_pass_net = txt_pass_net + "\n"+"    "
            for i in pass_crs_net2:
                if n%7!=0 or n==0 or n==7:
                    txt_pass_net = txt_pass_net + i +" - "
                    n = n + 1
                else:
                    txt_pass_net = txt_pass_net + i +" \n"+"    "
                    n = n + 1
        #-------------------------------------------------
        if pass_crs_pro1!=[]:
            n=0
            txt_pass_pro = txt_pass_pro + "Programming: "
            for i in pass_crs_pro1:
                if n==3:
                    txt_pass_pro = txt_pass_pro + i +" \n"+"    "
                    n = n + 1
                elif n!=3 or n==0 or n%4!=0:
                    txt_pass_pro = txt_pass_pro + i +" - "
                    n = n + 1
                else:
                    txt_pass_pro = txt_pass_pro + i +" \n"+"    "
                    n = n + 1
        if pass_crs_pro2!=[]:
            if txt_pass_pro=="    ":
                txt_pass_pro = txt_pass_pro + "Programming: "
            else:
                txt_pass_pro = txt_pass_pro +" \n"+"    "
            n=0
            for i in pass_crs_pro2:
                if n==4:
                    txt_pass_pro = txt_pass_pro + i +" \n"+"    "
                    n = n + 1
                elif n!=4 or n==0 or n%4!=0:
                    txt_pass_pro = txt_pass_pro + i +" - "
                    n = n + 1
                else:
                    txt_pass_pro = txt_pass_pro + i +" \n"+"    "
        #-------------------------------------------------
        if reg_crs_beg!=[]:
            for i in reg_crs_beg:
                txt_reg_beg = txt_reg_beg + i +" - "
        #-------------------------------------------------
        if reg_crs_ict!=[]:
            txt_reg_ict = txt_reg_ict + "ICT: "
            for i in reg_crs_ict:
                txt_reg_ict = txt_reg_ict + i +" - "
        #-------------------------------------------------
        if reg_crs_web!=[]:
            n = 0
            txt_reg_web = txt_reg_web + "Web: "
            for i in reg_crs_web:
                if n%5!=0 or n==0:
                    txt_reg_web = txt_reg_web + i +" - "
                    n = n + 1
                else:
                    txt_reg_web = txt_reg_web + i +" \n"+"    "
                    n = n + 1
        #-------------------------------------------------
        if reg_crs_net1!=[]:
            n = 0
            txt_reg_net = txt_reg_net + "Network: "
            for i in reg_crs_net1:
                if n%5!=0 or n==0:
                    txt_reg_net = txt_reg_net + i +" - "
                    n = n + 1
                else:
                    txt_reg_net = txt_reg_net + i +" \n"+"    "
                    n = n + 1
        if reg_crs_net2!=[]:
            if txt_reg_net=="    ":
                n=0
                txt_reg_net = txt_reg_net + "Network: "
            for i in reg_crs_net2:
                if n%5!=0 or n==0:
                    txt_reg_net = txt_reg_net + i +" - "
                    n = n + 1
                else:
                    txt_reg_net = txt_reg_net + i +" \n"+"    "
                    n = n + 1
        #-------------------------------------------------
        if reg_crs_pro1!=[]:
            n=0
            txt_reg_pro = txt_reg_pro + "Programming: "
            for i in reg_crs_pro1:
                if n==3:
                    txt_reg_pro = txt_reg_pro + i +" \n"+"    "
                    n = n + 1
                elif n!=3 or n==0 or n%4!=0:
                    txt_reg_pro = txt_reg_pro + i +" - "
                    n = n + 1
                else:
                    txt_reg_pro = txt_reg_pro + i +" \n"+"    "
                    n = n + 1
        if reg_crs_pro2!=[]:
            if txt_reg_pro=="    ":
                txt_reg_pro = txt_reg_pro + "Programming: "
            else:
                txt_reg_pro = txt_reg_pro +" \n"+"    "
            n=0
            for i in reg_crs_pro2:
                if n==4:
                    txt_reg_pro = txt_reg_pro + i +" \n"+"    "
                    n = n + 1
                elif n!=4 or n==0 or n%4!=0:
                    txt_reg_pro = txt_reg_pro + i +" - "
                    n = n + 1
                else:
                    txt_reg_pro = txt_reg_pro + i +" \n"+"    "
        #-------------------------------------------------------------------------------------------------
        if txt_pass_beg=="    " and txt_pass_ict=="    " and txt_pass_web=="    " and txt_pass_net=="    " and txt_pass_pro=="    ":
            txt_pass_beg = "!شما درسي را نگذرانده ايد    "
        if txt_reg_beg=="    " and txt_reg_ict=="    " and txt_reg_web=="    " and txt_reg_net=="    " and txt_reg_pro=="    ":
            txt_reg_beg = "!درسي در حال حاضر ثبت نام نشده است    "
        #-------------------------------------------------------------------------------------------------
        if  txt_pass_beg == "!شما درسي را نگذرانده ايد    ":
            self.lbl_pass_beg.configure(anchor ="e",font=self.logfont)
        else:
            self.lbl_pass_beg.configure(anchor ="w",font=self.font)
            
        #--------------------------------------------------------
        if txt_reg_beg == "!درسي در حال حاضر ثبت نام نشده است    ":
            self.lbl_reg_beg.configure(anchor ="e",font=self.logfont)
        else:
            self.lbl_reg_beg.configure(anchor ="w",font=self.font)
        #---------------------------------------------------------------------------------------------------   
        self.lbl_pass_beg.config(text = txt_pass_beg)
        self.lbl_pass_ict.config(text = txt_pass_ict)
        self.lbl_pass_web.config(text = txt_pass_web)
        self.lbl_pass_net.config(text = txt_pass_net)
        self.lbl_pass_pro.config(text = txt_pass_pro)
        
        self.lbl_reg_beg.config(text = txt_reg_beg)
        self.lbl_reg_ict.config(text = txt_reg_ict)
        self.lbl_reg_web.config(text = txt_reg_web)
        self.lbl_reg_net.config(text = txt_reg_net)
        self.lbl_reg_pro.config(text = txt_reg_pro)
        #-----------------------------------------------------------------------------------------------------
        if txt_pass_beg != "    ":
            self.frm_pass_beg.pack(side="top", fill="x",anchor ="w",pady=1)
        if txt_pass_ict != "    ":
            self.frm_pass_ict.pack(side="top", fill="x",anchor ="w",pady=1)
        if txt_pass_web != "    ":
            self.frm_pass_web.pack(side="top", fill="x",anchor ="w",pady=1)
        if txt_pass_net != "    ":
            self.frm_pass_net.pack(side="top", fill="x",anchor ="w",pady=1)
        if txt_pass_pro != "    ":
            self.frm_pass_pro.pack(side="top", fill="x",anchor ="w",pady=1)
        #-------------------------------------------------------
        if txt_reg_beg != "    ":
            self.frm_reg_beg.pack(side="top", fill="x",anchor ="w",pady=1)
        if txt_reg_ict != "    ":
            self.frm_reg_ict.pack(side="top", fill="x",anchor ="w",pady=1)
        if txt_reg_web != "    ":
            self.frm_reg_web.pack(side="top", fill="x",anchor ="w",pady=1)
        if txt_reg_net != "    ":
            self.frm_reg_net.pack(side="top", fill="x",anchor ="w",pady=1)
        if txt_reg_pro != "    ":
            self.frm_reg_pro.pack(side="top", fill="x",anchor ="w",pady=1)
            
#Class child6: Change_User ------------------------------------------------------------------------------------------------------------------------------------------
class Change_User(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.show_frame = controller.show_frame
        self.gotopage =  controller.gotopage
        self.signout = controller.signout2
        self.tkhide = controller.tkhide
        self.tkshow = controller.tkshow
        self.show_hide_psw = controller.show_hide_psw
        self.dbname = controller.dbname
        #Variables--------------------------------------------------------------
        global logkey_var
        self.name_var = controller.name_var
        self.lname_var = controller.lname_var
        self.fname_var = controller.fname_var
        self.code_var = controller.code_var
        self.email_var = controller.email_var
        self.phone_var = controller.phone_var
        self.pw_var = controller.pw_var
        self.pwagain_var = controller.pwagain_var
        self.err_var = controller.err_var
        self.Err_lbl_email_txt = controller.Err_lbl_email_txt
        #Fonts-----------------------------------------------------------------------------------
        self.Blblfont = controller.Blblfont
        self.lblfont = controller.lblfont
        self.btnfont = controller.btnfont
        self.logfont = controller.logfont
        self.title_font = controller.title_font
        self.font = controller.english_font
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #----Space--------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #----frames-------------------------------------------------------------
        self.chguser_lfr = tk.LabelFrame(self,text = "  تغيير اطلاعات کاربر  ",labelanchor='ne',relief = 'ridge',font=self.logfont)
        self.chguser_lfr.pack(side="top", fill="x",padx=5,pady=10,ipadx=10,ipady=5,)
        #-----------------------------------------------------------------------
        self.fram1 = tk.Frame(self.chguser_lfr)
        self.fram2 = tk.Frame(self.chguser_lfr)
        self.fram3 = tk.Frame(self.chguser_lfr)
        self.fram4 = tk.Frame(self.chguser_lfr)
        self.fram5 = tk.Frame(self.chguser_lfr)
        self.fram6 = tk.Frame(self.chguser_lfr)
        self.fram7 = tk.Frame(self.chguser_lfr)
        self.framE = tk.Frame(self.chguser_lfr)
        self.fram8 = tk.Frame(self.chguser_lfr)
        
        frams = [self.fram1,self.fram2,self.fram3,self.fram4,self.fram5,self.fram6,self.fram7,self.framE,self.fram8]
        for frame in frams:
            frame.pack(side="top", fill="x")
        #-----------------------------------------------------------------------
        self.lbl1 = tk.Label(self.fram1, text=". براي تغيير اطلاعات کاربر لطفا بر روي دکمه زير کليک کنيد",
                             font=controller.Blblfont)
        self.lbl1.pack(side="top",fill='x',padx = 25, ipadx=10,pady=10, ipady = 10)
        #-----------------------------------------------------------------------
        self.btnuser = tk.Button(self.fram1,font=self.Blblfont, bg="#316ba9",fg="white",cursor='hand2',
                                     text = "  ورود  ",command=lambda: self.update())
        self.btnuser.pack(side="top",fill='x',padx = 20, ipadx=10,pady=20)
        #----Footer-------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def update(self):
        if rowname!=[] and logkey_var != "0123456789":
            self.lbl1.pack_forget()
            self.btnuser.pack_forget()
            self.user = " !عزيز "+rowname[2]+" "+rowname[1]
            self.name_var.set(rowname[1])
            self.lname_var.set(rowname[2])
            self.fname_var.set(rowname[3])
            self.phone_var.set(rowname[4])
            self.email_var.set(rowname[5])
            self.pw_var.set("")
            self.pwagain_var.set("")
            #rowname = [Melli_code,Name,Last_Name,Father_Name,Phone,Email,Password,ICDL1,Algorithms,Network,web]
            validationInt = self.register(self.only_int)
            validationChrper = self.register(self.only_perchar)
            validationChreng = self.register(self.only_engchar)
            #----1st Frame for name--------------------------------------------------------
            tk.Label(self.fram1,text = "  ",pady = 5).pack(side="top", fill="x",padx=50)
            lb_name = tk.Label(self.fram1,text = ":نام (فارسی)                  ",
                    font=self.lblfont)
            lb_name.pack(side="right", fill="x",padx=4)
            tk.Label(self.fram1,text = "  ",pady = 5).pack(side="left", fill="x",padx=50)

            en_name = tk.Entry(self.fram1,textvariable = self.name_var,
                               font=self.btnfont,bd = 2,
                               validate='key',validatecommand=(validationChrper,'%s'))
            en_name.pack(side="left", fill="x",ipadx=60)
            #----2nd Frame for lastname---------------------------------------------------
            lb_lname = tk.Label(self.fram2,text = ":نام خانوادگی (فارسی)                  ",
                                font=self.lblfont)
            lb_lname.pack(side="right", fill="x",padx=4)
            tk.Label(self.fram2,text = "  ",pady = 5).pack(side="left", fill="x",padx=50)

            en_lname = tk.Entry(self.fram2,textvariable = self.lname_var,
                                font=self.btnfont,bd = 2,
                                validate='key',validatecommand=(validationChrper,'%s'))
            en_lname.pack(side="left", fill="x",ipadx=60)
            #----3rd Frame for fname------------------------------------------------------
            lb_fname = tk.Label(self.fram3,text = ":نام پدر (فارسی)                  ",
                                pady = 5, font=self.lblfont)
            lb_fname.pack(side="right", fill="x",padx=4)
            tk.Label(self.fram3,text = "  ",pady = 5).pack(side="left", fill="x",padx=50)

            en_fname = tk.Entry(self.fram3,textvariable = self.fname_var,
                                font=self.btnfont,bd = 2
                                ,validate='key', validatecommand=(validationChrper,'%s'))
            en_fname.pack(side="left", fill="x",ipadx=60)
            #----4th Frame for phonenumber-------------------------------------------------
            lb_phone = tk.Label(self.fram4,text = ":شماره همراه                  ",
                                pady = 5,
                                font=self.lblfont)
            lb_phone.pack(side="right", fill="x",padx=4)
            tk.Label(self.fram4,text = "  ",pady = 5).pack(side="left", fill="x",padx=50)

            en_phone = tk.Entry(self.fram4,textvariable = self.phone_var,
                               font=self.btnfont,bd = 2,
                               validate='key',validatecommand=(validationInt,'%s'))
            en_phone.pack(side="left", fill="x",ipadx=60)
            #----5th Frame for email---------------------------------------------------------
            lb_email = tk.Label(self.fram5,text = ":ايميل                   ",
                                pady = 5,font=self.lblfont)
            lb_email.pack(side="right", fill="x")

            tk.Label(self.fram5,text = "  ",pady = 5).pack(side="left", fill="x",padx=35)

            self.Err_lbl_email = tk.Label(self.fram5,text="    ",fg = "red",
                                     font=self.lblfont)
            self.Err_lbl_email.pack(side="left", fill="x",padx=2)

            en_email = tk.Entry(self.fram5,textvariable = self.email_var,
                                font=self.btnfont, bd = 2,
                                validate='key', validatecommand=(validationChreng,'%s'))
            en_email.pack(side="left", fill="x",ipadx=60)
            #----6th Frame for psw------------------------------------------------------
            lb_psw = tk.Label(self.fram6,text = ":رمز عبور                  ",
                              pady = 5,
                              font=self.lblfont)
            lb_psw.pack(side="right", fill="x",padx=4)
            tk.Label(self.fram6,text = "  ",pady = 5).pack(side="left", fill="x",padx=35)
            #showpsw
            show_btn1 = tk.Button(self.fram6,image=self.tkshow,
                                 command=lambda: self.show_hide_psw(show_btn1,en_psw,0),
                                 pady = 5, bd =0)
            show_btn1.pack(side="left", fill="x",padx = 1)
            en_psw = tk.Entry(self.fram6,textvariable = self.pw_var,
                              font=self.btnfont,show="*",bd = 2,
                              validate='key', validatecommand=(validationChreng,'%s'))
            en_psw.pack(side="left", fill="x",anchor="center",padx=1,ipadx=60)
            #----7th Frame for againpsw------------------------------------------------------
            lb_pswagain = tk.Label(self.fram7,text = ":تکرار رمز عبور                  ",
                    pady = 5,font=self.lblfont)
            lb_pswagain.pack(side="right", fill="x",padx=4)
            tk.Label(self.fram7,text = "  ",pady = 5).pack(side="left", fill="x",padx=35)
            #showagainpsw
            show_btn2 = tk.Button(self.fram7,image=self.tkshow,
                                 command=lambda: self.show_hide_psw(show_btn2,en_pswagain,0),
                                 pady = 5, bd =0)
            show_btn2.pack(side="left", fill="x",padx = 1)
            en_pswagain = tk.Entry(self.fram7,textvariable = self.pwagain_var,
                    font=self.btnfont,bd = 2, show="*",
                                   validate='key', validatecommand=(validationChreng,'%s'))
            en_pswagain.pack(side="left", fill="x",padx=1,ipadx=60)
            #----8th Frame for errors ------------------------------------------------------
            self.Err_lbl = tk.Label(self.framE,text="", fg = "red",
                                     font=self.lblfont)
            self.Err_lbl.pack(side="top", fill="x",padx=2)
            #----Submit_btn---------------------------------------------------------
            # Button that will call the submit function
            self.sub_btn=tk.Button(self.fram8,text = 'ثبت',
                                   fg="#f0f0f0",disabledforeground = "#85b1d4",cursor='hand2',
                                   bg="#316ba9", font = self.btnfont ,
                                   command = lambda: self.submit(), state = 'disable')
            self.sub_btn.pack(side="left",anchor='w',padx = 85, ipadx=40,pady=10)
            #----signin_btn---------------------------------------------------------
            # Button that will call the signin function
            self.signin_btn=tk.Button(self.fram8,text = 'بازگشت به پنل کاربر',font=self.btnfont,
                                      fg="black", disabledforeground = "#85b1da",
                                      bg="#a9d9f4",cursor='hand2',
                                      command = lambda: self.show_frame("User"), state = 'normal')
            self.signin_btn.pack(side="left",anchor='w', ipadx=50,pady=10)
            #-----------------------------------------------------------------------
            self.name_var.trace('w',self.btn_enable)
            self.lname_var.trace('w',self.btn_enable)
            self.fname_var.trace('w',self.btn_enable)
            self.email_var.trace('w',self.btn_enable)
            self.phone_var.trace('w',self.btn_enable)
            self.pw_var.trace('w',self.btn_enable)
            self.pwagain_var.trace('w',self.btn_enable)
            #-----------------------------------------------------------------------
        else:
            fram1 = tk.Frame(self.chguser_lfr)
            fram1.pack(side="top", fill="x")
            lb_txt = tk.Label(fram1,text = "!اجازه دسترسي به اين صفحه را نداريد",
                font=controller.lblfont)
            lb_txt.pack(side="right", fill="x",padx=4)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def btn_enable(self,*arg):
        a = self.name_var.get()
        b = self.lname_var.get()
        c = self.fname_var.get()
        d = self.email_var.get()
        e = self.phone_var.get()
        f = self.pw_var.get()
        g = self.pwagain_var.get()
        if a and b and c and d and e and f and g:
            self.sub_btn.configure(state = 'normal')
            self.signin_btn.configure(state = 'disable')
            self.Err_lbl_email.configure(text = "    ")
            self.err_var.set("")
            self.Err_lbl.configure(text = self.err_var.get())
        else:
            self.sub_btn.configure(state = 'disable')
            self.signin_btn.configure(state = 'normal')
            self.err_var.set("    ")
            self.Err_lbl.configure(text = self.err_var.get())
    #*--------------------------------------------------------------------------------------------------------------------------------
    def only_engchar(self,char):
        for i in char:
            if(32<=ord(i)<127):
                return True
            else:
                return False
    #*--------------------------------------------------------------------------------------------------------------------------------
    def only_perchar(self,char):
        check = False
        if char.isalpha()==True:
            for i in char:
                if(1568<=ord(i)<1632 or 1649<=ord(i)<1752 or 1872<=ord(i)<1920):
                    check = True
                else:
                    check = False
            return check
        else:
            for i in char:
                if(ord(i)==32 or 48<=ord(i)<=57):
                    check = True
                else:
                    check = False
            return check
    #*--------------------------------------------------------------------------------------------------------------------------------
    def only_int(self,Int):
        return Int.isdigit()
    #*--------------------------------------------------------------------------------------------------------------------------------
    def submit(self):
        global logkey_var
        name = self.name_var.get()
        lname = self.lname_var.get()
        fname = self.fname_var.get()
        phone = self.phone_var.get()
        pw = self.pw_var.get()
        pwagain = self.pwagain_var.get()

        #emailcheck and pswcheck:------------------------------------
        email_checker = False

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex,self.email_var.get()):
            email_checker = True
        else:
            email_checker = False
        #------------------------------------------------------------
        if pw == pwagain and email_checker == True:
            email = self.email_var.get()
            password = self.pwagain_var.get()
            A = any(x.isupper() for x in password)
            B = any(x.islower() for x in password)
            C = any(x.isdigit() for x in password)
            D = any(x.isalpha() for x in password)
            E = len(password)>=8
            if A and B and C and D and E:
                self.submit_db(name,lname,fname,email,phone,password)
                
                self.err_var.set("")
                self.Err_lbl.configure(text = self.err_var.get())
                self.Err_lbl_email.configure(text = "    ")
    
            if D==False:
                tk.messagebox.showinfo("! خطا",".رمز عبور بايد شامل حداقل دو حرف باشد")
                self.pwagain_var.set("")
                password = ""
            if D:
                if A==False:
                    tk.messagebox.showinfo("! خطا",".رمز عبور بايد شامل حداقل يک حرف بزرگ باشد")
                    self.pwagain_var.set("")
                    password = ""
                if B==False:
                    tk.messagebox.showinfo("! خطا",".رمز عبور بايد شامل حداقل يک حرف کوچک باشد")
                    self.pwagain_var.set("")
                    password = ""
                if C==False:
                    tk.messagebox.showinfo("! خطا",".رمز عبور بايد شامل حداقل يک عدد باشد")
                    self.pwagain_var.set("")
                    password = ""
            if E==False:
                tk.messagebox.showinfo("! خطا",".طول رمز عبور بايد بيشتر از 8 کاراکتر باشد")
                self.pwagain_var.set("")
                password = ""
        elif pw == pwagain and email_checker == False:
            self.err_var.set("!لطفا دوباره ايميل خود را وارد کنيد")
            self.Err_lbl.configure(text = self.err_var.get())
            self.Err_lbl_email.configure(text = "**")

        elif pw != pwagain and email_checker == False:
            self.pw_var.set("")
            self.pwagain_var.set("")
            self.err_var.set(". عدم تشابه رمز عبور و ایمیل اشتباه، لطفاً دوباره ایمیل و رمز عبور خود را وارد کنید")
            self.Err_lbl.configure(text = self.err_var.get())
            self.Err_lbl_email.configure(text = "**")

        elif pw != pwagain and email_checker == True:
            self.pw_var.set("")
            self.pwagain_var.set("")
            self.err_var.set(". عدم تشابه رمز، لطفاً دوباره رمز خود را وارد کنید")
            self.Err_lbl.configure(text = self.err_var.get())
            self.Err_lbl_email.configure(text = "    ")
            
        else:
            self.err_var.set("")
            self.Err_lbl.configure(text = self.err_var.get())
            self.Err_lbl_email.configure(text = "    ")
    #*--------------------------------------------------------------------------------------------------------------------------------
    def submit_db(self,name,lname,fname,email,phone,password):
        global logkey_var
        global rowname
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        password = self.pwagain_var.get()
        
        if rowname[1] == name and rowname[2] == lname and rowname[3] == fname and rowname[4] == phone and rowname[5] == email:
            cursor.execute('''SELECT * from STUDENT''')
            row = cursor.fetchall()
            for r in row :
                if r[0]==logkey_var and r[6]==password:
                    self.show_frame("User")
                    sett = True
                    txt1 = "."+name +" "+ lname + " عزيز "+"\n"+".اطلاعاتي تغيير نکرد"
                    tk.messagebox.showinfo("پيام",txt1)
                    self.pw_var.set("")
                    self.pwagain_var.set("")
                    break
                else:
                    sett = False
            if sett == False:
                txt = "UPDATE STUDENT SET Password=? WHERE Melli_code=?"
                cursor.execute(txt,(password,logkey_var))
                mftdb.commit()
                mftdb.close()
                txt1 = "."+name +" "+ lname + " عزيز "+"\n"+"."+"اطلاعات تغيير کرد! لطفا مجدد وارد شويد"
                tk.messagebox.showinfo("پيام",txt1)
                self.signout()
        else:
            passd = False
            dbchange = False
            verifyentry = False
            cursor.execute('''SELECT * from STUDENT''')
            row = cursor.fetchall()
            for r in row :
                if r[0]==logkey_var and r[6]==password:
                    passd = False
                    dbchange = False
                    break
                elif r[0]==logkey_var and r[6]!=password:
                    passd = True
                    dbchange = True
                    break
                else:
                     pass
            #-------------------------------------------------------------------------
            if rowname[1] != name:
                check = False
                if name.isalpha()==True:
                    for i in name:
                        if(1568<=ord(i)<1632 or 1649<=ord(i)<1752 or 1872<=ord(i)<1920):
                            check = True
                        else:
                            check = False
                else:
                    for i in name:
                        if(ord(i)==32 or 48<=ord(i)<=57):
                            check = True
                        else:
                            check = False
                if check==True:
                    txt = "UPDATE STUDENT SET Name=? WHERE Melli_code=?"
                    cursor.execute(txt,(name,logkey_var))
                    dbchange = True
                    verifyentry = True
                else:
                    tk.messagebox.showinfo("! خطا",".در فیلد نام فقط کاراکتر فارسي وارد کنيد")
                    self.pwagain_var.set("")
                    dbchange = False
                    verifyentry = False
            #-------------------------------------------------------------------------
            if rowname[2] != lname:
                check = False
                if lname.isalpha()==True:
                    for i in lname:
                        if(1568<=ord(i)<1632 or 1649<=ord(i)<1752 or 1872<=ord(i)<1920):
                            check = True
                        else:
                            check = False
                else:
                    for i in lname:
                        if(ord(i)==32 or 48<=ord(i)<=57):
                            check = True
                        else:
                            check = False
                if check==True:
                    txt = "UPDATE STUDENT SET Last_Name=? WHERE Melli_code=?"
                    cursor.execute(txt,(lname,logkey_var))
                    dbchange = True
                    verifyentry = True
                else:
                    tk.messagebox.showinfo("! خطا",".در فیلد نام خانوادگی فقط کاراکتر فارسي وارد کنيد")
                    self.pwagain_var.set("")
                    dbchange = False
                    verifyentry = False
            #-------------------------------------------------------------------------
            if rowname[3] != fname:
                check = False
                if fname.isalpha()==True:
                    for i in fname:
                        if(1568<=ord(i)<1632 or 1649<=ord(i)<1752 or 1872<=ord(i)<1920):
                            check = True
                        else:
                            check = False
                else:
                    for i in fname:
                        if(ord(i)==32 or 48<=ord(i)<=57):
                            check = True
                        else:
                            check = False
                if check==True:
                    txt = "UPDATE STUDENT SET Father_Name=? WHERE Melli_code=?"
                    cursor.execute(txt,(fname,logkey_var))
                    dbchange = True
                    verifyentry = True
                else:
                    tk.messagebox.showinfo("! خطا",".در فیلد نام پدر فقط کاراکتر فارسي وارد کنيد")
                    self.pwagain_var.set("")
                    dbchange = False
                    verifyentry = False
            #-------------------------------------------------------------------------
            if rowname[4] != phone:
                if phone.isdigit()==True:
                    if len(phone)==11:
                        phonchecker = True
                        txt = "UPDATE STUDENT SET Phone=? WHERE Melli_code=?"
                        cursor.execute(txt,(phone,logkey_var))
                        dbchange = True
                        verifyentry = True
                    else:
                        phonchecker = False
                        tk.messagebox.showinfo("! خطا",".شماره همراه بايد 11 رقمي باشد\nبه طور مثال : 09121010101")
                        self.pwagain_var.set("")
                        dbchange = False
                        verifyentry = False
                else:
                    tk.messagebox.showinfo("! خطا",".در فیلد تلفن همراه فقط عدد وارد کنيد")
                    self.pwagain_var.set("")
                    dbchange = False
                    verifyentry = False
            #-------------------------------------------------------------------------
            if rowname[5] != email:
                txt = "UPDATE STUDENT SET Email=? WHERE Melli_code=?"
                cursor.execute(txt,(email,logkey_var))
                dbchange = True
                verifyentry = True
            #-------------------------------------------------------------------------
            if passd == True and dbchange == True and verifyentry == True:
                txt = "UPDATE STUDENT SET Password=? WHERE Melli_code=?"
                cursor.execute(txt,(password,logkey_var))
                txt1 = "."+name +" "+ lname + " عزيز "+"\n"+"."+"اطلاعات تغيير کرد! لطفا مجدد وارد شويد"
                tk.messagebox.showinfo("پيام",txt1)
                self.signout()
            #-------------------------------------------------------------------------    
            elif passd == False and dbchange == True and verifyentry == True:
                txt1 = "."+name +" "+ lname + " عزيز "+"\n"+"."+"اطلاعات تغيير کرد"
                tk.messagebox.showinfo("پيام",txt1)
                tk.messagebox.showinfo("! هشدار",".براي مشاهده تغييرات در پنل کاربر صفحه را رفرش کنيد")
                mftdb.commit()
                mftdb.close()
                self.dbname()
                self.name_var.set(rowname[1])
                self.lname_var.set(rowname[2])
                self.fname_var.set(rowname[3])
                self.phone_var.set(rowname[4])
                self.email_var.set(rowname[5])
                self.pw_var.set("")
                self.pwagain_var.set("")
                self.show_frame("User")
            #-------------------------------------------------------------------------     
            elif password == False and dbchange == False and verifyentry == True:
                self.pw_var.set("")
                self.pwagain_var.set("")
                txt1 = "."+name +" "+ lname + " عزيز "+"\n"+".اطلاعاتي تغيير نکرد"
                tk.messagebox.showinfo("پيام",txt1)
                self.show_frame("User")
            elif verifyentry == False:
                pass
#Class child7: SET_CRS ------------------------------------------------------------------------------------------------------------------------------------------
class SET_CRS(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.show_frame = controller.show_frame
        global logkey_var
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #----Space--------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #----Lbl----------------------------------------------------------------
        ict_lfr = tk.LabelFrame(self,text = "  دوره هاي مجتمع فني  ",labelanchor='ne',relief = 'ridge',font=controller.logfont)
        ict_lfr.pack(side="top", fill="x",padx=5,pady=10,ipadx=10,ipady=5,)

        ict_fr = tk.Frame(ict_lfr)
        ict_fr.pack(side="top", fill="x")
        #------------------------------------------------------------------------
        fram1 = tk.Frame(ict_fr)
        fram2 = tk.Frame(ict_fr)
        fram3 = tk.Frame(ict_fr)
        fram4 = tk.Frame(ict_fr)
        fram5 = tk.Frame(ict_fr)
        fram6 = tk.Frame(ict_fr)
        
        for frame in (fram1, fram2, fram3, fram4, fram5, fram6):
            frame.pack(side="top", fill="x")
        #----Courses-------------------------------------------------------------
        co1_fr = tk.Frame(fram1)
        co1_fr.pack(side="top", fill="x")

        tk.Label(co1_fr,font=controller.btnfont).pack(side="right", padx=20)
        co1_lbl = tk.Label(co1_fr, text=" دوره هاي مهارت پايه ",font=controller.Blblfont)
        co1_lbl.pack(side="right", fill="x", padx = 1, pady = 20)

        co1_btn = tk.Button(co1_fr, text=" نمايش ", font=controller.btnfont,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",cursor="hand2",
                            command=lambda: controller.show_frame('ict'))
        co1_btn.pack(side="left", padx = 90, ipadx=60)
        #-------------------------------------------------------------------------
        co2_fr = tk.Frame(fram2)
        co2_fr.pack(side="top", fill="x")
        tk.Label(co2_fr,font=controller.btnfont).pack(side="right", padx=20)

        co2_lbl = tk.Label(co2_fr, text=" دوره هاي وب ",font=controller.Blblfont)
        co2_lbl.pack(side="right", fill="x", padx = 1, pady = 20)

        co2_btn = tk.Button(co2_fr, text=" نمايش ", font=controller.btnfont,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",cursor="hand2",
                            command=lambda: controller.show_frame('web'))
        co2_btn.pack(side="left", padx = 90, ipadx=60)
        #-------------------------------------------------------------------------
        co3_fr = tk.Frame(fram3)
        co3_fr.pack(side="top", fill="x")
        tk.Label(co3_fr,font=controller.btnfont).pack(side="right", padx=20)

        co3_lbl = tk.Label(co3_fr, text=" دوره هاي شبکه ",font=controller.Blblfont)
        co3_lbl.pack(side="right", fill="x", padx = 1, pady = 20)

        co3_btn = tk.Button(co3_fr, text=" نمايش ", font=controller.btnfont,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",cursor="hand2",
                            command=lambda: controller.show_frame('net'))
        co3_btn.pack(side="left", padx = 90, ipadx=60)
        #-------------------------------------------------------------------------
        co4_fr = tk.Frame(fram4)
        co4_fr.pack(side="top", fill="x")
        tk.Label(co4_fr,font=controller.btnfont).pack(side="right", padx=20)

        co4_lbl = tk.Label(co4_fr, text="1 دوره هاي برنامه نويسي ",font=controller.Blblfont)
        co4_lbl.pack(side="right", fill="x", padx = 1, pady = 20)

        co4_btn = tk.Button(co4_fr, text=" نمايش ", font=controller.btnfont, fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",cursor="hand2",
                            command=lambda: controller.show_frame('programming1'))
        co4_btn.pack(side="left", padx = 90, ipadx=60)
        #-------------------------------------------------------------------------
        co5_fr = tk.Frame(fram5)
        co5_fr.pack(side="top", fill="x")
        tk.Label(co5_fr,font=controller.btnfont).pack(side="right", padx=20)

        co5_lbl = tk.Label(co5_fr, text="2 دوره هاي برنامه نويسي ",font=controller.Blblfont)
        co5_lbl.pack(side="right", fill="x", padx = 1, pady = 20)

        co5_btn = tk.Button(co5_fr, text=" نمايش ", font=controller.btnfont, fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",cursor="hand2",
                            command=lambda: controller.show_frame('programming2'))
        co5_btn.pack(side="left", padx = 90, ipadx=60)
        #-------------------------------------------------------------------------
        ttk.Separator(fram6,orient = 'horizontal').pack(side='top',anchor='center',pady = 10, ipadx = 1000)
        self.back = tk.Button(fram6, text="بازگشت",font=controller.btnfont,cursor="hand2",
                              command=lambda: self.back_cr()
                              ,fg="black", disabledforeground = "#85b1da",bg="#a9d9f4",)
        self.back.pack(side="left", padx=30, pady=10, ipadx=50)
        #----Footer-------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def back_cr(self):
        global logkey_var
        global back
        global bk
        
        if logkey_var=="0123456789":
            self.show_frame("HomePage")
        
        elif logkey_var!="":
            if bk[0]=="HomePage" and bk[1]=="SET_CRS" or bk[1]=="HomePage" and bk[2]=="SET_CRS":
                self.show_frame("HomePage")
            elif bk[0]=="User" and bk[1]=="SET_CRS" or bk[1]=="User" and bk[2]=="SET_CRS":
                self.show_frame("User")
            elif bk[2]=="User" and bk[3]=="SET_CRS":
                self.show_frame("User")
            else:
                self.show_frame(bk[2])
        else:
            self.show_frame("HomePage")
        
#Class child8: ict ------------------------------------------------------------------------------------------------------------------------------------------
class ict(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.signout = controller.signout
        self.show_frame = controller.show_frame
        self.pishniyaz = controller.pishniyaz
        self.errpishniyaz = controller.errpishniyaz
        self.gotopage = controller.gotopage
        #-------------------------------------------
        global logkey_var
        global back
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #----Space--------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #----Lbl----------------------------------------------------------------
        ict_lfr = tk.LabelFrame(self,text = "  دروس مهارت پايه  ",labelanchor='ne',relief = 'ridge',font=controller.logfont)
        ict_lfr.pack(side="top", fill="x",padx=5,pady=10,ipadx=10,ipady=5,)

        ict_fr = tk.Frame(ict_lfr)
        ict_fr.pack(side="top", fill="x")
        #------------------------------------------------------------------------
        fram1 = tk.Frame(ict_fr)
        fram2 = tk.Frame(ict_fr)
        fram3 = tk.Frame(ict_fr)
        fram4 = tk.Frame(ict_fr)
        fram5 = tk.Frame(ict_fr)

        for frame in (fram1, fram2, fram3, fram4, fram5):
            frame.pack(side="top", fill="x")
        #----Lbl and btn-------------------------------------------------------------------
        label1 = tk.Label(fram1, text="ICDL1  دوره        ",font=controller.Blblfont)
        label1.pack(side="right", fill="x", pady=10)
        button1 = tk.Button(fram1, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_ict('ICDL1')
                            ,fg="#f0f0f0",cursor="hand2", bg="#316ba9",)
        button1.pack(side="left", padx=120, pady=10, ipadx=30)
        #-----------------------------------------------------------------------
        label2 = tk.Label(fram2, text="ICDL2  دوره        ",font=controller.Blblfont)
        label2.pack(side="right", fill="x", pady=10)
        button2 = tk.Button(fram2, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_ict('ICDL2')
                            ,fg="#f0f0f0",cursor="hand2", bg="#316ba9",)
        button2.pack(side="left", padx=120, pady=10, ipadx=30)
        #-----------------------------------------------------------------------
        label3 = tk.Label(fram3, text="Excel Expert  دوره        ",font=controller.Blblfont)
        label3.pack(side="right", fill="x")
        button3 = tk.Button(fram3, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_ict('Excel_Expert')
                            ,fg="#f0f0f0",cursor="hand2", bg="#316ba9",)
        button3.pack(side="left", padx=120, pady=10, ipadx=30)
        #-----------------------------------------------------------------------
        label4 = tk.Label(fram4, text="Power BI  دوره        ",font=controller.Blblfont)
        label4.pack(side="right", fill="x", pady=10)
        button4 = tk.Button(fram4, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_ict('Power_BI')
                            ,fg="#f0f0f0",cursor="hand2", bg="#316ba9",)
        button4.pack(side="left", padx=120, pady=10, ipadx=30)
        #-----------------------------------------------------------------------
        ttk.Separator(fram5,orient = 'horizontal').pack(side='top',anchor='center',pady = 10, ipadx = 1000)
        #-----------------------------------------------------------------------
        self.back = tk.Button(fram5, text="بازگشت",font=controller.btnfont,command=lambda: self.back_ict()
                              ,fg="black",bg="#a9d9f4",cursor="hand2",)
        self.back.pack(side="left", padx=50, pady=10, ipadx=50)
        #----Footer-------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def back_ict(self):
        global logkey_var
        global bk
        if logkey_var=="0123456789":
            if bk[2]=="SET_CRS":
                self.show_frame("SET_CRS")
            elif bk[2]=="HomePage":
                self.show_frame("HomePage")
            else:
            	self.show_frame("HomePage")
        elif logkey_var!="":
            if bk[2]=="SET_CRS":
                self.show_frame("SET_CRS")
            elif bk[2]=="HomePage":
                self.show_frame("HomePage")
            else:
                self.show_frame(bk[2])
        else:
            self.show_frame(back[0])
    #*--------------------------------------------------------------------------------------------------------------------------------
    def submit_ict(self,name):
        global rowname
        global rowict
        global rowweb
        global rowname
        global rowict
        global rowweb
        global rownet1
        global rownet2
        global rowpro1
        global rowpro2
        global back
        global logkey_var
        code = logkey_var
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        ict = ["ICDL2","Excel_Expert","Power_BI"]
        #rowict = [ICDL2,Excel,Power]
        if rowname!=[] and logkey_var !="0123456789":
            user = " !عزيز "+rowname[2]+" "+rowname[1]
            #------------------------------------------------------------------------------------------------------------------
            if name != "ICDL1":
                if rowict == []:
                    ictrow = [(logkey_var,'notregister','notregister','notregister')]
                    cursor.executemany('''INSERT INTO ict values(?,?,?,?)''',ictrow)
                    ictlist(['notregister','notregister','notregister'])
                    mftdb.commit()
                    mftdb.close()
            ICDL1 = self.pishniyaz(rowname[7])
            #name == "ICDL1":------------------------------------------------------------------
            if name == "ICDL1":
                self.errpishniyaz(True,"STUDENT","ICDL1","ICDL1",rowname[7],name)
            #name == "ICDL2":------------------------------------------------------------------
            elif name == "ICDL2":
                self.errpishniyaz(ICDL1,"ict","ICDL2","ICDL1",rowict[0],name)
            #name == "Excel_Expert":------------------------------------------------------------------
            elif name == "Excel_Expert":
                ICDL2 = self.pishniyaz(rowict[0])
                if ICDL1:
                   self.errpishniyaz(ICDL2,"ict","Excel Expert","ICDL2",rowict[1],name)
                else:
                   self.errpishniyaz(ICDL1,"ict","Excel Expert","ICDL1",rowict[1],name)
            #name == "Power_BI":------------------------------------------------------------------
            elif name == "Power_BI":
                ICDL2 = self.pishniyaz(rowict[0])
                Excel_Expert = self.pishniyaz(rowict[1])
                if ICDL1 and ICDL2:
                    self.errpishniyaz(Excel_Expert,"ict","Power BI","Excel Expert",rowict[2],name)
                elif ICDL1 and ICDL2 == False:
                    self.errpishniyaz(ICDL2,"ict","Power BI","ICDL2",rowict[2],name)
                else:
                    self.errpishniyaz(ICDL1,"ict","Power BI","ICDL1",rowict[2],name)
            else: pass
        #------------------------------------------------------------------------------------------------------------------
        elif logkey_var == "0123456789":
            tk.messagebox.showwarning("عدم اجازه دسترسي","!سلام ادمين عزيز. شما اجازه ثبت درس را نداريد")
        else:
            tk.messagebox.showwarning("عدم عضويت در سايت","!سلام! شما هنوز در سامانه عضو نشده ايد")
            ertxt2 = "آيا قصد وارد شدن به پنل کاربري را داريد؟"
            msg = tk.messagebox.askquestion("وارد شدن به پنل کاربري",ertxt2)
            if msg == 'yes':
                self.show_frame("SigninPage")
            else:
                pass

#Class child9: web ------------------------------------------------------------------------------------------------------------------------------------------
class web(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.show_frame = controller.show_frame
        self.pishniyaz = controller.pishniyaz
        self.errpishniyaz = controller.errpishniyaz
        self.gotopage = controller.gotopage
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #-----------------------------------------------------------------------
        #----Space--------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #----Lbl-------------------------------------------------------------
        web_lfr = tk.LabelFrame(self,text = "  دوره هاي وب  ",labelanchor='ne',relief = 'ridge',font=controller.logfont)
        web_lfr.pack(side="top", fill="x",padx=5,pady=5,ipadx=10)

        web_fr = tk.Frame(web_lfr)
        web_fr.pack(side="top", fill="x")
        lfram1 = tk.LabelFrame(web_lfr,text = "  بدون برنامه نويسي  ",labelanchor='ne',relief = 'ridge',font=controller.btnfont)
        lfram2 = tk.LabelFrame(web_lfr,text = "  فرانت اند  ",labelanchor='ne',relief = 'ridge',font=controller.btnfont)
        lfram3 = tk.LabelFrame(web_lfr,text = "  بک اند  ",labelanchor='ne',relief = 'ridge',font=controller.btnfont)
        for lframe in (lfram1, lfram2, lfram3):
            lframe.pack(side="top", fill="x",padx=5,ipadx=10,ipady=1,)
        #--------------------------------------------------------------------------------
        fram1 = tk.Frame(web_fr)
        fram2 = tk.Frame(web_fr)
        fram3 = tk.Frame(lfram1)
        fram4 = tk.Frame(lfram1)
        fram5 = tk.Frame(lfram2)
        fram6 = tk.Frame(lfram2)
        fram7 = tk.Frame(lfram3)
        fram8 = tk.Frame(lfram3)

        for frame in (fram1, fram2, fram3, fram4, fram5, fram6, fram7, fram8):
            frame.pack(side="top", fill="x")
        ttk.Separator(web_lfr,orient = 'horizontal').pack(side='top',anchor='center',pady = 5, ipadx = 1000)
        bfram = tk.Frame(web_lfr)
        bfram.pack(side="top", fill="x",padx=5,ipadx=8,ipady=5,)
        #----Lbl and btn-------------------------------------------------------------------
        tk.Label(fram1,font=controller.btnfont).pack(side="right", padx=13)
        label1 = tk.Label(fram1, text="Web1  دوره",font=controller.lblfont)
        label1.pack(side="right", fill="x", pady=12)

        tk.Label(fram1,font=controller.btnfont).pack(side="left", padx=23)
        button2 = tk.Button(fram1, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_web('Algorithms')
                            ,fg="#f0f0f0",cursor="hand2",
                               bg="#316ba9",)
        button2.pack(side="left", pady=10, ipadx=15)

        tk.Label(fram1,font=controller.btnfont).pack(side="left", padx=18)
        label2 = tk.Label(fram1, text="Algorithms دوره",font=controller.lblfont)
        label2.pack(side="left", fill="x", pady=12)

        tk.Label(fram1,font=controller.btnfont).pack(side="left", padx=10)
        button1 = tk.Button(fram1, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_web('web')
                            ,fg="#f0f0f0",cursor="hand2",
                               bg="#316ba9",)
        button1.pack(side="left", pady=10, ipadx=15)
        ttk.Separator(fram2,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #----------------------------------------------------------------------------------
        tk.Label(fram3,font=controller.btnfont).pack(side="right", padx=10)
        label3 = tk.Label(fram3, text="UI/UX  دوره",font=controller.lblfont)
        label3.pack(side="right", fill="x", pady=12)

        tk.Label(fram3,font=controller.btnfont).pack(side="left", padx=20)
        button4 = tk.Button(fram3, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_web('Wordpress')
                            ,fg="#f0f0f0",cursor="hand2",
                               bg="#316ba9",)
        button4.pack(side="left", pady=10, ipadx=15)

        tk.Label(fram3,font=controller.btnfont).pack(side="left", padx=16)
        label4 = tk.Label(fram3, text="Wordpress دوره",font=controller.lblfont)
        label4.pack(side="left", fill="x", pady=12)

        tk.Label(fram3,font=controller.btnfont).pack(side="left", padx=10)
        button3 = tk.Button(fram3, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_web('UI_UX')
                            ,fg="#f0f0f0",cursor="hand2",
                               bg="#316ba9",)
        button3.pack(side="left", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram4,font=controller.btnfont).pack(side="right", padx=10)
        label5 = tk.Label(fram4, text="Seo  دوره",font=controller.lblfont)
        label5.pack(side="right", fill="x", pady=12)


        tk.Label(fram4,font=controller.btnfont).pack(side="left", padx=20)
        button6 = tk.Button(fram4, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_web('Woocommerce')
                            ,fg="#f0f0f0",cursor="hand2",
                               bg="#316ba9",)
        button6.pack(side="left", pady=10, ipadx=15)
        tk.Label(fram4,font=controller.btnfont).pack(side="left", padx=3)
        label6 = tk.Label(fram4, text="Woocommerce دوره",font=controller.lblfont)
        label6.pack(side="left", fill="x", pady=12)
        tk.Label(fram4,font=controller.btnfont).pack(side="left", padx=10)
        button5 = tk.Button(fram4, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_web('Seo')
                            ,fg="#f0f0f0",cursor="hand2",
                               bg="#316ba9",)
        button5.pack(side="left", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram5,font=controller.btnfont).pack(side="right", padx=10)
        label7 = tk.Label(fram5, text=" Web2 دوره",font=controller.lblfont)
        label7.pack(side="right", fill="x", pady=12)

        tk.Label(fram5,font=controller.btnfont).pack(side="left", padx=20)
        button8 = tk.Button(fram5, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_web('React')
                            ,fg="#f0f0f0",cursor="hand2",
                               bg="#316ba9",)
        button8.pack(side="left", pady=10, ipadx=15)

        tk.Label(fram5,font=controller.btnfont).pack(side="left", padx=37)
        label8 = tk.Label(fram5, text="React  دوره",font=controller.lblfont)
        label8.pack(side="left", fill="x", pady=12)

        tk.Label(fram5,font=controller.btnfont).pack(side="left", padx=10)
        button7 = tk.Button(fram5, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_web('web2')
                            ,fg="#f0f0f0",cursor="hand2",
                               bg="#316ba9",)
        button7.pack(side="left", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram6,font=controller.btnfont).pack(side="right", padx=10)
        label9 = tk.Label(fram6, text="  Web3 دوره",font=controller.lblfont)
        label9.pack(side="right", fill="x", pady=12)

        tk.Label(fram6,font=controller.btnfont).pack(side="left", padx=20)
        button10 = tk.Button(fram6, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_web('Node_JS')
                            ,fg="#f0f0f0",cursor="hand2", bg="#316ba9",)
        button10.pack(side="left", pady=10, ipadx=15)

        tk.Label(fram6,font=controller.btnfont).pack(side="left", padx=26)
        label10 = tk.Label(fram6, text="NodeJS  دوره",font=controller.lblfont)
        label10.pack(side="left", fill="x", pady=8)

        tk.Label(fram6,font=controller.btnfont).pack(side="left", padx=10)
        button9 = tk.Button(fram6, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_web('web3')
                            ,fg="#f0f0f0",cursor="hand2",
                               bg="#316ba9",)
        button9.pack(side="left", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram7,font=controller.btnfont).pack(side="right", padx=10)
        label11 = tk.Label(fram7, text="Python دوره",font=controller.lblfont)
        label11.pack(side="right", fill="x", pady=12)

        tk.Label(fram7,font=controller.btnfont).pack(side="left", padx=20)
        button12 = tk.Button(fram7, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_web('Django')
                            ,fg="#f0f0f0",cursor="hand2",
                               bg="#316ba9",)
        button12.pack(side="left", pady=10, ipadx=15)

        tk.Label(fram7,font=controller.btnfont).pack(side="left", padx=34)

        label12 = tk.Label(fram7, text="Django دوره",font=controller.lblfont)
        label12.pack(side="left", fill="x", pady=12)

        tk.Label(fram7,font=controller.btnfont).pack(side="left", padx=10)
        button11 = tk.Button(fram7, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_web('python')
                            ,fg="#f0f0f0",cursor="hand2",
                               bg="#316ba9",)
        button11.pack(side="left", pady=10, ipadx=15)

        #----------------------------------------------------------------------------------
        tk.Label(fram8,font=controller.btnfont).pack(side="right", padx=10)


        label12 = tk.Label(fram8, text="Php  دوره",font=controller.lblfont)
        label12.pack(side="right", fill="x", pady=8)
        tk.Label(fram8,font=controller.btnfont).pack(side="right", padx=30)
        button12 = tk.Button(fram8, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_web('PHP')
                            ,fg="#f0f0f0",cursor="hand2",
                               bg="#316ba9",)
        button12.pack(side="right", pady=10, ipadx=15)

        tk.Label(fram8,font=controller.btnfont).pack(side="left", padx=1)
        #----------------------------------------------------------------------------------
        self.back = tk.Button(bfram, text="بازگشت",font=controller.btnfont, command=lambda: self.back_web()
                              ,fg="black",bg="#a9d9f4",cursor="hand2",)
        self.back.pack(side="left", pady=10, ipadx=50, padx=50)
        #----------------------------------------------------------------------------------
        #----Footer------------------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def back_web(self):
        global logkey_var
        global bk
        if logkey_var=="0123456789":
            if bk[2]=="SET_CRS":
                self.show_frame("SET_CRS")
            elif bk[2]=="HomePage":
                self.show_frame("HomePage")
            else:
            	self.show_frame("HomePage")
        elif logkey_var!="":
            if bk[2]=="SET_CRS":
                self.show_frame("SET_CRS")
            elif bk[2]=="HomePage":
                self.show_frame("HomePage")
            else:
                self.show_frame(bk[2])
        else:
            self.show_frame(back[0])

    #*--------------------------------------------------------------------------------------------------------------------------------
    def submit_web(self,name):
        global logkey_var
        global rowname
        global rowict
        global rowweb
        global rowname
        global rowict
        global rowweb
        global rownet1
        global rownet2
        global rowpro1
        global rowpro2
        global back
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        web = ["Web2","Web3","React","Node JS","PHP","Django","Wordpress","","UI/UX","Seo"]
        #rowict = [ICDL2,Excel,Power]
        #rowweb = [web2,web3,React,Node,PHP,Django,Wordpress,Woocommerce,UIUX,Seo]
        #errpishniyaz(self,pishniyaz,dbname,darsname,darspishniyaz,point,course)
        if rowname!=[] and logkey_var != "0123456789":
            self.back.configure(command=lambda: self.show_frame("User"))
            user = " !عزيز "+rowname[2]+" "+rowname[1]
            #------------------------------------------------------------------------------------------------------------------
            if name!="Algorithms" or  name != "web":
                if rowweb == []:
                    webrow = [(logkey_var,'notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister')]
                    cursor.executemany('''INSERT INTO web values(?,?,?,?,?,?,?,?,?,?,?)''',webrow)
                    weblist(['notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister'])
                    mftdb.commit()
            if name == "python" or  name == "Django":
                if rowpro1 == []:
                    pro1row = [(logkey_var,'notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister')]
                    cursor.executemany('''INSERT INTO pro1 values(?,?,?,?,?,?,?,?,?,?,?)''',pro1row)
                    pro1= ['notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister']
                    pro1list(pro1)
                    mftdb.commit()
            mftdb.close()
            #------------------------------------------------------------------------------------------------------------------
            icdl1 = self.pishniyaz(rowname[7])
            web1 = self.pishniyaz(rowname[10])
            #------------------------------------------------------------------------------------------------------------------
            #name == "Algorithms":------------------------------------------------------------------
            if name == "Algorithms":
                self.errpishniyaz(icdl1,"STUDENT","Algorithms","ICDL1",rowname[8],name)
            #name == "web":------------------------------------------------------------------
            elif  name == "web":
                self.errpishniyaz(icdl1,"STUDENT","Web1","ICDL1",rowname[10],name)
            #name == "web2":------------------------------------------------------------------
            elif name == "web2":
                if icdl1:
                    self.errpishniyaz(web1,"web","Web2","Web1",rowweb[0],name)
                else:
                    self.errpishniyaz(icdl1,"web","web2","ICDL1",rowweb[0],name)
            #name == "Wordpress":-------------------------------------------------------------
            elif name == "Wordpress":
                if icdl1:
                    self.errpishniyaz(web1,"web","Wordpress","Web1",rowweb[6],name)
                else:
                    self.errpishniyaz(icdl1,"web","Wordpress","ICDL1",rowweb[6],name)
            #name == "UI_UX":-----------------------------------------------------------------
            elif name == "UI_UX":
                if icdl1:
                    self.errpishniyaz(web1,"web","UI/UX","Web1",rowweb[8],name)
                else:
                    self.errpishniyaz(icdl1,"web","UI/UX","ICDL1",rowweb[8],name)
            #name == "Seo":-------------------------------------------------------------------
            elif name == "Seo":
                if icdl1:
                    self.errpishniyaz(web1,"web","Seo","Web1",rowweb[9],name)
                else:
                    self.errpishniyaz(icdl1,"web","Seo","ICDL1",rowweb[9],name)
            #name == "Woocommerce":-------------------------------------------------------------
            elif name == "Woocommerce":
                wordpress = self.pishniyaz(rowweb[6])
                if icdl1 and web1:
                    self.errpishniyaz(wordpress,"web","Woocommerce","Wordpress",rowweb[7],name)
                elif icdl1 and web1 == False:
                    self.errpishniyaz(web1,"web","Woocommerce","Web1",rowweb[7],name)
                else:
                    self.errpishniyaz(icdl1,"web","Woocommerce","ICDL1",rowweb[7],name)
            #name == "Web3":-------------------------------------------------------------
            elif name == "web3":
                web2 = self.pishniyaz(rowweb[0])
                if icdl1 and web1:
                    self.errpishniyaz(web2,"web","Web3","Web2",rowweb[1],name)
                elif icdl1 and web1 == False:
                    self.errpishniyaz(web1,"web","Web3","Web1",rowweb[1],name)
                else:
                     self.errpishniyaz(icdl1,"web","Web3","ICDL1",rowweb[1],name)
            #name == "React":-------------------------------------------------------------
            elif name == "React":
                web2 = self.pishniyaz(rowweb[0])
                web3 = self.pishniyaz(rowweb[1])
                if icdl1 and web1 and web2:
                    self.errpishniyaz(web3,"web","React","Web3",rowweb[2],name)
                elif icdl1 and web1 and web2 == False:
                    self.errpishniyaz(web2,"web","React","Web2",rowweb[2],name)
                elif icdl1 and web1 == False and web2 == False:
                    self.errpishniyaz(web1,"web","React","Web1",rowweb[2],name)
                else:
                    self.errpishniyaz(icdl1,"web","React","ICDL1",rowweb[2],name)
            #name == "Node_JS":-------------------------------------------------------------
            elif name == "Node_JS":
                web2 = self.pishniyaz(rowweb[0])
                web3 = self.pishniyaz(rowweb[1])
                if icdl1 and web1 and web2:
                    self.errpishniyaz(web3,"web","Node JS","Web3",rowweb[3],name)
                elif icdl1 and web1 and web2 == False:
                    self.errpishniyaz(web2,"web","Node JS","Web2",rowweb[3],name)
                elif icdl1 and web1 == False and web2 == False:
                    self.errpishniyaz(web1,"web","Node JS","Web1",rowweb[3],name)
                else:
                    self.errpishniyaz(icdl1,"web","Node JS","ICDL1",rowweb[3],name)
            #name == "python":-------------------------------------------------------------
            elif name == "python":
                Algorithms = self.pishniyaz(rowname[8])
                if icdl1:
                    self.errpishniyaz(Algorithms,"pro1",'Python',"Algorithms",rowpro1[0],name)
                else:
                    self.errpishniyaz(icdl1,"pro1",'Python','ICDL1',rowpro1[0],name)
            #name == "PHP":-------------------------------------------------------------
            elif name == "PHP":
                Algorithms = self.pishniyaz(rowname[8])
                if icdl1 and web1:
                    self.errpishniyaz(Algorithms,"web","PHP","Algorithms",rowweb[4],name)
                elif icdl1 and web1 == False:
                    self.errpishniyaz(web1,"web","PHP","Web1",rowweb[4],name)
                else:
                    self.errpishniyaz(icdl1,"web","PHP","ICDL1",rowweb[4],name)
            #name == "Django":-------------------------------------------------------------
            elif name == "Django":
                Algorithms = self.pishniyaz(rowname[8])
                Python = self.pishniyaz(rowpro1[0])
                if icdl1 and web1 and Algorithms:
                    self.errpishniyaz(Python,"web","Django","Python",rowweb[5],name)
                elif icdl1 and Algorithms and web1 == False:
                    self.errpishniyaz(web1,"web","Django","Web1",rowweb[5],name)
                elif icdl1 and web1 == False and Algorithms == False: 
                    self.errpishniyaz(Algorithms,"web","Django","Algorithms",rowweb[5],name)
                else:
                    self.errpishniyaz(icdl1,"web","Django","ICDL1",rowweb[5],name)
        #------------------------------------------------------------------------------------------------------------------
        elif logkey_var == "0123456789":
            tk.messagebox.showwarning("عدم اجازه دسترسي","!سلام ادمين عزيز. شما اجازه ثبت درس را نداريد")
        else:
            tk.messagebox.showwarning("عدم عضويت در سايت","!سلام! شما هنوز در سامانه عضو نشده ايد")
            self.back.configure(command=lambda: self.show_frame("HomePage"))
            ertxt2 = "آيا قصد وارد شدن به پنل کاربري را داريد؟"
            msg = tk.messagebox.askquestion("وارد شدن به پنل کاربري",ertxt2)
            if msg == 'yes':
                self.show_frame("SigninPage")
            else:
                pass
            
#Class child10: net ------------------------------------------------------------------------------------------------------------------------------------------
class net(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller = controller
        self.show_frame = controller.show_frame
        self.pishniyaz = controller.pishniyaz
        self.errpishniyaz = controller.errpishniyaz
        self.gotopage = controller.gotopage
        global logkey_var
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #----Space--------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #----Lbl----------------------------------------------------------------
        net_lfr = tk.LabelFrame(self,text = "  دوره هاي نت  ",labelanchor='ne',relief = 'ridge',font=controller.logfont)
        net_lfr.pack(side="top", fill="x",padx=5,pady=5,ipadx=10)

        fram1 = tk.Frame(net_lfr)
        fram1.pack(side="top", fill="x")
        
        lfram1 = tk.LabelFrame(net_lfr,text = "  گروه اول  ",labelanchor='ne',relief = 'ridge',font=controller.btnfont)
        lfram2 = tk.LabelFrame(net_lfr,text = "  گروه دوم  ",labelanchor='ne',relief = 'ridge',font=controller.btnfont)
        for lframe in (lfram1, lfram2):
            lframe.pack(side="top", fill="x",ipadx=10,ipady=1,padx=5)

        
        fram2 = tk.Frame(lfram1)
        fram3 = tk.Frame(lfram1)
        fram4 = tk.Frame(lfram1)
        fram5 = tk.Frame(lfram1)
        fram6 = tk.Frame(lfram2)
        fram7 = tk.Frame(lfram2)
        fram8 = tk.Frame(lfram2)
        fram9 = tk.Frame(net_lfr)

        for frame in (fram1, fram2, fram3, fram4, fram5, fram6, fram7, fram8, fram9):
            frame.pack(side="top", fill="x")
        ttk.Separator(net_lfr,orient = 'horizontal').pack(side='top',anchor='center',pady = 5, ipadx = 1000)
        bfram = tk.Frame(net_lfr)
        bfram.pack(side="top", fill="x",padx=5,ipadx=8,ipady=5,)
        #----Lbl and btn-------------------------------------------------------------------
        tk.Label(fram1,font=controller.btnfont).pack(side="right", padx=13)
        label1 = tk.Label(fram1, text="Network  دوره",font=controller.lblfont)
        label1.pack(side="right", fill="x", pady=9)


        tk.Label(fram1,font=controller.btnfont).pack(side="right", padx=35)
        button1 = tk.Button(fram1, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_net('Network')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button1.pack(side="right", pady=9, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram2,font=controller.btnfont).pack(side="right", padx=10)
        label2 = tk.Label(fram2, text="Winlo  دوره",font=controller.lblfont)
        label2.pack(side="right", fill="x", pady=9)

        tk.Label(fram2,font=controller.btnfont).pack(side="left", padx=20)
        button3 = tk.Button(fram2, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_net('exchange')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button3.pack(side="left", pady=9, ipadx=15)

        label3 = tk.Label(fram2, text=" Exchange دوره",font=controller.lblfont)
        label3.pack(side="left", fill="x", pady=9)

        tk.Label(fram2,font=controller.btnfont).pack(side="left", padx=10)
        button2 = tk.Button(fram2, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_net('winlo')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button2.pack(side="left", pady=9, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram3,font=controller.btnfont).pack(side="right", padx=10)
        label4 = tk.Label(fram3, text="Server1 دوره",font=controller.lblfont)
        label4.pack(side="right", fill="x", pady=9)


        tk.Label(fram3,font=controller.btnfont).pack(side="left", padx=20)
        button5 = tk.Button(fram3, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_net('vmware')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button5.pack(side="left", pady=9, ipadx=15)

        tk.Label(fram3,font=controller.btnfont).pack(side="left", padx=6)
        label5 = tk.Label(fram3, text="Vmware دوره",font=controller.lblfont)
        label5.pack(side="left", fill="x", pady=9)

        tk.Label(fram3,font=controller.btnfont).pack(side="left", padx=10)
        button4 = tk.Button(fram3, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_net('server1')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button4.pack(side="left", pady=9, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram4,font=controller.btnfont).pack(side="right", padx=10)
        label6 = tk.Label(fram4, text=" Server2 دوره",font=controller.lblfont)
        label6.pack(side="right", fill="x", pady=7)

        tk.Label(fram4,font=controller.btnfont).pack(side="left", padx=20)
        button7 = tk.Button(fram4, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_net('vdi')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button7.pack(side="left", pady=9, ipadx=15)

        tk.Label(fram4,font=controller.btnfont).pack(side="left", padx=24)
        label7 = tk.Label(fram4, text="VDI  دوره",font=controller.lblfont)
        label7.pack(side="left", fill="x", pady=9)

        tk.Label(fram4,font=controller.btnfont).pack(side="left", padx=10)
        button6 = tk.Button(fram4, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_net('server2')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button6.pack(side="left", pady=9, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram5,font=controller.btnfont).pack(side="right", padx=10)
        label8 = tk.Label(fram5, text=" Server3 دوره",font=controller.lblfont)
        label8.pack(side="right", fill="x", pady=9)

        tk.Label(fram5,font=controller.btnfont).pack(side="right", padx=37)

        button8 = tk.Button(fram5, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_net('server3')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button8.pack(side="right", pady=9, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram6,font=controller.btnfont).pack(side="right", padx=10)
        label9 = tk.Label(fram6, text="CCNA  دوره",font=controller.lblfont)
        label9.pack(side="right", fill="x", pady=9)

        tk.Label(fram6,font=controller.btnfont).pack(side="left", padx=20)
        button10 = tk.Button(fram6, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_net('ceh')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button10.pack(side="left", pady=9, ipadx=15)

        tk.Label(fram6,font=controller.btnfont).pack(side="left", padx=22)
        label10 = tk.Label(fram6, text="CEH دوره",font=controller.lblfont)
        label10.pack(side="left", fill="x", pady=9)

        tk.Label(fram6,font=controller.btnfont).pack(side="left", padx=10)
        button9 = tk.Button(fram6, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_net('ccna')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button9.pack(side="left", pady=9, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram7,font=controller.btnfont).pack(side="right", padx=10)
        label11 = tk.Label(fram7, text="CCNA Security دوره",font=controller.lblfont)
        label11.pack(side="right", fill="x", pady=9)


        tk.Label(fram7,font=controller.btnfont).pack(side="left", padx=20)
        button12 = tk.Button(fram7, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_net('lpic1')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button12.pack(side="left", pady=9, ipadx=15)
        tk.Label(fram7,font=controller.btnfont).pack(side="left", padx=20)
        label12 = tk.Label(fram7, text="Lpic1 دوره",font=controller.lblfont)
        label12.pack(side="left", fill="x", pady=9)
        tk.Label(fram7,font=controller.btnfont).pack(side="left", padx=10)
        button11 = tk.Button(fram7, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_net('ccna_security')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button11.pack(side="left", pady=9, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram8,font=controller.btnfont).pack(side="right", padx=10)
        label13 = tk.Label(fram8, text=" CCNP دوره",font=controller.lblfont)
        label13.pack(side="right", fill="x", pady=9)

        tk.Label(fram8,font=controller.btnfont).pack(side="left", padx=20)
        button14 = tk.Button(fram8, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_net('lpic2')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button14.pack(side="left", pady=9, ipadx=15)

        tk.Label(fram8,font=controller.btnfont).pack(side="left", padx=15)
        label14 = tk.Label(fram8, text=" Lpic2  دوره",font=controller.lblfont)
        label14.pack(side="left", fill="x", pady=9)

        tk.Label(fram8,font=controller.btnfont).pack(side="left", padx=10)
        button13 = tk.Button(fram8, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_net('ccnp')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",cursor="hand2",
                               bg="#316ba9",)
        button13.pack(side="left", pady=9, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram9,font=controller.btnfont).pack(side="left", padx=1)
        #----------------------------------------------------------------------------------
        self.back = tk.Button(bfram, text="بازگشت",font=controller.btnfont,command=lambda: self.back_net()
                              ,fg="black", disabledforeground = "#85b1da",bg="#a9d9f4",cursor="hand2",)
        self.back.pack(side="left", pady=10, ipadx=50, padx=50)
        #----Footer-------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def back_net(self):
        global logkey_var
        global bk
        if logkey_var=="0123456789":
            if bk[2]=="SET_CRS":
                self.show_frame("SET_CRS")
            elif bk[2]=="HomePage":
                self.show_frame("HomePage")
            else:
            	self.show_frame("HomePage")
        elif logkey_var!="":
            if bk[2]=="SET_CRS":
                self.show_frame("SET_CRS")
            elif bk[2]=="HomePage":
                self.show_frame("HomePage")
            else:
                self.show_frame(bk[2])
        else:
            self.show_frame(back[0])
    #*--------------------------------------------------------------------------------------------------------------------------------
    def submit_net(self,name):
        global logkey_var
        global rowname
        global rowict
        global rowweb
        global rowname
        global rowict
        global rowweb
        global rownet1
        global rownet2
        global rowpro1
        global rowpro2
        global back
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        net1 = ['Winlo','Server1','Server2','Server3','Exchange','Vmware','VDI']
        net2 = ["CCNA", "CCNA security","CCNP","CEH", "Lpic1", "Lpic2"]
        #rownet1 = [Winlo, Server1, Server2, Server3, Exchange, Vmware,VDI]
        #rownet2 = [CCNA, CCNA_S, CCNP, CEH, Lpic1, Lpic2]
        #------------------------------------------------------------------------------------------------------------------
        if rowname!=[] and logkey_var != "0123456789":
            self.back.configure(command=lambda: self.show_frame("User"))
            user = " !عزيز "+rowname[2]+" "+rowname[1]
            if name != "Network":
                if rownet1 == []:
                    net1row = [(logkey_var,'notregister','notregister','notregister','notregister','notregister','notregister','notregister')]
                    cursor.executemany('''INSERT INTO NET1 values(?,?,?,?,?,?,?,?)''',net1row)
                    net1list(['notregister','notregister','notregister','notregister','notregister','notregister','notregister'])
                    mftdb.commit()
            list1 = ['ccna',"ccna_security","ccnp","ceh","lpic1","lpic2"]
            if name in list1:
                if rownet2 == []:
                    net2row = [(logkey_var,'notregister','notregister','notregister','notregister','notregister','notregister')]
                    cursor.executemany('''INSERT INTO NET2 values(?,?,?,?,?,?,?)''',net2row)
                    net2list(['notregister','notregister','notregister','notregister','notregister','notregister'])
                    mftdb.commit()
            #------------------------------------------------------------------------------------------------------------------
            icdl1 = self.pishniyaz(rowname[7])
            net1 = self.pishniyaz(rowname[9])
            #------------------------------------------------------------------------------------------------------------------
            #name == "Network":-------------------------------------------------------------------
            if name == "Network":
                self.errpishniyaz(icdl1,"STUDENT","Network",'ICDL1',rowname[9],name)
            elif name == "winlo":
                if icdl1:
                    self.errpishniyaz(net1,"NET1",'Winlo',"Network",rownet1[0],name)
                else:
                    self.errpishniyaz(icdl1,"NET1",'Winlo','ICDL1',rownet1[0],name)
            #name == "server1":-------------------------------------------------------------------
            elif name == "server1":
                winlo = self.pishniyaz(rownet1[0])
                if icdl1 and net1:
                    self.errpishniyaz(winlo,"NET1","Server1",'Winlo',rownet1[1],name)
                elif icdl1 and net1 == False:
                    self.errpishniyaz(net1,"NET1","Server1","Network",rownet1[1],name)
                else:
                    self.errpishniyaz(icdl1,"NET1","Server1",'ICDL1',rownet1[1],name)
            #name == "server2":-------------------------------------------------------------------
            elif name == "server2":
                winlo = self.pishniyaz(rownet1[0])
                server1 = self.pishniyaz(rownet1[1])
                if icdl1 and net1 and winlo:
                    self.errpishniyaz(server1,"NET1","Server2","Server1",rownet1[2],name)
                elif icdl1 and net1:
                    self.errpishniyaz(winlo,"NET1","Server2",'Winlo',rownet1[2],name)
                elif icdl1:
                    self.errpishniyaz(net1,"NET1","Server2","Network",rownet1[2],name) 
                else:
                    self.errpishniyaz(icdl1,"NET1","Server2","ICDL1",rownet1[2],name)
            #name == "server3":-------------------------------------------------------------------
            elif name == "server3":
                winlo = self.pishniyaz(rownet1[0])
                server1 = self.pishniyaz(rownet1[1])
                server2 = self.pishniyaz(rownet1[2])
                if icdl1 and net1 and winlo and server1:
                    self.errpishniyaz(server2,"NET1","Server3","Server2",rownet1[3],name)
                elif icdl1 and net1 and winlo and server1 == False:
                    self.errpishniyaz(server1,"NET1","Server3","Server1",rownet1[3],name)
                elif icdl1 and net1 and winlo == False and server1 == False:
                    self.errpishniyaz(winlo,"NET1","Server3","Winlo",rownet1[3],name)
                elif icdl1 and net1 == False and winlo == False and server1 == False:
                    self.errpishniyaz(net1,"NET1","Server3","Network",rownet1[3],name)
                else:
                    self.errpishniyaz(icdl1,"NET1","Server3","ICDL1",rownet1[3],name)
            #name == "exchange":-------------------------------------------------------------------
            elif name == "exchange":
                winlo = self.pishniyaz(rownet1[0])
                server1 = self.pishniyaz(rownet1[1])
                server2 = self.pishniyaz(rownet1[2])
                server3 = self.pishniyaz(rownet1[3])
                if icdl1 and net1 and winlo and server1 and server2:
                    self.errpishniyaz(server3,"NET1",'Exchange',"Server3",rownet1[4],name)
                elif icdl1 and net1 and winlo and server1 and server2 == False:
                    self.errpishniyaz(server2,"NET1",'Exchange',"Server2",rownet1[4],name)
                elif icdl1 and net1 and winlo and server1 == False and server2 == False:
                    self.errpishniyaz(server1,"NET1",'Exchange',"Server1",rownet1[4],name)
                elif icdl1 and net1 and winlo == False and server1 == False and server2 == False:
                    self.errpishniyaz(winlo,"NET1",'Exchange',"Winlo",rownet1[4],name)
                elif icdl1 and net1 == False and winlo == False and server1 == False and server2 == False:
                    self.errpishniyaz(net1,"NET1",'Exchange',"Network",rownet1[4],name)
                else:
                    self.errpishniyaz(icdl1,"NET1",'Exchange',"ICDL1",rownet1[4],name)
            #name == "vmware":---------------------------------------------------------------------
            elif name == "vmware":
                winlo = self.pishniyaz(rownet1[0])
                server1 = self.pishniyaz(rownet1[1])
                server2 = self.pishniyaz(rownet1[2])
                server3 = self.pishniyaz(rownet1[3])
                exchange = self.pishniyaz(rownet1[4])
                if icdl1 and net1 and winlo and server1 and server2 and server3:
                    self.errpishniyaz(exchange,"NET1",'Vmware','Exchange',rownet1[5],name)
                elif icdl1 and net1 and winlo and server1 and server2 and server3 == False:
                    self.errpishniyaz(server3,"NET1",'Vmware','Server3',rownet1[5],name)
                elif icdl1 and net1 and winlo and server1 and server2 == False and server3 == False:
                    self.errpishniyaz(server2,"NET1",'Vmware','Server2',rownet1[5],name)
                elif icdl1 and net1 and winlo and server1 == False and server2 == False and server3 == False:
                    self.errpishniyaz(server1,"NET1",'Vmware','Server1',rownet1[5],name)
                elif icdl1 and net1 and winlo == False and server1 == False and server2 == False and server3 == False:
                    self.errpishniyaz(winlo,"NET1",'Vmware','Winlo',rownet1[5],name)
                elif icdl1 and net1 == False and winlo == False and server1 == False and server2 == False and server3 == False:
                    self.errpishniyaz(net1,"NET1",'Vmware','Network',rownet1[5],name)
                else:
                    self.errpishniyaz(icdl1,"NET1",'Vmware','ICDL1',rownet1[5],name)
            #name == "vdi":---------------------------------------------------------------------
            elif name == "vdi":
                winlo = self.pishniyaz(rownet1[0])
                server1 = self.pishniyaz(rownet1[1])
                server2 = self.pishniyaz(rownet1[2])
                server3 = self.pishniyaz(rownet1[3])
                exchange = self.pishniyaz(rownet1[4])
                vmware = self.pishniyaz(rownet1[5])
                if icdl1 and net1 and winlo and server1 and server2 and server3 and exchange:
                    self.errpishniyaz(vmware,"NET1","VDI",'Vmware',rownet1[6],name)
                elif icdl1 and net1 and winlo and server1 and server2 and server3 and exchange == False:
                    self.errpishniyaz(exchange,"NET1","VDI",'Exchange',rownet1[6],name)
                elif icdl1 and net1 and winlo and server1 and server2 and server3 == False and exchange == False:
                    self.errpishniyaz(server3,"NET1","VDI",'Server3',rownet1[6],name)
                elif icdl1 and net1 and winlo and server1 and server2 == False and server3 == False and exchange == False:
                    self.errpishniyaz(server2,"NET1","VDI",'Server2',rownet1[6],name)
                elif icdl1 and net1 and winlo and server1 == False and server2 == False and server3 == False and exchange == False:
                    self.errpishniyaz(server1,"NET1","VDI",'Server1',rownet1[6],name)
                elif icdl1 and net1 and winlo == False and server1 == False and server2 == False and server3 == False and exchange == False:
                    self.errpishniyaz(winlo,"NET1","VDI",'Winlo',rownet1[6],name)
                elif icdl1 and net1 == False and winlo == False and server1 == False and server2 == False and server3 == False and exchange == False:
                    self.errpishniyaz(net1,"NET1","VDI",'Network',rownet1[6],name)
                else:
                    self.errpishniyaz(icdl1,"NET1","VDI",'ICDL1',rownet1[6],name)
            #name == "ccna":---------------------------------------------------------------------
            elif name == "ccna":
                if icdl1:
                    self.errpishniyaz(net1,"NET2","CCNA",'Network',rownet2[0],name)
                else:
                    self.errpishniyaz(icdl1,"NET2","CCNA",'ICDL1',rownet2[0],name)
            #name == "ccna_security":------------------------------------------------------------
            elif name == "ccna_security":
                CCNA = self.pishniyaz(rownet2[0])
                if icdl1 and net1:
                    self.errpishniyaz(CCNA,"NET2","CCNA Security",'CCNA',rownet2[1],name)
                elif icdl1 and net1 == False:
                    self.errpishniyaz(net1,"NET2","CCNA Security",'Network',rownet2[1],name)
                else:
                    self.errpishniyaz(icdl1,"NET2","CCNA Security",'ICDL1',rownet2[1],name)
            #name == "ccnp":---------------------------------------------------------------------
            elif name == "ccnp":
                CCNA = self.pishniyaz(rownet2[0])
                ccna_security = self.pishniyaz(rownet2[1])
                if icdl1 and net1 and CCNA:
                    self.errpishniyaz(ccna_security,"NET2","CCNP",'CCNA Security',rownet2[2],name)
                elif icdl1 and net1 and CCNA == False:
                    self.errpishniyaz(CCNA,"NET2","CCNP",'CCNA',rownet2[2],name)
                elif icdl1 and net1 == False and CCNA == False:
                    self.errpishniyaz(net1,"NET2","CCNP",'Network',rownet2[2],name)
                else:
                    self.errpishniyaz(icdl1,"NET2","CCNP",'ICDL1',rownet2[2],name)
            #name == "ceh":---------------------------------------------------------------------
            elif name == "ceh":
                if icdl1:
                    self.errpishniyaz(net1,"NET2","Ceh",'Network',rownet2[3],name)
                else:
                    self.errpishniyaz(icdl1,"NET2","Ceh",'ICDL1',rownet2[3],name)
            #name == "lpic1":-------------------------------------------------------------------
            elif name == "lpic1":
                if icdl1:
                    self.errpishniyaz(net1,"NET2","Lpic1",'Network',rownet2[4],name)
                else:
                    self.errpishniyaz(icdl1,"NET2","Lpic1",'ICDL1',rownet2[4],name)
            #name == "lpic2":-------------------------------------------------------------------
            elif name == "lpic2":
                lpic1 = self.pishniyaz(rownet2[4])
                if icdl1 and net1:
                    self.errpishniyaz(lpic1,"NET2","Lpic2",'Lpic1',rownet2[5],name)
                elif icdl1 and net1 == False:
                    self.errpishniyaz(net1,"NET2","Lpic2",'Network',rownet2[5],name)
                else:
                    self.errpishniyaz(icdl1,"NET2","Lpic2",'ICDL1',rownet2[5],name)
        #------------------------------------------------------------------------------------------------------------------
        elif logkey_var == "0123456789":
            tk.messagebox.showwarning("عدم اجازه دسترسي","!سلام ادمين عزيز. شما اجازه ثبت درس را نداريد")
        else:
            tk.messagebox.showwarning("عدم عضويت در سايت","!سلام! شما هنوز در سامانه عضو نشده ايد")
            self.back.configure(command=lambda: self.show_frame("HomePage"))
            ertxt2 = "آيا قصد وارد شدن به پنل کاربري را داريد؟"
            msg = tk.messagebox.askquestion("وارد شدن به پنل کاربري",ertxt2)
            if msg == 'yes':
                self.show_frame("SigninPage")
            else:
                pass

#Class child11: programming1 ------------------------------------------------------------------------------------------------------------------------------------------
class programming1(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller = controller
        self.show_frame = controller.show_frame
        self.pishniyaz = controller.pishniyaz
        self.errpishniyaz = controller.errpishniyaz
        self.gotopage = controller.gotopage
        global logkey_var
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #----Space--------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #----Lbl----------------------------------------------------------------
        pro_lfr = tk.LabelFrame(self,text = " 1 دوره هاي برنامه نويسي  ",labelanchor='ne',relief = 'ridge',font=controller.logfont)
        pro_lfr.pack(side="top", fill="x",padx=5,pady=5,ipadx=10)

        pro_fr = tk.Frame(pro_lfr)
        pro_fr.pack(side="top", fill="x")
        #----------------------------------------------------------------------------------
        lfram1 = tk.LabelFrame(pro_lfr,text = "  گروه اول  ",labelanchor='ne',relief = 'ridge',font=controller.btnfont)
        lfram2 = tk.LabelFrame(pro_lfr,text = "  گروه دوم  ",labelanchor='ne',relief = 'ridge',font=controller.btnfont)
        lfram3 = tk.LabelFrame(pro_lfr,text = "  گروه سوم  ",labelanchor='ne',relief = 'ridge',font=controller.btnfont)

        for lframe in (lfram1, lfram2, lfram3):
            lframe.pack(side="top", fill="x",padx=5,ipadx=10,ipady=1,pady=2)
        #----------------------------------------------------------------------------------
        fram1 = tk.Frame(pro_fr)
        fram2 = tk.Frame(lfram1)
        fram3 = tk.Frame(lfram1)
        fram4 = tk.Frame(lfram2)
        fram5 = tk.Frame(lfram3)
        fram6 = tk.Frame(lfram3)
        fram7 = tk.Frame(lfram2)

        for frame in (fram1, fram2, fram3, fram4, fram5, fram6, fram7):
            frame.pack(side="top", fill="x")
        #----------------------------------------------------------------------------------
        ttk.Separator(pro_lfr,orient = 'horizontal').pack(side='top',anchor='center',pady = 5, ipadx = 1000)
        #----------------------------------------------------------------------------------
        bfram = tk.Frame(pro_lfr)
        bfram.pack(side="top", fill="x",padx=5,ipadx=8,ipady=5,)
        #----Lbl and btn-------------------------------------------------------------------
        tk.Label(fram1,font=controller.btnfont).pack(side="right", padx=10)
        label1 = tk.Label(fram1, text="Algorithms  دوره",font=controller.lblfont)
        label1.pack(side="right", fill="x", pady=12)

        tk.Label(fram1,font=controller.btnfont).pack(side="right", padx=12)
        button1 = tk.Button(fram1, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro1('Algorithms')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button1.pack(side="right", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram2,font=controller.btnfont).pack(side="right", padx=10)
        label2 = tk.Label(fram2, text="C ++  دوره",font=controller.lblfont)
        label2.pack(side="right", fill="x", pady=12)

        tk.Label(fram2,font=controller.btnfont).pack(side="left", padx=23)
        button3 = tk.Button(fram2, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_pro1('sql')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button3.pack(side="left", pady=10, ipadx=15)

        tk.Label(fram2,font=controller.btnfont).pack(side="left", padx=39)
        label3 = tk.Label(fram2, text="SQL دوره",font=controller.lblfont)
        label3.pack(side="left", fill="x", pady=12)

        tk.Label(fram2,font=controller.btnfont).pack(side="left", padx=10)
        button2 = tk.Button(fram2, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro1('c_plusplus')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button2.pack(side="left", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram3,font=controller.btnfont).pack(side="right", padx=10)
        label4 = tk.Label(fram3, text="C #  دوره",font=controller.lblfont)
        label4.pack(side="right", fill="x", pady=12)

        tk.Label(fram3,font=controller.btnfont).pack(side="left", padx=23)
        button5 = tk.Button(fram3, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_pro1('asp_net')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button5.pack(side="left", pady=10, ipadx=15)

        tk.Label(fram3,font=controller.btnfont).pack(side="left", padx=18)
        label5 = tk.Label(fram3, text="ASP.NET دوره",font=controller.lblfont)
        label5.pack(side="left", fill="x", pady=12)

        tk.Label(fram3,font=controller.btnfont).pack(side="left", padx=10)
        button4 = tk.Button(fram3, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro1('c_sharp')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button4.pack(side="left", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram4,font=controller.btnfont).pack(side="right", padx=10)
        label6 = tk.Label(fram4, text="JavaScript  دوره",font=controller.lblfont)
        label6.pack(side="right", fill="x", pady=12)

        tk.Label(fram4,font=controller.btnfont).pack(side="left", padx=23)
        button7 = tk.Button(fram4, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_pro1('block_chain')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button7.pack(side="left", pady=10, ipadx=15)

        tk.Label(fram4,font=controller.btnfont).pack(side="left", padx=7)
        label7 = tk.Label(fram4, text="Block Chain دوره",font=controller.lblfont)
        label7.pack(side="left", fill="x", pady=12)

        tk.Label(fram4,font=controller.btnfont).pack(side="left", padx=10)
        button6 = tk.Button(fram4, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro1('javascriPt')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button6.pack(side="left", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram5,font=controller.btnfont).pack(side="right", padx=10)
        label8 = tk.Label(fram5, text="Python  دوره",font=controller.lblfont)
        label8.pack(side="right", fill="x", pady=12)

        tk.Label(fram5,font=controller.btnfont).pack(side="left", padx=23)
        button9 = tk.Button(fram5, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_pro1('deep_learning')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button9.pack(side="left", pady=10, ipadx=15)

        tk.Label(fram5,font=controller.btnfont).pack(side="left", padx=14)
        label9 = tk.Label(fram5, text="Deep Learning دوره",font=controller.lblfont)
        label9.pack(side="left", fill="x", pady=12)

        tk.Label(fram5,font=controller.btnfont).pack(side="left", padx=10)
        button8 = tk.Button(fram5, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro1('python')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button8.pack(side="left", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram6,font=controller.btnfont).pack(side="right", padx=10)
        label10 = tk.Label(fram6, text="ML  دوره",font=controller.lblfont)
        label10.pack(side="right", fill="x", pady=12)

        tk.Label(fram6,font=controller.btnfont).pack(side="left", padx=23)
        button11 = tk.Button(fram6, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_pro1('Image_proccessing')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button11.pack(side="left", pady=10, ipadx=15)

        tk.Label(fram6,font=controller.btnfont).pack(side="left", padx=1)
        label11 = tk.Label(fram6, text="Image Processing دوره",font=controller.lblfont)
        label11.pack(side="left", fill="x", pady=12)

        tk.Label(fram6,font=controller.btnfont).pack(side="left", padx=10)
        button10 = tk.Button(fram6, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro1('ml')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button10.pack(side="left", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        self.next = tk.Button(bfram, text="ليست دروس برنامه نويسي 2",font=controller.btnfont,command=lambda: self.show_frame("programming2")
                              ,fg="black", disabledforeground = "#85b1da",bg="#a9d9f4",)
        self.next.pack(side="right", pady=10, ipadx=25, padx=50)

        self.back = tk.Button(bfram, text="بازگشت",font=controller.btnfont,command=lambda: self.back_pro()
                              ,fg="black", disabledforeground = "#85b1da",bg="#a9d9f4",)
        self.back.pack(side="left", pady=10, ipadx=55, padx=50)
        #----Footer------------------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def back_pro(self):
        global logkey_var
        global bk
        if logkey_var=="0123456789":
            if bk[2]=="SET_CRS":
                self.show_frame("SET_CRS")
            elif bk[2]=="HomePage":
                self.show_frame("HomePage")
            else:
            	self.show_frame("HomePage")
        elif logkey_var!="":
            if bk[2]=="SET_CRS":
                self.show_frame("SET_CRS")
            elif bk[2]=="HomePage":
                self.show_frame("HomePage")
            else:
                self.show_frame(bk[2]) 
        else:
            self.show_frame(back[0])
    #*--------------------------------------------------------------------------------------------------------------------------------
    def submit_pro1(self,name):
        global logkey_var
        global rowname
        global rowict
        global rowweb
        global rowname
        global rowict
        global rowweb
        global rownet1
        global rownet2
        global rowpro1
        global rowpro2
        global back
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        #rowpro1 = [Python,ML,DeepL,ImagePro,Cplus,Csharp,SQL,ASP,JS,Block_C]
        #rowpro2 = [Java,SE,EE,Android,Kotlin,Android_Java,IOS]
        #------------------------------------------------------------------------------------------------------------------
        if rowname!=[] and logkey_var != "0123456789":
            self.back.configure(command=lambda: self.show_frame("User"))
            user = " !عزيز "+rowname[2]+" "+rowname[1]
            if name !='Algorithm':
                if rowpro1 == []:
                    pro1row = [(logkey_var,'notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister')]
                    cursor.executemany('''INSERT INTO pro1 values(?,?,?,?,?,?,?,?,?,?,?)''',pro1row)
                    pro1list(['notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister'])
                    mftdb.commit()
            #------------------------------------------------------------------------------------------------------------------
            icdl1 = self.pishniyaz(rowname[7])
            Algorithm = self.pishniyaz(rowname[8])
            #------------------------------------------------------------------------------------------------------------------
            #name == "Algorithms":----------------------------------------------------------------------------
            if name == "Algorithms":
                self.errpishniyaz(icdl1,"STUDENT","Algorithms",'ICDL1',rowname[8],name)
            #name == "python":---------------------------------------------------------------------------
            elif name == "python":
                if icdl1:
                    self.errpishniyaz(Algorithm,"pro1",'Python',"Algorithms",rowpro1[0],name)
                else:
                    self.errpishniyaz(icdl1,"pro1",'Python','ICDL1',rowpro1[0],name)
            #name == "ml":------------------------------------------------------------------------------
            elif name == "ml":
                python = self.pishniyaz(rowpro1[0])
                if icdl1 and Algorithm:
                    self.errpishniyaz(python,"pro1",'ML',"Python",rowpro1[1],name)
                elif icdl1:
                    self.errpishniyaz(Algorithm,"pro1",'ML',"Algorithms",rowpro1[1],name)
                else:
                    self.errpishniyaz(icdl1,"pro1",'ML','ICDL1',rowpro1[1],name)
            #name == "deep_learning":------------------------------------------------------------------------------
            elif name == "deep_learning":
                python = self.pishniyaz(rowpro1[0])
                ml = self.pishniyaz(rowpro1[1])
                if icdl1 and Algorithm and python:
                    self.errpishniyaz(ml,"pro1",'Deep Learning',"ML",rowpro1[2],name)
                elif icdl1 and Algorithm:
                    self.errpishniyaz(python,"pro1",'Deep Learning',"Python",rowpro1[2],name)
                elif icdl1:
                    self.errpishniyaz(Algorithm,"pro1",'Deep Learning',"Algorithms",rowpro1[2],name)
                else:
                    self.errpishniyaz(icdl1,"pro1",'Deep Learning','ICDL1',rowpro1[2],name)
            #name == "Image_processing":------------------------------------------------------------------------------
            elif name == "Image_proccessing":
                python = self.pishniyaz(rowpro1[0])
                ml = self.pishniyaz(rowpro1[1])
                deep_learning = self.pishniyaz(rowpro1[2])
                if icdl1 and Algorithm and python and ml:
                    self.errpishniyaz(deep_learning,"pro1",'Image Processing',"Deep Learning",rowpro1[3],name)
                elif icdl1 and Algorithm and python:
                    self.errpishniyaz(ml,"pro1",'Image Processing',"ML",rowpro1[3],name)
                elif icdl1 and Algorithm:
                    self.errpishniyaz(python,"pro1",'Image Processing',"Python",rowpro1[3],name)
                elif icdl1:
                    self.errpishniyaz(Algorithm,"pro1",'Image Processing',"Algorithms",rowpro1[3],name)
                else:
                    self.errpishniyaz(icdl1,"pro1",'Image Processing','ICDL1',rowpro1[3],name)
            #name == "c_plusplus":---------------------------------------------------------------------------
            elif name == "c_plusplus":
                if icdl1:
                    self.errpishniyaz(Algorithm,"pro1",'C ++',"Algorithms",rowpro1[4],name)
                else:
                    self.errpishniyaz(icdl1,"pro1",'C ++','ICDL1',rowpro1[4],name)
            #name == "c_sharp":---------------------------------------------------------------------------
            elif name == "c_sharp":
                if icdl1:
                    self.errpishniyaz(Algorithm,"pro1",'C #',"Algorithms",rowpro1[5],name)
                else:
                    self.errpishniyaz(icdl1,"pro1",'C #','ICDL1',rowpro1[5],name)
            #name == "sql":------------------------------------------------------------------------------
            elif name == "sql":
                c_sharp = self.pishniyaz(rowpro1[5])
                if icdl1 and Algorithm:
                    self.errpishniyaz(c_sharp,"pro1",'SQL',"C #",rowpro1[6],name)
                elif icdl1:
                    self.errpishniyaz(Algorithm,"pro1",'SQL',"Algorithms",rowpro1[6],name)
                else:
                    self.errpishniyaz(icdl1,"pro1",'SQL','ICDL1',rowpro1[6],name)
            #name == "asp_net":------------------------------------------------------------------------------
            elif name == "asp_net":
                c_sharp = self.pishniyaz(rowpro1[5])
                sql = self.pishniyaz(rowpro1[6])
                
                if icdl1 and Algorithm and c_sharp:
                    self.errpishniyaz(sql,"pro1",'ASP.NET',"SQL",rowpro1[7],name)
                elif icdl1 and Algorithm:
                    self.errpishniyaz(c_sharp,"pro1",'ASP.NET',"C #",rowpro1[7],name)
                elif icdl1:
                    self.errpishniyaz(Algorithm,"pro1",'ASP.NET',"Algorithms",rowpro1[7],name)
                else:
                    self.errpishniyaz(icdl1,"pro1",'ASP.NET','ICDL1',rowpro1[7],name)
            #name == "javascriPt":---------------------------------------------------------------------------
            elif name == "javascriPt":
                if icdl1:
                    self.errpishniyaz(Algorithm,"pro1",'Java Script',"Algorithms",rowpro1[8],name)
                else:
                    self.errpishniyaz(icdl1,"pro1",'Java Script','ICDL1',rowpro1[8],name)
            #name == "block_chain":------------------------------------------------------------------------------
            elif name == "block_chain":
                javascriPt = self.pishniyaz(rowpro1[8])
                if icdl1 and Algorithm:
                    self.errpishniyaz(javascriPt,"pro1",'Block Chain',"Java Script",rowpro1[9],name)
                elif icdl1:
                    self.errpishniyaz(Algorithm,"pro1",'Block Chain',"Algorithms",rowpro1[9],name)
                else:
                    self.errpishniyaz(icdl1,"pro1",'Block Chain','ICDL1',rowpro1[9],name)
        #------------------------------------------------------------------------------------------------------------------
        elif logkey_var == "0123456789":
            tk.messagebox.showwarning("عدم اجازه دسترسي","!سلام ادمين عزيز. شما اجازه ثبت درس را نداريد")
        else:
            tk.messagebox.showwarning("عدم عضويت در سايت","!سلام! شما هنوز در سامانه عضو نشده ايد")
            ertxt2 = "آيا قصد وارد شدن به پنل کاربري را داريد؟"
            msg = tk.messagebox.askquestion("وارد شدن به پنل کاربري",ertxt2)
            if msg == 'yes':
                self.show_frame("SigninPage")
            else:
                pass

#Class child12: programming2 ------------------------------------------------------------------------------------------------------------------------------------------
class programming2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller = controller
        self.show_frame = controller.show_frame
        self.pishniyaz = controller.pishniyaz
        self.errpishniyaz = controller.errpishniyaz
        self.gotopage = controller.gotopage
        global logkey_var
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #----Space--------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #----Lbl----------------------------------------------------------------
        pro_lfr = tk.LabelFrame(self,text = " 2 دوره هاي برنامه نويسي  ",labelanchor='ne',relief = 'ridge',font=controller.logfont)
        pro_lfr.pack(side="top", fill="x",padx=5,pady=5,ipadx=10)

        pro_fr = tk.Frame(pro_lfr)
        pro_fr.pack(side="top", fill="x")

        lfram1 = tk.LabelFrame(pro_lfr,text = "  گروه چهارم  ",labelanchor='ne',relief = 'ridge',font=controller.btnfont)
        lfram2 = tk.LabelFrame(pro_lfr,text = "  گروه پنجم  ",labelanchor='ne',relief = 'ridge',font=controller.btnfont)
        lfram1.pack(side="top", fill="x",padx=5,ipadx=10,ipady=1,)
        lfram2.pack(side="top", fill="x",padx=5,ipadx=10,ipady=1,)
        #--------------------------------------------------------------------------------
        fram1 = tk.Frame(pro_fr)
        fram2 = tk.Frame(lfram1)
        fram3 = tk.Frame(lfram1)
        fram4 = tk.Frame(lfram2)
        fram5 = tk.Frame(lfram2)
        fram6 = tk.Frame(lfram2)
        fram7 = tk.Frame(lfram2)

        for frame in (fram1, fram2, fram3, fram4, fram5, fram6, fram7):
            frame.pack(side="top", fill="x")
        ttk.Separator(pro_lfr,orient = 'horizontal').pack(side='top',anchor='center',pady = 5, ipadx = 1000)
        bfram = tk.Frame(pro_lfr)
        bfram.pack(side="top", fill="x",padx=5,ipadx=8,ipady=5,)
        #----Lbl and btn-------------------------------------------------------------------
        tk.Label(fram1,font=controller.btnfont).pack(side="right", padx=10)
        label1 = tk.Label(fram1, text="Algorithms  دوره",font=controller.lblfont)
        label1.pack(side="right", fill="x", pady=12)

        tk.Label(fram1,font=controller.btnfont).pack(side="left", padx=23)
        button2 = tk.Button(fram1, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_pro2('c_plusplus')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button2.pack(side="left", pady=10, ipadx=15)

        tk.Label(fram1,font=controller.btnfont).pack(side="left", padx=30)
        label2 = tk.Label(fram1, text="C++ دوره",font=controller.lblfont)
        label2.pack(side="left", fill="x", pady=12)

        tk.Label(fram1,font=controller.btnfont).pack(side="left", padx=10)
        button1 = tk.Button(fram1, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro2('Algorithms')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button1.pack(side="left", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram2,font=controller.btnfont).pack(side="right", padx=10)
        label2 = tk.Label(fram2, text="Java SE  دوره",font=controller.lblfont)
        label2.pack(side="right", fill="x", pady=12)

        tk.Label(fram2,font=controller.btnfont).pack(side="left", padx=20)
        button3 = tk.Button(fram2, text="ثبت نام", font=controller.btnfont,command=lambda: self.submit_pro2('java')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button3.pack(side="left", pady=10, ipadx=15)

        tk.Label(fram2,font=controller.btnfont).pack(side="left", padx=20)
        label3 = tk.Label(fram2, text="Java  دوره",font=controller.lblfont)
        label3.pack(side="left", fill="x", pady=12)

        tk.Label(fram2,font=controller.btnfont).pack(side="left", padx=9)
        button2 = tk.Button(fram2, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro2('java_se')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button2.pack(side="left", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram3,font=controller.btnfont).pack(side="right", padx=10)
        label3 = tk.Label(fram3, text="Java EE  دوره",font=controller.lblfont)
        label3.pack(side="right", fill="x", pady=12)

        tk.Label(fram3,font=controller.btnfont).pack(side="right", padx=33)
        button3 = tk.Button(fram3, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro2('java_ee')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button3.pack(side="right", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram4,font=controller.btnfont).pack(side="right", padx=10)
        label4 = tk.Label(fram4, text="Android  دوره",font=controller.lblfont)
        label4.pack(side="right", fill="x", pady=12)

        tk.Label(fram4,font=controller.btnfont).pack(side="right", padx=64)
        button4 = tk.Button(fram4, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro2('android')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button4.pack(side="right", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram5,font=controller.btnfont).pack(side="right", padx=10)
        label5 = tk.Label(fram5, text="Android with Kotlin  دوره",font=controller.lblfont)
        label5.pack(side="right", fill="x", pady=12)

        tk.Label(fram5,font=controller.btnfont).pack(side="right", padx=17)
        button5 = tk.Button(fram5, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro2('android_with_kotlin')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button5.pack(side="right", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram6,font=controller.btnfont).pack(side="right", padx=10)
        label6 = tk.Label(fram6, text="Android with Java  دوره",font=controller.lblfont)
        label6.pack(side="right", fill="x", pady=12)

        tk.Label(fram6,font=controller.btnfont).pack(side="right", padx=20)
        button6 = tk.Button(fram6, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro2('android_with_java')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button6.pack(side="right", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        tk.Label(fram7,font=controller.btnfont).pack(side="right", padx=10)
        label7 = tk.Label(fram7, text="IOS with Swift  دوره",font=controller.lblfont)
        label7.pack(side="right", fill="x", pady=12)

        tk.Label(fram7,font=controller.btnfont).pack(side="right", padx=37)
        button7 = tk.Button(fram7, text="ثبت نام",font=controller.btnfont,command=lambda: self.submit_pro2('ios')
                            ,fg="#f0f0f0",disabledforeground = "#85b1d4",
                               bg="#316ba9",)
        button7.pack(side="right", pady=10, ipadx=15)
        #----------------------------------------------------------------------------------
        self.next = tk.Button(bfram, text="ليست دروس برنامه نويسي 1",font=controller.btnfont,command=lambda: self.show_frame("programming1")
                              ,fg="black", disabledforeground = "#85b1da",bg="#a9d9f4",)
        self.next.pack(side="right", pady=10, ipadx=25, padx=50)

        self.back = tk.Button(bfram, text="بازگشت",font=controller.btnfont,command=lambda: self.back_pro()
                              ,fg="black", disabledforeground = "#85b1da",bg="#a9d9f4",)
        self.back.pack(side="left", pady=10, ipadx=55, padx=50)
        #---------------------------------------------------------------------------------
        #----Footer----------------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def back_pro(self):
        global logkey_var
        global back
        global bk
        if logkey_var=="0123456789":
            if bk[2]=="SET_CRS":
                self.show_frame("SET_CRS")
            elif bk[2]=="HomePage":
                self.show_frame("HomePage")
            else:
            	self.show_frame("HomePage")
        elif logkey_var!="":
            if bk[2]=="SET_CRS":
                self.show_frame("SET_CRS")
            elif bk[2]=="HomePage":
                self.show_frame("HomePage")
            else:
                self.show_frame(bk[2]) 
        else:
            self.show_frame(back[0])
    #*--------------------------------------------------------------------------------------------------------------------------------       
    def submit_pro2(self,name):
        global logkey_var
        global rowname
        global rowict
        global rowweb
        global rowname
        global rowict
        global rowweb
        global rownet1
        global rownet2
        global rowpro1
        global rowpro2
        global back
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        pro1 = []
        pro2 = []
        #rowpro1 = [Python,ML,DeepL,ImagePro,Cplus,Csharp,SQL,ASP,JS,Block_C]
        #rowpro2 = [Java,SE,EE,Android,Kotlin,Android_Java,IOS]
        #------------------------------------------------------------------------------------------------------------------
        if rowname!=[] and logkey_var != "0123456789":
            self.back.configure(command=lambda: self.show_frame("User"))
            user = " !عزيز "+rowname[2]+" "+rowname[1]
            if name =='c_plusplus':
                if rowpro1 == []:
                    pro1row = [(logkey_var,'notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister')]
                    cursor.executemany('''INSERT INTO pro1 values(?,?,?,?,?,?,?,?,?,?,?)''',pro1row)
                    pro1list(['notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister'])
                    mftdb.commit()
            list1 = ["java_se","java_ee","android_with_java"]
            if name in list1:
                if rowpro1 == []:
                    pro1row = [(logkey_var,'notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister')]
                    cursor.executemany('''INSERT INTO pro1 values(?,?,?,?,?,?,?,?,?,?,?)''',pro1row)
                    pro1list(['notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister'])
                    mftdb.commit()
                if rowpro2 == []:
                    pro2row = [(logkey_var,'notregister','notregister','notregister','notregister','notregister','notregister','notregister')]
                    cursor.executemany('''INSERT INTO pro2 values(?,?,?,?,?,?,?,?)''',pro2row)
                    pro2list(['notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister'])
                    mftdb.commit()
            list2 = ['java',"android","android_with_kotlin","ios",]
            if name in list2:
                if rowpro2 == []:
                    pro2row = [(logkey_var,'notregister','notregister','notregister','notregister','notregister','notregister','notregister')]
                    cursor.executemany('''INSERT INTO pro2 values(?,?,?,?,?,?,?,?)''',pro2row)
                    pro2list(['notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister'])
                    mftdb.commit()
            #------------------------------------------------------------------------------------------------
            icdl1 = self.pishniyaz(rowname[7])
            Algorithm = self.pishniyaz(rowname[8])
            #------------------------------------------------------------------------------------------------
            #name == "Algorithms":----------------------------------------------------------------------------
            if name == "Algorithms":
                self.errpishniyaz(icdl1,"STUDENT","Algorithms",'ICDL1',rowname[8],name)
            #name == "c_plusplus":---------------------------------------------------------------------------
            elif name == "c_plusplus":
                if icdl1:
                    self.errpishniyaz(Algorithm,"pro1",'C ++',"Algorithms",rowpro1[4],name)
                else:
                    self.errpishniyaz(icdl1,"pro1",'C ++','ICDL1',rowpro1[4],name)
            #name == "java_se":------------------------------------------------------------------------------
            elif name == "java_se":
                c_plusplus = self.pishniyaz(rowpro1[4])

                if icdl1 and Algorithm:
                    self.errpishniyaz(c_plusplus,"pro2",'Java SE',"C ++",rowpro2[1],name)
                elif icdl1:
                    self.errpishniyaz(Algorithm,"pro2",'Java SE',"Algorithms",rowpro2[1],name)
                else:
                    self.errpishniyaz(icdl1,"pro2",'Java SE','ICDL1',rowpro2[1],name)
            #name == "java_ee":-------------------------------------------------------------------------------
            elif name == "java_ee":
                c_plusplus = self.pishniyaz(rowpro1[4])
                java_se = self.pishniyaz(rowpro2[1])

                if icdl1 and Algorithm and c_plusplus:
                    self.errpishniyaz(java_se,"pro2",'Java EE','Java SE',rowpro2[2],name)
                elif icdl1 and Algorithm:
                    self.errpishniyaz(c_plusplus,"pro2",'Java EE',"C ++",rowpro2[2],name)
                elif icdl1:
                    self.errpishniyaz(Algorithm,"pro2",'Java EE',"Algorithms",rowpro2[2],name)
                else:
                    self.errpishniyaz(icdl1,"pro2",'Java EE','ICDL1',rowpro2[2],name)
            #name == "android_with_java":---------------------------------------------------------------------
            elif name == "android_with_java":
                c_plusplus = self.pishniyaz(rowpro1[4])
                java_se = self.pishniyaz(rowpro2[1])
                java_ee = self.pishniyaz(rowpro2[2])

                if icdl1 and Algorithm and c_plusplus and java_se:
                    self.errpishniyaz(java_ee,"pro2",'Android With Java','Java EE',rowpro2[5],name)
                elif icdl1 and Algorithm and c_plusplus:
                    self.errpishniyaz(java_se,"pro2",'Android With Java','Java SE',rowpro2[5],name)
                elif icdl1 and Algorithm:
                    self.errpishniyaz(c_plusplus,"pro2",'Android With Java',"C ++",rowpro2[5],name)
                elif icdl1:
                    self.errpishniyaz(Algorithm,"pro2",'Android With Java',"Algorithms",rowpro2[5],name)
                else:
                    self.errpishniyaz(icdl1,"pro2",'Android With Java','ICDL1',rowpro2[5],name)
            #name == "android":-------------------------------------------------------------------------------
            elif name == "android":
                if icdl1:
                    self.errpishniyaz(Algorithm,"pro2",'Android',"Algorithms",rowpro2[3],name)
                else:
                    self.errpishniyaz(icdl1,"pro2",'Android','ICDL1',rowpro2[3],name)
            #name == "android_with_kotlin":-------------------------------------------------------------------
            elif name == "android_with_kotlin":
                if icdl1:
                    self.errpishniyaz(Algorithm,"pro2",'Android With Kotlin',"Algorithms",rowpro2[4],name)
                else:
                    self.errpishniyaz(icdl1,"pro2",'Android With Kotlin','ICDL1',rowpro2[4],name)
            #name == "ios":-----------------------------------------------------------------------------------
            elif name == "ios":
                if icdl1:
                    self.errpishniyaz(Algorithm,"pro2",'IOS',"Algorithms",rowpro2[6],name)
                else:
                    self.errpishniyaz(icdl1,"pro2",'IOS','ICDL1',rowpro2[6],name)
            #name == "java":-----------------------------------------------------------------------------------
            elif name == "java":
                if icdl1:
                    self.errpishniyaz(Algorithm,"pro2",'Java',"Algorithms",rowpro2[0],name)
                else:
                    self.errpishniyaz(icdl1,"pro2",'Java','ICDL1',rowpro2[0],name)
        #------------------------------------------------------------------------------------------------------------------
        elif logkey_var == "0123456789":
            tk.messagebox.showwarning("عدم اجازه دسترسي","!سلام ادمين عزيز. شما اجازه ثبت درس را نداريد")
        else:
            tk.messagebox.showwarning("عدم عضويت در سايت","!سلام! شما هنوز در سامانه عضو نشده ايد")
            ertxt2 = "آيا قصد وارد شدن به پنل کاربري را داريد؟"
            msg = tk.messagebox.askquestion("وارد شدن به پنل کاربري",ertxt2)
            if msg == 'yes':
                self.show_frame("SigninPage")
            else:
                pass

#Class child13: Admin ------------------------------------------------------------------------------------------------------------------------------------------
class Admin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Blblfont = controller.Blblfont
        self.lblfont = controller.lblfont
        self.logfont = controller.logfont
        self.btnfont = controller.btnfont
        self.font = controller.english_font
        self.elblfont = controller.english_lblfont
        #------------------------------------------
        alist = []
        ictlist(alist)
        net1list(alist)
        net2list(alist)
        weblist(alist)
        pro1list(alist)
        pro2list(alist)
        #------------------------------------------
        self.search = tk.StringVar()
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var4 = tk.StringVar()
        self.var5 = tk.StringVar()
        self.var6 = tk.StringVar()
        self.var7 = tk.StringVar()
        self.var8 = tk.StringVar()
        self.var9 = tk.StringVar()
        self.var10 = tk.StringVar()
        #------------------------------------------
        self.envar1 = tk.StringVar()
        self.envar2 = tk.StringVar()
        self.envar3 = tk.StringVar()
        self.envar4 = tk.StringVar()
        self.envar5 = tk.StringVar()
        self.envar6 = tk.StringVar()
        self.envar7 = tk.StringVar()
        self.envar8 = tk.StringVar()
        self.envar9 = tk.StringVar()
        self.envar10 = tk.StringVar()
        validationInt = self.register(self.only_int)
        #----MenuBar------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #-----------------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        #---------------------------------------------------------------------------------------------------------
        self.Admin_lblf = tk.LabelFrame(self,text = "  پنل ادمين  ",labelanchor='ne',relief = 'ridge',font=self.logfont)
        self.Admin_lblf.pack(side="top", fill="x",padx=5,pady=10,ipadx=10,ipady=5,)
        #---------------------------------------------------------------------------------------------------------
        self.fram1 = tk.Frame(self.Admin_lblf)
        self.fram2 = tk.Frame(self.Admin_lblf)
        self.fram3 = tk.Frame(self.Admin_lblf)
        self.fram4 = tk.Frame(self.Admin_lblf)
        self.fram5 = tk.Frame(self.Admin_lblf)
        self.fram5 = tk.Frame(self.Admin_lblf)
        self.fram6 = tk.Frame(self.Admin_lblf)
        self.fram7 = tk.Frame(self.Admin_lblf)
        self.fram8 = tk.Frame(self.Admin_lblf)
        self.fram9 = tk.Frame(self.Admin_lblf)
        self.fram10 = tk.Frame(self.Admin_lblf)
        self.fram11 = tk.Frame(self.Admin_lblf)
        self.fram12 = tk.Frame(self.Admin_lblf)
        self.fram13 = tk.Frame(self.Admin_lblf)
        self.fram14 = tk.Frame(self.Admin_lblf)
        #---------------------------------------------------------------------------------------------------------
        for frame in (self.fram1, self.fram2):
            frame.pack(side="top", fill="x")
        #---------------------------------------------------------------------------------------------------------
        self.lbl1 = tk.Label(self.fram1,text=":جستجو بر اساس کد ملي يا شماره ی همراه", font=self.logfont)
        self.lbl1.pack(side="right", pady=10, padx=10)
        #---------------------------------------------------------------------------------------------------------
        self.ent_search = tk.Entry(self.fram1,textvariable = self.search,
                                   font=self.btnfont,bd = 2,
                                   validate='key',validatecommand=(validationInt,'%S'))
        self.ent_search.pack(side="right", ipadx=50, ipady=5, pady=10, padx=5)
        #---------------------------------------------------------------------------------------------------------
        self.btn_search = tk.Button(self.fram1,text = 'جستجو', font = self.btnfont,cursor='hand2',
                                    fg="#f0f0f0",disabledforeground = "#85b1d4",bg="#316ba9",
                                    command = lambda: self.searching(), state = 'disable')
        self.btn_search.pack(side="right", ipadx=20, ipady=1, pady=10, padx=5)
        #---------------------------------------------------------------------------------------------------------
        self.lbl2 = tk.Label(self.fram3,text="", font=self.logfont)
        #---------------------------------------------------------------------------------------------------------
        self.btn2 = tk.Button(self.fram4,text = 'اطلاعات کاربر', font = self.btnfont,cursor='hand2',
                                fg="black",disabledforeground = "#85b1d4",bg="#a9d9f4", bd =1,
                                command = lambda: self.database('STUDENT'))
        self.btn3 = tk.Button(self.fram4,text = 'مهارت پايه', font = self.btnfont,cursor='hand2',
                                fg="black",disabledforeground = "#85b1d4",bg="#a9d9f4", bd =1,
                                command = lambda: self.database('ict'))
        self.btn4 = tk.Button(self.fram4,text = 'وب', font = self.btnfont,cursor='hand2',
                                fg="black",disabledforeground = "#85b1d4",bg="#a9d9f4", bd =1,
                                command = lambda: self.database('web'))

        self.btn5 = tk.Button(self.fram4,text = 'برنامه نويسي 1', font = self.btnfont,cursor='hand2',
                                fg="black",disabledforeground = "#85b1d4",bg="#a9d9f4", bd =1,
                                command = lambda: self.database('pro1'))
        self.btn6 = tk.Button(self.fram4,text = 'برنامه نويسي 2', font = self.btnfont,cursor='hand2',
                                fg="black",disabledforeground = "#85b1d4",bg="#a9d9f4", bd =1,
                                command = lambda: self.database('pro2'))
        self.btn7 = tk.Button(self.fram4,text = '1 نت', font = self.btnfont,cursor='hand2',
                                fg="black",disabledforeground = "#85b1d4",bg="#a9d9f4", bd =1,
                                command = lambda: self.database('net1'))
        self.btn8 = tk.Button(self.fram4,text = '2 نت', font = self.btnfont,cursor='hand2',
                                fg="black",disabledforeground = "#85b1d4",bg="#a9d9f4", bd =1,
                                command = lambda: self.database('net2'))
        #---------------------------------------------------------------------------------------------------------
        ttk.Separator(self.fram5,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        self.lb1 = tk.Label(self.fram5,textvariable = self.var1,font=self.lblfont)
        self.lb2 = tk.Label(self.fram6,textvariable = self.var2,font=self.lblfont)
        self.lb3 = tk.Label(self.fram7,textvariable = self.var3,font=self.lblfont)
        self.lb4 = tk.Label(self.fram8,textvariable = self.var4,font=self.lblfont)
        self.lb5 = tk.Label(self.fram9,textvariable = self.var5,font=self.lblfont)
        self.lb6 = tk.Label(self.fram10,textvariable = self.var6,font=self.lblfont)
        self.lb7 = tk.Label(self.fram11,textvariable = self.var7,font=self.font)
        self.lb8 = tk.Label(self.fram12,textvariable = self.var8,font=self.font)
        self.lb9 = tk.Label(self.fram13,textvariable = self.var9,font=self.font)
        self.lb10 = tk.Label(self.fram14,textvariable = self.var10,font=self.font)
        #---------------------------------------------------------------------------------------------------------
        self.en1 = tk.Entry(self.fram5,textvariable = self.envar1,font=self.elblfont,bd = 1)
        self.en2 = tk.Entry(self.fram6,textvariable = self.envar2,font=self.elblfont,bd = 1)
        self.en3 = tk.Entry(self.fram7,textvariable = self.envar3,font=self.elblfont,bd = 1)
        self.en4 = tk.Entry(self.fram8,textvariable = self.envar4,font=self.elblfont,bd = 1)
        self.en5 = tk.Entry(self.fram9,textvariable = self.envar5,font=self.elblfont,bd = 1)
        self.en6 = tk.Entry(self.fram10,textvariable = self.envar6,font=self.elblfont,bd = 1)
        self.en7 = tk.Entry(self.fram11,textvariable = self.envar7,font=self.elblfont,bd = 1)
        self.en8 = tk.Entry(self.fram12,textvariable = self.envar8,font=self.elblfont,bd = 1)
        self.en9 = tk.Entry(self.fram13,textvariable = self.envar9,font=self.elblfont,bd = 1)
        self.en10 = tk.Entry(self.fram14,textvariable = self.envar10,font=self.elblfont,bd = 1)
        #---------------------------------------------------------------------------------------------------------
        self.sub_btn = tk.Button(self.Admin_lblf,text = 'اعمال تغييرات', font = self.btnfont,
                                fg="#f0f0f0",disabledforeground = "#85b1d4",bg="#316ba9",cursor="hand2",
                                 command = lambda: self.coursecheck('STUDENT'))
        self.remove_btn = tk.Button(self.Admin_lblf,text = 'حذف کاربر', font = self.btnfont,
                                fg="#f0f0f0",disabledforeground = "#85b1d4",bg="#316ba9",cursor="hand2",
                                 command = lambda: self.removedb())
        #---------------------------------------------------------------------------------------------------------
        self.btns = (self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8)
        self.search.trace('w',self.codecheck)
        #----Footer-----------------------------------------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
    #*--------------------------------------------------------------------------------------------------------------------------------
    def removedb(self):
        global rowname
        idd = rowname[0]
        err_txt = " آيا مي خواهيد کاربر با کد ملي  "+idd+"  حذف شود "+"؟"
        msg = tk.messagebox.askquestion("حذف کاربر",err_txt)
        if msg == 'yes':
            #------------------------
            self.search.set("")
            for frame in (self.fram2, self.fram3, self.fram4, self.fram5, self.fram6, self.fram7, self.fram8, self.fram9, self.fram10, self.fram11, self.fram12, self.fram13,self.fram14):
                frame.pack_forget()
            #------------------------  
            self.sub_btn.pack_forget()
            self.remove_btn.pack_forget()
            #-------------------------------------------------------------------------
            mftdb = sqlite3.connect('mft01.db')
            cursor = mftdb.cursor()
            txt1 = 'DELETE from STUDENT WHERE Melli_code="'+idd+'"'    
            txt2 = 'DELETE from ict WHERE Melli_code="'+idd+'"'  
            txt3 = 'DELETE from pro1 WHERE Melli_code="'+idd+'"'  
            txt4 = 'DELETE from pro2 WHERE Melli_code="'+idd+'"'  
            txt5 = 'DELETE from NET1 WHERE Melli_code="'+idd+'"'  
            txt6 = 'DELETE from NET2 WHERE Melli_code="'+idd+'"'  
            txt7 = 'DELETE from web WHERE Melli_code="'+idd+'"'  
            cursor.execute(txt1)
            cursor.execute(txt2)
            cursor.execute(txt3)
            cursor.execute(txt4)
            cursor.execute(txt5)
            cursor.execute(txt6)
            cursor.execute(txt7)
            #-------------------
            mftdb.commit()
            mftdb.close()
            err_txt1 = ".کاربر با کد ملي "+idd+"  حذف شود "
            tk.messagebox.showinfo("پيام",err_txt1)
        else:
            pass
    #*--------------------------------------------------------------------------------------------------------------------------------
    def only_int(self,Int):
        return Int.isdigit()
    #*--------------------------------------------------------------------------------------------------------------------------------
    def codecheck(self,*arg):
        a = self.search.get()
        if 10<=len(a)<=11:
            self.btn_search.configure(state = 'normal')
        else:
            self.btn_search.configure(state = 'disable')
    #*--------------------------------------------------------------------------------------------------------------------------------
    def searching(self):
        self.var1.set(':کد ملي          ')
        self.var2.set(':نام          ')
        self.var3.set(':نام خانوادگي          ')
        self.var4.set(':نام پدر          ')
        self.var5.set(':شماره ي همراه          ')
        self.var6.set(':ايميل          ')
        self.var7.set(':ICDL1          ')
        self.var8.set(':Algorithms          ')
        self.var9.set(':Network          ')
        self.var10.set(':Web1          ')
        for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6):
                    lbl.configure(font=self.lblfont)
        for lbl in (self.lb7,self.lb8,self.lb9,self.lb10):
                    lbl.configure(font=self.font)
        entry = self.search.get()
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT(Melli_code text, Name text, Last_Name text, Father_Name text, Phone int, Email text, Password text, ICDL1 text, Algorithms text, Network text, Web text)''')
        cursor.execute('''SELECT * from STUDENT''')
        row = cursor.fetchall()
        for r in row :
            if r[0]==entry or r[4]==entry:
                if r[0]=='0123456789':
                    code = r[0]
                    search = False
                else:
                    search = True
                    code = r[0]
                    name = r[1]
                    lname = r[2]
                    fname = r[3]
                    phone = r[4]
                    email = r[5]
                    ICDL1 = r[7]
                    Algorithms = r[8]
                    Network = r[9]
                    Web = r[10]
                    rowname = [code,name,lname,fname,phone,email,"",ICDL1,Algorithms,Network,Web]
                    searchlist = [("ايميل","شماره همراه","نام پدر","نام خانوادگي کاربر","نام کاربر","کد ملي"),(email,phone,fname,lname,name,code)]
                break
            else:
                search = False
        #---------------------------------------------------------------------------------------------------------
        if search ==True:
            try:
                for frame in (self.fram1, self.fram2, self.fram3, self.fram4, self.fram5, self.fram6, self.fram7, self.fram8, self.fram9, self.fram10, self.fram11, self.fram12, self.fram13,self.fram14):
                    frame.pack(side="top", fill="x")
            except: pass
            #---------------------------
            namelist(rowname)
            finalrows = len(searchlist)
            finalcolumns = len(searchlist[0])
            for i in range (finalrows):
                for j in range (finalcolumns):
                    self.e1 = tk.Entry(self.fram2, width=15,justify='center',
                                   font=self.btnfont,bd = 1)
                    self.e1.grid(row=i, column=j, sticky='news',ipadx=8, padx=2)
                    self.e1.insert('end', searchlist[i][j])
            self.lbl2.configure(text=": ميخواهيد در کدام يک از جداول زير تغييرات اعمال کنيد")
            self.lbl2.pack(side="top", pady=2, padx=2)

            #btns = (self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8)
            for btn in self.btns:
                btn.pack(side="right", ipadx=10, ipady=2, pady=10, padx=5)
            self.envar1.set(code)
            self.envar2.set(name)
            self.envar3.set(lname)
            self.envar4.set(fname)
            self.envar5.set(phone)
            self.envar6.set(email)
            self.envar7.set(ICDL1)
            self.envar8.set(Algorithms)
            self.envar9.set(Network)
            self.envar10.set(Web)
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.pack(side="right", fill="x")

            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7,self.en8,self.en9,self.en10):
                en.pack(side="left", fill="x",padx=80, ipadx=60)
            self.sub_btn.pack(side="left", fill="x",padx=5, ipadx=10)
            self.remove_btn.pack(side="left", fill="x",padx=5, ipadx=10)
        #---------------------------------------------------------------------------------------------------------
        elif self.search.get() =='0123456789':
            tk.messagebox.showinfo("پيام",".اجازه دسترسي به صفحه خود را نداريد")
            try:
                self.search.set("")
                for frame in (self.fram2, self.fram3, self.fram4, self.fram5, self.fram6, self.fram7, self.fram8, self.fram9, self.fram10, self.fram11, self.fram12, self.fram13,self.fram14):
                    frame.pack_forget()
                #------------------------  
                self.sub_btn.pack_forget()
                self.remove_btn.pack_forget()
            except:
                pass
        #---------------------------------------------------------------------------------------------------------
        else:
            tk.messagebox.showinfo("پيام",".کاربري با اين کد ملي و يا شماره ی همراه پيدا نشد")
            try:
                self.search.set("")
                for frame in (self.fram2, self.fram3, self.fram4, self.fram5, self.fram6, self.fram7, self.fram8, self.fram9, self.fram10, self.fram11, self.fram12, self.fram13,self.fram14):
                    frame.pack_forget()
                #------------------------  
                self.sub_btn.pack_forget()
                self.remove_btn.pack_forget()
            except:
                pass
    #*--------------------------------------------------------------------------------------------------------------------------------
    def database(self,db):
        global rowname
        global rownet1
        global rownet2
        global rowpro1
        global rowpro2
        global rowict
        global rowweb
        if  db == 'STUDENT':
            code = rowname[0]
            arowname = []
            mftdb = sqlite3.connect('mft01.db')
            cursor = mftdb.cursor()
            cursor.execute('''SELECT * from STUDENT''')
            row = cursor.fetchall()
            for r in row :
                if r[0]==code:
                    code = r[0]
                    name = r[1]
                    lname = r[2]
                    fname = r[3]
                    phone = r[4]
                    email = r[5]
                    ICDL1 = r[7]
                    Algorithms = r[8]
                    Network = r[9]
                    Web = r[10]
                    arowname = [code,name,lname,fname,phone,email,"",ICDL1,Algorithms,Network,Web]
                    break
                else:
                    pass
            namelist(arowname)
            self.sub_btn.configure(command = lambda: self.coursecheck('STUDENT'))
            self.envar1.set(code)
            self.envar2.set(name)
            self.envar3.set(lname)
            self.envar4.set(fname)
            self.envar5.set(phone)
            self.envar6.set(email)
            self.envar7.set(ICDL1)
            self.envar8.set(Algorithms)
            self.envar9.set(Network)
            self.envar10.set(Web)
            self.var1.set(':کد ملي          ')
            self.var2.set(':نام          ')
            self.var3.set(':نام خانوادگي          ')
            self.var4.set(':نام پدر          ')
            self.var5.set(':شماره ي همراه          ')
            self.var6.set(':ايميل          ')
            self.var7.set(':ICDL1          ')
            self.var8.set(':Algorithms          ')
            self.var9.set(':Network          ')
            self.var10.set(':Web1          ')
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.pack_forget()
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7,self.en8,self.en9,self.en10):
                en.pack_forget()
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.pack(side="right", fill="x")
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7,self.en8,self.en9,self.en10):
                en.pack(side="left", fill="x",padx=80, ipadx=60)
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6):
                lbl.configure(font=self.lblfont)
            for lbl in (self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.configure(font=self.font)
        #--------------------------------------------------------------------------------------------------------------
        elif db == 'net1':
            self.sub_btn.configure(command = lambda: self.coursecheck('net1'))
            self.var1.set(':Winlo          ')
            self.var2.set(':Server1          ')
            self.var3.set(':Server2          ')
            self.var4.set(':Server3          ')
            self.var5.set(':Exchange          ')
            self.var6.set(':Vmware          ')
            self.var7.set(':VDI          ')
            code = rowname[0]
            arownet1 = []
            mftdb = sqlite3.connect('mft01.db')
            cursor = mftdb.cursor()
            cursor.execute('''SELECT * from NET1''')
            row = cursor.fetchall()
            for r in row :
                if r[0]==code:
                    search = True
                    Winlo = r[1]
                    Server1 = r[2]
                    Server2 = r[3]
                    Server3 = r[4]
                    Exchange = r[5]
                    Vmware = r[6]
                    VDI = r[7]
                    arownet1 = [Winlo, Server1, Server2, Server3, Exchange, Vmware,VDI]
                    break
                else:
                    pass
            net1list(arownet1)
            if rownet1 == []:
                self.envar1.set("notregister")
                self.envar2.set("notregister")
                self.envar3.set("notregister")
                self.envar4.set("notregister")
                self.envar5.set("notregister")
                self.envar6.set("notregister")
                self.envar7.set("notregister")
                arownet1 = ["notregister","notregister","notregister","notregister","notregister","notregister","notregister"]
                net1list(arownet1)
            else:
                self.envar1.set(Winlo)
                self.envar2.set(Server1)
                self.envar3.set(Server2)
                self.envar4.set(Server3)
                self.envar5.set(Exchange)
                self.envar6.set(Vmware)
                self.envar7.set(VDI)
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.pack_forget()
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7,self.en8,self.en9,self.en10):
                en.pack_forget()
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7):
                lbl.pack(side="right", fill="x")
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7):
                en.pack(side="left", fill="x",padx=80, ipadx=60)
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7):
                lbl.configure(font=self.font)
        #--------------------------------------------------------------------------------------------------------------
        elif db == 'net2':
            self.sub_btn.configure(command = lambda: self.coursecheck('net2'))
            self.var1.set(':CCNA          ')
            self.var2.set(':CCNA_S          ')
            self.var3.set(':CCNP          ')
            self.var4.set(':CEH          ')
            self.var5.set(':Lpic1          ')
            self.var6.set(':Lpic2          ')
            code = rowname[0]
            arownet2 = []
            mftdb = sqlite3.connect('mft01.db')
            cursor = mftdb.cursor()
            cursor.execute('''SELECT * from NET2''')
            row = cursor.fetchall()
            for r in row:
                if code==r[0]:
                    CCNA = r[1]
                    CCNA_S = r[2]
                    CCNP = r[3]
                    CEH = r[4]
                    Lpic1 = r[5]
                    Lpic2 = r[6]
                    arownet2 = [CCNA, CCNA_S, CCNP, CEH, Lpic1, Lpic2]
                    break
                else:
                    search = False
            net2list(arownet2)
            if rownet2 == []:
                self.envar1.set("notregister")
                self.envar2.set("notregister")
                self.envar3.set("notregister")
                self.envar4.set("notregister")
                self.envar5.set("notregister")
                self.envar6.set("notregister")
                arownet2 = ["notregister", "notregister", "notregister", "notregister", "notregister", "notregister"]
                net2list(arownet2)
            else:
                self.envar1.set(CCNA)
                self.envar2.set(CCNA_S)
                self.envar3.set(CCNP)
                self.envar4.set(CEH)
                self.envar5.set(Lpic1)
                self.envar6.set(Lpic2)
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.pack_forget()
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7,self.en8,self.en9,self.en10):
                en.pack_forget()
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6):
                lbl.pack(side="right", fill="x")
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6):
                en.pack(side="left", fill="x",padx=80, ipadx=60)
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6):
                lbl.configure(font=self.font)
        #--------------------------------------------------------------------------------------------------------------
        elif db == 'pro1':
            self.sub_btn.configure(command = lambda: self.coursecheck('pro1'))
            self.var1.set(':Python          ')
            self.var2.set(':ML          ')
            self.var3.set(':Deep Learning          ')
            self.var4.set(':Image processing          ')
            self.var5.set(':C ++          ')
            self.var6.set(':C#          ')
            self.var7.set(':SQL          ')
            self.var8.set(':ASP.net          ')
            self.var9.set(':JavaScript          ')
            self.var10.set(':Block Chain          ')
            code = rowname[0]
            arowpro1 = []
            mftdb = sqlite3.connect('mft01.db')
            cursor = mftdb.cursor()
            cursor.execute('''SELECT * from pro1''')
            row = cursor.fetchall()
            for r in row :
                if r[0]==code:
                    search = True
                    Python = r[1]
                    ML = r[2]
                    DeepL = r[3]
                    ImagePro = r[4]
                    Cplus = r[5]
                    Csharp = r[6]
                    SQL = r[7]
                    ASP = r[8]
                    JS = r[9]
                    Block_C = r[10]
                    arowpro1 = [Python,ML,DeepL,ImagePro,Cplus,Csharp,SQL,ASP,JS,Block_C]
                    break
                else:
                    search = False
            pro1list(arowpro1)
            if rowpro1 == []:
                self.envar1.set("notregister")
                self.envar2.set("notregister")
                self.envar3.set("notregister")
                self.envar4.set("notregister")
                self.envar5.set("notregister")
                self.envar6.set("notregister")
                self.envar7.set("notregister")
                self.envar8.set("notregister")
                self.envar9.set("notregister")
                self.envar10.set("notregister")
                arowpro1 = ["notregister","notregister","notregister","notregister","notregister","notregister","notregister","notregister","notregister","notregister"]
                pro1list(arowpro1)
            else:
                self.envar1.set(Python)
                self.envar2.set(ML)
                self.envar3.set(DeepL)
                self.envar4.set(ImagePro)
                self.envar5.set(Cplus)
                self.envar6.set(Csharp)
                self.envar7.set(SQL)
                self.envar8.set(ASP)
                self.envar9.set(JS)
                self.envar10.set(Block_C)
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.pack_forget()
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7,self.en8,self.en9,self.en10):
                en.pack_forget()
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.pack(side="right", fill="x")
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7,self.en8,self.en9,self.en10):
                en.pack(side="left", fill="x",padx=80, ipadx=40)
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.configure(font=self.font)
        #------------------------------------------------------------------------------------------------------------
        elif db == 'pro2':
            self.sub_btn.configure(command = lambda: self.coursecheck('pro2'))
            self.var1.set(':JAVA          ')
            self.var2.set(':JAVA SE          ')
            self.var3.set(':JAVE EE          ')
            self.var4.set(':Android          ')
            self.var5.set(':Android with Kotlin          ')
            self.var6.set(':Android with JAVA          ')
            self.var7.set(':IOS          ')
            code = rowname[0]
            arowpro2 = []
            mftdb = sqlite3.connect('mft01.db')
            cursor = mftdb.cursor()
            cursor.execute('''SELECT * from pro2''')
            row = cursor.fetchall()
            for r in row :
                if r[0]==code:
                    search = True
                    Java = r[1]
                    SE = r[2]
                    EE = r[3]
                    Android = r[4]
                    Kotlin = r[5]
                    Android_Java = r[6]
                    IOS = r[7]
                    arowpro2 = [Java,SE,EE,Android,Kotlin,Android_Java,IOS]
                    break
                else:
                    search = False
            pro2list(arowpro2)
            if rowpro2 == []:
                self.envar1.set("notregister")
                self.envar2.set("notregister")
                self.envar3.set("notregister")
                self.envar4.set("notregister")
                self.envar5.set("notregister")
                self.envar6.set("notregister")
                self.envar7.set("notregister")
                arowpro2 = ["notregister","notregister","notregister","notregister","notregister","notregister","notregister"]
                pro2list(arowpro2)
            else:
                self.envar1.set(Java)
                self.envar2.set(SE)
                self.envar3.set(EE)
                self.envar4.set(Android)
                self.envar5.set(Kotlin)
                self.envar6.set(Android_Java)
                self.envar7.set(IOS)
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.pack_forget()
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7,self.en8,self.en9,self.en10):
                en.pack_forget()
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7):
                lbl.pack(side="right", fill="x")
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7):
                en.pack(side="left", fill="x",padx=80, ipadx=35)
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7):
                lbl.configure(font=self.font)
        #--------------------------------------------------------------------------------------------------------------
        elif db =='ict':
            self.sub_btn.configure(command = lambda: self.coursecheck('ict'))
            self.var1.set(':ICDL2          ')
            self.var2.set(':Excel Expert          ')
            self.var3.set(':Power BI          ')
            code = rowname[0]
            arowict = []
            mftdb = sqlite3.connect('mft01.db')
            cursor = mftdb.cursor()
            cursor.execute('''SELECT * from ict''')
            row = cursor.fetchall()
            for r in row :
                if r[0]==code:
                    search = True
                    ICDL2 = r[1]
                    Excel = r[2]
                    Power = r[3]
                    arowict = [ICDL2,Excel,Power]
                    break
                else:
                    search = False
            ictlist(arowict)
            if rowict == []:
                self.envar1.set("notregister")
                self.envar2.set("notregister")
                self.envar3.set("notregister")
                arowict = ["notregister","notregister","notregister"]
                ictlist(arowict)
            else:
                self.envar1.set(ICDL2)
                self.envar2.set(Excel)
                self.envar3.set(Power)
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.pack_forget()
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7,self.en8,self.en9,self.en10):
                en.pack_forget()
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3):
                lbl.pack(side="right", fill="x")
            for en in (self.en1,self.en2,self.en3):
                en.pack(side="left", fill="x",padx=80, ipadx=60)
            for lbl in (self.lb1,self.lb2,self.lb3):
                lbl.configure(font=self.font)
        #--------------------------------------------------------------------------------------------------------------
        elif db == 'web':
            self.sub_btn.configure(command = lambda: self.coursecheck('web'))
            self.var1.set(':Web2          ')
            self.var2.set(':Web3          ')
            self.var3.set(':React          ')
            self.var4.set(':Node JS          ')
            self.var5.set(':PHP          ')
            self.var6.set(':Django          ')
            self.var7.set(':Wordpress          ')
            self.var8.set(':Woocommerce          ')
            self.var9.set(':UI/UX          ')
            self.var10.set(':Seo          ')
            code = rowname[0]
            arowweb = []
            mftdb = sqlite3.connect('mft01.db')
            cursor = mftdb.cursor()
            cursor.execute('''SELECT * from web''')
            row = cursor.fetchall()
            for r in row :
                if r[0]==code:
                    search = True
                    web2 = r[1]
                    web3 = r[2]
                    React = r[3]
                    Node = r[4]
                    PHP = r[5]
                    Django = r[6]
                    Wordpress = r[7]
                    Woocommerce = r[8]
                    UIUX = r[9]
                    Seo = r[10]
                    arowweb = [web2,web3,React,Node,PHP,Django,Wordpress,Woocommerce,UIUX,Seo]
                    break
                else:
                    search = False
            weblist(arowweb)
            if rowweb == []:
                self.envar1.set("notregister")
                self.envar2.set("notregister")
                self.envar3.set("notregister")
                self.envar4.set("notregister")
                self.envar5.set("notregister")
                self.envar6.set("notregister")
                self.envar7.set("notregister")
                self.envar8.set("notregister")
                self.envar9.set("notregister")
                self.envar10.set("notregister")
                arowweb = ["notregister","notregister","notregister","notregister","notregister","notregister","notregister","notregister","notregister","notregister"]
                weblist(arowweb)
            else:
                self.envar1.set(web2)
                self.envar2.set(web3)
                self.envar3.set(React)
                self.envar4.set(Node)
                self.envar5.set(PHP)
                self.envar6.set(Django)
                self.envar7.set(Wordpress)
                self.envar8.set(Woocommerce)
                self.envar9.set(UIUX)
                self.envar10.set(Seo)
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.pack_forget()
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7,self.en8,self.en9,self.en10):
                en.pack_forget()
            #---------------------------------------------------------------------------------------------------------
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.pack(side="right", fill="x")
            for en in (self.en1,self.en2,self.en3,self.en4,self.en5,self.en6,self.en7,self.en8,self.en9,self.en10):
                en.pack(side="left", fill="x",padx=80, ipadx=40)
            for lbl in (self.lb1,self.lb2,self.lb3,self.lb4,self.lb5,self.lb6,self.lb7,self.lb8,self.lb9,self.lb10):
                lbl.configure(font=self.font)
   #*--------------------------------------------------------------------------------------------------------------------------------
    def coursecheck(self,name):
        global rowname
        global rowict
        global rowweb
        global rowpro1
        global rowpro2
        global rownet1
        global rownet2
        en1 = self.envar1.get()
        en2 = self.envar2.get()
        en3 = self.envar3.get()
        en4 = self.envar4.get()
        en5 = self.envar5.get()
        en6 = self.envar6.get()
        en7 = self.envar7.get()
        en8 = self.envar8.get()
        en9 = self.envar9.get()
        en10 = self.envar10.get()
        #----------------------------------------------------------------------------------------------------
        if name == 'STUDENT':
            db = 'STUDENT'
            #rowname = [Melli_code,Name,Last_Name,Father_Name,Phone,Email,Password,ICDL1,Algorithms,Network,web]
            a = True
            b = True
            c = True
            d = True
            e = True
            f = True
            #---------------------
            g = (rowname[7]==en7)
            h = (rowname[8]==en8)
            i = (rowname[9]==en9)
            j = (rowname[10]==en10)
        #----------------------------------------------------------------------------------------------------
        elif name == 'ict':
            db = 'ict'
            #arowict = [ICDL2,Excel,Power]
            a = (rowict[0]==en1)
            b = (rowict[1]==en2)
            c = (rowict[2]==en3)
            d = True
            e = True
            f = True
            g = True
            h = True
            i = True
            j = True
        #----------------------------------------------------------------------------------------------------
        elif name == 'web':
            db = 'web'
            #arowweb = [web2,web3,React,Node,PHP,Django,Wordpress,Woocommerce,UIUX,Seo]
            a = (rowweb[0]==en1)
            b = (rowweb[1]==en2)
            c = (rowweb[2]==en3)
            d = (rowweb[3]==en4)
            e = (rowweb[4]==en5)
            f = (rowweb[5]==en6)
            g = (rowweb[6]==en7)
            h = (rowweb[7]==en8)
            i = (rowweb[8]==en9)
            j = (rowweb[9]==en10)
        #----------------------------------------------------------------------------------------------------
        elif name == 'pro1':
            db = 'pro1'
            #arowpro1 = [Python,ML,DeepL,ImagePro,Cplus,Csharp,SQL,ASP,JS,Block_C]
            a = (rowpro1[0]==en1)
            b = (rowpro1[1]==en2)
            c = (rowpro1[2]==en3)
            d = (rowpro1[3]==en4)
            e = (rowpro1[4]==en5)
            f = (rowpro1[5]==en6)
            g = (rowpro1[6]==en7)
            h = (rowpro1[7]==en8)
            i = (rowpro1[8]==en9)
            j = (rowpro1[9]==en10)
        #----------------------------------------------------------------------------------------------------
        elif name == 'pro2':
            db = 'pro2'
            #arowpro2 = [Java,SE,EE,Android,Kotlin,Android_Java,IOS]
            a = (rowpro2[0]==en1)
            b = (rowpro2[1]==en2)
            c = (rowpro2[2]==en3)
            d = (rowpro2[3]==en4)
            e = (rowpro2[4]==en5)
            f = (rowpro2[5]==en6)
            g = (rowpro2[6]==en7)
            h = True
            i = True
            j = True
        #----------------------------------------------------------------------------------------------------
        elif name == 'net1':
            db = 'net1'
            #arownet1 = [Winlo, Server1, Server2, Server3, Exchange, Vmware,VDI]
            a = (rownet1[0]==en1)
            b = (rownet1[1]==en2)
            c = (rownet1[2]==en3)
            d = (rownet1[3]==en4)
            e = (rownet1[4]==en5)
            f = (rownet1[5]==en6)
            g = (rownet1[6]==en7)
            h = True
            i = True
            j = True
        #----------------------------------------------------------------------------------------------------
        elif name == 'net2':
            db = 'net2'
            #arownet2 = [CCNA, CCNA_S, CCNP, CEH, Lpic1, Lpic2]
            a = (rownet2[0]==en1)
            b = (rownet2[1]==en2)
            c = (rownet2[2]==en3)
            d = (rownet2[3]==en4)
            e = (rownet2[4]==en5)
            f = (rownet2[5]==en6)
            g = True
            h = True
            i = True
            j = True
        #----------------------------------------------------------------------------------------------------
        if a and b and c and d and e and f and g and h and i and j:
            messagebox.showinfo("پيام",".تغييري اعمال نشد")
        else:
            message = False
            dbchange = False
            if a==False:
                if en1=='pass' or en1=='notregister' or en1=='register':
                    self.database_submit(db,en1,0)
                    dbchange = True
                    message = False
                else:
                    dbchange = False
                    message = True
            #------------------------------------------------------------
            if b==False:
                if en2=='pass' or en2=='notregister' or en2=='register':
                    self.database_submit(db,en2,1)
                    dbchange = True
                    message = False
                else:
                    dbchange = False
                    message = True
            #------------------------------------------------------------
            if c==False:
                if en3=='pass' or en3=='notregister' or en3=='register':
                    self.database_submit(db,en3,2)
                    dbchange = True
                    message = False
                else:
                    dbchange = False
                    message = True
            #------------------------------------------------------------
            if d==False:
                if en4=='pass' or en4=='notregister' or en4=='register':
                    self.database_submit(db,en4,3)
                    dbchange = True
                    message = False
                else:
                    dbchange = False
                    message = True
            #------------------------------------------------------------
            if e==False:
                if en5=='pass' or en5=='notregister' or en5=='register':
                    self.database_submit(db,en5,4)
                    dbchange = True
                    message = False
                else:
                    dbchange = False
                    message = True
            #------------------------------------------------------------
            if f==False:
                if en6=='pass' or en6=='notregister' or en6=='register':
                    self.database_submit(db,en6,5)
                    dbchange = True
                    message = False
                else:
                    dbchange = False
                    message = True
            #------------------------------------------------------------
            if g==False:
                if en7=='pass' or en7=='notregister' or en7=='register':
                    self.database_submit(db,en7,6)
                    dbchange = True
                    message = False
                else:
                    dbchange = False
                    message = True
            #------------------------------------------------------------
            if h==False:
                if en8=='pass' or en8=='notregister' or en8=='register':
                    self.database_submit(db,en8,7)
                    dbchange = True
                    message = False
                else:
                    dbchange = False
                    message = True
            #------------------------------------------------------------
            if i==False:
                if en9=='pass' or en9=='notregister' or en9=='register':
                    self.database_submit(db,en9,8)
                    dbchange = True
                    message = False
                else:
                    dbchange = False
                    message = True
            #------------------------------------------------------------
            if j==False:
                if en10=='pass' or en10=='notregister' or en10=='register':
                    self.database_submit(db,en10,9)
                    dbchange = True
                    message = False
                else:
                    dbchange = False
                    message = True
                    

            if message == True:
                tk.messagebox.showinfo("پيام","لطفا از لغات در نظر گرفته شده استفاده کنید\n'pass','notregister','register'")
            else:
                pass

            if dbchange == True:
                tk.messagebox.showinfo("پيام",".تغييرات فقط در جدول انتخاب شده اعمال شد")
            else:
                tk.messagebox.showinfo("پيام",".تغييري اعمال نشد")
    #*--------------------------------------------------------------------------------------------------------------------------------
    def database_submit(self,db,entry,index):
        en1 = self.envar1.get()
        en2 = self.envar2.get()
        en3 = self.envar3.get()
        en4 = self.envar4.get()
        en5 = self.envar5.get()
        en6 = self.envar6.get()
        en7 = self.envar7.get()
        en8 = self.envar8.get()
        en9 = self.envar9.get()
        en10 = self.envar10.get()
        mftdb = sqlite3.connect('mft01.db')
        cursor = mftdb.cursor()
        #---------------------------------------------------------------------------------------------------------
        if db == 'web':
            rowtxt = ['web2','web3','React','Node_JS','PHP','Django','Wordpress','Woocommerce','UI_UX','Seo']
            cursor.execute('''SELECT * from web''')
            row = cursor.fetchall()
            for r in row:
                if rowname[0]==r[0]:
                    entity = True
                    break
                else:
                    entity = False
            if entity == True:
                dbtxt = "UPDATE web SET "+rowtxt[index]+"='"+entry+"' WHERE Melli_code='"+rowname[0]+"'"
                cursor.execute(dbtxt)
            else:
                r1 = [rowname[0],'notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister']
                r1[index+1]=entry
                record=[(r1[0],r1[1],r1[2],r1[3],r1[4],r1[5],r1[6],r1[7],r1[8],r1[9],r1[10])]
                cursor.executemany('''INSERT INTO web values(?,?,?,?,?,?,?,?,?,?,?)''',record)
            mftdb.commit()
        #---------------------------------------------------------------------------------------------------------
        elif db == 'STUDENT':
            rowtxt = ['Melli_code','Name','Last_Name','Father_Name','Phone','Email','ICDL1','Algorithms','Network','Web']
            dbtxt = "UPDATE STUDENT SET "+rowtxt[index]+"='"+entry+"' WHERE Melli_code='"+rowname[0]+"'"
            cursor.execute(dbtxt)
            mftdb.commit()
        #---------------------------------------------------------------------------------------------------------
        elif db == 'ict':
            rowtxt = ['ICDL2','Excel_Expert','Power_BI']
            cursor.execute('''SELECT * from ict''')
            row = cursor.fetchall()
            for r in row:
                if rowname[0]==r[0]:
                    entity = True
                    break
                else:
                    entity = False
            if entity == True:
                dbtxt = "UPDATE ict SET "+rowtxt[index]+"='"+entry+"' WHERE Melli_code='"+rowname[0]+"'"
                cursor.execute(dbtxt)
            else:
                r1 = [rowname[0],'notregister','notregister','notregister']
                r1[index+1]=entry
                record=[(r1[0],r1[1],r1[2],r1[3])]
                cursor.executemany('''INSERT INTO ict values(?,?,?,?)''',record)
            mftdb.commit()
        #---------------------------------------------------------------------------------------------------------
        elif db == 'pro1':
            rowtxt = ['python','ml','deep_learning','Image_proccessing','c_plusplus','c_sharp','sql','asp_net','javascriPt','block_chain']
            cursor.execute('''SELECT * from pro1''')
            row = cursor.fetchall()
            for r in row:
                if rowname[0]==r[0]:
                    entity = True
                    break
                else:
                    entity = False
            if entity == True:
                dbtxt = "UPDATE pro1 SET "+rowtxt[index]+"='"+entry+"' WHERE Melli_code='"+rowname[0]+"'"
                cursor.execute(dbtxt)
            else:
                r1 = [rowname[0],'notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister','notregister']
                r1[index+1]=entry
                record=[(r1[0],r1[1],r1[2],r1[3],r1[4],r1[5],r1[6],r1[7],r1[8],r1[9],r1[10])]
                cursor.executemany('''INSERT INTO pro1 values(?,?,?,?,?,?,?,?,?,?,?)''',record)
            mftdb.commit()
        #---------------------------------------------------------------------------------------------------------
        elif db == 'pro2':
            rowtxt = ['java','java_se','java_ee','android','android_with_kotlin','android_with_java','ios']
            cursor.execute('''SELECT * from pro2''')
            row = cursor.fetchall()
            for r in row:
                if rowname[0]==r[0]:
                    entity = True
                    break
                else:
                    entity = False
            if entity == True:
                dbtxt = "UPDATE pro2 SET "+rowtxt[index]+"='"+entry+"' WHERE Melli_code='"+rowname[0]+"'"
                cursor.execute(dbtxt)
            else:
                r1 = [rowname[0],'notregister','notregister','notregister','notregister','notregister','notregister','notregister']
                r1[index+1]=entry
                record=[(r1[0],r1[1],r1[2],r1[3],r1[4],r1[5],r1[6],r1[7])]
                cursor.executemany('''INSERT INTO pro2 values(?,?,?,?,?,?,?,?)''',record)
            mftdb.commit()
        #---------------------------------------------------------------------------------------------------------
        elif db == 'net1':
            rowtxt = ['winlo','server1','server2','server3','exchange','vmware','vdi']
            cursor.execute('''SELECT * from net1''')
            row = cursor.fetchall()
            for r in row:
                if rowname[0]==r[0]:
                    entity = True
                    break
                else:
                    entity = False
            if entity == True:
                dbtxt = "UPDATE net1 SET "+rowtxt[index]+"='"+entry+"' WHERE Melli_code='"+rowname[0]+"'"
                cursor.execute(dbtxt)
            else:
                r1 = [rowname[0],'notregister','notregister','notregister','notregister','notregister','notregister','notregister']
                r1[index+1]=entry
                record=[(r1[0],r1[1],r1[2],r1[3],r1[4],r1[5],r1[6],r1[7])]
                cursor.executemany('''INSERT INTO NET1 values(?,?,?,?,?,?,?,?)''',record)
            mftdb.commit()
        #---------------------------------------------------------------------------------------------------------
        elif db == 'net2':
            rowtxt = ['ccna','ccna_security','ccnp','ceh','lpic1','lpic2']
            cursor.execute('''SELECT * from net2''')
            row = cursor.fetchall()
            for r in row:
                if rowname[0]==r[0]:
                    entity = True
                    break
                else:
                    entity = False
            if entity == True:
                dbtxt = "UPDATE net2 SET "+rowtxt[index]+"='"+entry+"' WHERE Melli_code='"+rowname[0]+"'"
                cursor.execute(dbtxt)
            else:
                r1 = [rowname[0],'notregister','notregister','notregister','notregister','notregister','notregister']
                r1[index+1]=entry
                record=[(r1[0],r1[1],r1[2],r1[3],r1[4],r1[5],r1[6])]
                cursor.executemany('''INSERT INTO NET2 values(?,?,?,?,?,?,?)''',record)
            mftdb.commit()

#Class child14: Menu_Admin ------------------------------------------------------------------------------------------------------------------------------------------
class Menu_Admin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #----MenuBar------------------------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #------------------------------------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 10, ipadx = 1000)
        #------------------------------------------------------------------------------------------
        label = tk.Label(self, text="دسترسي سريع به صفحات",font=controller.lblfont)
        label.pack(side="top", fill="x", pady=10)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        firstpage_btn = tk.Button(self, text="صفحه معرفي",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("StartPage"), activebackground ="white")
        firstpage_btn.pack(side="top", fill="x",pady=2)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        home_btn = tk.Button(self, text="صفحه اصلي",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("HomePage"), activebackground ="white")
        home_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        signup_btn = tk.Button(self, text="صفحه ادمين",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("Admin"), activebackground ="white")
        signup_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        login_btn = tk.Button(self, text="خارج شدن از پنل ادمين",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.signout(), activebackground ="white")
        login_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        close_btn = tk.Button(self, text="بستن برنامه",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.close(), activebackground ="white")
        close_btn.pack(side="top", fill="x",pady=2)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #----Footer--------------------------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)

#Class child15: Menu_login ------------------------------------------------------------------------------------------------------------------------------------------
class Menu_login(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #----MenuBar------------------------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #------------------------------------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 10, ipadx = 1000)
        #------------------------------------------------------------------------------------------
        label = tk.Label(self, text="دسترسي سريع به صفحات",font=controller.lblfont)
        label.pack(side="top", fill="x", pady=10)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        firstpage_btn = tk.Button(self, text="صفحه معرفي",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("StartPage"), activebackground ="white")
        firstpage_btn.pack(side="top", fill="x",pady=2)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        home_btn = tk.Button(self, text="صفحه اصلي",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("HomePage"), activebackground ="white")
        home_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        signup_btn = tk.Button(self, text="پنل کاربر",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("User"), activebackground ="white")
        signup_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        login_btn = tk.Button(self, text="خارج شدن از پنل کاربر",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.signout(), activebackground ="white")
        login_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        changeuser_btn = tk.Button(self, text="تغيير اطلاعات کاربر",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("Change_User"), activebackground ="white")
        changeuser_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        SET_CRS_btn = tk.Button(self, text="ليست دوره هاي مجتمع فني",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("SET_CRS"), activebackground ="white")
        SET_CRS_btn.pack(side="top", fill="x",pady=2)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        ict_btn = tk.Button(self, text="ليست دروس مهارت پايه",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("ict"), activebackground ="white")
        ict_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        web_btn = tk.Button(self, text="ليست دروس وب",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("web"), activebackground ="white")
        web_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        programming1_btn = tk.Button(self, text="ليست دروس برنامه نويسي 1",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("programming1"), activebackground ="white")
        programming1_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        programming2_btn = tk.Button(self, text="ليست دروس برنامه نويسي 2",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("programming2"), activebackground ="white")
        programming2_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        net_btn = tk.Button(self, text="ليست دروس نت",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("net"), activebackground ="white")
        net_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        close_btn = tk.Button(self, text="بستن برنامه",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.close(), activebackground ="white")
        close_btn.pack(side="top", fill="x",pady=2)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #----Footer--------------------------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)

#Class child16: Menu_logout ------------------------------------------------------------------------------------------------------------------------------------------
class Menu_logout(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #----MenuBar------------------------------------------------------------------------------
        menubtn_fr = tk.Frame(self)
        menubtn_fr.pack(side="top", fill="x")
        controller.menubar(menubtn_fr)
        #------------------------------------------------------------------------------------------
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center',pady = 10, ipadx = 1000)
        #------------------------------------------------------------------------------------------
        label = tk.Label(self, text="دسترسي سريع به صفحات",font=controller.lblfont)
        label.pack(side="top", fill="x", pady=10)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        firstpage_btn = tk.Button(self, text="صفحه معرفي",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("StartPage"), activebackground ="white")
        firstpage_btn.pack(side="top", fill="x",pady=2)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        home_btn = tk.Button(self, text="صفحه اصلي",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("HomePage"), activebackground ="white")
        home_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        signup_btn = tk.Button(self, text="صفحه ثبت نام در سامانه",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("SignupPage"), activebackground ="white")
        signup_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        login_btn = tk.Button(self, text="صفحه ورود",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("SigninPage"), activebackground ="white")
        login_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        Forgetpsw_btn = tk.Button(self, text="فراموشي رمز عبور",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("Forgetpsw"), activebackground ="white")
        Forgetpsw_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        SET_CRS_btn = tk.Button(self, text="ليست دوره هاي مجتمع فني",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("SET_CRS"), activebackground ="white")
        SET_CRS_btn.pack(side="top", fill="x",pady=2)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        ict_btn = tk.Button(self, text="ليست دروس مهارت پايه",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("ict"), activebackground ="white")
        ict_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        web_btn = tk.Button(self, text="ليست دروس وب",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("web"), activebackground ="white")
        web_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        programming1_btn = tk.Button(self, text="ليست دروس برنامه نويسي 1",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("programming1"), activebackground ="white")
        programming1_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        programming2_btn = tk.Button(self, text="ليست دروس برنامه نويسي 2",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("programming2"), activebackground ="white")
        programming2_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        net_btn = tk.Button(self, text="ليست دروس نت",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.show_frame("net"), activebackground ="white")
        net_btn.pack(side="top", fill="x",pady=1)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #------------------------------------------------------------------------------------------
        close_btn = tk.Button(self, text="بستن برنامه",font=controller.menufont,bd=0,cursor='hand2',
                            command=lambda: controller.close(), activebackground ="white")
        close_btn.pack(side="top", fill="x",pady=2)
        ttk.Separator(self,orient = 'horizontal').pack(side='top',anchor='center', ipadx = 1000)
        #----Footer--------------------------------------------------------------------------------
        footer_fr = tk.Frame(self)
        ttk.Separator(footer_fr,orient = 'horizontal').pack(side='top',anchor='center',pady = 1, ipadx = 1000)
        footer_fr.pack(side="bottom", fill="x")
        controller.Footer(footer_fr)
#------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
