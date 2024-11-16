x,n=map(int,input().split())
c=x*100
need=max(0,n-c)
new_planes=(need+99)//100
print(new_planes)
