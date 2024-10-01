
from Task import Task
import os
import sqlite3
class Course:
    def __init__(self, name:str, color:str):
        self.name = name
        self.color = color
        self.tasks = []
        conn = sqlite3.connect('work_organizer.db')
        cursor = conn.execute("SELECT * FROM Assignments WHERE CourseName = '{}'".format(self.name))
        for row in cursor:
            self.tasks.append(Task(row[0], row[1], row[3], row[4]))
        conn.commit()
        conn.close()
    def add_task(self, task:Task):
        self.tasks.append(task)
        conn = sqlite3.connect('work_organizer.db')
        conn.execute("INSERT INTO COURSES (taskID, taskName, CourseName, dueDate, description) VALUES ('{}','{}','{}', '{}', '{}')".format(task.taskId, task.taskName, self.name,task.dueDate, task.description))
        conn.commit()
        
    def load_tasks(self):
        conn = sqlite3.connect('work_organizer.db')
        cursor = conn.execute("SELECT * FROM Assignments WHERE CourseName = '{}'".format(self.name))
        for row in cursor:
            self.tasks.append(Task(row[0], row[1], row[3], row[4]))
        conn.commit()
        conn.close()
        
    def get_tasks(self):
        return self.tasks
    
        
    
    
    
    #def update_tasks(self):
        
    # def load_tasks(self):
       