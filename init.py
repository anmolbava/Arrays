class Student:
 def __init__(self):
   self.name="Anmol"
   self.rollno=1
   self.dept="cyber  security"
   print("initfunction:-")
   print(self.name)
   print(self.rollno)
   print(self.dept) 
 def allprint(self):
    print("allprint  :-")
    print(self.name)
    print(self.rollno)
    print(self.dept) 

s1=Student()
s1.allprint()
s2=Student()
s2.allprint()
