n=int(input())
arr=list(map(int,input().split()))
unique_arr=[]
for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)
for i in unique_arr:
    print(i,end=" ")
