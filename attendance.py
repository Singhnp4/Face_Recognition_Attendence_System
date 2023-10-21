from distutils.util import execute
from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import string
from tkinter import*
from tkinter import ttk
from turtle import right
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import CascadeClassifier
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1260x670+0+0")
        self.root.title("face Recognition System")

        #***varibles****
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_course=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()


        # Background image
        imgb=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\s1.jpg")
        imgb=imgb.resize((1900,700),Image.ANTIALIAS)
        self.photoimgb=ImageTk.PhotoImage(imgb)

        bg_img=Label(self.root,image=self.photoimgb)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=15,y=20,width=1230,height=610)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",21,"bold"))
        left_frame.place(x=10,y=10,width=340,height=570)

        attendance_label=Label(left_frame,text="Attendance ID",font=("times new roman",12,"bold"))
        attendance_label.grid(row=0,column=0,padx=10)

        attendance_entry=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendance_entry.grid(row=0,column=1,pady=10,sticky=W)

        rollLabel=Label(left_frame,text="Roll No",font=("times new roman",12,"bold"))
        rollLabel.grid(row=1,column=0,padx=10)

        atten_roll=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        atten_roll.grid(row=1,column=1,pady=10,sticky=W)

        nameLabel=Label(left_frame,text="Name",font=("times new roman",12,"bold"))
        nameLabel.grid(row=2,column=0,padx=10)

        atten_name=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name.grid(row=2,column=1,pady=10,sticky=W)

        dateLabel=Label(left_frame,text="Date",font=("times new roman",12,"bold"))
        dateLabel.grid(row=3,column=0,padx=10)

        atten_date=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date.grid(row=3,column=1,pady=10,sticky=W)

        timeLabel=Label(left_frame,text="Time",font=("times new roman",12,"bold"))
        timeLabel.grid(row=4,column=0,padx=10)

        atten_time=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time.grid(row=4,column=1,pady=10,sticky=W)

        courseLabel=Label(left_frame,text="Course",font=("times new roman",12,"bold"))
        courseLabel.grid(row=5,column=0,padx=10)

        atten_course=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_course,font=("times new roman",12,"bold"))
        atten_course.grid(row=5,column=1,pady=10,sticky=W)

        attendanceLabel=Label(left_frame,text="Attendance Status",font=("times new roman",12,"bold"))
        attendanceLabel.grid(row=6,column=0,padx=10)

        self.atten_status=ttk.Combobox(left_frame,width=17,textvariable=self.var_atten_attendence,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=6,column=1,padx=2,pady=10,sticky=W)



        #buttons Frame
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=330,width=325,height=80)

        imgf=Image.open(r"C:\Users\nps10\Desktop\project\Face_recognition_System\Images\s1.jpg")
        imgf=imgf.resize((650,300),Image.ANTIALIAS)
        self.photoimgf=ImageTk.PhotoImage(imgf)

        fr_img=Label(btn_frame,image=self.photoimgf)
        fr_img.place(x=0,y=0,relwidth=1,relheight=1)

        imp_btn=Button(btn_frame,width=10,text="Import csv",command=self.importCsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        imp_btn.place(x=10,y=5,width=140,height=30)

        exp_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        exp_btn.place(x=170,y=5,width=140,height=30)

        rest_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        rest_btn.place(x=90,y=40,width=140,height=30)

        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance List",font=("times new roman",21,"bold"))
        right_frame.place(x=370,y=10,width=840,height=570)

        #table
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=10,y=5,width=820,height=500)

        scrl_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrl_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReport_table=ttk.Treeview(table_frame,column=("id","roll","name","course","time","date","attendance"),xscrollcommand=scrl_x.set,yscrollcommand=scrl_y.set)

        scrl_x.pack(side=BOTTOM,fill=X)
        scrl_y.pack(side=RIGHT,fill=Y)
        scrl_x.config(command=self.AttendanceReport_table.xview)
        scrl_y.config(command=self.AttendanceReport_table.yview)

        self.AttendanceReport_table.heading("id",text="Attendance id")
        self.AttendanceReport_table.heading("roll",text="Roll no")
        self.AttendanceReport_table.heading("name",text="Name")
        self.AttendanceReport_table.heading("course",text="Course")
        self.AttendanceReport_table.heading("time",text="Time")
        self.AttendanceReport_table.heading("date",text="Date")
        self.AttendanceReport_table.heading("attendance",text="Status")
        self.AttendanceReport_table["show"]="headings"

        self.AttendanceReport_table.pack(fill=BOTH,expand=1)
        self.AttendanceReport_table.bind("<ButtonRelease>",self.get_cursor)
        #self.fetch_data()
        
    #fetch data
    def fetchData(self,rows):
        self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())
        for i in rows:
            self.AttendanceReport_table.insert("",END,values=i)

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All files","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)
        

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReport_table.focus()
        content=self.AttendanceReport_table.item(cursor_row)
        row=content["values"]
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_course.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendence.set(row[6])
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_course.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")




if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()