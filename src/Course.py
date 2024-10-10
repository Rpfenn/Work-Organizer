
from Task import Task
import os
import sqlite3
import customtkinter as ctk
from customtkinter import *
from customtkinter import CTkLabel
from tkinter import *
import pywinstyles
class Course:
    def __init__(self, name:str, color:str):
        self.name = name
        self.color = color
        self.tasks = []
        conn = sqlite3.connect('work_organizer.db')
        cursor = conn.execute("SELECT * FROM Assignments WHERE CourseName = '{}'".format(self.name))
        for row in cursor:
            self.tasks.append(Task(row[0], row[1], row[3], row[4], row[5]))
        conn.commit()
        conn.close()
    def add_task(self, windowframe:ctk, cframe:ctk):
        frame = ctk.CTkFrame(windowframe, width=200, height=200, border_color="black", border_width=4)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Set explicit width and height for the frame
        frame.configure(width=200, height=300)
        
        frame_label = ctk.CTkLabel(frame, width=180, height=20, text="Add Task", font=("Corbel", 15))
        frame_label.place(x=10, y=10)  # Use place to position the label within the frame
        
        task_entry = ctk.CTkEntry(frame, width=180, height=20, placeholder_text="Task Name")
        task_entry.place(x=10, y=40)  # Use place to position the entry within the frame
        
        description_entry = ctk.CTkEntry(frame, width=180, height=20, placeholder_text="Task Description")
        description_entry.place(x=10, y=70)  # Use place to position the entry within the frame
        
        date_entry = ctk.CTkEntry(frame, width=180, height=20, placeholder_text="Due Date")
        date_entry.place(x=10, y=100)  # Use place to position the entry within the frame
        
        close_button = ctk.CTkButton(frame, width=20, height=20,corner_radius=10, text="X", command=lambda: frame.destroy())
        close_button.place(x=170, y=10)
        # time_entry = ctk.CTkEntry(frame, width=180, height=20, placeholder_text="Time")
        # time_entry.place(x=10, y=130)  # Use place to position the entry within the frame
        
        
        def add_task_action():
            task_name = task_entry.get()
            description = description_entry.get()
            if date_entry.get() == "":
                dueDate = "No Due Date"
            else:
                dueDate = date_entry.get()
            task = Task(self.get_nextId(),task_name, dueDate, description, 0) 
            self.tasks.append(task)
            frame.destroy()
            conn = sqlite3.connect('work_organizer.db')
            conn.execute("INSERT INTO Assignments (taskID, taskName, CourseName, dueDate, description, completed) VALUES ('{}','{}','{}', '{}', '{}', '{}')".format(task.id, task.taskName, self.name,task.dueDate, task.description, task.completed))
            conn.commit()
            task.draw(cframe)
        add_button = ctk.CTkButton(frame, width=180, height=20, text="Add", command=add_task_action)
        add_button.place(x=10, y=130)  # Use place to position the button within the frame
        
        
    def load_tasks(self):
        conn = sqlite3.connect('work_organizer.db')
        cursor = conn.execute("SELECT * FROM Assignments WHERE CourseName = '{}'".format(self.name))
        for row in cursor:
            self.tasks.append(Task(row[0], row[1], row[3], row[4], row[5]))
        conn.commit()
        conn.close()
        
    def get_tasks(self):
        return self.tasks
    
    def get_nextId(self):
        conn = sqlite3.connect('work_organizer.db')
        cursor = conn.execute("SELECT MAX(TaskID) FROM Assignments")
        for row in cursor:
            if(row[0] == None):
                return 1
            return row[0]+1
        conn.commit()
        conn.close()
        
        
    
    def draw(self, frame:ctk):
        course_frame = ctk.CTkFrame(frame, width = 200, height = 400, border_color="black", border_width=4)
        course_frame.pack(side = LEFT, fill = Y, padx = 5)
        course_frame.pack_propagate(False)
        course_label = ctk.CTkLabel(course_frame, width = 192, height = 36, corner_radius= 2,text = self.name, fg_color=self.color, font=("Corbel", 20))
        course_label.pack(pady=3)
        for task in self.tasks:
            task.draw(course_frame)
        add_task_button = ctk.CTkButton(course_frame, width = 192, height = 36, corner_radius = 2, text = "Add Task", command = lambda: self.add_task(frame, course_frame))
        add_task_button.pack(side = BOTTOM, pady=3)
        options_button = ctk.CTkButton(course_frame, width = 20, height = 20, corner_radius = 10, fg_color= "transparent",text = "...", bg_color= "#000001",command = lambda: self.show_options(course_frame))
        options_button.place(x=160, y=10)
        pywinstyles.set_opacity(options_button, color="#000001")
    def delete_course(self, course_frame):
        conn = sqlite3.connect('work_organizer.db')
        conn.execute("DELETE FROM Courses WHERE CourseName = '{}'".format(self.name))
        conn.execute("DELETE FROM Assignments WHERE CourseName = '{}'".format(self.name))
        conn.commit()
        conn.close()
        self.tasks = []
        course_frame.destroy()
        
    
    def show_options(self, course_frame):
        options_frame = ctk.CTkFrame(course_frame, width = 200, height = 200, border_color="black", border_width=4)
        options_frame.place(relx=0.5, rely=0.5, anchor="center")
        options_frame.configure(width=200, height=200)
        options_label = ctk.CTkLabel(options_frame, width=180, height=20, text="Options", font=("Corbel", 15))
        options_label.place(x=10, y=10)
        delete_button = ctk.CTkButton(options_frame, width=180, height=20, text="Delete Course", command=lambda: self.delete_course(course_frame))
        delete_button.place(x=10, y=40)
        close_button = ctk.CTkButton(options_frame, width=20, height=20,corner_radius=10, text="X", command=lambda: options_frame.destroy())
        close_button.place(x=170, y=10)
        # change_color = ctk.CTkOptionMenu(options_frame, values=["red", "blue", "green", "yellow", "purple", "orange", "pink"], width=180, height=20)
        # change_color.place(x=10, y=70)
        # change_color_button = ctk.CTkButton(options_frame, width=180, height=20, text="Change Color", command=lambda: self.change_color(change_color))
        # change_color_button.place(x=10, y=100)
    #def update_tasks(self):
        
    # def load_tasks(self):
       
    # def change_color(self, color_menu:ctk):
    #     self.color = color_menu.get()
    #     conn = sqlite3.connect('work_organizer.db')
    #     conn.execute("UPDATE Courses SET Color = '{}' WHERE CourseName = '{}'".format(self.color, self.name))
    #     conn.commit()
    #     conn.close()