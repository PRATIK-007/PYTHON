def display(word):
    mark=""
    print(word[6]+"|"+word[7]+"|"+word[8])
    print("-|-|-")
    print(word[3]+"|"+word[4]+"|"+word[5])
    print("-|-|-")
    print(word[0]+"|"+word[1]+"|"+word[2])

display("xoxoxoxox")

def inputp():
    player1=""
    player2=""
    while player1!='x' and player1!='o':
        player1=input("enter the player1 : X or O : ")
        if player1=='x':
            player2='o'
        else:
            player2='x'

    print(" player1 has selected : ",player1)
    print(" player2 has got      : ",player2)

    return player1,player2

    
x,y=inputp()


print ("---------------- Play with NUMPAD ---------------------------")
def play_game():
    flag = 0
    var="         "
    while (var[0]!=('x' or 'o') or var[1]!=('x' or 'o') or var[2]!=('x' or 'o') or var[3]!=('x' or 'o') or var[4]!=('x' or 'o') or var[5]!=('x' or 'o') or var[6]!=('x' or 'o') or var[7]!=('x' or 'o') or var[8]!=('x' or 'o') ):
        if (var[0]!= y or var[1]!=y or var[2]!= y) and (var[2]!= y or var[5]!=y or var[8]!= y) and (var[1]!= y or var[4]!=y or var[7]!= y) and (var[0]!= y or var[3]!=y or var[6]!= y) and (var[3]!= y or var[4]!=y or var[5]!= y) and (var[6]!= y or var[7]!=y or var[8]!= y)and (var[0]!= y or var[4]!=y or var[8]!= y) and (var[6]!= y or var[4]!=y or var[2]!= y):
            while(True):
                input1=input(" player1 : ")
                if  var[int(input1)-1]==" ":
                    var = var[:int(input1)-1] + x + var[int(input1):]
                    print(var)
                    display(var)
                    break
                else:
                    print("enter valid position")
        else:
            print("------------------Player 2 has won the game---------")
            break    

        if flag<9:
            flag=flag+1
        
        print(flag)
        if (flag==9) and (var[0]!= x or var[1]!=x or var[2]!= x) and (var[2]!= x or var[5]!=x or var[8]!= x) and (var[1]!= x or var[4]!=x or var[7]!= x) and (var[0]!= x or var[3]!=x or var[6]!= x) and (var[3]!= x or var[4]!=x or var[5]!= x) and (var[6]!= x or var[7]!=x or var[8]!= x)and (var[0]!= x or var[4]!=x or var[8]!= x) and (var[6]!= x or var[4]!=x or var[2]!= x):
            print("game has been tied")
            break
        if flag==9 :
            print("------------------Player 1 has won the game---------")
            break

        if (var[0]!= x or var[1]!=x or var[2]!= x) and (var[2]!= x or var[5]!=x or var[8]!= x) and (var[1]!= x or var[4]!=x or var[7]!= x) and (var[0]!= x or var[3]!=x or var[6]!= x) and (var[3]!= x or var[4]!=x or var[5]!= x) and (var[6]!= x or var[7]!=x or var[8]!= x)and (var[0]!= x or var[4]!=x or var[8]!= x) and (var[6]!= x or var[4]!=x or var[2]!= x):
            while(True):
                input2=input(" player2 : ")
                if  var[int(input2)-1]==" ":
                    var = var[:int(input2)-1] + y + var[int(input2):]
                    display(var)
                    break
                else:
                    print("enter at valid position ")
        else:
            print("------------------Player 1 has won the game---------")
            break
        
        
        flag=flag+1

play_game()
