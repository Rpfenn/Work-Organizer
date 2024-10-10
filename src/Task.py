

import customtkinter as ctk
from customtkinter import *
from customtkinter import CTkLabel
from tkinter import *

class Task:
    def __init__(self,id,taskName, dueDate, description, completed):
        self.taskName = taskName
        self.dueDate = dueDate
        self.description = description
        self.completed = completed
        self.id = id
        
        
        
    def draw(self, course_frame:ctk):
        task_frame = ctk.CTkFrame(course_frame, width = 190, height = 60, border_color="black", border_width=4)
        task_frame.pack(side = TOP, pady = 3)
        task_frame.pack_propagate(False)
        if self.completed == 0:
            tempcolor = "grey"
        else:
            tempcolor = "green"
        task_label = ctk.CTkLabel(task_frame, width = 190, height = 30, corner_radius= 2,text = self.taskName, font=("Corbel", 15))
        task_label.pack(pady=3)
        date_label = ctk.CTkLabel(task_frame, width = 190, height = 20, corner_radius= 2,text = self.get_duedate(), font=("Corbel", 10))
        date_label.pack(side = BOTTOM, pady=3)
        task_label.bind("<Button-1>", self.toggle_complete(task_label))
    
    def toggle_complete(self, label:ctk):
        if self.completed == 0:
            self.completed = 1
            label.configure(fg_color = "green")
        else:
            self.completed = 0
            label.configure(fg_color = "grey")
    
    
    def get_duedate(self):
        if(self.dueDate == None or self.dueDate == ""):
            return "No Due Date"
        full_date = self.dueDate.split("/")
        month = ""
        day = ""
        date = ""
        postfix = ""
        
        
        match full_date[0]:
            case "01" | "1":
                month = "January"
            case "02"|"2":
                month = "February"
            case "03"|"3":
                month = "March"
            case "04"|"4":
                month = "April"
            case "05"| "5":
                month = "May"
            case "06"|"6":
                month = "June"
            case "07"|"7":
                month = "July"
            case "08"|"8":
                month = "August"
            case "09"|"9":
                month = "September"
            case "10": 
                month = "October"
            case "11":
                month = "November"
            case "12":
                month = "December"
            case _:
                date = ""
                return date
        
        if full_date[1] == "1":
            postfix = "st"
        elif full_date[1] == "2":
            postfix = "nd"
        elif full_date[1] == "3":
            postfix = "rd"
        else:
            postfix = "th"
        day = full_date[1]
        date = f"{month} {day+postfix}" 
        return date
    
        