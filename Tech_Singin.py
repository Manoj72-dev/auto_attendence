from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class tech:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x350+0+0")
        self.root.title("data entry form")
        self.root.resizable(0,0)

        self.f_name=StringVar()
        self.l_name=StringVar()
        self.uni_name=StringVar()
        self.age=StringVar()
        self.passward=StringVar()
        self.id=StringVar()
        self.gender=StringVar()
        self.sec=StringVar()


        user_info_frame=LabelFrame(self.root,text="User info",font=("Helvetica", 12, "bold"))
        user_info_frame.grid(row=0,column=0,ipadx=3,ipady=5,padx=3,pady=3)

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

        #spin box
        age_label= Label(user_info_frame,text="Age")
        age_spinbox=Spinbox(user_info_frame,from_=25,to= 75,textvariable=self.age)
        age_label.grid(row=2,column=0)
        age_spinbox.grid(row=3,column=0)

        #passward 
        passward_lable = Label(user_info_frame,text="Passward ")
        passward_entry = Entry(user_info_frame,textvariable=self.passward)
        passward_lable.grid(row=4,column=0)
        passward_entry.grid(row=5,column=0,pady=5)

        #Id
        id_lable = Label(user_info_frame,text="Teacher Id")
        id_entry= Entry(user_info_frame,textvariable=self.id)
        id_lable.grid(row=4,column=1)
        id_entry.grid(row=5,column=1,pady=5)
        

        gender_label = Label(user_info_frame,text="Gender")
        gender_comboBox= ttk.Combobox(user_info_frame,values=["Male","female"],textvariable=self.gender)
        gender_label.grid(row= 2,column=2)
        gender_comboBox.grid(row=3,column=2)

        section_label= Label(user_info_frame,text="SECTION")
        section_combobox= ttk.Combobox(user_info_frame,values=["A","B"],textvariable=self.sec)
        section_label.grid(row=2,column=1)
        section_combobox.grid(row=3,column=1)

        #terms and condition
        terms_frame = LabelFrame(self.root,text="Terms & condtios* ")
        terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=5)
        self.check=IntVar()
        terms_check= Checkbutton(terms_frame,text="I accept all the univesity rules and norms.",offvalue=0,onvalue=1,variable=self.check)
        terms_check.grid(row=0,column=0)

        #padding all grids all at once.
        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10,pady=2)



        button = Button(self.root,text="Submit",padx=220,command=self.add_data)
        button.grid(pady=10)

        return 
    def add_data(self):
        if self.f_name.get()=="" or self.l_name.get()=="" or self.uni_name.get()=="" or self.passward.get()=="" or self.id.get()=="" or self.gender.get()=="" or self.check.get()==0:
            messagebox.showerror("Error","All Fileds are requied")
        elif self.sec.get() not in ("A","B"):
            messagebox.showerror("Error","Wrong Section")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="@root@123",database="new_schema")
                c = conn.cursor()
                c.execute("insert into teacher values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.f_name.get(),
                                                                                        self.l_name.get(),
                                                                                        self.uni_name.get(),
                                                                                        self.age.get(),
                                                                                        self.passward.get(),
                                                                                        self.gender.get(),
                                                                                        self.id.get(),
                                                                                        self.sec.get()   
                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registed")
                self.root.destroy()
            except Exception as es :
                messagebox.showerror("Error",f"Due To :{str(es)}")
    


if __name__=="__main__":
    root = Tk()
    obj=tech(root)
    root.mainloop()

    