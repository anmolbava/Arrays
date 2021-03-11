n=int(input())
firstval=0
secondval=1
i=0
while i<n:
   if i<=1:
      next=i
      
   else:
      next=firstval+secondval
      firstval=secondval
      secondval=next
      
    
   i=i+1
print (next)
