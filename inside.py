n=int(input())
i=1
sume=0
sumo=0
while i<=n:
   if i%2==0:
      sume=sume+i
      i=i+1   
   else:
      sumo=sumo+i
      i=i+1

print ("the even sum is ",sume)
print("the odd sum is",sumo)
