from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import numpy as np

from Tech_Singin import tech
from Std_Singin import user
from Student_Login import Student_info
from Teacher_Login import Teacher_info


class login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("470x250+0+0")
        self.root.title("Log in page")
        self.root.resizable(0,0)
        frame_1 = Frame(self.root,highlightbackground="black",highlightthickness=1)
        frame_1.grid(row=0,column=0,padx=5,pady=10,columnspan=4)
        lable_1 = Label(frame_1,text ="ATTENDENCE SYSTEM")
        lable_1.pack(padx=130)

        frame_2 =Frame(self.root,highlightbackground="black",highlightthickness=1)
        frame_2.grid(row=1,column=0,padx=1,pady=2,columnspan=2)
        lable_2= Label(frame_2,text = "For Student")
        lable_2.grid(row=1,padx=58,pady=3,columnspan=2)
        self.stid=IntVar()
        lable_3=Label(frame_2,text="Student ID - ")
        lable_3.grid(row=2,column=0,pady=2)

        entry_1 = Entry(frame_2,textvariable=self.stid)
        entry_1.grid(row=2,column=1,pady=2,padx=1)
        self.pp=StringVar()
        lable_4=Label(frame_2,text="Passward - ")
        lable_4.grid(row=3,column=0,pady=2)

        entry_1 = Entry(frame_2,textvariable=self.pp)
        entry_1.grid(row=3,column=1,pady=2)

        button_1 = Button(frame_2,text="Log in",command=self.log_in)
        button_1.grid(row=4,column=1,pady=2,padx=2)

        lable_5=Label(frame_2,text="you can register - ")
        lable_5.grid(row=5,pady=10)

        button_2 = Button(frame_2,text="Sign up",command=self.sign)
        button_2.grid(row=5,column=1,pady=10)

        frame_3 =Frame(self.root,highlightbackground="black",highlightthickness=1)
        frame_3.grid(row=1,column=2,padx=1,pady=2,columnspan=2)
        lable_6= Label(frame_3,text = "For Teachers")
        lable_6.grid(row=1,columnspan=2,padx=58,pady=3)
        self.tid=IntVar()
        lable_7=Label(frame_3,text="Teacher ID - ")
        lable_7.grid(row=2,column=0,pady=2)

        entry_2 = Entry(frame_3,textvariable=self.tid)
        entry_2.grid(row=2,column=1,pady=2,padx=1)
        self.tpp=StringVar()
        lable_8=Label(frame_3,text="Passward - ")
        lable_8.grid(row=3,column=0,pady=2)

        entry_3 = Entry(frame_3,textvariable=self.tpp)
        entry_3.grid(row=3,column=1,pady=2)

        button_3 = Button(frame_3,text="Log in",command=self.tlog_in)
        button_3.grid(row=4,column=1,pady=2,padx=2)

        lable_9=Label(frame_3,text="you can register - ")
        lable_9.grid(row=5,column=0,pady=10)

        button_4 = Button(frame_3,text="Sign up",command=self.tsign)
        button_4.grid(row=5,column=1,pady=10)

    def sign(self):
        self.reset_data()
        self.new_window=Toplevel(self.root)
        self.submitt=user(self.new_window)
    
    def tsign(self):
        self.reset_data()
        self.new_window=Toplevel(self.root)
        self.submitt=tech(self.new_window)

    def open_im():
        os.startfile("data")

    def log_in(self):
        if self.pp.get()=="" or self.stid.get()=="":
            messagebox.showerror("Error","Student Id or passward not entered")
        else:
            try :
                conn = mysql.connector.connect(host="localhost", username="root", password="@root@123", database="new_schema")
                c = conn.cursor()
                c.execute("SELECT passward FROM student WHERE Student_ID=%s", (self.stid.get(),))
                result = c.fetchone()
                if result and result[0] == self.pp.get():
                    self.sobj=Student_info(self.stid.get())
                    
                else:
                    self.reset_data()
                    messagebox.showerror("Error", "Invalid Student Id or password")
                    

            except Exception as es:
                self.reset_data()
                messagebox.showerror("Error", f"Due To: {str(es)}")
            finally:
                self.reset_data()
                conn.close()


    

    def tlog_in(self):
        teacher_id = self.tid.get()
        password = self.tpp.get()

        if teacher_id == "" or password == "":
            messagebox.showerror("Error", "Teacher Id or password not entered")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="@root@123", database="new_schema")
                c = conn.cursor()
                c.execute("SELECT passward FROM teacher WHERE Teacher_ID=%s", (teacher_id,))
                my_result = c.fetchone()

                if my_result and my_result[0] == password:
                    self.tobj=Teacher_info(teacher_id)
                else:
                    self.reset_data()
                    messagebox.showerror("Error", "Invalid Teacher Id or password")

            except mysql.connector.Error as e:
                self.reset_data()
                messagebox.showerror("Error", f"Due to: {str(e)}")
            finally:
                self.reset_data()
                conn.close()

    def reset_data(self):
        self.stid.set("")
        self.pp.set("")
        self.tid.set("")
        self.tpp.set("")



if __name__=="__main__":
    root=Tk()
    obj=login(root)
    root.mainloop()