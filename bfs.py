n=int(input("Enter number of vertices: "))
m=int(input("Enter number of edges: "))
l={}
print("Enter edges (source, destination)")
for i in range(m):
    u,v=map(int,input().split())
    if u in l:
        l[u].append(v)
    else:
        l[u]=[v]
    if v in l:
        l[v].append(u)
    else:
        l[v]=[u]
start=int(input("Enter starting node: "))
print("Breadth first order is")
vist={i:False for i in l}
q=[start]
while q:
    v=q[0]
    q.pop(0)
    if vist[v]:
        continue
    vist[v]=True
    print(v)
    for i in l[v]:
        q.append(i)
