def twosum():
 list1=[1,2,3,4,5,6,7,8,9]
 for i in range (0,9):
    print "the members of the list are",list1[i]
 tar=int(input("enter the target sum please"))
 for a in range(0,9): 
   for b in range (0,9):
        total= list1[a] + list1[b]
        if total==tar :
           print "target found"  
           print  list1[a],list1[b]
           return tar
twosum()
