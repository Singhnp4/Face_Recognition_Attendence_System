from distutils.util import execute
from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from tkinter import*
from tkinter import ttk
from turtle import right
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import CascadeClassifier
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1260x670+0+0")
        self.root.title("face Recognition System")

        #variables
        self.var_course=StringVar()
        self.var_email=StringVar()
        self.var_session=StringVar()
        self.var_semester=StringVar()
        self.var_student_id=StringVar()
        self.var_reg_no=StringVar()
        self.var_student_name=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone_no=StringVar()
        self.var_address=StringVar()
        self.var_radio1=StringVar()


        # Background image
        imgb=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\s1.jpg")
        imgb=imgb.resize((1500,700),Image.ANTIALIAS)
        self.photoimgb=ImageTk.PhotoImage(imgb)

        bg_img=Label(self.root,image=self.photoimgb)
        bg_img.place(x=0,y=0,width=1500,height=700)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=15,y=20,width=1230,height=610)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",21,"bold"))
        left_frame.place(x=10,y=10,width=560,height=570)


        cou_label=Label(left_frame,text="Course",font=("times new roman",12,"bold"))
        cou_label.grid(row=0,column=0,padx=10)

        cou_combo=ttk.Combobox(left_frame,textvariable=self.var_course,width=17,font=("times new roman",12,"bold"),state="readonly")
        cou_combo["values"]=("Select Course","B.Tech","M.Tech","MBA")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        email_label=Label(left_frame,text="Email ID",font=("times new roman",12,"bold"))
        email_label.grid(row=0,column=2,padx=10)

        email_entry=ttk.Entry(left_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=0,column=3,pady=10,sticky=W)

        ses_label=Label(left_frame,text="Session",font=("times new roman",12,"bold"))
        ses_label.grid(row=1,column=0,padx=10)

        ses_entry=ttk.Entry(left_frame,textvariable=self.var_session,width=20,font=("times new roman",12,"bold"))
        ses_entry.grid(row=1,column=1,pady=10,sticky=W)

        sem_label=Label(left_frame,text="Semester",font=("times new roman",12,"bold"))
        sem_label.grid(row=1,column=2,padx=10)

        sem_combo=ttk.Combobox(left_frame,textvariable=self.var_semester,width=17,font=("times new roman",12,"bold"),state="readonly")
        sem_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        st_ID_label=Label(left_frame,text="Student ID",font=("times new roman",12,"bold"))
        st_ID_label.grid(row=2,column=0,padx=10)

        st_ID_entry=ttk.Entry(left_frame,textvariable=self.var_student_id,width=20,font=("times new roman",12,"bold"))
        st_ID_entry.grid(row=2,column=1,pady=10,sticky=W)

        reg_label=Label(left_frame,text="Reg No",font=("times new roman",12,"bold"))
        reg_label.grid(row=2,column=2,padx=10)

        reg_entry=ttk.Entry(left_frame,textvariable=self.var_reg_no,width=20,font=("times new roman",12,"bold"))
        reg_entry.grid(row=2,column=3,pady=10,sticky=W)

        st_label=Label(left_frame,text="Student Name",font=("times new roman",12,"bold"))
        st_label.grid(row=3,column=0,padx=10)

        st_entry=ttk.Entry(left_frame,textvariable=self.var_student_name,width=20,font=("times new roman",12,"bold"))
        st_entry.grid(row=3,column=1,pady=10,sticky=W)

        rol_label=Label(left_frame,text="Roll No",font=("times new roman",12,"bold"))
        rol_label.grid(row=3,column=2,padx=10)

        rol_entry=ttk.Entry(left_frame,textvariable=self.var_roll_no,width=20,font=("times new roman",12,"bold"))
        rol_entry.grid(row=3,column=3,pady=10,sticky=W)

        gen_label=Label(left_frame,text="Gender",font=("times new roman",12,"bold"))
        gen_label.grid(row=4,column=0,padx=10)

        gen_entry=ttk.Entry(left_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        gen_entry.grid(row=4,column=1,pady=10,sticky=W)

        dob_label=Label(left_frame,text="D.O.B",font=("times new roman",12,"bold"))
        dob_label.grid(row=4,column=2,padx=10)

        dob_entry=ttk.Entry(left_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=4,column=3,pady=10,sticky=W)

        phon_label=Label(left_frame,text="Phone No",font=("times new roman",12,"bold"))
        phon_label.grid(row=5,column=0,padx=10)

        phon_entry=ttk.Entry(left_frame,textvariable=self.var_phone_no,width=20,font=("times new roman",12,"bold"))
        phon_entry.grid(row=5,column=1,pady=10,sticky=W)

        add_label=Label(left_frame,text="Address",font=("times new roman",12,"bold"))
        add_label.grid(row=5,column=2,padx=10)

        add_entry=ttk.Entry(left_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        add_entry.grid(row=5,column=3,pady=10,sticky=W)

        imga=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\ad.jpg")
        imga=imga.resize((550,250),Image.ANTIALIAS)
        self.photoimga=ImageTk.PhotoImage(imga)

        a_img=Label(left_frame,image=self.photoimga)
        a_img.place(x=5,y=300,width=540,height=400)


        #Radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(left_frame,variable=self.var_radio1,text="take photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0,padx=5)

        radiobtn2=ttk.Radiobutton(left_frame,variable=self.var_radio1,text="no photo sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #buttons Frame
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="gray")
        btn_frame.place(x=5,y=300,width=540,height=85)

        imgf=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\s1.jpg")
        imgf=imgf.resize((650,300),Image.ANTIALIAS)
        self.photoimgf=ImageTk.PhotoImage(imgf)

        fr_img=Label(btn_frame,image=self.photoimgf)
        fr_img.place(x=0,y=0,width=540,height=85)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",12,"bold"),bg="blue",fg="white",bd=4)
        save_btn.place(x=20,y=10,width=150,height=30)

        upd_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",12,"bold"),bg="blue",fg="white",bd=4)
        upd_btn.place(x=195,y=10,width=150,height=30)

        del_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),bg="blue",fg="white",bd=4)
        del_btn.place(x=365,y=10,width=150,height=30)

        rest_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white",bd=4)
        rest_btn.place(x=275,y=45,width=240,height=30)

        tk_phto_btn=Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,font=("times new roman",12,"bold"),bg="blue",fg="white",bd=4)
        tk_phto_btn.place(x=20,y=45,width=240,height=30)


         #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student List",font=("times new roman",21,"bold"))
        right_frame.place(x=580,y=10,width=630,height=570)


        #table
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=10,width=628,height=500)

        scrl_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrl_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("course","email","session","semester","student_id","student_name","roll_no","reg_no","gender","dob","phone_no","address","photosample"),xscrollcommand=scrl_x.set,yscrollcommand=scrl_y.set)

        scrl_x.pack(side=BOTTOM,fill=X)
        scrl_y.pack(side=RIGHT,fill=Y)
        scrl_x.config(command=self.student_table.xview)
        scrl_y.config(command=self.student_table.yview)

        self.student_table.heading("course",text="Course")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("session",text="Session")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("student_id",text="Student_id")
        self.student_table.heading("student_name",text="Student_name")
        self.student_table.heading("roll_no",text="Roll_No")
        self.student_table.heading("reg_no",text="Reg_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("phone_no",text="Phone_No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photosample",text="photosample")
        self.student_table["show"]="headings"

        #self.student_table.column("course",width=50)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #function declearition
    def add_data(self):
        if self.var_course.get()=="Select Course" or self.var_student_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All field Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="neeraj@123",database="face")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,(

                                                                                                        self.var_course.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_session.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_student_id.get(),
                                                                                                        self.var_student_name.get(),
                                                                                                        self.var_roll_no.get(),
                                                                                                        self.var_reg_no.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_phone_no.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_radio1.get(),

                                                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student detail has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)



    #********Fath data*******
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="neeraj@123",database="face")
        my_cursor=conn.cursor()
        my_cursor.execute("select* from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #***GET CURSOR
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_course.set(data[0]),
        self.var_email.set(data[1]),
        self.var_session.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_student_id.set(data[4]),
        self.var_student_name.set(data[5]),
        self.var_roll_no.set(data[6]),
        self.var_reg_no.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_phone_no.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])

    #update function
    def update_data(self):
        if self.var_course.get()=="Select Course" or self.var_student_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All field Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","do you want to update the details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="neeraj@123",database="face")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set course=%s,email=%s,session=%s,semester=%s,student_name=%s,roll_no=%s,reg_no=%s,gender=%s,dob=%s,phone_no=%s,address=%s,photosample=%s where student_ID=%s",(
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_session.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_student_name.get(),
                                                                                                                                                                                    self.var_roll_no.get(),
                                                                                                                                                                                    self.var_reg_no.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_phone_no.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_student_id.get()
                                                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_student_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete the student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="neeraj@123",database="face")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #reset
    def reset_data(self):
        self.var_course.set("select course")
        self.var_email.set("")
        self.var_session.set("")
        self.var_semester.set("select semester")
        self.var_student_id.set("")
        self.var_reg_no.set("")
        self.var_student_name.set("")
        self.var_roll_no.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_phone_no.set("")
        self.var_address.set("")
        self.var_radio1.set("")
    
    #generate data set
    def generate_dataset(self):
        if self.var_course.get()=="Select Course" or self.var_student_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All field Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","do you want to update the details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="neeraj@123",database="face")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select* from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                    my_cursor.execute("update student set course=%s,email=%s,session=%s,semester=%s,student_name=%s,roll_no=%s,reg_no=%s,gender=%s,dob=%s,phone_no=%s,address=%s,photosample=%s where student_ID=%s",(
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_session.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_student_name.get(),
                                                                                                                                                                                    self.var_roll_no.get(),
                                                                                                                                                                                    self.var_reg_no.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_phone_no.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_student_id.get()
                                                                                                                                                                                ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()  

                    #load predefined data on face frontals from opencv

                    face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  
                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3
                        #Minimum Neighbour=5

                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped  
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret, my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                            cv2.imshow("Cropped face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    

    #def back(self):
     #   self.root.window.history.back()



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()