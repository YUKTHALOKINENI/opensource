n=int(input())
m=1
for i in range(1,n+1):
    for j in range(i):
        print(m,end=" ")
        m+=1
    print()
