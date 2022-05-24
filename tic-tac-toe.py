# This program uses min-max algorithm

def printBoard(board):
    for i in range(3):
        print(" "+board[i][0]+"|"+board[i][1]+"|"+board[i][2])
        if i<2:
            print("-------")

board=[[" ", " ", " "] for i in range(3)]

def isFull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                return False
    return True

def winner(player,board):
    if board[0][0]==board[1][1]==board[2][2]==player:
        return True
    if board[0][2]==board[1][1]==board[2][0]==player:
        return True
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]==player:
            return True
        if board[0][i]==board[1][i]==board[2][i]==player:
            return True
    return False

def player():
    print("Player's Turn")
    v=int(input())
    v-=1
    x=v//3
    y=v%3
    if board[x][y]==" ":
        board[x][y]="X"
        printBoard(board)
    else:
        print("Invalid tile already selected")
        player()

def avail():
    l=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                l.append((i,j))
    return l

def getScore():
    if winner("X",board):
        return -1
    if winner("O",board):
        return 1
    return 0

players=["O","X"]
def minimax(depth, is_max):
    score = getScore()
    if score==1:
        return score
    if score==-1:
        return score
    if isFull(board):
        return 0
    if is_max:
        best=-100
        l=avail()
        for i in l:
            board[i[0]][i[1]]=players[0]
            best=max(best,minimax(depth+1,not is_max))
            board[i[0]][i[1]]=" "
    else:
        best=100
        l=avail()
        for i in l:
            board[i[0]][i[1]]=players[1]
            best=min(best,minimax(depth+1,not is_max))
            board[i[0]][i[1]]=" "
    return best

def getBestMove():
    l=avail()
    best=-1
    score=-100
    for i in l:
        board[i[0]][i[1]]=players[0]
        t=minimax(0,False)
        board[i[0]][i[1]]=" "
        if t>score:
            best=i
            score=t
    return best

choice=1
human=True
while choice==1:
    if human:
        printBoard(board)
        while not winner("X",board) and not winner("O",board) and not isFull(board):
            player()
            if winner("X",board):
                print("Well done, You won")
                break
            if isFull(board):
                print("Game is Tie!")
                break
            move = getBestMove()
            board[move[0]][move[1]]='O'
            printBoard(board)
            if winner("O",board):
                print("Sorry, You loose")
                break
    else:
        while not winner("X",board) and not winner("O",board) and not isFull(board):
            move = getBestMove()
            board[move[0]][move[1]]='O'
            printBoard(board)
            if winner("O",board):
                print("Sorry, You loose")
                break
            if isFull(board):
                print("Game is Tie!")
                break
            player()
            if winner("X",board):
                print("Well done, You won")
                break
    choice=int(input("Do you want play again(0/1):"))
    human = not human
    board=[[" ", " ", " "] for i in range(3)]
