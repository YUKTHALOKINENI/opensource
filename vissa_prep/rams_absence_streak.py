n=int(input())
attendance=input().split()
absent=0
count=0
for i in attendance:
    if i=='0':
        count+=1
        absent=max(absent,count)
    else:
        count=0
print(absent)
