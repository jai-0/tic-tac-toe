theboard={'7':'7','8':'8','9':'9', '4':'4','5':'5','6':'6','1':'1','2': '2','3': '3'}
def printBoard(board):
        print (' --- '+'--- '*2)
        
        print(f"| {board['7']} |" + f" {board['8']} |" + f" {board['9']} |")
        
        print (' --- '+'--- '*2)
              
        print(f"| {board['4']} |" + f" {board['5']} |" + f" {board['6']} |")
              
        print (' --- '+'--- '*2)
              
        print(f"| {board['1']} |" + f" {board['2']} |" + f" {board['3']} |")
              
        print (' --- '+'--- '*2)
printBoard(theboard)

def game():
    boxesLeft=['1','2','3','4','5','6','7','8','9']
    correctInputs=['1','2','3','4','5','6','7','8','9']
    boxesDone=[]
    input_valid=False
    boardDone= True
    count=0
    for n in range(0,10):
        
        if n == 0 or n%2 == 0:
            move='X'
        else:
            move='O'
           
        if (theboard['7']==theboard['8']==theboard['9']=='X') or (theboard['7']==theboard['4']==theboard['1']=='X') or (theboard['1']==theboard['2']==theboard['3']=='X') or (theboard['3']==theboard['6']==theboard['9']=='X') or (theboard['7']==theboard['5']==theboard['3']=='X') or (theboard['8']==theboard['5']==theboard['2']=='X') or (theboard['4']==theboard['5']==theboard['6']=='X') or (theboard['9']==theboard['5']==theboard['1']=='X'): 
            print('The winner is X')
            count=1
            break
        elif (theboard['7']==theboard['8']==theboard['9']=='O') or (theboard['7']==theboard['4']==theboard['1']=='O') or (theboard['1']==theboard['2']==theboard['3']=='O') or (theboard['3']==theboard['6']==theboard['9']=='O') or (theboard['7']==theboard['5']==theboard['3']=='O') or (theboard['8']==theboard['5']==theboard['2']=='O') or (theboard['4']==theboard['5']==theboard['6']=='O') or (theboard['9']==theboard['5']==theboard['1']=='O'): 
            print('The winner is O')
            count=1
            break
        elif len(boxesDone)==9:
                print("Nobody won, try again.")
                break
        else:
            pass
        
            
        
            print (f"This is {move}'s move")
            while input_valid==False or boardDone==True:
                theinput=input('Please Select the Box Number you want to replace by entering the coressponding number(1,2,3,4,5,6,7,8,9): ')
                
                if theinput in correctInputs:
                    input_valid=True
                else:
                     print('Please choose a number between 1 and 9 (1,2,3,4,5,6,7,8,9)')


                if theinput in boxesDone:
                    print(f'Box number {theinput} is already filled, Please choose another box')

                else:
                    boardDone=False
                
            
            
            
        boxesDone.append(theinput)
        theboard[f'{theinput}']=move 
        input_valid=False
        boardDone=True
        printBoard(theboard) 
        
game()
