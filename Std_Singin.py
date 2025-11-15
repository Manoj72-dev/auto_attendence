from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
from traing import tran
    
class user:
    def __init__(self,root):
        self.root=root
        self.root.title("data entry form")
        self.root.resizable(0,0)
        
#""""""""variables to store entry filed data"""""""""
        self.f_name=StringVar()
        self.l_name=StringVar()
        self.uni_name=StringVar()
        self.age=StringVar()
        self.sec=StringVar()
        self.roll_no=StringVar()
        self.passward=StringVar()
        self.id=StringVar()
        self.r=StringVar()
        self.r.set("hehe")
        self.check=IntVar()
#""""""""""""""""""""""""""""""""""""""""""""""""""""
        
        user_info_frame=LabelFrame(self.root,text="User info",font=("Helvetica", 12, "bold"))
        user_info_frame.grid(row=0,column=0,ipadx=3,ipady=5,padx=3,pady=3,rowspan=6)

        first_name_label = Label(user_info_frame,text="First name")
        first_name_label.grid(row=0,column=0)
        last_name_label= Label(user_info_frame,text="last name")
        last_name_label.grid(row=0,column=1)

        first_name_entry = Entry(user_info_frame,textvariable=self.f_name)
        last_name_entry = Entry(user_info_frame,textvariable=self.l_name)
        first_name_entry.grid(row=1,column=0)
        last_name_entry.grid(row=1,column=1)


        #title making
        university_label = Label(user_info_frame,text="University Name")
        university_comboBox= ttk.Combobox(user_info_frame,values=["Hill univerisity","deemed university","bhimtal","haldwani"],textvariable=self.uni_name)
        university_label.grid(row= 0,column=2)
        university_comboBox.grid(row=1,column=2)

        #second title
        section_label= Label(user_info_frame,text="SECTION")
        section_combobox= ttk.Combobox(user_info_frame,values=["A","B"],textvariable=self.sec)
        section_label.grid(row=2,column=1)
        section_combobox.grid(row=3,column=1)

        #spin box
        age_label= Label(user_info_frame,text="Age")
        age_spinbox=Spinbox(user_info_frame,from_=18,to= 28,textvariable=self.age)
        age_label.grid(row=2,column=0)
        age_spinbox.grid(row=3,column=0)

        #roll
        roll_label= Label(user_info_frame,text="Roll number")
        roll_spinbox=Spinbox(user_info_frame,from_=1,to=80,textvariable=self.roll_no)
        roll_label.grid(row=2,column=2)
        roll_spinbox.grid(row=3,column=2)

        #passward 
        passward_lable = Label(user_info_frame,text="Passward ")
        passward_entry = Entry(user_info_frame,textvariable=self.passward)
        passward_lable.grid(row=4,column=0)
        passward_entry.grid(row=5,column=0)

        #Id
        id_lable = Label(user_info_frame,text="Student Id")
        id_entry= Entry(user_info_frame,textvariable=self.id)
        id_lable.grid(row=4,column=1)
        id_entry.grid(row=5,column=1)
        
        #terms and condition
        terms_frame = LabelFrame(self.root,text="Terms & condtios* ")
        terms_frame.grid(row=8,column=0,sticky="news",padx=20,pady=20)

        terms_check= Checkbutton(terms_frame,text="I accept all the univesity rules and norms.",offvalue=0,onvalue=1,variable=self.check)
        terms_check.grid(row=0,column=0)

        #padding all grids all at once.
        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10,pady=2)

        #part two:
        course_frame = LabelFrame(self.root)
        course_frame.grid(row=7 ,column=0,sticky="news",padx=20,pady=20)

        sem_registration_label= Label(course_frame,text=" Add photo sample - ")
        Radiobutton(course_frame,text="yes",value="yes",variable=self.r).grid(row=1,column=0)
        Radiobutton(course_frame,text="no",value="no",variable=self.r).grid(row=1,column=1)
        sem_registration_label.grid(row=0,column=0)
    
        button = Button(self.root,text="Submit",padx=220,command=self.add_data)
        button.grid(pady=10)


    def add_data(self):

        if self.f_name.get()=="" or self.l_name.get()=="" or self.uni_name.get()=="" or self.sec.get()=="" or self.passward.get()=="" or self.id.get()=="" or self.r.get()=="hehe" or self.check.get()==0:
            messagebox.showerror("Error","All Fileds are requied")

        elif self.sec.get() not in ("A","B"):
            messagebox.showerror("Error","Wrong Section")
        else:
            if self.sec.get()=="A":
                try:
                    conn = mysql.connector.connect(host="localhost",username="root",password="@root@123",database="new_schema")
                    c = conn.cursor()
                    c.execute("insert into seca values(%s,%s,%s)",(
                                                                                        str(self.f_name.get())+" "+str(self.l_name.get()),
                                                                                        self.roll_no.get(),
                                                                                        self.id.get(),
                        ))
                    conn.commit()
                    conn.close()
                except Exception as es :
                    messagebox.showerror("Error",f"Due To :{str(es)}")
        
            
            if self.sec.get()=="B":
                try:
                    conn = mysql.connector.connect(host="localhost",username="root",password="@root@123",database="new_schema")
                    c = conn.cursor()
                    c.execute("insert into secb values(%s,%s,%s)",(
                                                                                        str(self.f_name.get())+" "+str(self.l_name.get()),
                                                                                        self.roll_no.get(),
                                                                                        self.id.get(),
                        ))
                    conn.commit()
                    conn.close()
                except Exception as es :
                    messagebox.showerror("Error",f"Due To :{str(es)}")
                

            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="@root@123",database="new_schema")
                c = conn.cursor()
                c.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.f_name.get(),
                                                                                        self.l_name.get(),
                                                                                        self.uni_name.get(),
                                                                                        self.age.get(),
                                                                                        self.sec.get(),
                                                                                        self.roll_no.get(),
                                                                                        self.passward.get(),
                                                                                        self.id.get(),
                                                                                        self.r.get()
                        ))
                conn.commit()
                conn.close()
                self.generate_dataset()
                self.root.destroy()
                messagebox.showinfo("Success","Registed")

            except Exception as es :
                conn = mysql.connector.connect(host="localhost",username="root",password="@root@123",database="new_schema")
                c = conn.cursor()
                queary="delete from seca where rollno=%s"
                c.execute(queary,(self.roll_no.get(),))
                conn.commit()
                conn.close()
                conn = mysql.connector.connect(host="localhost",username="root",password="@root@123",database="new_schema")
                c = conn.cursor()
                queary="delete from secb where rollno=%s"
                c.execute(queary,(self.roll_no.get(),))
                conn.commit()
                conn.close()
                messagebox.showerror("Error",f"Due To :{str(es)}")
    
                
                
            

    def reset_data(self):
        self.f_name.set("")
        self.l_name.set("")
        self.uni_name.set("")
        self.age.set("18")
        self.sec.set("")
        self.passward.set("")
        self.id.set("")
        self.r.set("hehe")

    def generate_dataset(self):
        if self.f_name.get()=="" or self.l_name.get()=="" or self.uni_name.get()=="" or self.sec.get()=="" or self.passward.get()=="" or self.id.get()=="" or self.r.get()=="hehe":
            messagebox.showerror("Error","All Fileds are requied")
        else:   
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,frame=cap.read()
                    if face_cropped(frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(self.id.get())+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                self.traing()
                messagebox.showinfo("Result","Generating data sets completed!!!!")
                
    def traing(self):
        self.submitt=tran()

if __name__=="__main__":
    root=Tk()
    obj=user(root)
    root.mainloop()
