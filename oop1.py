class Car:

  
 def __init__(self,mileage,gap):
     self.mileage=mileage
     self.gap=gap
 def printveh(self): 
   print ("the mileage for each type is",self.mileage,self.gap)
suv = Car(12,2)
sedan = Car(14,4)
xuv = Car(15,5) 

 


suv.printveh()
sedan.printveh()
xuv.printveh()    	
  
 
