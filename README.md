# DSUHackUMBC
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
    
    # returns X    
    def get_name(self):
        return self.name
    
    #returns Y
    def get_course(self):
        return self.course
    
    # returns indent
    def get_time(self):
        return self.time
        
    


    
class Event(Department) :
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Event {}".format(self.name)
    
    

    
class DepartmentTalk(Event) :
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Department Talk {}".format(self.name)

class TutoringMeeting(Event) :
   
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Tutoring Meeting {}".format(self.name)

class StudentEvent(Event) :
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Student Event {}".format(self.name)


    
    
class User(Department) :
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "User {}".format(self.name)


    
    
class Student(User) :
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Student {}".format(self.name)
    
class Tutor(Student) :
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Tutor {}".format(self.name)


    
    
class Faculty(User) :
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Faculty {}".format(self.name)

class Administrator(Faculty) :
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Administrator {}".format(self.name)

class Professor(Faculty) :
   
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Professor {}".format(self.name)
