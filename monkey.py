def solve(banana,box,height,monkey,hold):
    if monkey==banana and height==1:
        ans.append("Monkey took banana")
        return True
    if (banana,box,height,monkey,hold) in d:
        return False
    found=0
    d[(banana,box,height,monkey,hold)]=1
    options={1:"Move to box", 2:"Move to banana", 3:"Climb onto the box", 4:"Hold box to move"}
    for option in options:
        if option==1 and hold==0 and height==0 and solve(banana,box,height,box,hold):
            ans.append(options[option])
            found=1
            break
        elif option==2 and height==0 and ((hold==1 and solve(banana,banana,height,banana,hold)) or (hold==0 and solve(banana,box,height,banana,hold))):
            ans.append(options[option])
            found=1
            break
        elif option==3 and height==0 and monkey==box and solve(banana,box,height+1,monkey,0):
            ans.append(options[option])
            found=1
            break
        elif option==4 and height==0 and monkey==box and solve(banana,box,height,monkey,1):
            ans.append(options[option])
            found=1
            break
    return found

n=int(input("Enter the size of the world: "))
world=[[0]*n for i in range(n)]
x,y=map(int,input("Enter tree position: ").split())
world[x][y]=1
x,y=map(int,input("Enter box position: ").split())
world[x][y]=-1
x,y=map(int,input("Enter monkey position: ").split())
for i in range(n):
    for j in range(n):
        if world[i][j]==1:
            print(f"Monkey found the banana tree at ({i},{j})")
            banana=(i,j)
        if world[i][j]==-1:
            print(f"Box found at ({i},{j})")
            box=(i,j)
d={}
ans=[]
solve(banana,box,0,(x,y),0)
ans.reverse()
print(*ans,sep="\n")

'''
5
2 2
4 4
0 0
'''
