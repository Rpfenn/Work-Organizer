from datetime import datetime
import customtkinter as ctk
from customtkinter import *
from tkinter import *
from tkinter import Label
from Course import Course
from Task import Task
#import tkMessageBox

#import threading
class GUI:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.minsize(600, 450)
        self.window.title("Work Organizer")
        self.date_time = Label(self.window, text="", font=('Times 14'), width=30, height=10)
        self.date_time.place(x = 150, y = -75)
        update(self)
        self.window.mainloop()


   

def update(self):
    now = datetime.now()
    self.date_time.config(text=now.strftime("%A %B %d, %Y  %I:%M%p"))
    
    
    
    self.window.after(1000, update)
   
    