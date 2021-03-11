def recursion(n):
    if (n==1 or n==2):
        return 1
    num1=recursion(n-1)
    num2=recursion(n-2)
    sum = num1 + num2
    print (sum)
    return sum
    
n=int(input())    
print(recursion(n))
