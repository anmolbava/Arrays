N=int(input())
sumo=0
sume=0
i=0
while N>0:
  i=N%10
  if i%2==0:
      sume=sume+i
  else:
      sumo=sumo+i
  N=N//10  
print(sume)
print(sumo)
