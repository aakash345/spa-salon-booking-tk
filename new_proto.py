import tkinter
from tkinter import *
from tkcalendar import Calendar
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql
import PIL
from PIL import Image,ImageTk


def main():
    start_root.destroy()
    # Main Window
    root = Tk()
    canvas_width = root.winfo_screenwidth()
    canvas_height = root.winfo_screenheight()
    root.geometry(f"{canvas_width}x{canvas_height}")
    root.title('Spa and Salon Booking')
    root.config(bg='powder blue')

    # bg_photo = Image.open("spa_img (1).png").resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    # bg_photo = ImageTk.PhotoImage(bg_photo)
    # background_label = Label(root, image=bg_photo)
    # background_label.place(x=0, y=0, relwidth=1, relheight=1)

    text = Label(root, text='TCET SPA & SALON', font="comicsans 15 bold", borderwidth=0, padx=0, pady=0,
                 bg='powder blue')
    text.place(x=root.winfo_screenwidth() / 2 - 120, y=40)

    # Name Label & Entry
    l1 = Label(root, text='Name', font="comicsans 14", bg='lime')
    l1.place(x=root.winfo_screenwidth() / 2 - 180, y=100)
    name_text = StringVar()
    e1 = Entry(root, textvariable=name_text, borderwidth=2)
    e1.place(x=root.winfo_screenwidth() / 2 + 5, y=104)

    # Gender Label & Radiobutton
    l2 = Label(root, text='Gender', font="comicsans 14", bg='lime')
    l2.place(x=root.winfo_screenwidth() / 2 - 180, y=150)
    var = StringVar(root, "M")
    r1 = Radiobutton(root, text='Male', variable=var, value="M").place(x=root.winfo_screenwidth() / 2 + 5, y=150)
    r2 = Radiobutton(root, text='Female', variable=var, value="F").place(x=root.winfo_screenwidth() / 2 + 70, y=150)

    # Mobile Label & Entry
    l3 = Label(root, text='Mobile No.', font="comicsans 14", bg='lime')
    l3.place(x=root.winfo_screenwidth() / 2 - 180, y=200)
    mobile_text = StringVar()
    e3 = Entry(root, textvariable=mobile_text)
    e3.place(x=root.winfo_screenwidth() / 2 + 5, y=200)

    # Functions to show calendar and get Date
    def get_adate():
        l5.insert(0, cal.get_date())
        f1.place_forget()

    def show_calendar():
        f1.place(x=root.winfo_screenwidth() / 2 + 200, y=250)
        cal.grid(row=4, column=3)
        button_2 = Button(root, text="Select Date", command=get_adate)
        button_2.place(x=root.winfo_screenwidth() / 2 + 120, y=250)

    # Appointment Date Label, Open calendar button, select Date Button and Calendar
    l4 = Label(root, text='Appointment Date', font="comicsans 14", bg='lime')
    l4.place(x=root.winfo_screenwidth() / 2 - 180, y=250)
    f1 = Frame(root, bg="yellow", borderwidth=4)
    f1.place(x=root.winfo_screenwidth() / 2 + 280, y=250)
    cal = Calendar(f1, selectmode='day', date_pattern=('dd-mm-yy'),
                   year=2021, month=5,
                   day=22)

    # photo = Image.open("calendar_icon.jpg").resize((27, 25))
    # photo = ImageTk.PhotoImage(photo)
    # date_button = Button(root, image=photo, command=show_calendar).place(x=root.winfo_screenwidth() / 2 + 80, y=250)

    vdate = StringVar()
    l5 = Entry(root, text="", width=9, borderwidth=3, textvariable=vdate, relief=SUNKEN, fg="Green")
    l5.place(x=root.winfo_screenwidth() / 2 + 5, y=250)

    def character_limit(vdate):
        if len(vdate.get()) > 0:
            vdate.set(vdate.get()[:8])

    vdate.trace("w", lambda *args: character_limit(vdate))

    # Visiting Time Label and Dropdown
    l6 = Label(root, text='Visiting Time', font="comicsans 14", bg='lime')
    l6.place(x=root.winfo_screenwidth() / 2 - 180, y=300)
    vtime = StringVar()
    timechoosen = ttk.Combobox(root, width=16, textvariable=vtime)
    timechoosen['values'] = ('8:00AM-12:00PM', '12:00PM-4:00PM', '4:00PM-8:00PM')
    timechoosen.place(x=root.winfo_screenwidth() / 2 + 5, y=300)
    timechoosen.current()

    # Service Required Label and Dropdown
    l7 = Label(root, text="Book Services", font="comicsans 14", bg='lime')
    l7.place(x=root.winfo_screenwidth() / 2 - 180, y=350)
    service = StringVar()
    servicechoosen = ttk.Combobox(root, width=16, textvariable=service)
    servicechoosen['values'] = ('Facial', 'Hair', 'Nails', 'Body', 'Makeup', 'Massage')
    servicechoosen.place(x=root.winfo_screenwidth() / 2 + 5, y=350)
    servicechoosen.current()

    def submit():
        if (
                name_text.get() != "" and var.get() != "" and mobile_text.get() != "" and vdate.get() != "" and vtime.get() != "" and service.get() != ""):
            insert(name_text.get(), var.get(), mobile_text.get(), vdate.get(), vtime.get(), service.get())
            messagebox.showinfo("SPA & SALON", f"Booking Successful for {vdate.get()} between {vtime.get()}")
        elif (
                name_text.get() != "" or var.get() != "" or mobile_text.get() != "" or vdate.get() != "" or vtime.get() != "" or service.get() != ""):
            messagebox.showerror("SPA & SALON", "FILL ALL REQUIRED FIELDS")

    def on_enter(e):
        submit_btn['background'] = 'grey'
        submit_btn.config(font="calibri 10 bold underline")

    def on_leave(e):
        submit_btn['background'] = 'SystemButtonFace'
        submit_btn.config(font="calibri 10 bold")

    # Submit Button
    submit_btn = Button(root,text="SUBMIT", command=submit, height=2, width=10, font=('calibri', 10, 'bold'),
                        foreground='red')
    submit_btn.place(x=root.winfo_screenwidth() / 2 - 70, y=430)
    submit_btn.bind("<Enter>", on_enter)
    submit_btn.bind("<Leave>", on_leave)

    # Functions to create Database and Table
    def createdb():
        conn = mysql.connect(host="localhost", user="root", password="")
        cur = conn.cursor()
        cur.execute("CREATE DATABASE bookinginfo")
        cur.execute("commit")
        print("Database Created")
        conn.close()

    def createtable():
        conn = mysql.connect(host="localhost", user="root", password="", database="bookinginfo")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE booked ( id int(100) NOT NULL auto_increment, Name varchar(50), Gender varchar(50),MobileNo varchar(50),BookingDate varchar(50),BookingTime varchar(50),Service varchar(50),PRIMARY KEY(id) );")
        cur.execute("commit")
        print("Table Created")
        conn.close()

    # Function to insert data into Database
    def insert(name, gender, mobile, book_date, book_time, book_service):
        conn = mysql.connect(host="localhost", user="root", password="", database="bookinginfo")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO booked (Name,Gender,MobileNo,BookingDate,BookingTime,Service) VALUES (%s,%s,%s,%s,%s,%s)",
            (name, gender, mobile, book_date, book_time, book_service))
        print("working")
        cur.execute("commit")
        conn.close()

    # Run the program once by uncommenting this 2 functions and then again comment them, so that Database and Table would be created
    # createdb()
    # createtable()
    root.mainloop()

