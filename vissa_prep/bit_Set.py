N=int(input())
K=int(input())
m=1<<(K-1)
if (N&m) !=0:
    print("true")
else:
    print("false")
