def solve(v,c,d,dis):
    if v==x and c==n:
        return dis[v]
    ans=float('inf')
    for i in l[v]:
        u,w=i
        if u==x and c!=n-1:
            continue
        if u not in d:
            d[u]=v
            dis[u]=w+dis[v]
            ans=min(ans,solve(u,c+1,d,dis))
            del d[u]
    return ans

n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))
l={i:[] for i in range(1,n+1)}
print("Enter edges (source, destination, weight)")
for i in range(m):
    u, v, w = map(int, input().split())
    l[u].append([v,w])
x = int(input("Enter starting node: "))
dis={x:0}
d={}
print("Shortest distance:",solve(x,0,d,dis))



'''

Sample input:-

1 2 10
2 1 5
1 3 15
3 1 6
1 4 20
4 1 8
2 4 10
4 2 8
2 3 9
3 2 13
3 4 12
4 3 9

'''