def register_win():
    start_root.destroy()
    register_root = Tk()
    canvas_width = register_root.winfo_screenwidth()
    canvas_height = register_root.winfo_screenheight()
    register_root.geometry(f"{canvas_width}x{canvas_height}")
    register_root.title('Spa and Salon Booking')
    register_root.config(bg='powder blue')

    text = Label(register_root, text='TCET SPA & SALON', font="comicsans 15 bold", borderwidth=0, padx=0, pady=0,
                 bg='powder blue')
    text.place(x=register_root.winfo_screenwidth() / 2 - 120, y=40)

    # Name Label & Entry
    l1 = Label(register_root, text='Salon Name', font="comicsans 14", bg='lime')
    l1.place(x=register_root.winfo_screenwidth() / 2 - 180, y=100)
    name_text = StringVar()
    e1 = Entry(register_root, textvariable=name_text, borderwidth=2)
    e1.place(x=register_root.winfo_screenwidth() / 2 + 5, y=104)

    # Gender Label & Radiobutton
    l2 = Label(register_root, text='Gender', font="comicsans 14", bg='lime')
    l2.place(x=register_root.winfo_screenwidth() / 2 - 180, y=150)
    rvar = StringVar(register_root,"M")
    print(rvar.get())
    r1 = Radiobutton(register_root, text='Male',variable=rvar,value="M")
    r1.select()
    r1.place(x=register_root.winfo_screenwidth() / 2 + 5, y=150)
    r2 = Radiobutton(register_root, text='Female', variable=rvar, value="F")
    r2.deselect()
    r2.place(x=register_root.winfo_screenwidth() / 2 + 70, y=150)
    r3 = Radiobutton(register_root, text="Unisex",variable=rvar,value="U")
    r3.deselect()
    r3.place(x=register_root.winfo_screenwidth() / 2 + 150, y=150)
    r3.bind('<Motion>', lambda e: str(rvar.get()))
def login_win():
    pass

def on_enter(e):
    e.widget['background'] = 'lime'

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'
start_root = Tk()
def start():
    canvas_width = start_root.winfo_screenwidth()
    canvas_height = start_root.winfo_screenheight()
    start_root.geometry(f"{canvas_width}x{canvas_height}")
    start_root.title('Spa and Salon Booking')
    start_root.config(bg='powder blue')
    register_btn = Button(start_root,text="Register",command=register_win,font="comicsans 14")
    register_btn.place(x=700,y=200)
    register_btn.bind("<Enter>", on_enter)
    register_btn.bind("<Leave>", on_leave)
    login_btn = Button(start_root, text="Login", command=login_win, font="comicsans 14")
    login_btn.place(x=670, y=300)
    login_btn.bind("<Enter>", on_enter)
    login_btn.bind("<Leave>", on_leave)
    guest_btn = Button(start_root, text="Guest", command=main, font="comicsans 14")
    guest_btn.place(x=770, y=300)
    guest_btn.bind("<Enter>", on_enter)
    guest_btn.bind("<Leave>", on_leave)

    start_root.mainloop()

start()
