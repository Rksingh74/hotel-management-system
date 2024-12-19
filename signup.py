from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import pymysql


class SignupClass:
    def __init__(self):
        self.window  = Tk()
        # ---------------- settings -------------------
        self.window.title("HOTEL MANAGEMENT SYSTEM/Signup")
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()

        w1 = int(w/2)
        h1 = int(h/2)
        x1 = int(w/4)
        y1 = int(h/4)
        self.window.minsize(w1,h1)
        self.window.maxsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,x1,y1)) #w,h,x,y
        # -------------- widgets -------------------------
        myfont1 = ('Modern No. 20',18,'bold')
        mycolor1 ='#FFF6FA'
        mycolor2 = "#C13168"

        self.window.config(background=mycolor1)
        self.hdlbl = Label(self.window,text="HOTEL MANAGEMENT SYSTEM",font=('Algerian',30),
                           background=mycolor2,foreground='white')

        self.L1 = Label(self.window,text="Username",font=myfont1,background=mycolor1)
        self.L2 = Label(self.window,text="Password",font=myfont1,background=mycolor1)
        self.L3 = Label(self.window,text="Usertype",font=myfont1,background=mycolor1)

        self.t1 = Entry(self.window,font=myfont1)
        self.t2 = Entry(self.window,font=myfont1,show='*')
        self.v1 = StringVar()
        self.c1 = Combobox(self.window, values=['Admin','Co-Admin'] ,
                           font=myfont1,state='disable',textvariable=self.v1)
        self.c1.current(0)


        #------------------- buttons ------------------------
        self.b1= Button(self.window,text='Create Admin',font=myfont1,background=mycolor2,
                        foreground='white',command=self.saveData)
        #----------------- placements ----------------------
        self.hdlbl.place(x=0,y=0,width=w1,height=70)
        x1 = 100
        y1 = 100
        x_diff=150
        y_diff=40


        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=390,height=40)

        self.datebaseConnection()
        self.clearPage()
        self.window.mainloop()

    def datebaseConnection(self):
        try:
            self.conn = pymysql.connect(host='localhost',db='rental_db',user='root',password='')
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error","Database Connection Error : \n"+str(e),parent=self.window)

    def saveData(self):
        try:
            qry='insert into usertable values(%s,%s,%s)'
            rowcount = self.curr.execute(qry,(self.t1.get(),self.t2.get(), self.v1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Admin created successfully",parent=self.window)
                self.clearPage()
                self.window.destroy()
                from login import LoginClass
                LoginClass()
        except Exception as e:
            messagebox.showerror("Error","Insertion Query Error : \n"+str(e),parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)


if __name__ == '__main__':
    SignupClass()
