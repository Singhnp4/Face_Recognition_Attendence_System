from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_recognition_system
from register import Register

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("login")
        self.root.geometry("1200x690+20+10")

        self.var_username=StringVar()
        self.var_password=StringVar()
        self.var_secQ=StringVar()
        self.var_secA=StringVar()
        self.var_newpass=StringVar()


        # Background image
        imgb=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\s1.jpg")
        imgb=imgb.resize((1500,900),Image.ANTIALIAS)
        self.photoimgb=ImageTk.PhotoImage(imgb)

        bg_img=Label(self.root,image=self.photoimgb)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(bg_img,bg="black")
        frame.place(x=410,y=140,width=320,height=450)

        img1=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\Lo1.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        leb_img=Label(frame,image=self.photoimg1)
        leb_img.place(x=110,y=5,width=100,height=90)

        get_started=Label(frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg="blue")
        get_started.place(x=95,y=100)

        #lable
        usernamel=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="black",fg="blue")
        usernamel.place(x=55,y=150)

        self.uentry=ttk.Entry(frame,width=30,textvariable=self.var_username,font=("times new roman",12,"bold"))
        self.uentry.place(x=35,y=180)

        passworl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="blue")
        passworl.place(x=55,y=220)

        self.pentry=ttk.Entry(frame,width=30,textvariable=self.var_password,font=("times new roman",12,"bold"))
        self.pentry.place(x=35,y=250)

        #*****icone image*****
        i=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\user.png")
        i=i.resize((30,30),Image.ANTIALIAS)
        self.photoi=ImageTk.PhotoImage(i)

        leb_i=Label(frame,image=self.photoi,bg="black",borderwidth=0)
        leb_i.place(x=36,y=150,width=20,height=25)

        i2=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\lock.png")
        i2=i2.resize((30,25),Image.ANTIALIAS)
        self.photoi2=ImageTk.PhotoImage(i2)

        leb_i2=Label(frame,image=self.photoi2,bg="black",borderwidth=0)
        leb_i2.place(x=36,y=220,width=20,height=25)

        #** btn***
        
        login_btn=Button(frame,text="Login",command=self.login,font=("times new roman",12,"bold"),bd=2,relief=RIDGE,bg="blue",fg="white",activeforeground="white",activebackground="blue")
        login_btn.place(x=100,y=300,width=120,height=30)

        reg_btn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",12,"bold"),bd=0,relief=RIDGE,bg="black",fg="white",activeforeground="white",activebackground="black")
        reg_btn.place(x=26,y=350,width=150,height=30)

        for_btn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",12,"bold"),bd=0,relief=RIDGE,bg="black",fg="white",activeforeground="white",activebackground="black")
        for_btn.place(x=30,y=380,width=120,height=30)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
     
        
    def login(self):
        if self.uentry.get()=="" or self.pentry.get()=="":
            messagebox.showerror("error","all field required")
        elif self.uentry.get()=="simmi" and self.pentry.get()=="rani":
            messagebox.showinfo("success","welcome")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="neeraj@123",database="face")
            my_cursor=conn.cursor()
            my_cursor.execute("select* from register where email=%s and password=%s",(
                                                                                        self.var_username.get(),
                                                                                        self.var_password.get(),
                                                                                      ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("yes","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_recognition_system(self.new_window)
                    self.var_username.set("")
                    self.var_password.set("")
                    
                else:
                    if not open_main:
                        return
                
            conn.commit()
            conn.close()

    #**** reset password **** 
    def reset_pass(self):
        if self.q_combo.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.aentry.get()=="":
            messagebox.showerror("Error","Please Enter the answer",parent=self.root2)
        elif self.newpass.get()=="":
            messagebox.showerror("Error","Please enter the new Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="neeraj@123",database="face")
            my_cursor=conn.cursor()
            qury=("Select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.var_username.get(),self.var_secQ.get(),self.var_secA.get())
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.var_newpass.get(),self.var_username.get()) 
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset , please login new password",parent=self.root2)   
                self.root2.destroy()



    #******* forget password *******
    def forget_password_window(self):
        if self.uentry.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="neeraj@123",database="face")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_username.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My error","Please enter the valid user name",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+410+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)

                squestion=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"))
                squestion.place(x=50,y=80)
                self.q_combo=ttk.Combobox(self.root2,textvariable=self.var_secQ,width=20,font=("times new roman",12,"bold"),state="readonly")
                self.q_combo["values"]=("Select","Your Birth Place","Your favorite day","your favorite color")
                self.q_combo.current(0)
                self.q_combo.place(x=50,y=110,width=250)

                sanswer=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"))
                sanswer.place(x=50,y=150)
                self.aentry=ttk.Entry(self.root2,textvariable=self.var_secA,width=20,font=("times new roman",15,"bold"))
                self.aentry.place(x=50,y=180,width=250) 

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"))
                new_password.place(x=50,y=220)
                self.newpass=ttk.Entry(self.root2,textvariable=self.var_newpass,width=20,font=("times new roman",12,"bold"))
                self.newpass.place(x=50,y=250,width=250) 

                btn=Button(self.root2,text='Reset',command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=130,y=290)







if __name__=="__main__":
    main()

        