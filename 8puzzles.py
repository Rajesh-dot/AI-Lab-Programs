sour=[]
dest=[]
d={}
print("Enter Source Matrix")
for i in range(3):
    a,b,c=map(int,input().split())
    sour.extend([a,b,c])
print("Enter Destination Matrix")
for i in range(3):
    a,b,c=map(int,input().split())
    dest.extend([a,b,c])
d={}
sour=tuple(sour)
dest=tuple(dest)
d[sour]=sour
q=[sour]
f=0
while q:
    cur=q[0]
    q.pop(0)
    if cur==dest:
        f=1
        break
    for i in range(9):
        if cur[i]==0:
            idx=i
            break
    temp=list(cur)
    if idx>=3:
        a=temp[:]
        a[idx],a[idx-3]=a[idx-3],a[idx]
        a=tuple(a)
        if a not in d:
            d[a]=cur
            q.append(a)
    if idx<=5:
        a=temp[:]
        a[idx],a[idx+3]=a[idx+3],a[idx]
        a=tuple(a)
        if a not in d:
            d[a]=cur
            q.append(a)
    if idx%3!=2:
        a=temp[:]
        a[idx],a[idx+1]=a[idx+1],a[idx]
        a=tuple(a)
        if a not in d:
            d[a]=cur
            q.append(a)
    if idx%3!=0:
        a=temp[:]
        a[idx],a[idx-1]=a[idx-1],a[idx]
        a=tuple(a)
        if a not in d:
            d[a]=cur
            q.append(a)

if f==0:
    print("There are no solutions")
else:
    print("Solution")
    ans=[]
    while d[cur]!=cur:
        ans.append(cur)
        cur=d[cur]
    ans.append(sour)
    ans.reverse()
    for i in ans:
        c=0
        for j in range(3):
            for k in range(3):
                print(i[k+c*3],end=' ')
            print()
            c+=1
        print()
