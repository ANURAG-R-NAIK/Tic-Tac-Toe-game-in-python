def sum(a,b,c):
    return a+b+c

def printboard(xstop,ystop):
    zero= "X" if xstop[0] else ("O" if ystop[0] else 0) #this is used to replace the input values with X and and O when 
    one= "X" if xstop[1] else ("O" if ystop[1] else 1)  ##when they are being assigned
    two= "X" if xstop[2] else ("O" if ystop[2] else 2)  
    three= "X" if xstop[3] else ("O" if ystop[3] else 3)  
    four= "X" if xstop[4] else ("O" if ystop[4] else 4)  
    five= "X" if xstop[5] else ("O" if ystop[5] else 5)  
    six= "X" if xstop[6] else ("O" if ystop[6] else 6)  
    seven= "X" if xstop[7] else ("O" if ystop[7] else 7)  
    eight= "X" if xstop[8] else ("O" if ystop[8] else 8) 
    
     
    print(f"{zero} | {one} | {two} ")    #here we are definig the basic board design with the positions defined with the numbers
    print("--|---|---|")
    print(f"{three} | {four} | {five} ")
    print("--|---|---|")
    print(f"{six} | {seven} | {eight} ")

def checkwin(xstop,ystop):
    wins = [[0,1,2],[1,4,7],[2,5,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]] #here it is defined for all the possible comibinations the winner is selected
    for win in wins:
        if (sum(xstop[win[0]],xstop[win[1]],xstop[win[2]]) ==  3):
            print('X has won the match')
            return 1
        if (sum(ystop[win[0]],ystop[win[1]],ystop[win[2]]) ==  3):
            print('Y has won the match')
            return 0
    return -1
if __name__== "__main__":
    xstop=[0,0,0,0,0,0,0,0,0] #here we are defining all the values for xstop and ystop
    ystop=[0,0,0,0,0,0,0,0,0]
    turn=1  #here we will put 1 for X and 0 fro O
    
    print("Welcome To-Tic-Tac-Toe")
    while(True):
        printboard(xstop,ystop)
        if (turn==1):
            print("X's Chance")
            value =int(input("please enter a valid value"))
            xstop[value]= 1
        else:
            print("Y'chance")
            value =int(input("please enter a valid value"))
            ystop[value]=1
       
        winner=checkwin(xstop,ystop)  
        if (winner != -1):
            print('match is over')
            break
        turn=1-turn
        
        #CONTINUE HARRY VIDEO FROM 14:00
    
