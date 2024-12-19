
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
import pymysql
import mysql.connector
import random
from room import roombooking
from tkinter import messagebox





class cust_wind:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x565+232+222")


        #=========================== variable ====================

        self.var_ref=StringVar()
        # X=random.randint(1000,9999)
        # self.var_ref.set(str(X))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        

         #=========================== Title===============================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1535,height=50)
      
        #============================ level frame =========================
        levelframeleft=LabelFrame(self.root,bd=4,relief=RIDGE,text="CUSTOMER DETAILS",font=("times new roman",20,"bold"),padx=2)
        levelframeleft.place(x=5,y=50,width=455,height=490)
        
        #============================ levels and entry ====================
        lbl_customer_ref=Label(levelframeleft,text="Customer ref",font=("times new roman",14,"bold"),padx=2,pady=5)
        lbl_customer_ref.grid(row=0,column=0,sticky=W)

        enty_ref = ttk.Entry(levelframeleft,textvariable=self.var_ref,font=("times new roman",14,"bold"),width=19)
        enty_ref.grid(row=0,column=1)

        #========cust name ==========
        lbl_customer_name=Label(levelframeleft,text="Customer name",font=("times new roman",14,"bold"),padx=2,pady=5)
        lbl_customer_name.grid(row=1,column=0,sticky=W)

        enty_ref = ttk.Entry(levelframeleft,textvariable=self.var_cust_name,font=("times new roman",14,"bold"),width=19)
        enty_ref.grid(row=1,column=1)






# ========mother name ==========

        lbl_mname=Label(levelframeleft,text="Customer mother's name",font=("times new roman",14,"bold"),padx=2,pady=5)
        lbl_mname.grid(row=2,column=0,sticky=W)

        enty_ref = ttk.Entry(levelframeleft,textvariable=self.var_mother,font=("times new roman",14,"bold"),width=19)
        enty_ref.grid(row=2,column=1)

