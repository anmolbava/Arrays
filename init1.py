class Student:
 def __init__(self,name,rollno,dept):
    self.name=name
    self.rollno=rollno
    self.dept=dept
 def printall(self):
    print(self.name)
    print(self.rollno)
    print(self.dept)
s1=Student("Anmol",1,"cyber security")   
s2=Student("onkar",2,"data analytics")
s3=Student("raj",3,"management")
s1._printall()
#s2.printall()
#s3.printall()  

