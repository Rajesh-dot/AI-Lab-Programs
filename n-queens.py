ans=0
def printBoard(x):
    print(f"Solution - {ans}")
    for i in range(n):
        for j in range(n):
            if x[i]==j:
                print("Q",end=' ')
            else:
                print(".",end=' ')
        print()

def solve(x,cur,n):
    global ans
    if cur==n:
        ans+=1
        printBoard(x)
    for i in range(n):
        f=0
        for j in range(cur):
            if x[j]==i or abs(cur-j)==abs(i-x[j]):
                f=1
                break
        if f==0:
            x[cur]=i
            solve(x,cur+1,n)

n=int(input("Enter the size of the board: "))
x=[0]*n
solve(x,0,n)
if ans==0:
    print("There are no solutions")
