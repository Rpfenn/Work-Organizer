
from Course import Course
from Task import Task
import sqlite3

class CourseManager:
    
    def __init__(self):
        self.courses = []
        self.load_courses()
    
    
    def add_course(self, course:Course):
        self.courses.append(course)
        conn = sqlite3.connect('work_organizer.db')
        conn.execute("INSERT INTO COURSES (CourseId, CourseName, Color) VALUES ('{}','{}', '{}')".format(self.get_nextId(),course.name, course.color))
        conn.commit()
        conn.close()
    
    def load_courses(self):
        conn = sqlite3.connect('work_organizer.db')
        cursor = conn.execute("SELECT * FROM Courses")
        for row in cursor:
            self.courses.append(Course(row[1], row[2]))
        conn.commit()
        conn.close()
    
    
    def delete_course(self, course:Course):
        self.courses.remove(course)
        conn = sqlite3.connect('work_organizer.db')
        conn.execute("DELETE FROM COURSES WHERE CourseName = '{}'".format(course.name))
        conn.commit()
        conn.close()
        
    def get_nextId(self):
        conn = sqlite3.connect('work_organizer.db')
        cursor = conn.execute("SELECT MAX(CourseId) FROM Courses")
        for row in cursor:
            if(row[0] == None):
                return 1
            return row[0]+1
        conn.commit()
        conn.close()
    
    def get_courses(self):
        return self.courses