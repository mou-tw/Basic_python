def fib (n):
    if n ==1 or n==2:
        return 1
    return fib(n-1)+ fib(n-2)
print(fib(10))

def fib2(n,l=[0]):
    l[0]+=1
    if n ==1 or n==2:
        if l[0]==1:
            return 1
        l[0]-=1
        return 1,1
    else:
        a ,b = fib2(n-1)
        l[0]-=1
        if l[0] ==0:
            return a+b
        return b ,a+b

print(fib2(50))