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
import os
import csv
from tkinter import filedialog

mydata=[]

mydata.clear()
class Teacher_info:
    def __init__(self,teacher_id):
        self.new = Tk()
        self.new.geometry("400x250+0+0")

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="@root@123", database="new_schema")
            c = conn.cursor()
            c.execute("SELECT first_name, last_name, uni_name, age,Gender,section FROM teacher WHERE Teacher_ID=%s", (teacher_id,))
            self.result = c.fetchone()

            info_labels = [
                "Teacher name :- ", "University name :- ", "Age :- ", "Teacher Id :- ", "Gender :- ","Section :- "]

            frame_1=LabelFrame(self.new,text="Teacher info",font=("Helvetica", 12, "bold"))
            frame_1.grid(row=0,column=0,ipadx=3,ipady=5,padx=3,pady=3,rowspan=6)

            Lable_q=Label(frame_1,text=info_labels[0],font=("Helvetica", 9, "bold"))
            Lable_q.grid(row=1,column=0,padx=1,pady=2,sticky="w")
            label = Label(frame_1, text=str(self.result[0])+" "+str(self.result[1]))
            label.grid(row=1,column=1,padx=1,pady=1)

            Lable_w=Label(frame_1,text=info_labels[1],font=("Helvetica", 9, "bold"))
            Lable_w.grid(row=2,column=0,padx=1,pady=2,sticky="w")
            label_2 = Label(frame_1, text=str(self.result[2]))
            label_2.grid(row=2,column=1,padx=1,pady=1)

            Lable_e=Label(frame_1,text=info_labels[2],font=("Helvetica", 9, "bold"))
            Lable_e.grid(row=3,column=0,padx=1,pady=2,sticky="w")
            label_3 = Label(frame_1, text=str(self.result[3]))
            label_3.grid(row=3,column=1,padx=1,pady=1)

            Lable_r=Label(frame_1,text=info_labels[3],font=("Helvetica", 9, "bold"))
            Lable_r.grid(row=4,column=0,padx=1,pady=2,sticky="w")
            label_4 = Label(frame_1, text=teacher_id)
            label_4.grid(row=4,column=1,padx=1,pady=1)

            Lable_t=Label(frame_1,text=info_labels[4],font=("Helvetica", 9, "bold"))
            Lable_t.grid(row=5,column=0,padx=1,pady=2,sticky="w")
            label_5 = Label(frame_1, text=str(self.result[4]))
            label_5.grid(row=5,column=1,padx=1,pady=1)

            frame_2=LabelFrame(self.new)
            frame_2.grid(row=0,column=1,ipadx=30,ipady=5,padx=3,pady=3,rowspan=6,sticky="s")

            Lable_s=Label(frame_2,text=info_labels[5],font=("Helvetica", 9, "bold"))
            Lable_s.grid(row=0,column=0,padx=1,pady=2,sticky="nw")
            label_6 = Label(frame_2, text=str(self.result[5]))
            label_6.grid(row=0,column=1,padx=1,pady=1,sticky="n")

            
            button = Button(self.new, text="Take Attendence",command=self.face_data)
            button.grid(row=6,column=0,sticky="we",padx=2,pady=3)

            button_1 = Button(self.new, text="Logout",command=self.logout)
            button_1.grid(row=7,column=1,sticky="ew",padx=2,pady=3)
            button = Button(self.new, text="See attendence",command=self.table)
            button.grid(row=6,column=1,sticky="we",padx=2,pady=3)

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")
        finally:
            conn.close()

    def open_im():
        os.startfile("data")
    
    def logout(self):
        self.new.destroy()


    
    def  face_data(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@root@123", database="new_schema")
                    c = conn.cursor()

                    c.execute("SELECT first_name FROM student WHERE Student_ID = %s", (id,))
                    name_result = c.fetchone()
                    n_ = name_result[0] if name_result else "Unknown"

                    c.execute("SELECT Roll_no FROM student WHERE Student_ID = %s", (id,))
                    roll_result = c.fetchone()
                    r = roll_result[0] if roll_result else "N/A"

                    c.execute("SELECT Student_ID FROM student WHERE Student_ID = %s", (id,))
                    id_result = c.fetchone()
                    i = id_result[0] if id_result else "N/A"

                    conn.close()

                    if isinstance(n_, str):
                        n_ = [n_] 

                    if isinstance(n_, list):
                        n_ = '+'.join(map(str, n_))

                    if confidence > 75:
                        cv2.putText(img, f"Name : {n_}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendence(i, r, n_)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    coord = [x, y, w, h]

                except mysql.connector.Error as e:
                    print(f"Database error: {e}")

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Attendence",img)
            
            if cv2.waitKey(1)==13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()
    
    def mark_attendence(self,i,r,n):
        with open("attt.csv","r+",newline='\n') as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list)) :
                now = datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{dtString},{d1},Present")


    def table(self):
        self.new1=Tk()
        self.new1.geometry("400x400")
        frame_3=LabelFrame(self.new1,text="Attendence",font=("Helvetica", 12, "bold"))
        frame_3.place(x=5,y=5,height=150,width=370)

        scroll_=Scrollbar(frame_3,orient=HORIZONTAL)
        scroll_1=Scrollbar(frame_3,orient=VERTICAL)
        

        self.std_table=ttk.Treeview(frame_3,columns=("Student ID","Roll.no","Name","date","time"),xscrollcommand=scroll_.set,yscrollcommand=scroll_1.set)
        scroll_.pack(side=BOTTOM,fill=X)
        scroll_1.pack(side=RIGHT,fill=Y)
        scroll_.config(command=self.std_table.xview)
        scroll_1.config(command=self.std_table.yview)
        self.std_table.heading("Student ID",text="Student ID")
        self.std_table.heading("Roll.no",text="Roll.no")
        self.std_table.heading("Name",text="Name")
        self.std_table.heading("date",text="Date")
        self.std_table.heading("time",text="Time")
        self.std_table["show"]="headings"
        self.std_table.column("Student ID",width=50)
        self.std_table.column("Roll.no",width=50)
        self.std_table.column("Name",width=50)
        self.std_table.column("date",width=50)
        self.std_table.column("time",width=50)
        self.std_table.pack(fill=BOTH,expand=1)
        button=Button(self.new1,text="Import Attendence",command=self.importCcv)
        button.place(x=5,y=155)
        button_1=Button(self.new1,text="Export Attendence",command=self.exportCsv)
        button_1.place(x=120,y=155)
        self.new1.mainloop()

    def fetchData(self,rows):
        self.std_table.delete(*self.std_table.get_children())
        for i in rows:
             self.std_table.insert("",END,value=i)

    def importCcv(self):
         global mydata
         fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("All File","*.*",)),parent=self.new1)
         with open(fin) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.new1)
                return False
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("All File","*.*",)),parent=self.new)
            with open(fin,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Expored","Your data exported to "+os.path.basename(fin)+"successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}")
