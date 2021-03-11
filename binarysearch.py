def binarysearch():
  List1=[11,22,33,44,55,66,77,88,99,100]
  low=0
  high=10
  for i in range(0,10):
   print List1[i]
  mid = low + high / 2
  print "your midpoint of list is"
  print (mid)
  print (List1[mid])
  num = int(input("enter the number to be searched"))
  while high>=low:
   	mid = (low + high) / 2
        if List1[mid]==num:
             print "number found at",mid
        elif num>List1[mid]:
             low = mid
             mid = low + high/2 
        elif  num<List1[mid]:
             high=mid     
             mid = high-low/2
        else:
              print  "element	not	found"
binarysearch()
