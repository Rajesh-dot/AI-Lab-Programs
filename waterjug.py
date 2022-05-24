x=int(input("Size of first jar: "))
y=int(input("Size of second jar: "))
z=int(input("Required Amount: "))
q=[(0,0)]
d={(0,0):(0,0)}
f=0
sol=[]
while q:
    a,b=q[0]
    q.pop(0)
    if(a==z or y==z):
        f=1
        sol.append((a,b))
        continue
    pos=[(x,b),(a,y),(0,b),(a,0),(min(a+b,x),max(b-(x-a),0)),(max(a-(y-b),0),min(b+a,y))]
    for i in pos:
        if i in d:
            continue
        d[(i[0],i[1])]=(a,b)
        q.append((i[0],i[1]))
if f==0:
    print("There is no solution")
else:
    for j in range(len(sol)):
        print("Solution - {}".format(j+1))
        ans=[]
        cur=sol[j]
        while d[cur]!=cur:
            ans.append(cur)
            cur=d[cur]
        ans.append((0,0))
        ans.reverse()
        for i in ans:
            print(i)
