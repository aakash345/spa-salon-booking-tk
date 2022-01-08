import tkinter
from tkinter import *
from tkcalendar import Calendar
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql
import PIL
from PIL import Image,ImageTk

#Main Window
root = Tk()
canvas_width = root.winfo_screenwidth()
canvas_height = root.winfo_screenheight()
root.geometry(f"{canvas_width}x{canvas_height}")
root.title('Spa and Salon Booking')
root.config(bg='powder blue')

bg_photo = Image.open("spa_img.png").resize((root.winfo_screenwidth(),root.winfo_screenheight()))
bg_photo = ImageTk.PhotoImage(bg_photo)
background_label = Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

text = Label(root,text='TCET SPA & SALON',font="comicsans 15 bold",borderwidth=0,padx=0,pady=0,bg='powder blue')
text.place(x=root.winfo_screenwidth()/2-100,y=40)

#Name Label & Entry
l1 = Label(root,text='Name',font="comicsans 14",bg='lime')
l1.place(x=root.winfo_screenwidth()/2-140,y=100)
name_text = StringVar()
e1 = Entry(root,textvariable=name_text,borderwidth=2)
e1.place(x=root.winfo_screenwidth()/2+5,y=104)

#Gender Label & Radiobutton
l2 = Label(root,text='Gender',font="comicsans 14",bg='lime')
l2.place(x=root.winfo_screenwidth()/2-145,y=150)
var = StringVar(root,"M")
r1 = Radiobutton(root,text='Male',variable=var,value="M").place(x=root.winfo_screenwidth()/2+5,y=150)
r2 = Radiobutton(root,text='Female',variable=var,value="F").place(x=root.winfo_screenwidth()/2+100,y=150)

#Mobile Label & Entry
l3 = Label(root,text='Mobile No.',font="comicsans 14",bg='lime')
l3.place(x=root.winfo_screenwidth()/2-155,y=200)
mobile_text = StringVar()
e3 = Entry(root,textvariable=mobile_text)
e3.place(x=root.winfo_screenwidth()/2+5,y=200)

#Functions to show calendar and get Date
def get_adate():
    l5.insert(0,cal.get_date())
    f1.place_forget()

def show_calendar():
    f1.place(x=root.winfo_screenwidth()/2+280,y=250)
    cal.grid(row=4,column=3)
    button_2 = Button(root,text="Select Date",command = get_adate)
    button_2.place(x=root.winfo_screenwidth()/2+150,y=250)
#Appointment Date Label, Open calendar button, select Date Button and Calendar
l4 = Label(root,text='Appointment Date',font="comicsans 14",bg='lime')
l4.place(x=root.winfo_screenwidth()/2-180,y=250)
f1 = Frame(root,bg="yellow",borderwidth=4)
f1.place(x=root.winfo_screenwidth()/2+280,y=250)
cal = Calendar(f1, selectmode='day',date_pattern=('dd-mm-yy'),
               year=2021, month=5,
               day=22)

photo = Image.open("calendar_icon.jpg").resize((27, 25))
photo = ImageTk.PhotoImage(photo)
date_button = Button(root,image=photo,command = show_calendar).place(x=root.winfo_screenwidth()/2+220,y=250)

vdate=StringVar()
l5 = Entry(root, text = "",width=8,borderwidth=3,textvariable=vdate,relief=SUNKEN,fg="Green")
l5.place(x=root.winfo_screenwidth()/2+40,y=250)


#Visiting Time Label and Dropdown
l6 = Label(root,text='Visiting Time',font="comicsans 14",bg='lime')
l6.place(x=root.winfo_screenwidth()/2-155,y=300)
vtime = StringVar()
timechoosen = ttk.Combobox(root, width=16, textvariable=vtime)
timechoosen['values'] = ('8:00AM-12:00PM','12:00PM-4:00PM','4:00PM-8:00PM')
timechoosen.place(x=root.winfo_screenwidth()/2+5,y=300)
timechoosen.current()

#Service Required Label and Dropdown
l7 = Label(root,text="Book Services",font="comicsans 14",bg='lime')
l7.place(x=root.winfo_screenwidth()/2-175,y=350)
service = StringVar()
servicechoosen = ttk.Combobox(root, width=16, textvariable=service)
servicechoosen['values'] = ('Facial','Hair','Nails','Body','Makeup','Massage')
servicechoosen.place(x=root.winfo_screenwidth()/2+5,y=350)
servicechoosen.current()


def submit():
    if(name_text.get()!="" and var.get()!="" and mobile_text.get()!="" and vdate.get()!="" and vtime.get()!="" and service.get()!=""):
        insert(name_text.get(),var.get(),mobile_text.get(),vdate.get(),vtime.get(),service.get())
        messagebox.showinfo("SPA & SALON", f"Booking Successful for {vdate.get()} between {vtime.get()}")
    elif(name_text.get()!="" or var.get()!="" or mobile_text.get()!="" or vdate.get()!="" or vtime.get()!="" or service.get()!=""):
        messagebox.showerror("SPA & SALON", "FILL ALL REQUIRED FIELDS")

def on_enter(e):
    submit_btn['background'] = 'grey'
    submit_btn.config(font="calibri 10 bold underline")

def on_leave(e):
    submit_btn['background'] = 'SystemButtonFace'
    submit_btn.config(font="calibri 10 bold")

#Submit Button
submit_btn = Button(text="SUBMIT",command=submit,height=2,width=10, font =
               ('calibri', 10, 'bold'),
                foreground = 'red')
submit_btn.place(x=root.winfo_screenwidth()/2-50,y=430)
submit_btn.bind("<Enter>", on_enter)
submit_btn.bind("<Leave>", on_leave)

#Functions to create Database and Table
def createdb():
    conn = mysql.connect(host="localhost", user="root", password="")
    cur = conn.cursor()
    cur.execute("CREATE DATABASE bookinginfo")
    cur.execute("commit")
    print("Database Created")
    conn.close()
def createtable():
    conn = mysql.connect(host="localhost", user="root", password="",database="bookinginfo")
    cur = conn.cursor()
    cur.execute("CREATE TABLE booked ( id int(100) NOT NULL auto_increment, Name varchar(50), Gender varchar(50),MobileNo varchar(50),BookingDate varchar(50),BookingTime varchar(50),Service varchar(50),PRIMARY KEY(id) );")
    cur.execute("commit")
    print("Table Created")
    conn.close()

#Function to insert data into Database
def insert(name, gender,mobile,book_date,book_time,book_service):
    conn = mysql.connect(host="localhost", user="root", password="", database="bookinginfo")
    cur = conn.cursor()
    cur.execute("INSERT INTO booked (Name,Gender,MobileNo,BookingDate,BookingTime,Service) VALUES (%s,%s,%s,%s,%s,%s)", (name, gender,mobile,book_date,book_time,book_service))
    print("working")
    cur.execute("commit")
    conn.close()

#Run the program once by uncommenting this 2 functions and then again comment them, so that Database and Table would be created
# createdb()
# createtable()


root.mainloop()