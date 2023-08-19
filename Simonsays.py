n=int(input())
arr=[]
yu=[]
for i in range(n):
    s=input()
    arr.append(s)
for c in arr:
    if c[:10]=="Simon says":
        ar=c[11:]
        yu.append(ar)
    else:
        pass

for v in yu:
    print(v)
