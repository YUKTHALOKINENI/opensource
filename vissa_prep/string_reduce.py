n=input()
m=""
count=1
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        count+=1
    else:
        m+=n[i-1]+str(count)
        count=1
m+=n[-1]+str(count)
print(m)
