import tkinter as tk
from tkinter import ttk
from tkinter import*
import mysql.connector
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata=[]
class Student_info:
    def __init__(self,i):
        self.new= Tk()
        self.new.geometry("210x220+0+0")
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="@root@123", database="new_schema")
            c = conn.cursor()
            c.execute("SELECT first_name, last_name, uni_name, age, section, Roll_no, passward, photosample FROM student WHERE Student_ID=%s", (i,))
            result = c.fetchone()
            info_labels = [
            "Student name :- ", "University :- ", "Age :- ", "Section :- ", "Roll No :- ", "Student ID :- "
            ]
            
            frame_1=LabelFrame(self.new,text="Student info",font=("Helvetica", 12, "bold"))
            frame_1.grid(row=0,column=0,ipadx=3,ipady=5,padx=3,pady=3,rowspan=6)

            Lable_q=Label(frame_1,text=info_labels[0],font=("Helvetica", 9, "bold"))
            Lable_q.grid(row=1,column=0,padx=1,pady=2,sticky="w")
            label = Label(frame_1, text=str(result[0])+" "+str(result[1]))
            label.grid(row=1,column=1,padx=1,pady=1)

            Lable_w=Label(frame_1,text=info_labels[1],font=("Helvetica", 9, "bold"))
            Lable_w.grid(row=2,column=0,padx=1,pady=2,sticky="w")
            label_2 = Label(frame_1, text=str(result[2]))
            label_2.grid(row=2,column=1,padx=1,pady=1)

            Lable_e=Label(frame_1,text=info_labels[2],font=("Helvetica", 9, "bold"))
            Lable_e.grid(row=3,column=0,padx=1,pady=2,sticky="w")
            label_3 = Label(frame_1, text=str(result[3]))
            label_3.grid(row=3,column=1,padx=1,pady=1)

            Lable_r=Label(frame_1,text=info_labels[3],font=("Helvetica", 9, "bold"))
            Lable_r.grid(row=4,column=0,padx=1,pady=2,sticky="w")
            label_4 = Label(frame_1, text=str(result[4]))
            label_4.grid(row=4,column=1,padx=1,pady=1)

            Lable_t=Label(frame_1,text=info_labels[4],font=("Helvetica", 9, "bold"))
            Lable_t.grid(row=5,column=0,padx=1,pady=2,sticky="w")
            label_5 = Label(frame_1, text=str(result[5]))
            label_5.grid(row=5,column=1,padx=1,pady=1)

            Lable_y=Label(frame_1,text=info_labels[5],font=("Helvetica", 9, "bold"))
            Lable_y.grid(row=6,column=0,padx=1,pady=2,sticky="w")
            label_6 = Label(frame_1, text=i)
            label_6.grid(row=6,column=1,padx=1,pady=1)


            button_1 = Button(self.new, text="Logout",command=self.logout)
            button_1.grid(row=7,column=0,sticky="ew",padx=2,pady=3)



        except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Database Error: {str(e)}")
        finally:
                conn.close()
        self.new,mainloop()
        
        
    
            
                


    def logout(self):
        self.new.destroy()



        



