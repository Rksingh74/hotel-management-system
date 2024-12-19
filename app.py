from tkinter import *
from tkinter import messagebox

import _tkinter
import pymysql
import HOTEL
class LoginClass:
    def __init__(self):
        self.window  = Tk()
        # ---------------- settings -------------------
        self.window.title("HOTEL MANAGEMENT STSTEM /Login")
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()

        w1 = int(w/2)
        h1 = int(h/2)
        x1 = int(w/4)
        y1 = int(h/4)
        self.window.minsize(w1,h1)
        self.window.maxsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,x1,y1))
        # -------------- widgets -------------------------
        myfont1 = ('Modern No. 20',18,'bold')
        mycolor1 ='#FFF6FA'
        mycolor2 = "#C13168"

        self.window.config(background=mycolor1)
        self.hdlbl = Label(self.window,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),
                           bg="black",fg="gold",bd=4,relief=RIDGE)

        self.L1 = Label(self.window,text="Username",font=myfont1,background=mycolor1)
        self.L2 = Label(self.window,text="Password",font=myfont1,background=mycolor1)

        self.t1 = Entry(self.window,font=myfont1)
        self.t2 = Entry(self.window,font=myfont1,show='*')


        #------------------- buttons ------------------------
        self.b1= Button(self.window,text='Login',font=myfont1,background=mycolor2,
                        foreground='white',command=self.checkData)
        #----------------- placements ----------------------
        self.hdlbl.place(x=0,y=0,width=w1,height=70)
        x1 = 100
        y1 = 100
        x_diff=150
        y_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=390,height=40)

        self.datebaseConnection()
        self.clearPage()
        self.window.mainloop()

    def datebaseConnection(self):
        try:

            self.conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
            self.curr = self.conn.cursor()
            # self.conn = pymysql.connect(host='localhost',db='rental_db',user='root',password='')
            # self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error","Database Connection Error : \n"+str(e),parent=self.window)

    def checkData(self):
        try:
            qry = 'select * from usertable where username=%s and password=%s'
            rowcount = self.curr.execute(qry, (self.t1.get(), self.t2.get()))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                un = data[0]
                ut = data[2]
                self.window.withdraw()  # Withdraw the current window without destroying it
                try:
                    from HOTEL import hotelmanagementsytem
                    hotelmanagementsytem(Toplevel(self.window), un, ut)  # Use Toplevel to create a new window
                except _tkinter.TclError:
                    pass  # Catch the exception if Toplevel command fails (window already destroyed)
            else:
                messagebox.showwarning("Empty", "Wrong username or password", parent=self.window)
        except Exception as e:
            messagebox.showerror("Error", "Select Query Error : \n" + str(e), parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)




if __name__ == '__main__':
    LoginClass()