

from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
import pymysql
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime

class roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x565+232+222")



        #variable
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        # =========================== Title ===============================
        lbl_title = Label(self.root, text="Room Booking", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1535, height=50)

        # ============================ Level Frame =========================
        levelframeleft = LabelFrame(self.root, bd=4, relief=RIDGE, text="Room Booking", font=("times new roman", 20, "bold"), padx=2)
        levelframeleft.place(x=5, y=50, width=455, height=490)

        # ============================ Levels and Entry ====================
        lbl_contact = Label(levelframeleft, text="Customer Contact", font=("times new roman", 14, "bold"), padx=2, pady=5)
        lbl_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(levelframeleft,textvariable=self.var_contact, font=("times new roman", 14, "bold"), width=16)
        enty_contact.grid(row=0, column=1, sticky=W)

        # Fetch data button
        btn_fetch = Button(levelframeleft,command=self.fetchcontact, text="Fetch Data", font=("times new roman", 10, "bold"), bg="black", fg="gold", width=10)
        btn_fetch.place(x=350, y=4)

        lbl_Check_in = Label(levelframeleft, text="Check in Date", font=("times new roman", 14, "bold"), padx=2, pady=5)
        lbl_Check_in.grid(row=1, column=0, sticky=W)

        enty_ref = ttk.Entry(levelframeleft,textvariable=self.var_checkin, font=("times new roman", 14, "bold"), width=23)
        enty_ref.grid(row=1, column=1)

        lbl_check_out = Label(levelframeleft, text="Check out Date", font=("times new roman", 14, "bold"), padx=2, pady=5)
        lbl_check_out.grid(row=2, column=0, sticky=W)

        enty_ref = ttk.Entry(levelframeleft,textvariable=self.var_checkout, font=("times new roman", 14, "bold"), width=23)
        enty_ref.grid(row=2, column=1)

        lbl_room_type = Label(levelframeleft, text="Room type", font=("times new roman", 14, "bold"), padx=4, pady=6)
        lbl_room_type.grid(row=3, column=0, sticky=W)

        conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
        my_cursor = conn.cursor()
        my_cursor.execute("select Roomtype from details",)
        id=my_cursor.fetchall()

        ent_room_type = ttk.Combobox(levelframeleft,textvariable=self.var_roomtype, font=("times new roman", 14, "bold"), width=21, state="readonly")
        ent_room_type["value"] = id
        ent_room_type.current(0)
        ent_room_type.grid(row=3, column=1)

        lbl_available = Label(levelframeleft, text="Available Room", font=("times new roman", 14, "bold"), padx=4, pady=6)
        lbl_available.grid(row=4, column=0, sticky=W)

        # ent_available = ttk.Entry(levelframeleft,textvariable=self.var_roomavailable, font=("times new roman", 14, "bold"), width=23)
        # ent_available.grid(row=4, column=1)

        conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
        my_cursor = conn.cursor()
        my_cursor.execute("select Roomno from details",)
        rows=my_cursor.fetchall()
                                
        ent_Roomno= ttk.Combobox(levelframeleft,textvariable=self.var_roomavailable, font=("times new roman", 14, "bold"), width=21, state="readonly")
        ent_Roomno["value"] = rows
        ent_Roomno.current(0)
        ent_Roomno.grid(row=4, column=1)




        lbl_meal = Label(levelframeleft, text="Meal", font=("times new roman", 14, "bold"), padx=4, pady=6)
        lbl_meal.grid(row=5, column=0, sticky=W)

        ent_meal = ttk.Entry(levelframeleft,textvariable=self.var_meal, font=("times new roman", 14, "bold"), width=23)
        ent_meal.grid(row=5, column=1)

        lbl_no_of_day = Label(levelframeleft, text="No of Day", font=("times new roman", 14, "bold"), padx=4, pady=6)
        lbl_no_of_day.grid(row=6, column=0, sticky=W)

        ent_NO_of_day = ttk.Entry(levelframeleft,textvariable=self.var_noofdays, font=("times new roman", 14, "bold"), width=23)
        ent_NO_of_day.grid(row=6, column=1)

        lbl_paid_text = Label(levelframeleft, text="Paid text", font=("times new roman", 14, "bold"), padx=4, pady=6)
        lbl_paid_text.grid(row=7, column=0, sticky=W)

        ent_text = ttk.Entry(levelframeleft,textvariable=self.var_paidtax, font=("times new roman", 14, "bold"), width=23)
        ent_text.grid(row=7, column=1)

        lbl_Sub_Total = Label(levelframeleft, text="Sub Total", font=("times new roman", 14, "bold"), padx=4, pady=6)
        lbl_Sub_Total.grid(row=7, column=0, sticky=W)

        ent_Sub_Total = ttk.Entry(levelframeleft,textvariable=self.var_actualtotal, font=("times new roman", 14, "bold"), width=23)
        ent_Sub_Total.grid(row=7, column=1)

        lbl_Total_Cost = Label(levelframeleft, text="Total Cost", font=("times new roman", 14, "bold"), padx=4, pady=6)
        lbl_Total_Cost.grid(row=8, column=0, sticky=W)

        ent_Cost = ttk.Entry(levelframeleft,textvariable=self.var_total, font=("times new roman", 14, "bold"), width=23)
        ent_Cost.grid(row=8, column=1)
        
