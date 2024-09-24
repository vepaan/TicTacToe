gameboard =["-","-","-",
            "-","-","-",
            "-","-","-"]

def boardprinter(gameboard):
    print(gameboard[0],' ',gameboard[1],' ',gameboard[2])
    print(gameboard[3],' ',gameboard[4],' ',gameboard[5])
    print(gameboard[6],' ',gameboard[7],' ',gameboard[8])

def decidewinner(gameboard):
    #horizantal O wins
    if gameboard[0]=='o' and gameboard[1]=='o' and gameboard[2]=='o' or gameboard[3]=='o' and gameboard[4]=='o' and gameboard[5]=='o' or gameboard[6]=='o' and gameboard[7]=='o' and gameboard[8]=='o':
        return "PLAYER ONE WINS!!"
    #vertical O wins
    elif gameboard[0]=='o' and gameboard[3]=='o' and gameboard[6]=='o' or gameboard[1]=='o' and gameboard[4]=='o' and gameboard[7]=='o' or gameboard[2]=='o' and gameboard[5]=='o' and gameboard[8]=='o':
        return "PLAYER ONE WINS!!"
    #diagonal O wins
    elif gameboard[0]=='o' and gameboard[4]=='o' and gameboard[8]=='o' or gameboard[2]=='o' and gameboard[4]=='o' and gameboard[6]=='o':
        return "PLAYER ONE WINS!!"
    #horizantal X wins
    elif gameboard[0]=='x' and gameboard[1]=='x' and gameboard[2]=='x' or gameboard[3]=='x' and gameboard[4]=='x' and gameboard[5]=='x' or gameboard[6]=='x' and gameboard[7]=='x' and gameboard[8]=='x':
        return "PLAYER TWO WINS!!"
    #vertical X wins
    elif gameboard[0]=='x' and gameboard[3]=='x' and gameboard[6]=='x' or gameboard[1]=='x' and gameboard[4]=='x' and gameboard[7]=='x' or gameboard[2]=='x' and gameboard[5]=='x' and gameboard[x]=='x':
        return "PLAYER TWO WINS!!"
    #diagonal X wins
    elif gameboard[0]=='x' and gameboard[4]=='x' and gameboard[8]=='x' or gameboard[2]=='x' and gameboard[4]=='x' and gameboard[6]=='x':
        return "PLAYER TWO WINS!!"
    else:
        return 0

print("TIC TAC TOE")
print("-----------")
print('Player one will use "o"')
print('Player two will use "x"')
print("Player one will go first")

boardprinter(gameboard)

win=False
moves_count=0

while win==True or moves_count<9:
    if moves_count%2==0:
        user_input=int(input('PLAYER ONE(o)...What position(1-9)(numbered horizantally)'))
        while gameboard[user_input-1]=='o' or gameboard[user_input-1]=='x':
            print("POSITON ALREADY FILLED")
            boardprinter(gameboard)
            user_input=int(input('PLAYER ONE(o)...What position(1-9)(numbered horizantally)'))
        gameboard[user_input-1]='o'
        boardprinter(gameboard)
        moves_count=moves_count+1
    else:
        user_input=int(input('PLAYER TWO(x)...What position(1-9)(numbered horizantally)'))
        while gameboard[user_input-1]=='o' or gameboard[user_input-1]=='x':
            print("POSITON ALREADY FILLED")
            boardprinter(gameboard)
            user_input=int(input('PLAYER TWO(x)...What position(1-9)(numbered horizantally)'))
        gameboard[user_input-1]='x'
        boardprinter(gameboard)
        moves_count=moves_count+1
    
    if decidewinner(gameboard)!=0:
        win=True
        print(decidewinner(gameboard))
        break