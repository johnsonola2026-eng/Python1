TheBoard={'7':'','8':'','9':'',
          '4':'','5':'','6':'',
          '1':'','2':'','3':'',}
board_keys=[]
for keys in TheBoard:
    board_keys.append(keys)
def printboard(board):
    print(board['7']+'|'+board['8']+'|'+board['9']+'|'
          +board['4']+'|'+board['5']+'|'+board['6']+'|'
          +board['1']+'|'+board['2']+'|'+board['3'])
def game():
    turn='x'
    count=0
    for i in range (10):
        printboard(TheBoard)
        print("it's your turn,"+turn+".move to which place?")
        move=input()
        if TheBoard[move]=='':
            TheBoard[move]=turn
            count+=1
        else:
         print("that place is already filled.\n move to which place")
         continue
        if count >=5:
            if TheBoard['7']==TheBoard['8']==TheBoard['9']!='':
                printboard(TheBoard)
                print("\n game over.\n")
                print("****"+turn+"won,****")
                break
            elif TheBoard['4']==TheBoard['5']==TheBoard['6']!='':
                printboard(TheBoard)
            print("\n game over.\n")
            print("****"+turn+"won,****")
            break
        if TheBoard['1']==TheBoard['2']==TheBoard['3']!='':
                printboard(TheBoard)
        print("\n game over.\n")
        print("****"+turn+"won,****")
        break