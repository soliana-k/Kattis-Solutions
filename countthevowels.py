v='aeiou'
stru=input()
stru=stru.casefold()
count=0
for char in stru:
    if char in v:
        count +=1
print(count) 
