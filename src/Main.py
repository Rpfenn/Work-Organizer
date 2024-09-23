from datetime import date
from datetime import datetime
from tkinter import *
#import tkMessageBox
import tkinter
#import threading

now = datetime.now()
current_date = now.strftime("%A %B %d, %Y  %I:%M%p")


window = tkinter.Tk()
window.minsize(600, 450)

print(current_date)

date_time = Label(window, text=current_date, font=('Times 14'), width=30, height=10).place(x = 150, y = -50)


    

def update():
    print("update")
    now = datetime.now()
    date_time.text.set(now.strftime("%A %B %d, %Y  %I:%M%p"))
    window.after(1000, update)


update()



    
    








window.mainloop()

# def calculate():
#     response = 0
#     entry1 = int(E1.get())
#     entry2 = int(E2.get())
#     operator = E3.get()
#     if operator == "+":
#         response = entry1+entry2
#     elif operator == "-":
#         response = entry1 - entry2
#     elif operator == "*":
#         response = entry1*entry2
#     elif operator == "/":
#         response = entry1/entry2
#     else:
#         response = "No operator"
#     E4.insert(0 ,response)



# dt = now.strftime("%A %B %d, %Y  %I:%M%p")
# print(dt)



# L1 = Label(top, text="My calculator",).grid(row=0,column=1)
# L2 = Label(top, text="Number 1",).grid(row=1,column=0)
# L3 = Label(top, text="Number 2",).grid(row=2,column=0)
# L4 = Label(top, text="Operator",).grid(row=3,column=0)
# L4 = Label(top, text="Answer",).grid(row=4,column=0)
# E1 = Entry(top, bd =5)
# E1.grid(row=1,column=1)
# E2 = Entry(top, bd =5)
# E2.grid(row=2,column=1)
# E3 = Entry(top, bd =5)
# E3.grid(row=3,column=1)
# E4 = Entry(top, bd =5)
# E4.grid(row=4,column=1)
# B=Button(top, text ="Submit", command=calculate).grid(row=5,column=1)










