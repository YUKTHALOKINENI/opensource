n=int(input())
rev=0
m=2**31 - 1
if n<0:
    s=-1
else:
    s=1
n=abs(n)
while n!=0:
    d=n%10
    n//=10
    if rev>m // 10 or (rev==m//10 and d>7):
        print(0)
        break
    rev=rev*10+d
else:
    print(s*rev)