# =========== gender ===============

        lbl_gender=Label(levelframeleft,text="Gender",font=("times new roman",14,"bold"),padx=2,pady=5)
        lbl_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(levelframeleft,textvariable=self.var_gender,font=("times new roman",14,"bold"),width=17,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

 



        # enty_ref = ttk.Entry(levelframeleft,font=("times new roman",12,"bold"),width=29)
        # enty_ref.grid(row=0,column=1)

#======================== post code ===========
        lbl_postcode=Label(levelframeleft,text="Pin code",font=("times new roman",14,"bold"),padx=2,pady=5)
        lbl_postcode.grid(row=4,column=0,sticky=W)

        enty_postcode = ttk.Entry(levelframeleft,textvariable=self.var_post,font=("times new roman",14,"bold"),width=19)
        enty_postcode.grid(row=4,column=1)


#====================== mobile number ==========

        lbl_custmobile=Label(levelframeleft,text="Customer mobile number",font=("times new roman",14,"bold"),padx=2,pady=5)
        lbl_custmobile.grid(row=5,column=0,sticky=W)
        enty_number = ttk.Entry(levelframeleft,textvariable=self.var_mobile,font=("times new roman",14,"bold"),width=19)
        enty_number.grid(row=5,column=1)

#====================== emails ===================


        lbl_customer_email=Label(levelframeleft,text="Customer email",font=("times new roman",14,"bold"),padx=2,pady=5)
        lbl_customer_email.grid(row=6,column=0,sticky=W)

        enty_email = ttk.Entry(levelframeleft,textvariable=self.var_email,font=("times new roman",14,"bold"),width=19)
        enty_email.grid(row=6,column=1)

#======================= Nationality ==================


        lbl_cust_nation=Label(levelframeleft,text="Customer nationality",font=("times new roman",14,"bold"),padx=2,pady=5)
        lbl_cust_nation.grid(row=7,column=0,sticky=W)

        combo_nation=ttk.Combobox(levelframeleft,textvariable=self.var_nationality,font=("times new roman",14,"bold"),width=17,state="readonly")
        combo_nation["value"]=("India","Pakistan","US","UK","japan","Other")
        combo_nation.current(0)
        combo_nation.grid(row=7,column=1)
        # enty_ref = ttk.Entry(levelframeleft,font=("times new roman",12,"bold"),width=29)
        # enty_ref.grid(row=0,column=1)

#========================= id proof ====================
        lbl_customer_id=Label(levelframeleft,text="Id proof type",font=("times new roman",14,"bold"),padx=2,pady=5)
        lbl_customer_id.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(levelframeleft,textvariable=self.var_id_proof,font=("times new roman",14,"bold"),width=17,state="readonly")
        combo_id["value"]=("AAdhar card","Driving licence","Other")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        # enty_ref = ttk.Entry(levelframeleft,font=("times new roman",12,"bold"),width=29)
        # enty_ref.grid(row=8,column=1)

#========================= id number ==================

        lbl_id_num=Label(levelframeleft,text="Customer id number",font=("times new roman",14,"bold"),padx=2,pady=5)
        lbl_id_num.grid(row=9,column=0,sticky=W)

        enty_idnum = ttk.Entry(levelframeleft,textvariable=self.var_id_number,font=("times new roman",14,"bold"),width=19)
        enty_idnum.grid(row=9,column=1)

#=========================address ====================

        lbl_address=Label(levelframeleft,text="Address",font=("times new roman",14,"bold"),padx=2,pady=5)
        lbl_address.grid(row=10,column=0,sticky=W)

        enty_address = ttk.Entry(levelframeleft,textvariable=self.var_address,font=("times new roman",14,"bold"),width=19)
        enty_address.grid(row=10,column=1)


#==================================button frame ==============================


        btn_frame=Frame(levelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btn_add=Button(btn_frame,text="add",command=self.add_data,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btn_add.grid(row=0,column=0,padx=1,pady=1)


        btn_update=Button(btn_frame,text="update",command=self.update,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btn_update.grid(row=0,column=1,padx=1,pady=1)



        btn_Delete=Button(btn_frame,text="Delete",command=self.adelete,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btn_Delete.grid(row=0,column=2,padx=1,pady=1)



        btn_Reset=Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btn_Reset.grid(row=0,column=3,padx=1,pady=1)

# ======================= table frame ================================
        tableframe=LabelFrame(self.root,bd=4,relief=RIDGE,text="View details and search ",font=("times new roman",20,"bold"),padx=2)
        tableframe.place(x=435,y=50,width=860,height=490)

        self.search_var=StringVar()

        lbl_search1=Label(tableframe,text="Search by: ",font=("times new roman",14,"bold"),bg="red",fg="white")
        lbl_search1.grid(row=0,column=0,sticky=W)

        self.text_search=StringVar()


        combo_search=ttk.Combobox(tableframe,textvariable=self.search_var,font=("times new roman",16,"bold"),width=20,state="readonly")
        combo_search["value"]=("mobile","ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=4)


        enty_idnum = ttk.Entry(tableframe,textvariable=self.text_search,font=("times new roman",16,"bold"),width=22)
        enty_idnum.grid(row=0,column=2,padx=1)

        btn_search=Button(tableframe,text="Search",command=self.btsearch,font=("times new roman",12,"bold"),bg="black",fg="gold",width=12)
        btn_search.grid(row=0,column=3,padx=1,pady=1)

        btn_Showall=Button(tableframe,text="Show All",command=self.fetchdata,font=("times new roman",12,"bold"),bg="black",fg="gold",width=12)
        btn_Showall.grid(row=0,column=4,padx=1,pady=1)




        #=============================== show data table =======================
        
        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        # scroll_x = ttk.Entry(details_table,orient=HORIZONTAL)
        # scroll_Y = ttk.Entry(details_table,orient=VERTICAL)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)




        self.cust_details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)
        
        # scroll_x.pack(side=BOTTOM,fill=X)
        # scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.pack(side=BOTTOM, fill='x')
        scroll_y.pack(side=RIGHT, fill='y')


        scroll_x.config(command=self.cust_details_Table.xview)
        scroll_y.config(command=self.cust_details_Table.yview)

        self.cust_details_Table.heading("ref",text="Refer No")
        self.cust_details_Table.heading("name",text="Name")
        self.cust_details_Table.heading("mother",text="Mother")
        self.cust_details_Table.heading("gender",text="Gender")
        self.cust_details_Table.heading("post",text="Post")
        self.cust_details_Table.heading("mobile",text="Mobile")
        self.cust_details_Table.heading("email",text="Email")
        self.cust_details_Table.heading("nationality",text="Nationality")
        self.cust_details_Table.heading("idproof",text="Id proof")
        self.cust_details_Table.heading("idnumber",text="Id number")
        self.cust_details_Table.heading("address",text="Address")
        
        self.cust_details_Table["show"]="headings"
                
        self.cust_details_Table.column("ref", width=100)
        self.cust_details_Table.column("name", width=100)
        self.cust_details_Table.column("mother", width=100)
        self.cust_details_Table.column("gender", width=100)
        self.cust_details_Table.column("post", width=100)
        self.cust_details_Table.column("mobile", width=100)
        self.cust_details_Table.column("email", width=100)
        self.cust_details_Table.column("nationality", width=100)
        self.cust_details_Table.column("idproof", width=100)
        self.cust_details_Table.column("idnumber", width=100)
        self.cust_details_Table.column("address", width=100)



        self.cust_details_Table.pack(fill=BOTH,expand=1)
        self.cust_details_Table.bind("<ButtonRelease>",self.get_cursor)
        self.fetchdata()


    def datebaseConnection(self):
        try:
            self.conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
            self.my_cursor = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error","Database Connection Error : \n"+str(e),parent=self.root)


        
    def add_data(self):
        if self.var_mobile.get()=="" or  self.var_mother.get()=="":
            messagebox.showerror("Error","All field are required")
        else:
            try:
                conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_ref.get(),
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),

                                                                ))
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("suceess","customer has been added",parent=self.root)
                
            
            except Exception as e:
                messagebox.showerror("Error","Database Connection Error : \n"+str(e),parent=self.root)
            #     conn = mysql.connector.connect(host='localhost',database='hotel_mgmt',user='root',password='')
            

    def fetchdata(self):

        conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer ")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_Table.delete(*self.cust_details_Table.get_children())
            for i in rows:
                self.cust_details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    def get_cursor(self,event=""):
        cursor_row=self.cust_details_Table.focus()
        content=self.cust_details_Table.item(cursor_row)
        row=content["values"]
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])


    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","please enter your mobile number",parent=self.root)
        else:
            conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where ref=%s",(
                                
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get()
                              
            ))
            conn.commit()
            self.fetchdata()
            conn.close()
            messagebox.showinfo("Update","customer data has been updated",parent=self.root)



    def adelete(self):
        adelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root)
        if adelete>0:
            conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
            my_cursor = conn.cursor()
            query="delete from customer where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not adelete:
                return
        conn.commit()
        self.fetchdata()

        conn.close()

    def reset(self):
                self.var_ref.set("")
                self.var_cust_name.set(""),
                self.var_mother.set(""),
                # self.var_gender.set(""),
                self.var_post.set(""),
                self.var_mobile.set(""),
                self.var_email.set(""),
                # self.var_nationality.set(""),
                # self.var_id_proof.set(""),
                self.var_id_number.set(""),
                self.var_address.set("")

   

    def btsearch(self):
        conn = pymysql.connect(host='localhost',db='hotel_mgmt',user='root',password='')
        my_cursor = conn.cursor()  
        query = "SELECT * FROM customer WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.text_search.get()) + "%'"
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

                
                              

            

        
    
if __name__ == '__main__':
    root = Tk()
    obj = cust_wind(root)
    root.mainloop()
