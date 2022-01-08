import tkinter
from tkinter import *
from tkcalendar import Calendar
root = Tk()
canvas_width = 800
canvas_height = 800
root.geometry(f"{canvas_width}x{canvas_height}")
root.title('Spa and Salon Booking')

f1 = Frame(root,bg="yellow",borderwidth=4)
f1.grid(row=5,column=7)
cal = Calendar(f1, selectmode='day',
               year=2020, month=5,
               day=22)
def get_adate():
    l5.config(text=cal.get_date())
    f1.grid_forget()

def show_calendar():
    f1.grid(row=5,column=7)
    cal.grid(row=5,column=7)
    button_2 = Button(root,text="Select Date",command = get_adate)
    button_2.grid(row=0,column=3)

date_button = Button(root, text = "Open Calendar",command = show_calendar).grid(row=0,column=0)

l5 = Label(root, text = "")
l5.grid(row=0,column=2)

root.mainloop()