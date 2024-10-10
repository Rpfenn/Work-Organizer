from Course import Course
from Task import Task
from GUI import GUI
from CourseManager import CourseManager
import sqlite3
import threading

conn = sqlite3.connect('work_organizer.db')
conn.execute('''CREATE TABLE IF NOT EXISTS Courses
            (CourseId INT PRIMARY KEY     NOT NULL,
            CourseName TEXT NOT NULL,
            Color TEXT NOT NULL);''')
conn.execute('''CREATE TABLE IF NOT EXISTS Assignments
            (TaskID INT PRIMARY KEY     NOT NULL,
            TaskName TEXT NOT NULL, 
            CourseName TEXT NOT NULL,
            DueDate TEXT NOT NULL,
            Description TEXT NOT NULL,
            Completed INT NOT NULL);''')
conn.execute
conn.commit()
conn.close() 


manager = CourseManager()
gui = GUI(manager)


# for course in manager.get_courses():
#     if course.name == "Math":
#         course.add_task("Homework", "10/10/2021", "Webassign 2")

#manager.add_course(Course("Databases", "blue"))

# class1.add_task(Task(2, "Homework", "10/10/2021", "Do the math homework"))


# tasks = class1.get_tasks()
# for task in tasks:
#     print(task.taskName)
#     print(task.dueDate)
#     print(task.description)






    
    









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










