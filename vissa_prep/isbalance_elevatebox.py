n=int(input())
arr=list(map(int,input().split()))
total=sum(arr)
balance=[]
left=0
for i in arr:
    right=total - left - i
    b= abs(left-right)
    balance.append(b)
    left+=i
for i in balance:
    print(i,end=" ")
