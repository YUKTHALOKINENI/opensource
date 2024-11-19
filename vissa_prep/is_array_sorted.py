n=int(input())
arr=list(map(int,input().split()))
res="true"
for i in range(n-1):
    if arr[i]>arr[i+1]:
        res="false"
print(res)
