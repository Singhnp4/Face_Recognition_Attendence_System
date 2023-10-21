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
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1260x670+0+0")
        self.root.title("face Recognition System")

        imgb=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\t1.jpg")
        imgb=imgb.resize((1500,700),Image.ANTIALIAS)
        self.photoimgb=ImageTk.PhotoImage(imgb)

        bg_img=Label(self.root,image=self.photoimgb)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=500,y=300,width=300,height=80)

        b1=Button(main_frame,text="TRAIN DATA",bd=8,command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="gray",fg="black")
        b1.place(x=0,y=0,width=300,height=80)



    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[-1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("training",imageNp)
            cv2.waitKey(1)==(13)

        ids=np.array(ids)

        ##train the classifier

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","training dataset completed",parent=self.root)






if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()