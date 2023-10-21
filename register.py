from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('Register')
        self.root.geometry("1200x620+20+10")

        #**variables**
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_passw=StringVar()
        self.var_confpassw=StringVar()





        imgb=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\s1.jpg")
        imgb=imgb.resize((1500,900),Image.ANTIALIAS)
        self.photoimgb=ImageTk.PhotoImage(imgb)

        bg_img=Label(self.root,image=self.photoimgb)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)

        imgr=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\register.jpg")
        imgr=imgr.resize((700,700),Image.ANTIALIAS)
        self.photoimgr=ImageTk.PhotoImage(imgr)

        r_img=Label(bg_img,image=self.photoimgr)
        r_img.place(x=10,y=15,width=400,height=580)

        frame=Frame(bg_img,bg="white")
        frame.place(x=410,y=15,width=770,height=580)

        #lable
        register_lbl=Label(frame,text="REGISTER HERE.....",font=("times new roman",20,"bold"),bg="white",fg="blue")
        register_lbl.place(x=20,y=20)

        #Lable and entry
        fname=Label(frame,text="First Name",font=("times new roman",20,"bold"))
        fname.place(x=50,y=100)
        self.fentry=ttk.Entry(frame,width=20,textvariable=self.var_fname,font=("times new roman",12,"bold"))
        self.fentry.place(x=50,y=135,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",20,"bold"))
        lname.place(x=400,y=100)
        self.lentry=ttk.Entry(frame,width=20,textvariable=self.var_lname,font=("times new roman",12,"bold"))
        self.lentry.place(x=400,y=135,width=250)

        contno=Label(frame,text="Contact No",font=("times new roman",20,"bold"))
        contno.place(x=50,y=170)
        self.contnoentry=ttk.Entry(frame,width=20,textvariable=self.var_contact,font=("times new roman",12,"bold"))
        self.contnoentry.place(x=50,y=205,width=250)

        email=Label(frame,text="Email",font=("times new roman",20,"bold"))
        email.place(x=400,y=170)
        self.emailentry=ttk.Entry(frame,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        self.emailentry.place(x=400,y=205,width=250)

        squestion=Label(frame,text="Select Security Questions",font=("times new roman",20,"bold"))
        squestion.place(x=50,y=240)
        self.q_combo=ttk.Combobox(frame,width=20,textvariable=self.var_securityQ,font=("times new roman",12,"bold"),state="readonly")
        self.q_combo["values"]=("Select","Your Birth Place","Your favorite day","your favorite color")
        self.q_combo.current(0)
        self.q_combo.place(x=50,y=275,width=250)

        sanswer=Label(frame,text="Security Answer",font=("times new roman",20,"bold"))
        sanswer.place(x=400,y=240)
        self.aentry=ttk.Entry(frame,width=20,textvariable=self.var_securityA,font=("times new roman",12,"bold"))
        self.aentry.place(x=400,y=275,width=250)

        password=Label(frame,text="Password",font=("times new roman",20,"bold"))
        password.place(x=50,y=320)
        self.entry=ttk.Entry(frame,width=20,textvariable=self.var_passw,font=("times new roman",12,"bold"))
        self.entry.place(x=50,y=355,width=250)

        cpassword=Label(frame,text="Confirm Password",font=("times new roman",20,"bold"))
        cpassword.place(x=400,y=320)
        self.centry=ttk.Entry(frame,width=20,textvariable=self.var_confpassw,font=("times new roman",12,"bold"))
        self.centry.place(x=400,y=355,width=250)

        #check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & condition",font=("times new roman",12,"bold"),bg="White",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=390)

        #************Buttons****
        img=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\register1.jpg")
        img=img.resize((200,60),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        img=Button(frame,image=self.photoimg,command=self.register_data,bg="white",borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        img.place(x=70,y=440,width=202)
        
        img1=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\login.jpg")
        img1=img1.resize((200,60),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        img1=Button(frame,image=self.photoimg1,command=self.back_login,bg="white",borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        img1.place(x=400,y=440,width=202)

    #*******Function Declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All field are Required")
        elif self.var_passw.get()!=self.var_confpassw.get():
            messagebox.showerror("Error","Password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our tearms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="neeraj@123",database="face")
            my_cursor=conn.cursor()
            query=("select* from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_passw.get(),
                                                                                 ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully",parent=self.root)

    def back_login(self):
        self.root.destroy()


        
        





if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()