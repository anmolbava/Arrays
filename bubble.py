def bubble():
 num1=[10,9,8,7,6,5,4,3,2,1]
 for a in range (0,10):
   print "the numbers are ",num1[a] 
 for i in range (0,9):
   for j in range(0,9):
    if num1[j]>num1[j+1]:
     temp=num1[j]
     num1[j]=num1[j+1]
     num1[j+1]=temp
 for p in range(0,10):
  print num1[p]



bubble()
