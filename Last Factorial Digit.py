def fact(n):
    factorial = 1
    if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i
            f=repr(factorial)
            last_digit=f[-1]
            fa=int(last_digit)
    print(fa)
c=int(input())
ls=[]
for i in range(c):
    s=int(input())
    ls.append(s)
for j in ls:
   fact(j)
