x,y,z = map(int,input().split())
minutes = 24 * 60
total = x * y
if total <= minutes * z:
    print("YES")
else:
    print("NO")
