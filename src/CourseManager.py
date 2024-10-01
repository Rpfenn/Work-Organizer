
from Course import Course
from Task import Task
import sqlite3

class CourseManager:
    
    def init(self):
        self.courses = []
        self.load_courses()
    
    
    def add_course(self, course:Course):
        self.courses.append(course)
        conn = sqlite3.connect('work_organizer.db')
        conn.execute("INSERT INTO COURSES (CourseName, Color) VALUES ('{}','{}')".format(course.name, course.color))
        conn.commit()
        conn.close()
    
    def load_courses(self):
        conn = sqlite3.connect('work_organizer.db')
        cursor = conn.execute("SELECT * FROM Courses")
        for row in cursor:
            self.courses.append(Course(row[0], row[1]))
        conn.commit()
        conn.close()
        