# ===============button =================
        btn_add = Button(levelframeleft, text="Bill",command=self.total, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_add.grid(row=9, column=0, padx=1, sticky=W)

        btn_frame = Frame(levelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btn_add = Button(btn_frame, text="Add",command=self.add_data, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_add.grid(row=0, column=0, padx=1, pady=1)

        btn_update = Button(btn_frame, text="Update",command=self.update, font=("times new roman", 12, "bold"), bg="black", fg="gold",width=11)
        btn_update.grid(row=0, column=1, padx=1, pady=1)

        btn_Delete = Button(btn_frame, text="Delete",command=self.mdelete, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=11)
        btn_Delete.grid(row=0, column=2, padx=1, pady=1)

        btn_Reset = Button(btn_frame, text="Reset",command=self.reset, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=8)
        btn_Reset.grid(row=0, column=3, padx=1, pady=1)

        # Right side image
        img3 = Image.open("C:/Users/rahul/OneDrive/Desktop/try/New folder/hotel.jpg")
        img3 = img3.resize((550, 300), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=820, y=55, width=450, height=250)

        # Table frame with search data
        tableframe = LabelFrame(self.root, bd=4, relief=RIDGE, text="View details and search", font=("times new roman", 20, "bold"), padx=2)
        tableframe.place(x=455, y=280, width=850, height=260)

        self.search_var = StringVar()

        lbl_search1 = Label(tableframe, text="Search by: ", font=("times new roman", 14, "bold"), bg="red", fg="white")
        lbl_search1.grid(row=0, column=0, sticky=W)

        self.text_search = StringVar()

        combo_search = ttk.Combobox(tableframe, textvariable=self.search_var, font=("times new roman", 16, "bold"), width=20, state="readonly")
        combo_search["value"] = ("mobile", "roomavailable")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=4)

        enty_idnum = ttk.Entry(tableframe, textvariable=self.text_search, font=("times new roman", 16, "bold"), width=22)
        enty_idnum.grid(row=0, column=2, padx=1)

        btn_search = Button(tableframe, text="Search",command=self.btsearch, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=12)
        btn_search.grid(row=0, column=3, padx=1, pady=1)

        btn_Showall = Button(tableframe, text="Show All",command=self.fetchdata, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=12)
        btn_Showall.grid(row=0, column=4, padx=1, pady=1)

        # Show table
        room_table = Frame(tableframe, bd=2, relief=RIDGE)
        room_table.place(x=0, y=50, width=850, height=180)

        scroll_x = ttk.Scrollbar(room_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(room_table, orient=VERTICAL)

        self.cust_details_Table = ttk.Treeview(
            room_table,
            column=("contact", "checkine", "checkout", "roomtype", "roomavailable", "meal", "noofdays"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill='x')
        scroll_y.pack(side=RIGHT, fill='y')

        scroll_x.config(command=self.cust_details_Table.xview)
        scroll_y.config(command=self.cust_details_Table.yview)

        self.cust_details_Table.heading("contact", text="Mobile")
        self.cust_details_Table.heading("checkine", text="Check-in")
        self.cust_details_Table.heading("checkout", text="Check-out")
        self.cust_details_Table.heading("roomtype", text="Room Type")
        self.cust_details_Table.heading("roomavailable", text="Room no")
        self.cust_details_Table.heading("meal", text="Meal")
        self.cust_details_Table.heading("noofdays", text="Noofdays")

        self.cust_details_Table["show"] = "headings"
        self.cust_details_Table.column("contact", width=100)


        # self.cust_details_Table.column("contact", width=100)
        self.cust_details_Table.column("checkine", width=100)
        self.cust_details_Table.column("checkout", width=100)
        self.cust_details_Table.column("roomtype", width=100)
        self.cust_details_Table.column("roomavailable", width=100)
        self.cust_details_Table.column("meal", width=100)
        self.cust_details_Table.column("noofdays", width=100)
        self.cust_details_Table.column("noofdays", width=100)

        self.cust_details_Table.pack(fill=BOTH, expand=1)
        self.cust_details_Table.bind("<ButtonRelease>",self.get_cursor)
        self.fetchdata()


    def fetchcontact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","pleaseenter contact number",parent=self.root)
        else:
            conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
            my_cursor = conn.cursor()  
            query = ("SELECT Name FROM customer WHERE Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=465,y=56,width=300,height=180)

                lblName=Label(showDataframe,text="Name",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
                my_cursor = conn.cursor()  
                query = ("SELECT Gender FROM customer WHERE Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showDataframe,text="Gender",font=("arial",12,"bold"))
                lblgender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)




                conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
                my_cursor = conn.cursor()  
                query = ("SELECT Email FROM customer WHERE Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Email",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)


                conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
                my_cursor = conn.cursor()  
                query = ("SELECT Address FROM customer WHERE Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showDataframe,text="Address",font=("arial",12,"bold"))
                lblgender.place(x=0,y=90)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=90)


                conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
                my_cursor = conn.cursor()  
                query = ("SELECT Nationality FROM customer WHERE Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblnationality=Label(showDataframe,text="Nationality",font=("arial",12,"bold"))
                lblnationality.place(x=0,y=120)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=120)


#===============search system ==============

    def btsearch(self):
        conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
        my_cursor = conn.cursor()  
        query = "SELECT * FROM room WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.text_search.get()) + "%'"
        print(query)
        my_cursor.execute(query)

        # my_cursor.execute("select * from customer where "+str(self.search_var.get())+"LIKE  '%"+str(self.text_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.cust_details_Table.delete(*self.cust_details_Table.get_children())
            for i in rows:
                self.cust_details_Table.insert("",END,values=i)
            conn.commit()
            
        conn.close()


#===============tatal bill calculation ==========

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
      

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tex="Rs."+str("%.2f"%((q5)*0.1))
            st="Rs."+str("%.2f"%((q5)))
            tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tex)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get()=="Lanch" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tex="Rs."+str("%.2f"%((q5)*0.1))
            st="Rs."+str("%.2f"%((q5)))
            tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tex)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get()=="Lanch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tex="Rs."+str("%.2f"%((q5)*0.1))
            st="Rs."+str("%.2f"%((q5)))
            tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tex)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get()=="Lanch" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tex="Rs."+str("%.2f"%((q5)*0.1))
            st="Rs."+str("%.2f"%((q5)))
            tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tex)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tex="Rs."+str("%.2f"%((q5)*0.1))
            st="Rs."+str("%.2f"%((q5)))
            tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tex)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)










    def add_data(self):
        if self.var_contact.get()=="" or  self.var_checkin.get()=="":
            messagebox.showerror("Error","All field are required")
        else:
            try:
                conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                
                  self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),


                                                                ))
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("suceess","Room Booked",parent=self.root)
                
            
            except Exception as e:
                messagebox.showerror("Error","Something went wrong : \n"+str(e),parent=self.root)
            #     conn = mysql.connector.connect(host='localhost',database='hotel_mgmt',user='root',password='')
            

    #fetch data 
    def fetchdata(self):

        conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room ")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_Table.delete(*self.cust_details_Table.get_children())
            for i in rows:
                self.cust_details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

#========CURSOR============


    def get_cursor(self,event=""):
        cursor_row=self.cust_details_Table.focus()
        content=self.cust_details_Table.item(cursor_row)
        row=content["values"]
        
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
    


    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root)
        if mdelete>0:
            conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
            my_cursor = conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetchdata()
        conn.close()


    def reset(self):
                self.var_contact.set("")
                self.var_checkin.set(""),
                self.var_checkout.set(""),
                # self.var_gender.set(""),
                self.var_actualtotal.set(""),
                self.var_noofdays.set(""),
                self.var_meal.set(""),
                # self.var_nationality.set(""),
                # self.var_id_proof.set(""),
                self.var_roomavailable.set(""),
                self.var_roomtype.set("")
                self.var_total.set("")
    
   

        


# update
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter your mobile number", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host='localhost', db='hotel_mgmt', user='root', password='')
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE room SET `check-in` = %s, `check-out` = %s, roomtype = %s, roomavailable = %s, meal = %s, noofdays = %s WHERE contact = %s", (
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_contact.get()
                ))
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("Update", "Room data has been updated", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", "Something went wrong: \n" + str(e), parent=self.root)





if __name__ == '__main__':
    root = Tk()
    obj = roombooking(root)
    root.mainloop()


