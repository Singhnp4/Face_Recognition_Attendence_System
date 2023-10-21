from distutils import command
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from Student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1260x670+0+0")
        self.root.title("face Recognition System")

        
        
        # Background image
        imgb=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\s1.jpg")
        imgb=imgb.resize((1500,900),Image.ANTIALIAS)
        self.photoimgb=ImageTk.PhotoImage(imgb)

        bg_img=Label(self.root,image=self.photoimgb)
        bg_img.place(x=0,y=0,width=1500,height=700)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=-5,y=20,width=1400,height=45)

        # student buttom
        imgs=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\studentd.jpg")
        imgs=imgs.resize((260,260),Image.ANTIALIAS)
        self.photoimgs=ImageTk.PhotoImage(imgs)

        b1=Button(bg_img,image=self.photoimgs,command=self.Student_details,cursor="hand2")
        b1.place(x=50,y=250,width=180,height=180)

        b1_1=Button(bg_img,text="Student details",command=self.Student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="red")
        b1_1.place(x=50,y=450,width=180,height=35)

        #photos
        imgp=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\photos.jfif")
        imgp=imgp.resize((230,230),Image.ANTIALIAS)
        self.photoimgp=ImageTk.PhotoImage(imgp)

        b1=Button(bg_img,image=self.photoimgp,cursor="hand2",command=self.open_img)
        b1.place(x=280,y=250,width=180,height=180)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="red")
        b1_1.place(x=280,y=450,width=180,height=35)

        #train data
        imgt=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\train.jpg")
        imgt=imgt.resize((220,220),Image.ANTIALIAS)
        self.photoimgt=ImageTk.PhotoImage(imgt)

        b1=Button(bg_img,image=self.photoimgt,cursor="hand2",command=self.train_data)
        b1.place(x=530,y=250,width=180,height=180)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="red")
        b1_1.place(x=530,y=450,width=180,height=35)

        #face detection
        imgf=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\face.jpg")
        imgf=imgf.resize((260,260),Image.ANTIALIAS)
        self.photoimgf=ImageTk.PhotoImage(imgf)

        b1=Button(bg_img,image=self.photoimgf,cursor="hand2",command=self.face_data)
        b1.place(x=780,y=250,width=180,height=180)

        b1_1=Button(bg_img,text="Face Recognition",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black",fg="red")
        b1_1.place(x=780,y=450,width=180,height=35)

        #attendence 
        imga=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\r1.jfif")
        imga=imga.resize((250,250),Image.ANTIALIAS)
        self.photoimga=ImageTk.PhotoImage(imga)

        b1=Button(bg_img,image=self.photoimga,cursor="hand2",command=self.attendance_data)
        b1.place(x=1020,y=250,width=180,height=180)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black",fg="red")
        b1_1.place(x=1020,y=450,width=180,height=35)
        
    def open_img(self):
        os.startfile("data")





    #Function button
    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()