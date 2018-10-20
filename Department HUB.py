"""
***
Stephon Fonrose
Jorge Alejandre
Alex Trejo
Antonio Patino

10/20/18
v1.2
***
"""


class Department :
    def __init__(self,name,course,time):
        self.name = name
        self.course = course
        self.time = time
        
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Department {}".format(self.name)
    
    # returns name    
    def get_name(self):
        return self.name
    
    #returns course
    def get_course(self):
        return self.course
    
    # returns time
    def get_time(self):
        return self.time
        
    


    
class Event(Department) :
    
    def __init__(self,name,course,time,room):
        self.name = name
        self.course = course
        self.time = time
        self.room = room
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Event {}".format(self.name)
    
    # returns name    
    def get_name(self):
        return self.name
    
    #returns course
    def get_course(self):
        return self.course
    
    # returns time
    def get_time(self):
        return self.time
    
    # returns room
    def get_room(self):
        return self.room
    
    
    

    
class DepartmentTalk(Event) :
    
    def __init__(self,name,room,time,subject):
        self.name = name
        self.room = room
        self.time = time
        self.subject = subject
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Department Talk {}".format(self.name)
    
    # returns name    
    def get_name(self):
        return self.name
    
    # returns room
    def get_room(self):
        return self.room
    
    # returns time
    def get_time(self):
        return self.time
    
    #returns subject
    def get_subject(self):
        return self.subject

    
class TutoringMeeting(Event) :
    
    def __init__(self,tutor,student,course,time,room):
        self.tutor = tutor
        self.student = student
        self.course = course
        self.time = time
        self.room = room
   
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Tutoring Meeting {}".format(self.name)
    
    # returns tutor    
    def get_tutor(self):
        return self.tutor
    
    # returns student
    def get_student(self):
        return self.student
    
    #returns course
    def get_course(self):
        return self.course
    
    # returns time
    def get_time(self):
        return self.time
    
    # returns room
    def get_room(self):
        return self.room

class StudentEvent(Event) :
    
    def __init__(self,name,activity,time,place):
        self.name = name
        self.activity = activity
        self.time = time
        self.place = place
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Student Event {}".format(self.name)
    
    # returns name    
    def get_name(self):
        return self.name
    
    #returns activity
    def get_activity(self):
        return self.activity
    
    # returns time
    def get_time(self):
        return self.time
    
    # returns place
    def get_place(self):
        return self.place


    
    
class User(Department) :
    
    def __init__(self,category):
        self.category = category
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "User {}".format(self.name)
    
    # returns category    
    def get_category(self):
        return self.category
    
    def createEvent(self):
        
    def rescheduleEvent(self):
        
    def removeEvent(self):
        
    def acceptEvent(self):
        
    def declineEvent(self):
        
    


    
    
class Student(User) :
    
    def __init__(self,name,classification,course,department,time):
        self.name = name
        self.classification = classification
        self.course = course
        self.department = department
        self.time = time
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Student {}".format(self.name)
    
    # returns name    
    def get_name(self):
        return self.name
    
    # returns classification
    def get_classification(self):
        return self.classification
    
    #returns course
    def get_course(self):
        return self.course
    
    # returns department
    def get_department(self):
        return self.department
    
    # returns time
    def get_time(self):
        return self.time
    
    
class Tutor(Student) :
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Tutor {}".format(self.name)   


    
    
class Faculty(User) :
    
    def __init__(self,name,course,department,office,hours):
        self.name = name
        self.course = course
        self.department = department
        self.office = office
        self.hours = hours
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Faculty {}".format(self.name)
    
    # returns name    
    def get_name(self):
        return self.name
    
    # returns course
    def get_course(self):
        return self.course
    
    # returns department
    def get_department(self):
        return self.department
    
    # returns office
    def get_office(self):
        return self.office
    
    # returns hours
    def get_hours(self):
        return self.hours
    
    
    

class Administrator(Faculty) :
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Administrator {}".format(self.name)
    

class Professor(Faculty) :
    
   
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Professor {}".format(self.name)