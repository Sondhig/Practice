import numpy as np

arr1=np.zeros(3)
arr2=np.zeros(3)
arr3=np.zeros(3)

print("Player 1 goes first")


for i in range(3):  
    x=checkwinner()
    if(x==0):
        print("Winner")
    val=input("PLayer 1 Enter where you want to put X")
     x=checkwinner()
    if(x==0):
        print("Winner")
    val=input("PLayer 2 Enter where you want to put O")




def checkwinner():
    val=0

    if(arr1[0]=='X' & arr1[1]='X' & arr1[2]='X'):
        print("Player 1 Wins")
    
    elif((arr1[0]=='O' & arr1[1]='O' & arr1[2]='O'):
        print("Player 2 Wins")
        
    elif((arr2[0]=='X' & arr2[1]='X' & arr2[2]='X'):
        print("Player 1 Wins") 

    elif((arr2[0]=='O' & arr2[1]='O' & arr2[2]='O'):
        print("Player 2 Wins")

    elif((arr3[0]=='X' & arr3[1]='X' & arr3[2]='X'):
        print("Player 1 Wins")

    elif((arr3[0]=='O' & arr3[1]='O' & arr3[2]=''):
        print("Player 2 Wins")

    #Vertical
    elif((arr1[0]=='X' & arr2[0]='X' & arr3[0]='X'):
        print("Player 1 Wins") 

    elif((arr1[0]=='O' & arr2[0]='O' & arr3[0]='O'):
        print("Player 2 Wins")
    
    elif((arr1[1]=='X' & arr2[1]='X' & arr3[1]='X'):
        print("Player 1 Wins") 

    elif((arr1[1]=='O' & arr2[1]='O' & arr3[1]='O'):
        print("Player 2 Wins")
    
    elif((arr1[2]=='X' & arr2[2]='X' & arr3[2]='X'):
        print("Player 1 Wins") 

    elif((arr1[2]=='O' & arr2[2]='O' & arr3[2]='O'):
        print("Player 2 Wins")

    #Diagnol
    elif((arr1[0]=='X' & arr2[1]='X' & arr3[2]='X'):
        print("Player 1 Wins") 

    elif((arr1[0]=='O' & arr2[1]='O' & arr3[2]='O'):
        print("Player 2 Wins")

    elif((arr1[2]=='X' & arr2[1]='X' & arr3[0]='X'):
        print("Player 1 Wins") 

    elif((arr1[2]=='O' & arr2[1]='O' & arr3[0]='O'):
        print("Player 2 Wins")
    
    else:
        value=1

    return value
        