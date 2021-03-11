def selection():
 nums=[10,9,8,7,6,5,4,3,2,1]
 for k in range(0,10):
  print nums[k]
 for i  in range(0,10):
  minpos=i
  for j in range(i,10):
      if nums[j]< nums[minpos]:
            minpos=j  
 
  temp=nums[minpos]
  nums[minpos]=nums[i]
  nums[i]=temp
 print "the sorted List is"
 for a in range (0,10):
  print nums[a]	
selection()
