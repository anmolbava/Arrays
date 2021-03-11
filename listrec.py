def reclist(li):
   n=len(li)
   if(n==1):
      return li[0] 
   smallarr=reclist(li[:(n-1)})     
   return li[n-1] + smallarr
 

n=int(input())
li=[int (i) for i in input().split()]
reclist(li)
