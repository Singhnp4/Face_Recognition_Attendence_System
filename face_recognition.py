from distutils.util import execute
from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from tkinter import*
from tkinter import ttk
from turtle import right
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import CascadeClassifier
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1260x670+0+0")
        self.root.title("face Recognition System")

        # Background image
        imgb=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\f.jpg")
        imgb=imgb.resize((1300,700),Image.ANTIALIAS)
        self.photoimgb=ImageTk.PhotoImage(imgb)

        bg_img=Label(self.root,image=self.photoimgb)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=480,y=510,width=300,height=80)

        b1=Button(main_frame,text="Face Recognize",bd=8,cursor="hand2",command=self.face_recog,font=("times new roman",25,"bold"),bg="gray",fg="black")
        b1.place(x=0,y=0,width=300,height=80)

    # attendence
    def mark_attendance(self,i,r,n,c):
        with open("report.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (c not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{c},{dtString},{d1},Present")
                





    #face recognition
    def face_recog(self):
        def draw_boundray(img,classifier,scalefactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            feature=classifier.detectMultiScale(gray_image,scalefactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in feature:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="neeraj@123",database="face")
                my_cursor=conn.cursor()

                my_cursor.execute("select student_name from student where student_ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select course from student where student_ID="+str(id))
                c=my_cursor.fetchone()
                c="+".join(c)

                my_cursor.execute("select roll_no from student where student_ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select student_ID from student where student_ID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                if confidence>77:
                    cv2.putText(img,f"Student ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Course:{c}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,c)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img
        
        facecascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,facecascade)
            cv2.imshow("Welcome to face Recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()





if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()