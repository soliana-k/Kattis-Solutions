x, y, n = map(int, input().split())

for i in range(1, (n+1)):
    if  i%y==0 and i%x==0:
        print("FizzBuzz")
    elif i%y==0:
        print("Buzz")
    elif i%x==0:
        print("Fizz")
    else:
        print(i)
