from tkinter import *
from PIL import *
from PIL import Image,ImageTk
from customer import cust_wind
from room import roombooking
from details import detaillist

class hotelmanagementsytem:
    def __init__(self,root,username, user_type):
        self.root=root
        self.root.title("hotel management system - User: {}".format(username))
        self.root.geometry("1550x800+0+0")
      
        img1 = Image.open("C:/Users/rahul/OneDrive/Desktop/try/New folder/hotel.jpg")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        # img1=img1.resize((1550,140),Image.LANCZOS)

        # img1 = Image.open("C:/Users/rahul/OneDrive/Desktop/try/New folder/hotel.jpg")
        # img1 = img1.resize((1550, 140), Image.ANTIALIAS)

        

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)



        #=========================== Title===============================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM ",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        # =========================== main frame ==========================
        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        # ============================ manu ================================
        lbl_manu=Label(self.root,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_manu.place(x=5,y=190,width=230)

        # ============================= btn frame ==========================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=36,width=230,height=210)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombook,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.detailroom,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)

        # report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        # report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)



    # ============================== right side image ===============================================

        img2 = Image.open("C:/Users/rahul/OneDrive/Desktop/try/New folder/room.jpg")
        img2 = img2.resize((1305, 600), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg2.place(x=232,y=190,width=1305,height=600)

    # =============================== down image ==========================================


        img3 = Image.open("C:/Users/rahul/OneDrive/Desktop/try/New folder/side1.jpeg")
        img3 = img2.resize((230,210), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg3.place(x=0,y=440,width=230,height=210)


        img4 = Image.open("C:/Users/rahul/OneDrive/Desktop/try/New folder/side2.jpeg")
        img4 = img4.resize((230, 135), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg4.place(x=0,y=652,width=230,height=135)



    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_wind(self.new_window)

    def roombook(self):
        self.new_window=Toplevel(self.root)
        self.app=roombooking(self.new_window)
    

    def detailroom(self):
        self.new_window=Toplevel(self.root)
        self.app=detaillist(self.new_window)


    def logout(self):
        self.root.destroy()


    





if __name__ == '__main__':
    root = Tk()
    obj = hotelmanagementsytem(root, "DefaultUser", "DefaultType")
    root.mainloop()