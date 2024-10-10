from datetime import datetime
import customtkinter as ctk
from customtkinter import *
from customtkinter import CTkLabel
from tkinter import *
from Course import Course
from Task import Task
from CourseManager import CourseManager
import threading
import time
#import tkMessageBox

#import threading
class GUI:
    def __init__(self, manager:CourseManager):
        self.window = ctk.CTk()
        self.manager  = manager
        self.window.minsize(1000, 562.5)
        self.window.maxsize(1000, 562.5)
        self.window.title("Work Organizer")
        ctk.set_appearance_mode("dark")
        now = datetime.now()
        self.date_time = ctk.CTkLabel(self.window, text=now.strftime("%A %B %d, %Y  %I:%M%p"))
        self.colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]
        self.date_time.pack(pady = 10)
        self.add_course_button = ctk.CTkButton(self.window, width = 200, height = 50, corner_radius = 2, text = "Add Course", command = self.add_course)
        #self.courses_frame = ctk.CTkFrame(self.window, width = 1000, height = 500, border_color="black", border_width=4)
        self.courses_frame = ctk.CTkScrollableFrame(self.window, width=1000, height=500, border_color="black", border_width=4, orientation= "horizontal")
        self.courses_frame.pack(side = BOTTOM, fill = X)
        self.draw_courses()
        self.time_thread = threading.Thread(target=self.update_time)
        self.time_thread.daemon = True
        self.time_thread.start()
        self.window.mainloop()

    def update_time(self):
        while True:
            now = datetime.now()
            time_str = now.strftime("%A %B %d, %Y  %I:%M%p")
            self.window.after(0, self.update_label, time_str)
            time.sleep(1)

    def update_label(self, time_str):
        self.date_time.configure(text=time_str)



    def draw_courses(self):
        for course in self.manager.get_courses():
            course.draw(self.courses_frame)
        self.add_course_button = ctk.CTkButton(self.courses_frame, width = 200, height = 100, corner_radius = 2, text = "Add Course", command = self.add_course)
        self.add_course_button.pack(side = RIGHT, padx = 5)
        self.add_course_button.pack_propagate(False)
    def delete_course(self, course_frame, course):
        self.manager.delete_course(course)
        course_frame.destroy()
        
    def add_course(self):
        frame = ctk.CTkFrame(self.courses_frame, width=200, height=130, border_color="black", border_width=4)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Set explicit width and height for the frame
        frame.configure(width=200, height=130)
        
        frame_label = ctk.CTkLabel(frame, width=180, height=20, text="Add Course", font=("Corbel", 15))
        frame_label.place(x=10, y=10)  # Use place to position the label within the frame
        
        course_entry = ctk.CTkEntry(frame, width=180, height=20, placeholder_text="Course Name")
        course_entry.place(x=10, y=40)  # Use place to position the entry within the frame
        
        option_menu = ctk.CTkOptionMenu(frame, values=self.colors, width=180, height=20)
        option_menu.place(x=10, y=70)  # Use place to position the option menu within the frame
        
        def add_course_action():
            course_name = course_entry.get()
            choice = option_menu.get()
            course = Course(course_name, choice)
            self.manager.add_course(course)
            frame.destroy()
            #self.add_course_button.destroy()
            course.draw(self.courses_frame)
            # self.add_course_button = ctk.CTkButton(self.window, width = 200, height = 50, corner_radius = 2, text = "Add Course", command = self.add_course)
            # self.add_course_button.pack(side = LEFT, fill = Y, padx = 5)
            
        add_button = ctk.CTkButton(frame, width=180, height=20, text="Add", command=add_course_action)
        add_button.place(x=10, y=100)  # Use place to position the button within the frame
        
        
            
        
            
    
        
        
    
        