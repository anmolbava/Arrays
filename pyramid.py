n=int(input())
i=1
while(i<=n):
  s=1
  while(s<=n-i+1):
    print(" ",end='')
    s=s+1
  j=1
  while(j<i):
    print(j,end='')
    j=j+1
  k=i-1
  while(k>=1):
    print(k,end='')
    k=k+1
    k=k-1
  print()
  i=i+1  
    

    
