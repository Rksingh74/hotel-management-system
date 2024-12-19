
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
import pymysql
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime

class detaillist:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x565+232+222")

    
        # =========================== Title ===============================
        lbl_title = Label(self.root, text="Room Booking", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1535, height=50)

        # ============================ Level Frame =========================
        levelframeleft = LabelFrame(self.root, bd=4, relief=RIDGE, text="New Room Add", font=("times new roman", 20, "bold"), padx=2)
        levelframeleft.place(x=5, y=50, width=540, height=350)


      #======variable==========  
        self.var_Floor=StringVar()
        self.var_Roomno=StringVar()
        self.var_Roomtype=StringVar()
       

        # ============================ Levels and Entry ====================
        lbl_Floor = Label(levelframeleft, text="Floor", font=("times new roman", 14, "bold"), padx=2, pady=5)
        lbl_Floor.grid(row=0, column=0, sticky=W)

        enty_Floor = ttk.Entry(levelframeleft,textvariable=self.var_Floor, font=("times new roman", 14, "bold"), width=22)
        enty_Floor.grid(row=0, column=1, sticky=W)

        lbl_Room_no = Label(levelframeleft, text="Room No", font=("times new roman", 14, "bold"), padx=2, pady=5)
        lbl_Room_no.grid(row=1, column=0, sticky=W)

        enty_Room_no= ttk.Entry(levelframeleft,textvariable=self.var_Roomno, font=("times new roman", 14, "bold"), width=22)
        enty_Room_no.grid(row=1, column=1, sticky=W)

        lbl_Room_Type = Label(levelframeleft, text="Room Type", font=("times new roman", 14, "bold"), padx=2, pady=5)
        lbl_Room_Type.grid(row=2, column=0, sticky=W)

        enty_Room_Type= ttk.Entry(levelframeleft,textvariable=self.var_Roomtype, font=("times new roman", 14, "bold"), width=22)
        enty_Room_Type.grid(row=2, column=1, sticky=W)


        #===============button ==========


        btn_frame = Frame(levelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=500, height=40)

        btn_add = Button(btn_frame, text="Add",command=self.add_data, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=12)
        btn_add.grid(row=0, column=0, padx=1, pady=1)

        btn_update = Button(btn_frame, text="Update",command=self.update, font=("times new roman", 12, "bold"), bg="black", fg="gold",width=12)
        btn_update.grid(row=0, column=1, padx=1, pady=1)

        btn_Delete = Button(btn_frame, text="Delete",command=self.ddelete, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=12)
        btn_Delete.grid(row=0, column=2, padx=1, pady=1)

        btn_Reset = Button(btn_frame, text="Reset",command=self.reset, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=12)
        btn_Reset.grid(row=0, column=3, padx=1, pady=1)



        table_frame = LabelFrame(self.root, bd=4, relief=RIDGE, text="Show Room Details", font=("times new roman", 20, "bold"), padx=2)
        table_frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)


        


        self.cust_details_Table = ttk.Treeview(
            table_frame,
            column=("Floor","Roomno","Roomtype"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )
        scroll_x.pack(side=BOTTOM, fill='x')
        scroll_y.pack(side=RIGHT, fill='y')

        scroll_x.config(command=self.cust_details_Table.xview)
        scroll_y.config(command=self.cust_details_Table.yview)

        self.cust_details_Table.heading("Floor", text="Floor No")
        self.cust_details_Table.heading("Roomno", text="Room No")
        self.cust_details_Table.heading("Roomtype", text="Room Type")
       


        self.cust_details_Table["show"] = "headings"



        # self.cust_details_Table.column("contact", width=100)
        self.cust_details_Table.column("Floor", width=100)
        self.cust_details_Table.column("Roomno", width=100)
        self.cust_details_Table.column("Roomtype", width=100)

        self.cust_details_Table.pack(fill=BOTH,expand=1)
        self.cust_details_Table.bind("<ButtonRelease>",self.get_cursor)
        self.fetchdata()
    #========================add data===============
    def add_data(self):
        if self.var_Floor.get()=="" or  self.var_Roomtype.get()=="":
            messagebox.showerror("Error","All field are required")
        else:
            try:
                conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                
                  self.var_Floor.get(),
                    self.var_Roomno.get(),
                    self.var_Roomtype.get(),
                                                                ))
                conn.commit()
                # self.fetchdata()
                conn.close()
                messagebox.showinfo("suceess","New Room added successfully",parent=self.root)
                
            
            except Exception as e:
                messagebox.showerror("Error","Something went wrong : \n"+str(e),parent=self.root)
            #     conn = mysql.connector.connect(host='localhost',database='hotel_mgmt',user='root',password='')
            
    #fetch data 
    def fetchdata(self):

        conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details ")
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
        
        self.var_Floor.set(row[0])
        self.var_Roomno.set(row[1])
        self.var_Roomtype.set(row[2])

    # update
    def update(self):
        if self.var_Floor.get()=="":
            messagebox.showerror("Error","please enter Room details",parent=self.root)
        else:
            conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
            my_cursor = conn.cursor()
            my_cursor.execute("update details set Floor=%s,roomtype=%s where roomno=%s",(
                                
                self.var_Floor.get(),
                self.var_Roomtype.get(),
                self.var_Roomno.get(),
                              
            ))
            conn.commit()
            self.fetchdata()
            conn.close()
            messagebox.showinfo("Update","customer data has been updated",parent=self.root)


    def ddelete(self):
        ddelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room details?",parent=self.root)
        if ddelete>0:
            conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
            my_cursor = conn.cursor()
            query="delete from details where Roomno=%s"
            value=(self.var_Roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not ddelete:
                return
        conn.commit()
        self.fetchdata()

        conn.close()
#=============================reset=============
    def reset(self):
                self.var_Floor.set("")
                self.var_Roomno.set(""),
                self.var_Roomtype.set(""),
               

       
    

      







if __name__ == '__main__':
    root = Tk()
    obj = detaillist(root)
    root.mainloop()
