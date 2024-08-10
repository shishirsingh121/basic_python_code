# 1.polymorphism
class Animal:
    def __init__(self,name):
        self.name=name
    def showname(self):
        print(self.name)    
class human:
    def __init__(self,name) :
        self.name=name
    def showname(self):
        print(self.name)        
hum=human("shishir")
ani=Animal("i ma here")   
hum.showname()
ani.showname()

# 2.abstraction     
class student:
    def __init__(self,roll_number,name,class_name):
        self.roll_number=roll_number
        self.name=name
        self.class_name=class_name
        self.marks={}
                
    def add_marks(self,subject,marks):
        if subject in self.marks:
            print(f"{self.marks} is already marks {subject}")
        else:
            self.marks[subject]=marks
    
    def calculate_average_marks(self):
        if not self.marks:
            print("there are no marks available")
        total_marks=sum(self.marks.values())  
        average_marks=total_marks/len(self.marks)
        return average_marks
    
    def display_student_info(self):
        print("student info")
        print(f"Roll number:{self.roll_number}")
        print(f"enter your name:{self.name}")
        print(f"enter you class name:{self.class_name}")
        print(f"average marks:{self.calculate_average_marks()}")
student1=student(12,"shishir","12th")
student2=student(13,"damber","12th")
student1.add_marks("english",23)
student2.add_marks("science",45)
student1.add_marks("nepali",23)
student2.add_marks("social",45)
student1.display_student_info()
student2.display_student_info()
        
          
                
            
            
                    
        
    