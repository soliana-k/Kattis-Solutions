print((lambda g,t: g-t)(*map(int, input().split()[:-1]))*9//10-sum(map(int, input().split())))
